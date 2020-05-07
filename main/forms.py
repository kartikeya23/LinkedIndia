from django import forms
from .models import Employee, Employer


class EmployeeForm(forms.ModelForm):
	
	# name = forms.CharField(max_length=50)
	# dob = forms.DateField()
	# image = forms.ImageField(upload_to='images/')
	# phone = PhoneNumberField()
	# gender = forms.CharField(choices=GENDER_CHOICES, max_length=50, default=NOTA)
	# mail = forms.EmailField()
	# lang = forms.CharField(choices=LANGUAGE_CHOICES, max_length=50, blank=True)
	# city = forms.CharField(max_length=255)
	# location = PlainLocationField(based_fields=['city'], zoom=7)
	# adhaar = forms.CharField(max_length=12, default='0000000000')

	class Meta:
		model = Employee
		fields = '__all__'
		exclude = ['emp_status', 'location']



class EmployerForm(forms.ModelForm):
	class Meta:
		model = Employer
		fields = ('name', 'organisation')
		

class FindForm(forms.Form):
	city = forms.CharField(required=False, initial='')