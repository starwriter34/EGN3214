from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy
from django.db.models import Q
from datetime import datetime, date
from django.contrib import messages
from django.views.generic import (
	ListView,
	CreateView,
	UpdateView,
	DetailView,
	DeleteView,
	FormView,
)
from django.views.generic.base import TemplateView
from .forms import MachineDownReportsForm, MachineStatusForm, PermanentRecordsForm
from .models import MachineStatus, PermanentRecords, MachineDownReports
'''
Name:							Type:	
----------------------------------------
MachineStatusList				CBV
MachineStatusUpdate				CBV
MachineStatusCreate				CBV
MachineStatusDetail				CBV

MachineStatusOperations			FBV

PermanentRecordsCreate			CBV
PermanentRecordsUpdate			CBV
PermanentRecordsList			CBV
PermanentRecordsDelete			CBV 

MachineDownReportsList			CBV
MachineDownReportsCreate		CBV
MachineDownReportsUpdate		CBV
MachineDownReportsDelete		CBV

TotalLifeChartHome				FBV
CurrentYearChartHome			FBV
FirstQuarterChartHome			FBV
SecondQuarterChartHome			FBV
ThirdQuarterChartHome			FBV
FourthQuarterChartHome			FBV

TotalLifeChart					FBV
CurrentYearChart				FBV
CurrentYearFirstQuarterChart	FBV
CurrentYearSecondQuarterChart	FBV
CurrentYearThirdQuarterChart	FBV
CurrentYearFourthQuarterChart	FBV

** Note ** Not Created - Need to Write Function(s)
-----------------------------------------------------------------
'''
############################################################################
############# BEGIN CLASS OR FUNCTION: BEGIN CLASS OR FUNCTION: ############
############################################################################
class MachineStatusList(ListView):
	"""
	########################################################################
	Class: MachineStatusList

	Lists all the Machines with current status, the health of the
	machine, as well, as controls for adding, updatings, and checking.
		
		Methods Used In View:
		---------------------

		ListView

		Class View Data
		---------------
		1. Provide the model being used.
		2. Provide a Template to display data.
		3. Provide a context name to access the data.

		get_context_data
		----------------
		**kwargs
		----------------
		help_wiki : boolean
			shows or hides the help wiki button
		permissions_access : str <name_of_app>
			permissions for {Extra Button} you enter the name of the app

		get_queryset
		------------
		MachineStatus.objects.all()
			get a list of all machines from the table Machinestatus
	########################################################################
	"""
	model = MachineStatus
	template_name = 'mmaint/mmaint_list.html'
	context_object_name = 'mmaint'

	def get_context_data(self, **kwargs):
		kwargs['helpwiki'] = False
		kwargs['search_vis'] = True
		kwargs['backbutton'] = 'Back'
		if self.request.user.has_perm('perms.mmaint.machinestatus.mmaint_all'):
			kwargs['chart_permission_access'] = True
		context = super(MachineStatusList, self).get_context_data(**kwargs)
		
		
		if self.request.user.is_authenticated and self.request.user.has_perm('mmaint.machinestatus.mmaint_all'):
			year = int(datetime.now().year)
			start_year = date(year,1,1)
			end_year = date(year,12,31)

			qone_start = date(year,1,1)
			qone_end =  date(year,3,31)

			qtwo_start = date(year,4,1)
			qtwo_end =  date(year,6,30)

			qthree_start = date(year,7,1)
			qthree_end =  date(year,9,30)

			qfour_start = date(year,10,1)
			qfour_end =  date(year,12,31)
			
			context['lifechart'] = MachineDownReports.objects.all()
			# Current Year Reporting
			total_lists_cy = context['lifechart'].filter(Q(starttime__gte=start_year) & Q(endtime__lte=end_year)).exists()
			# Q1 Reporting
			total_lists_q1 = context['lifechart'].filter(Q(starttime__gte=qone_start) & Q(endtime__lte=qone_end)).exists()
			# Q2 Reporting
			total_lists_q2 = context['lifechart'].filter(Q(starttime__gte=qtwo_start) & Q(endtime__lte=qtwo_end)).exists()
			# Q3 Reporting
			total_lists_q3 = context['lifechart'].filter(Q(starttime__gte=qthree_start) & Q(endtime__lte=qthree_end)).exists()
			# Q4 Reporting	
			total_lists_q4 = context['lifechart'].filter(Q(starttime__gte=qfour_start) & Q(endtime__lte=qfour_end)).exists()
			context['lifechart_count'] = context['lifechart'].count()
			context['currentyearchart'] = total_lists_cy
			context['qoneyearchart'] = total_lists_q1
			context['qtwoyearchart'] = total_lists_q2
			context['qthreeyearchart'] = total_lists_q3
			context['qfouryearchart'] = total_lists_q4
		return context

	def get_queryset(self):
		result = super(MachineStatusList, self).get_queryset()
		query = self.request.GET.get('search')

		if query:
			result = MachineStatus.objects.filter(machine_name__icontains=query)
		else:
			result = MachineStatus.objects.all()
		return result
