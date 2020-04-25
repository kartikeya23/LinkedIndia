from django.db import models
from location_field.models.plain import PlainLocationField
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

class Employer(models.Model):

	name = models.CharField(max_length=50)
	organisation = models.CharField(max_length=100)
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	class Meta:
		verbose_name = "Employer"
		verbose_name_plural = "Employers" 


	def __str__(self):
		return self.name		


class Employee(models.Model):

	HINDI = 'HI'
	ENGLISH = 'EN'
	MARATHI = 'MR'
	RAJASTHANI = 'RJ'

	LANGUAGE_CHOICES = (
		(HINDI, 'Hindi'),
		(ENGLISH, 'English'),
		(MARATHI, 'Marathi'),
		(RAJASTHANI, 'Rajasthani'))

	name = models.CharField(max_length=50)
	dob = models.DateField()
	image = models.ImageField(upload_to='images/')
	phone = PhoneNumberField()
	mail = models.EmailField()
	lang = models.CharField(choices=LANGUAGE_CHOICES, max_length=50)
	city = models.CharField(max_length=255)
	location = PlainLocationField(based_fields=['city'], zoom=7)
	emp_status = models.BooleanField(default=False)


	class Meta:
		verbose_name = "Employee"
		verbose_name_plural = "Employees"

	def __str__(self):
			return self.name
		
		
