from django import forms
from .models import Team, Employee, Attendance


class DateInput(forms.DateInput):
    input_type = 'date'


class TeamForm(forms.ModelForm):
    crt_date = forms.DateField(widget=DateInput)

    class Meta:
        model = Team
        fields = ['team_name', 'supervisor', 'team_leader', 'crt_date', 'location']


class EmployeeForm(forms.ModelForm):
    date_of_joining = forms.DateField(widget=DateInput)
    date_of_leaving = forms.DateField(widget=DateInput)
    wage = forms.IntegerField()

    class Meta:
        model = Employee
        fields = ['promoter_id', 'promoter_name', 'address', 'city', 'state', 'pin_code', 'date_of_joining',
                  'date_of_leaving', 'kyc_document_type', 'kyc_document_number', 'wage', 'bank_name', 'name_on_account',
                  'account_number', 'ifsc_code', 'blood_group', 'emergency_number']


class AttendanceForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput)

    class Meta:
        model = Attendance
        fields = ['employee', 'time_manday', 'sale_manday', 'date']