############################################################################
### END CLASS OR FUNCTION: END CLASS OR FUNCTION: END CLASS OR FUNCTION: ###
############################################################################
############# BEGIN CLASS OR FUNCTION: BEGIN CLASS OR FUNCTION: ############
############################################################################
class MachineStatusUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
	"""
	########################################################################
	Class: MachineStatusUpdate

	Allows you to Update all the information regarding the machine. I.E.
	machine name, machine workstation number, row, and a temporary note
		
		Methods Used In View:
		---------------------
		LoginRequiredMixin
		PermissionRequiredMixin
		UpdateView
		
		Class View Data
		---------------
		1. Provide the model being used.
		2. Provide a Template to display data.
		3. Provide a Form to edit the data.
		4. Provide a log-in requirement to allow the user to edit the data.
		5. Utilize permissions to access the data.

		form_vaild
		----------
		Checks to make sure the form is valid and saves data.

		get_context_data
		----------------
		**kwargs
		----------------
		help_wiki : boolean
			shows or hides the help wiki button
		modelname : str
			name of the model
		create_update : str
			either create or update. Allows for both operations to be in one
			template file.

		get_success_url
		---------------
			Once updated it goes back to the detailview of the model
	########################################################################
	"""
	model = MachineStatus
	template_name = 'mmaint/mmaint_crud.djhtml'
	form_class = MachineStatusForm

	login_url = '/login/'
	redirect_field_name = 'blog-home'

	permission_required = ('mmaint.change_machinestatus')

	def form_valid(self, form):
		return super().form_valid(form)
	
	def get_success_url(self):
		return reverse_lazy('machinestatusdetail', kwargs={'pk': self.object.id})

	def get_context_data(self, **kwargs):
		kwargs['modelname'] = 'machinestatus'
		kwargs['helpwiki'] = False
		kwargs['create_update'] = 'update'
		context = super(MachineStatusUpdate, self).get_context_data(**kwargs)
		return context
	############################################################################
	### END CLASS OR FUNCTION: END CLASS OR FUNCTION: END CLASS OR FUNCTION: ###
	############################################################################
	############# BEGIN CLASS OR FUNCTION: BEGIN CLASS OR FUNCTION: ############
	############################################################################
class MachineStatusCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
	"""
	########################################################################
	Class: MachineStatusCreate

	Allows the user to create and track a new machine.
		
		Methods Used In View:
		---------------------
		LoginRequiredMixin
		PermissionRequiredMixin
		CreateView
		
		Class View Data
		---------------
		1. Provide the model being used.
		2. Provide a Template to display data.
		3. Provide a Form to edit the data.
		4. Provide a log-in requirement to allow the user to edit the data.
		5. Utilize permissions to access the data.

		form_vaild
		----------
		Checks to make sure the form is valid and saves data.

		get_context_data
		----------------
		**kwargs
		----------------
		help_wiki : boolean
			shows or hides the help wiki button
		modelname : str
			name of the model
		create_update : str
			either create or update. Allows for both operations to be in one
			template file.

		get_success_url
		---------------
			Once updated it goes back to the detailview of the model
	########################################################################
	"""
	model = MachineStatus
	template_name = 'mmaint/mmaint_crud.djhtml'
	form_class = MachineStatusForm

	login_url = '/login/'
	redirect_field_name = 'blog-home'

	permission_required = ('mmaint.add_machinestatus', 'mmaint.change_machinestatus', 'mmaint.delete_machinestatus', 'mmaint.view_machinestatus')

	def form_valid(self, form):
		return super().form_valid(form)

	def get_success_url(self):
		return reverse_lazy('machinestatusdetail', kwargs={'pk': self.object.id})
	
	def get_context_data(self, **kwargs):
		kwargs['modelname'] = 'machinestatus'
		kwargs['helpwiki'] = False
		kwargs['create_update'] = 'create'
		context = super(MachineStatusCreate, self).get_context_data(**kwargs)
		return context
	############################################################################
	### END CLASS OR FUNCTION: END CLASS OR FUNCTION: END CLASS OR FUNCTION: ###
	############################################################################
	############# BEGIN CLASS OR FUNCTION: BEGIN CLASS OR FUNCTION: ############
	############################################################################
class MachineStatusDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
	"""
	########################################################################
	Class: MachineStatusDetail

	Returns all information about the machine in one place. The health of 
	the machine, temporary notes, permanent records, as well, as downtime
		
		Methods Used In View:
		---------------------
		LoginRequiredMixin
		PermissionRequiredMixin
		DetailView
		
		Class View Data
		---------------
		1. Provide the model being used.
		2. Provide a Template to display data.
		3. Provide a Form to edit the data.
		4. Provide a log-in requirement to allow the user to edit the data.
		5. Utilize permissions to access the data.

		form_vaild
		----------
		Checks to make sure the form is valid and saves data.

		get_context_data
		----------------
		context data
		----------------
		
			total_list : queryset
				returns all machine downtime reports for the current year
			permanentnotes : queryset
				returns the five most recent permanent notes attached to the machine
			pn_count : queryset
				returns all the permanent notes records as a count
			machinedown_count_year : queryset
				returns all the current year machine down reports as a count
			machinedown_count_life : queryset
				returns all machine down records for the life of the machine as a count
			totalDowntime_year : float
				returns the total downtime for the current year
			totalDowntime : float
				returns the total downtime for the life of the machine
			machinedown_all : queryset
				returns the five most recent permanent notes attached to the machine

	########################################################################
	"""
	model = MachineStatus
	template_name = 'mmaint/mmaint_detail.html'

	login_url = '/login/'
	redirect_field_name = 'blog-home'

	permission_required = ('mmaint.change_machinestatus',)

	def form_valid(self, form):
		return super().form_valid(form)

	def get_context_data(self, **kwargs):
		year = int(datetime.now().year)
		start_year = date(year,1,1)
		end_year = date(year,12,31)
		
		total_list = MachineDownReports.objects.filter(machine_id=self.kwargs['pk'])
		total_list_year = MachineDownReports.objects.filter(
			Q(machine_id=self.kwargs['pk']) & Q(starttime__gte=start_year) & Q(endtime__lte=end_year)
		)
		
		totalDowntime_year = 0
		totalDowntime = 0
		
		for item in total_list:
			if item.endtime == None:
				totalDowntime += 0
			else:
				totalDowntime += round(float(item.total()), 2)

		for item in total_list_year:
			if item.endtime == None:
				totalDowntime_year += 0
			else:
				totalDowntime_year += round(float(item.total()), 2)

		context = super(MachineStatusDetail, self).get_context_data(id=self.kwargs['pk'], **kwargs)
		context['permanentnotes'] = PermanentRecords.objects.filter(
				machine_id=self.kwargs['pk']).order_by('-date', '-time')[0:5]
		context['pncount'] = PermanentRecords.objects.filter(machine_id=self.kwargs['pk']).count()
		context['machinedown_count_year'] = MachineDownReports.objects.filter(Q(machine_id=self.kwargs['pk']) & Q(starttime__gte=start_year) & Q(starttime__lte=end_year)).count()
		context['machinedown_count_life'] = MachineDownReports.objects.filter(machine_id=self.kwargs['pk']).count()
				
		context['totalDowntime_year'] = round(totalDowntime_year, 2)
		context['totalDowntime'] = round(totalDowntime, 2)
	
		if MachineDownReports.objects.filter(machine_id=self.kwargs['pk'],endtime=None):
			context['machinedown_all'] = MachineDownReports.objects.filter(machine_id=self.kwargs['pk']).order_by('-starttime')[:5]
		else:
			context['machinedown_all'] = MachineDownReports.objects.filter(machine_id=self.kwargs['pk']).order_by('-endtime')[:5]

		return context
	############################################################################
	### END CLASS OR FUNCTION: END CLASS OR FUNCTION: END CLASS OR FUNCTION: ###
	############################################################################
	############# BEGIN CLASS OR FUNCTION: BEGIN CLASS OR FUNCTION: ############
	############################################################################
