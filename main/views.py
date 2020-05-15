from django.shortcuts import render, redirect, get_object_or_404
from .forms import EmployeeForm, EmployerForm, FindForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Employee

# Create your views here.
def home(request):
	return render(request, 'main/landing.html')

def apply_job(request):
	if request.method == 'POST':
		form = EmployeeForm(request.POST, request.FILES)
		print(request.FILES['image'])
		print('recieved new form')
		if form.is_valid():
			print('form is valid')
			new_emp = form.save(commit=False)
			new_emp.name = new_emp.name.title()
			new_emp.save()
		else:
			print('invalid form')
			print(form.errors)
			return render(request, 'main/apply.html', {'form': form})
		return redirect('success')
	form = EmployeeForm()
	return render(request, 'main/apply.html', {'form': form})



def success(request):
	return render(request, 'main/apply_success.html')


def signup(request):
	if request.method == 'POST':
		u_form = UserCreationForm(request.POST)
		e_form = EmployerForm(request.POST)
		if u_form.is_valid() and e_form.is_valid():
			print('both form are valid')
			user = u_form.save()
			emp = e_form.save(commit=False)
			print('Employer account created')
			emp.user = user
			emp.name = emp.name.title()
			emp.save()
			print(f"Creater new employer: {emp.name}")
			login(request, user)
			return redirect('find')
		else:
			print('invalid form')
			print('user:')
			print(u_form.errors)
			print('employ:')
			print(e_form.errors)
			return render(request, 'registration/signup.html', {
				'u_form': u_form,
				'e_form': e_form
				})
	u_form = UserCreationForm()
	e_form = EmployerForm()
	return render(request, 'registration/signup.html', {
		'u_form': u_form,
		'e_form': e_form
		})


@login_required()
def find(request):
	user = request.user
	try:
		emp = user.employer
	except:
		print('error you have been logged out')
		return redirect('logout')
	employees = Employee.objects.all()[:15]
	# if request.method == 'GET':
	# 	form = FindForm(request.GET)
	# 	return render(request, 'main/find.html', {'form': form, 'employees': employees})
	# else:
	# 	form = FindForm(request.POST)
	# 	# print()
	# 	if form.is_valid():
	# 		error = None
	# 		data = form.cleaned_data
	# 		print(data)
	# 		if data['city'] != '':
	# 			employees = employees.filter(city=data['city'])
	# 		employees.filter(lang=data['language'])
	# 		print(employees)
	# 		if not employees.exists():
	# 			error = 'None were found with matching parameters'
	return render(request, 'main/find.html', {'employees': employees}) #, 'error': error, 'form': form,})
	return redirect('home')


@login_required()
def details(request, emp_id):
  employee = get_object_or_404(Employee, pk=emp_id)
  return render(request, 'main/details.html',{'employee':employee})