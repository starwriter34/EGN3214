from django.db import models
from django.db.models.query import prefetch_related_objects
from django.urls import reverse
from datetime import datetime, timedelta
import numpy as np
from .choices import machine_rows, machine_status, record_choice
from django.core.mail import EmailMessage
from django.conf import settings

class MachineStatus(models.Model):

	status = models.CharField(verbose_name='Machine Status', max_length=1, choices=machine_status, default='3')
	notes = models.CharField(max_length= 150, verbose_name='Notes', null=True, blank=True, help_text='150 Character Limit.')
	downtime = models.DateTimeField(auto_now=False, null=True, blank=True, help_text='If the machine is down enter Time and Date as shown: YYYY-MM-DD HH:MM:SS')
	machine_name = models.CharField(verbose_name='Machine Name', max_length=10,)
	machine_row = models.CharField(verbose_name='Machine Row', max_length=1, choices=machine_rows)
	machine_e2name = models.CharField(verbose_name='Work Station Name', max_length=10,)
	
	class Meta:
		verbose_name = 'Machine Status'
		verbose_name_plural = 'Machine Status'
		ordering = ['status', 'machine_name']
		permissions = [
            ("pso_indicating_fixture", "PSO's Indicating the fixture status"),
            ("pm_preventative_maintenance", "Can put machine into preventative maintenance status"),
			('machine_down_supervisor', 'Only has access to put machine up or down'),
			('mmaint_all', 'Will see all buttons for Machine Status')
        ]

	def __str__(self):
		return f'{self.machine_name}'

	def get_absolute_url(self):
		return reverse('machinestatuslist')

	@classmethod
	def sendemail(self, pk, status, *arg, **kwargs):
		machine = MachineStatus.objects.get(id=pk)
		if status == 'Down':
			d = str(datetime.now())[:19]
			if settings.DEBUG == True:
				email_to = ['Chris Oakley <oakley@keltecweapons.com>',]
				test_message = 'This is a Test'
				subject_line = f'This is a Test - Machine {status}'
			elif settings.DEBUG == False:
				test_message = None
				email_to = ['Chris Oakley <oakley@keltecweapons.com>',
							'Adrian Kellgren <akellgren@keltecweapons.com>',
							'Zack Flass <zachf@keltecweapons.com>',
							'Tom L <toml@keltecweapons.com>', 
				]
				subject_line = f'Machine {status}'
		elif status == 'Up':
			d = str(datetime.now())[:19]
			if settings.DEBUG == True:
				subject_line = f'This is a Test - Machine {status}'
				test_message = 'This is a Test'
				email_to = ['Chris Oakley <oakley@keltecweapons.com>',]
			elif settings.DEBUG == False:
				test_message = None
				subject_line = f'Machine {status}'
				email_to = ['Chris Oakley <oakley@keltecweapons.com>',
							'Adrian Kellgren <akellgren@keltecweapons.com>',
				]
		email_body=f'''
			<html>
			<head></head>
			<body>
			<h2>Machine {status} {test_message}</h2>
			<p style="font-size:16px"> The following machine<strong> {machine.machine_name}</strong> went {status.lower()} at {d} </p>
			</body>
			</html>
			'''
		
		email = EmailMessage(subject_line, email_body, 
					from_email='Bullet Support <6s1lmv7cwelgo3p10284h4g8547r5b@gmail.com>' , to=email_to)
		email.content_subtype = 'html'
		email.send()

	@classmethod
	def machinedown(self, pk):
		MachineStatus.objects.update_or_create(id=pk, defaults={'status': '1', 'downtime': datetime.now() })

	@classmethod
	def machinePM(self, pk):
		MachineStatus.objects.update_or_create(id=pk, defaults={'status': '2', 'downtime': datetime.now(), 'notes': 'Down for Preventative Maintence' })
	
	@classmethod
	def machineFixture(self, pk):
		MachineStatus.objects.update_or_create(id=pk, defaults={'status': '3', 'downtime': datetime.now(), 'notes': 'Down for Fixture Indication' })

	@classmethod
	def machinerunning(self, pk):
		machine = MachineStatus.objects.update_or_create(id=pk, defaults={'status': '4', 'downtime': None, 'notes': None })

class PermanentRecords(models.Model):
	
	machine_id = models.ForeignKey(MachineStatus, on_delete=models.CASCADE, verbose_name='Machine Number', related_name='machine_names')
	reason = models.CharField(max_length=2, verbose_name='Reason for Record', choices=record_choice)
	date = models.DateField(auto_now_add=True, verbose_name='Date')
	time = models.TimeField(auto_now_add=True, verbose_name='Time')
	note = models.TextField(verbose_name='Note', null=True, blank=True)

	class Meta:
		verbose_name = 'Repair Action Records'
		verbose_name_plural = 'Repair Actions Records'
		# ordering = ['-date',]

	def __str__(self):
		return f'{self.machine_id.machine_name}-{self.date}'

	@classmethod
	def machinedown_note(self, pk):
		PermanentRecords.objects.create(machine_id_id=pk, reason=5)

class MachineDownReports(models.Model):
	machine_id = models.ForeignKey('MachineStatus', on_delete=models.CASCADE, verbose_name='Machine Number', related_name='machines')
	starttime = models.DateTimeField(auto_now=False, null=True, blank=True,)
	endtime = models.DateTimeField(auto_now=False, null=True, blank=True,)
	status = models.CharField(max_length=20, null=True, blank=True,)
	
	def total(self):
		
		if self.endtime == None and self.status == 'Machine Down':
			busday = 'Machine Down No Calculation'
		else:
			if np.busday_count(datetime.date(self.starttime), datetime.date(self.endtime)) > 1:
				if datetime.time(self.starttime) == datetime.time(self.endtime):
					busday = np.busday_count(datetime.date(self.starttime), datetime.date(self.endtime))
					busdayhours = self.endtime-self.starttime
					busday = (busdayhours.seconds+(busday+1)*(86400))/3600
					busday = f'{busday:.2f}'
				else:
					busday = np.busday_count(datetime.date(self.starttime), datetime.date(self.endtime))
					busdayhours = self.endtime-self.starttime
					busday = (busdayhours.seconds+(busday*86400))/3600
					busday = f'{busday:.2f}'
			else:
				busdaytd = self.endtime - self.starttime
				busday = busdaytd.seconds / 3600
				busday = f'{busday:.2f}'

		return busday

	class Meta:
		verbose_name = 'Machine Down Reports'
		verbose_name_plural = 'Machine Down Reports'

	def __str__(self):
		return f'Machine {self.machine_id}'

	@classmethod
	def machinedown_re(self, pk):
		MachineDownReports.objects.create(machine_id_id=pk, starttime=datetime.now(), status='Machine Down')

	@classmethod
	def machinerunning_re(self, pk):
		getrecord = MachineDownReports.objects.filter(machine_id_id=pk, endtime=None)
		getrecord.update(endtime=datetime.now(), status='Machine Running')
		