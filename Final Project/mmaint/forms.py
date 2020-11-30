from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, HTML
from .models import MachineStatus, PermanentRecords, MachineDownReports
from flatpickr import DateTimePickerInput
from ckeditor.widgets import CKEditorWidget

class MachineStatusForm(forms.ModelForm):
    class Meta:
        model = MachineStatus
        fields = ['machine_name', 'machine_row', 'machine_e2name', 'notes', 'downtime',]
        widgets = {'notes': forms.TextInput(attrs={'autofocus': 'autofocus', 'onkeyup': 'charcountupdate(this.value)', }),}

    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)
        self.helper =  FormHelper(self)
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
				Column('machine_name', css_class='form-group col-md-6 col-sm-12 col-12'),
                Column('machine_row', css_class='form-group col-md-6 col-sm-12 col-12'),
                css_class='form-row'
			),

			Row(
				Column('machine_e2name', css_class='form-group col-md-6 col-sm-12 col-12'),
                Column('downtime', css_class='form-group col-md-6 col-sm-12 col-12'),
				css_class='form-row'
			),
			
            Row(
                Column('notes', css_class='form-group col-md-8 col-sm-8 col-8'),
                HTML('<small><span id="charcount" class="form-group text-danger" style="float: right; position: relative; top: 40px;"></span></small>'),
				
			),
		)

class PermanentRecordsForm(forms.ModelForm):
    class Meta:
        model = PermanentRecords
        fields = ['reason', 'note']

    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)
        self.helper =  FormHelper(self)
        self.helper.form_tag = False
        self.helper.layout = Layout(
			Row(
                Column('reason', css_class='form-group col-md-12 col-sm-12 col-12'),
                css_class='form_row'
			),

            Row(   
				Column('note', css_class='form-group col-md-12 col-sm-12 col-12'),
				css_class='form_row'
			),
		)
class MachineDownReportsForm(forms.ModelForm):
    class Meta:
        model = MachineDownReports
        fields = ['starttime', 'endtime']
        widgets = {'starttime': DateTimePickerInput(),
                    'endtime': DateTimePickerInput(),
        }
    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)
        self.helper =  FormHelper(self)
        self.helper.form_tag = False
        self.helper.layout = Layout(
			Row(
                Column('starttime', css_class='form-group col-md-6 col-sm-6 col-6 flatpickr'),
                Column('endtime', css_class='form-group col-md-6 col-sm-6 col-6 flatpickr'),
                css_class='form_row'
			),
		)