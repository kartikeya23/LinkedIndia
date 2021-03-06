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
		labels = {
			'name': 'यहाँ अपना नाम लिखो',
			'dob': 'अपनी उमर यहाँ दर्ज करें',
			'city': 'अपने शहर का नाम यहाँ दर्ज करें',
			'lang': 'अपनी भाषा चुनें',
			'phone': '"यहां अपना फोन नंबर डालें',
			'adhaar': 'यहां अपना आधार नंबर दर्ज करें',
			'gender': 'यहाँ अपना लिंग बताईं',
			'mail': 'यहाँ अपनी ई-मेल लिखें',
			'skills': 'न्यूनतम शिक्षा की आवश्यकताा [80 शब्द]',
			'education': 'अपने शिक्षा स्तर को इंगित करें',
			'salary': 'अपेक्षित भुगतान बताईं',
			'experience': 'यहां वांछित कौशल दर्ज करें',
			'image': 'अपनी एक तस्वीर डालें (आवश्यक नहीं)'
		}



class EmployerForm(forms.ModelForm):
	class Meta:
		model = Employer
		fields = ('name', 'organisation')
		

class FindForm(forms.Form):
	city = forms.CharField(required=False)
	language = forms.ChoiceField(choices=(Employee.LANGUAGE_CHOICES), required=False)