def MachineStatusOperations(request, operation, pk):
	"""
	########################################################################
	Function: MachineStatusOperations

		The backbone of machine maintenance module. The operations come
	from the buttons on the main listview (MachineStatusListView). The 
	different operations are listed below in the operations section. The 
	operation is what is happening with the machine. 
		The primary	key(pk) is the machine status record. This is attached 
	to the MachineDownRecords and PermenantNotesRecords. An email is sent on
	a machine down and a machine up operation to the various people needing to
	know. The information can be found in the models.py file: function 
	sendemail. The responce just refreshes the page.

		Operations
		----------
		down - Machine is down
		up - Machine is coming back online
		fixture - Machine is down do to a fixture reindication
		pm - Machine is down for Preventative Maintenance
		
		Paramemters Used In Function:
		---------------------
		request
		operation
		pk
		

	########################################################################
	"""
	machine = MachineStatus.objects.get(pk=pk)
	if operation == 'down':
		machine.machinedown(pk)
		MachineDownReports.machinedown_re(pk)
		PermanentRecords.machinedown_note(pk)
		machine.sendemail(pk, 'Down')
		messages.success(request, f'Machine Maintenance has been notified.')
	elif operation == 'up':
		machine.machinerunning(pk)
		MachineDownReports.machinerunning_re(pk)
		machine.sendemail(pk, 'Up')
	elif operation == 'pm':
		machine.machinePM(pk)
	elif operation == 'fixture':
		machine.machineFixture(pk)
	
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
	############################################################################
	### END CLASS OR FUNCTION: END CLASS OR FUNCTION: END CLASS OR FUNCTION: ###
	############################################################################
	############# BEGIN CLASS OR FUNCTION: BEGIN CLASS OR FUNCTION: ############
	############################################################################
