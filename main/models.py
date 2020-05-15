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

	LANGUAGE_CHOICES = (
		(HINDI, 'हिन्दी'),
		(ENGLISH, 'English'),
	)

	MALE = 'M'
	FEMALE = 'F'
	NOTA = 'N'

	GENDER_CHOICES = (
		(MALE, 'पुरुष'),
		(FEMALE, 'महिला'),
		(NOTA, 'कोई वरीयता नहीं')
	)

	COLLEGE = 'C'
	PRIMARY = 'P'
	HIGH_SCHOOL = 'H'

	EDU_CHOICES = (
		(PRIMARY, 'प्राथमिक विद्यालय'),
		(HIGH_SCHOOL, 'उच्च विद्यालय'),
		(COLLEGE, 'कॉलेज')
	)

	name = models.CharField(max_length=50)
	dob = models.DateField()
	image = models.ImageField(upload_to='images/', blank=True)
	phone = PhoneNumberField()
	gender = models.CharField(choices=GENDER_CHOICES, max_length=50, default=NOTA)
	mail = models.EmailField()
	lang = models.CharField(choices=LANGUAGE_CHOICES, max_length=50, blank=True)
	city = models.CharField(max_length=255)
	location = PlainLocationField(based_fields=['city'], zoom=7)
	adhaar = models.CharField(max_length=12, default='123456789012')
	emp_status = models.BooleanField(default=False)
	#skills related
	skills = models.CharField(max_length=80)
	education = models.CharField(choices=EDU_CHOICES, max_length=50)
	salary = models.PositiveIntegerField()
	experience = models.PositiveSmallIntegerField()


	class Meta:
		verbose_name = "Employee"
		verbose_name_plural = "Employees"

	def __str__(self):
			return self.name
		
		