class PermanentRecordsCreate(CreateView):
	"""
	########################################################################
	Class: PermanentRecordCreate

	Allows the user to create a permanent record(a repair action).
		
		Methods Used In View:
		---------------------
		CreateView
		
		Class View Data
		---------------
		1. Provide the model being used.
		2. Provide a Template to display data.
		3. Provide a Form to edit the data.

		form_vaild
		----------
		Checks to make sure the form is valid and saves data.

		get_context_data
		----------------
		**kwargs
		----------------
		help_wiki : boolean
			shows or hides the help wiki button
		modelname : str
			name of the model
		create_update : str
			either create or update. Allows for both operations to be in one
			template file.

		get_success_url
		---------------
			Once updated it goes back to the detailview of the model
	########################################################################
	"""
	model = PermanentRecords
	template_name = 'mmaint/mmaint_crud.djhtml'
	form_class = PermanentRecordsForm

	def form_valid(self, form):
		form.instance.machine_id = MachineStatus.objects.get(pk=self.kwargs['pk'])
		return super(PermanentRecordsCreate, self).form_valid(form)
	
	def get_success_url(self):
		return reverse_lazy('machinestatusdetail', kwargs={'pk': self.object.machine_id_id})

	def get_context_data(self, **kwargs):
		kwargs['modelname'] = 'permanentrecords'
		kwargs['helpwiki'] = False
		kwargs['create_update'] = 'create'
		context = super(PermanentRecordsCreate, self).get_context_data(**kwargs)
		return context
	############################################################################
	### END CLASS OR FUNCTION: END CLASS OR FUNCTION: END CLASS OR FUNCTION: ###
	############################################################################
	############# BEGIN CLASS OR FUNCTION: BEGIN CLASS OR FUNCTION: ############
	############################################################################
class PermanentRecordsList(ListView):
	"""
	########################################################################
	Class: PermanentRecordList

	Allows the user to create a list of permanent record(a repair action).
		
		Methods Used In View:
		---------------------
		ListView
		
		Class View Data
		---------------
		1. Provide the model being used.
		2. Provide a Template to display data.
		3. Provide a context name.

		get_context_data
		----------------
		**kwargs
		----------------
		help_wiki : boolean
			shows or hides the help wiki button
		modelname : str
			name of the model
		machine_name : queryset
			machine name for displaying the Machine Name in the title
		machine_pk
			machine primary key

		get_success_url
		---------------
			Once updated it goes back to the detailview of the model
	########################################################################
	"""
	model = PermanentRecords
	template_name = 'mmaint/permanentnotes_list.djhtml'
	context_object_name = 'mmaint'
	
	def get_queryset(self):

		return super(PermanentRecordsList, self).get_queryset().filter(machine_id_id=self.kwargs['pk'])

	def get_context_data(self, **kwargs):
		kwargs['modelname'] = 'permanentrecords'
		kwargs['helpwiki'] = False
		kwargs['backbutton'] = 'Back'
		context = super(PermanentRecordsList, self).get_context_data(**kwargs)
		context['machine_name'] = MachineStatus.objects.get(id=self.kwargs['pk'])
		context['machine_pk'] = self.kwargs['pk']
		return context
	############################################################################
	### END CLASS OR FUNCTION: END CLASS OR FUNCTION: END CLASS OR FUNCTION: ###
	############################################################################
	############# BEGIN CLASS OR FUNCTION: BEGIN CLASS OR FUNCTION: ############
	############################################################################
class PermanentRecordsUpdate(UpdateView):
	"""
	########################################################################
	Class: PermanentRecordUpdate

	Allows the user to update a permanent record(a repair action).
		
		Methods Used In View:
		---------------------
		CreateView
		
		Class View Data
		---------------
		1. Provide the model being used.
		2. Provide a Template to display data.
		3. Provide a Form to edit the data.

		form_vaild
		----------
		Checks to make sure the form is valid and saves data.

		get_context_data
		----------------
		**kwargs
		----------------
		help_wiki : boolean
			shows or hides the help wiki button
		modelname : str
			name of the model
		create_update : str
			either create or update. Allows for both operations to be in one
			template file.

		get_success_url
		---------------
			Once updated it goes back to the detailview of the model
	########################################################################
	"""
	model = PermanentRecords
	template_name = 'mmaint/mmaint_crud.djhtml'
	form_class = PermanentRecordsForm

	def form_valid(self, form):
		return super().form_valid(form)

	def get_success_url(self):
		return reverse_lazy('machinestatusdetail', kwargs={'pk': self.object.machine_id_id})

	def get_context_data(self, **kwargs):
		kwargs['modelname'] = 'permanentrecords'
		kwargs['helpwiki'] = False
		kwargs['create_update'] = 'update'
		context = super(PermanentRecordsUpdate, self).get_context_data(**kwargs)
		return context
class PermanentRecordsDelete(DeleteView):
	"""
	########################################################################
	Class: PermanentRecordDelete

	Allows the user to delete a record from permanent record(a repair action).
		
		Methods Used In View:
		---------------------
		ListView
		
		Class View Data
		---------------
		1. Provide the model being used.
		

		get
		----------------
		self, request, *args, **kwargs
		----------------
			so we don't need a confirm delete template.
		
	########################################################################
	"""
	model = PermanentRecords
	template_name= ('mmaint/permanentrecords_confirm_delete.html')
	
	def get_success_url(self):
		return reverse_lazy('machinestatuslist')
class MachineDownReportsDelete(DeleteView):
	"""
	########################################################################
	Class: PermanentRecordDelete

	Allows the user to delete a record from permanent record(a repair action).
		
		Methods Used In View:
		---------------------
		ListView
		
		Class View Data
		---------------
		1. Provide the model being used.
		

		get
		----------------
		self, request, *args, **kwargs
		----------------
			so we don't need a confirm delete template.
		
	########################################################################
	"""
	model = MachineDownReports
	template_name= ('mmaint/machinedownreports_confirm_delete.html')
	
	def get_success_url(self):
		return reverse_lazy('machinedownreport-list', kwargs={'pk': self.object.machine_id_id})
	############################################################################
	### END CLASS OR FUNCTION: END CLASS OR FUNCTION: END CLASS OR FUNCTION: ###
	############################################################################
	############# BEGIN CLASS OR FUNCTION: BEGIN CLASS OR FUNCTION: ############
	############################################################################
class MachineDownReportsCreate(CreateView):
	"""
	########################################################################
	Class: MachineDownReportsCreate

	Allows the user to create a permanent record(a repair action).
		
		Methods Used In View:
		---------------------
		CreateView
		
		Class View Data
		---------------
		1. Provide the model being used.
		2. Provide a Template to display data.
		3. Provide a Form to edit the data.

		form_vaild
		----------
		Checks to make sure the form is valid and saves data.

		get_context_data
		----------------
		**kwargs
		----------------
		help_wiki : boolean
			shows or hides the help wiki button
		modelname : str
			name of the model
		create_update : str
			either create or update. Allows for both operations to be in one
			template file.

		get_success_url
		---------------
			Once updated it goes back to the detailview of the model
	########################################################################
	"""
	model = MachineDownReports
	template_name = 'mmaint/machinedownreports_cr.djhtml'
	form_class = MachineDownReportsForm

	def form_valid(self, form):
		form.instance.machine_id = MachineStatus.objects.get(pk=self.kwargs['pk'])
		return super(MachineDownReportsCreate, self).form_valid(form)

	def get_success_url(self):
		return reverse_lazy('machinestatusdetail', kwargs={'pk': self.object.machine_id_id})

	def get_context_data(self, **kwargs):
		kwargs['modelname'] = 'machinedownreports'
		kwargs['helpwiki'] = False
		kwargs['create_update'] = 'create'
		context = super(MachineDownReportsCreate, self).get_context_data(**kwargs)
		return context
class MachineDownReportsUpdate(UpdateView):
	"""
	########################################################################
	Class: MachineDownReportsUpdate

	Allows the user to update a permanent record(a repair action).
		
		Methods Used In View:
		---------------------
		CreateView
		
		Class View Data
		---------------
		1. Provide the model being used.
		2. Provide a Template to display data.
		3. Provide a Form to edit the data.

		form_vaild
		----------
		Checks to make sure the form is valid and saves data.

		get_context_data
		----------------
		**kwargs
		----------------
		help_wiki : boolean
			shows or hides the help wiki button
		modelname : str
			name of the model
		create_update : str
			either create or update. Allows for both operations to be in one
			template file.

		get_success_url
		---------------
			Once updated it goes back to the detailview of the model
	########################################################################
	"""
	model = MachineDownReports
	template_name = 'mmaint/machinedownreports_up.djhtml'
	form_class = MachineDownReportsForm

	def form_valid(self, form):
		return super().form_valid(form)

	def get_success_url(self):
		return reverse_lazy('machinedownreport-list', kwargs={'pk': self.object.machine_id_id})

	def get_context_data(self, **kwargs):
		kwargs['modelname'] = 'machinedownreports'
		kwargs['helpwiki'] = False
		kwargs['create_update'] = 'update'
		context = super(MachineDownReportsUpdate, self).get_context_data(**kwargs)
		return context
	############################################################################
	### END CLASS OR FUNCTION: END CLASS OR FUNCTION: END CLASS OR FUNCTION: ###
	############################################################################
	############# BEGIN CLASS OR FUNCTION: BEGIN CLASS OR FUNCTION: ############
	############################################################################
class MachineDownReportsList(ListView):
	"""
	########################################################################
	Class: MachineDownReportsList

	Allows the user to create a list of permanent record(a repair action).
		
		Methods Used In View:
		---------------------
		ListView
		
		Class View Data
		---------------
		1. Provide the model being used.
		2. Provide a Template to display data.
		3. Provide a context name.

		get_context_data
		----------------
		**kwargs
		----------------
		help_wiki : boolean
			shows or hides the help wiki button
		modelname : str
			name of the model
		machine_name : queryset
			machine name for displaying the Machine Name in the title
		machine_pk
			machine primary key

		get_success_url
		---------------
			Once updated it goes back to the detailview of the model
	########################################################################
	"""
	model = MachineDownReports
	template_name = 'mmaint/machinedownreports_list.djhtml'
	context_object_name = 'mmaint'
	
	def get_queryset(self):

		return super(MachineDownReportsList, self).get_queryset().filter(machine_id_id=self.kwargs['pk']).order_by('-endtime')

	def get_context_data(self, **kwargs):
		kwargs['modelname'] = 'machinedownreports'
		kwargs['helpwiki'] = False
		kwargs['backbutton'] = 'Back'
		context = super(MachineDownReportsList, self).get_context_data(**kwargs)
		context['machine_name'] = MachineStatus.objects.get(id=self.kwargs['pk'])
		context['machine_pk'] = self.kwargs['pk']
		return context
	
	############################################################################
	### END CLASS OR FUNCTION: END CLASS OR FUNCTION: END CLASS OR FUNCTION: ###
	############################################################################
	############# BEGIN CLASS OR FUNCTION: BEGIN CLASS OR FUNCTION: ############
	############################################################################
	############################################################################
	### END CLASS OR FUNCTION: END CLASS OR FUNCTION: END CLASS OR FUNCTION: ###
	############################################################################
	############# BEGIN CLASS OR FUNCTION: BEGIN CLASS OR FUNCTION: ############
	############################################################################
	#▓▓▓▓▓▓▓▓▓▓▓▓▓▓ BEGIN REPORTING VIEWS: BEGIN REPORTING VIEWS: ▓▓▓▓▓▓▓▓▓▓▓▓▓#
	############################################################################
class MachineStatusCharts(TemplateView):
	template_name = 'mmaint/reports/charts.djhtml'

	def get_context_data(self, *args, **kwargs):
		
		chartType = self.kwargs['chartType'].lower()
		average = []
		downtime_records = []
		downtime_records_count = []
		year = int(datetime.now().year)
		context = super(MachineStatusCharts, self).get_context_data(**kwargs)
		context['names'] = MachineDownReports.objects.values_list('machine_id__machine_name').distinct()
		
		if chartType == 'life':
			for record in context['names']:
				total_lists = MachineDownReports.objects.filter(Q(machine_id__machine_name=record[0]))
				totaldowntime = 0
				downtime_count = 0
				for total in total_lists:
					if total.endtime == None:
						totaldowntime += 0
					else:
						totaldowntime += float(total.total())
					downtime_count += 1
				downtime_records.append(round(totaldowntime,2))
				downtime_records_count.append(downtime_count)
			context['chart'] = 'Life'

		elif chartType == 'year':
			
			start_year = date(year,1,1)
			end_year = date(year,12,31)

			for record in context['names']:
				total_lists = MachineDownReports.objects.filter(Q(machine_id__machine_name=record[0]) & Q(endtime__gte=start_year) & Q(endtime__lte=end_year))
				totaldowntime = 0
				downtime_count = 0
				for total in total_lists:
					if total.endtime == None:
						totaldowntime += 0
					else:
						totaldowntime += float(total.total())
					downtime_count += 1
				downtime_records.append(round(totaldowntime,2))
				downtime_records_count.append(downtime_count)
			context['chart'] = 'Current Year'
		elif chartType == 'yearq1':
			start_year = date(year,1,1)
			end_year = date(year,3,31)
			
			for record in context['names']:
				total_lists = MachineDownReports.objects.filter(Q(machine_id__machine_name=record[0]) & Q(endtime__gte=start_year) & Q(endtime__lte=end_year))
				totaldowntime = 0
				downtime_count = 0
				for total in total_lists:
					if total.endtime == None:
						totaldowntime += 0
					else:
						totaldowntime += float(total.total())
					downtime_count += 1
				downtime_records.append(round(totaldowntime,2))
				downtime_records_count.append(downtime_count)
			context['chart'] = 'Current Year First Quarter'
		elif chartType == 'yearq2':
			start_year = date(year,4,1)
			end_year = date(year,6,30)

			for record in context['names']:
				total_lists = MachineDownReports.objects.filter(Q(machine_id__machine_name=record[0]) & Q(endtime__gte=start_year) & Q(endtime__lte=end_year))
				totaldowntime = 0
				downtime_count = 0
				for total in total_lists:
					if total.endtime == None:
						totaldowntime += 0
					else:
						totaldowntime += float(total.total())
					downtime_count += 1
				downtime_records.append(round(totaldowntime,2))
				downtime_records_count.append(downtime_count)
			context['chart'] = 'Current Year Second Quarter'

		elif chartType == 'yearq3':
			start_year = date(year,7,1)
			end_year = date(year,9,30)

			for record in context['names']:
				total_lists = MachineDownReports.objects.filter(Q(machine_id__machine_name=record[0]) & Q(endtime__gte=start_year) & Q(endtime__lte=end_year))
				totaldowntime = 0
				downtime_count = 0
				for total in total_lists:
					if total.endtime == None:
						totaldowntime += 0
					else:
						totaldowntime += float(total.total())
					downtime_count += 1
				downtime_records.append(round(totaldowntime,2))
				downtime_records_count.append(downtime_count)
			context['chart'] = 'Current Year Third Quarter'
		elif chartType == 'yearq4':
			start_year = date(year,10,1)
			end_year = date(year,12,31)

			for record in context['names']:
				total_lists = MachineDownReports.objects.filter(Q(machine_id__machine_name=record[0]) & Q(endtime__gte=start_year) & Q(endtime__lte=end_year))
				totaldowntime = 0
				downtime_count = 0
				for total in total_lists:
					if total.endtime == None:
						totaldowntime += 0
					else:
						totaldowntime += float(total.total())
					downtime_count += 1
				downtime_records.append(round(totaldowntime,2))
				downtime_records_count.append(downtime_count)
			context['chart'] = 'Current Year Fourth Quarter'
		# Gather Data
		averageLength = len(downtime_records)
		downtime_average = round(sum(downtime_records)/sum(downtime_records_count),2)
		average.append(float(downtime_average))
		context['labels'] = list(context['names'])
		context['average'] = average*averageLength
		context['downtime_records'] = downtime_records
		context['downtime_records_count'] = downtime_records_count
		return context