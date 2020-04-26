from django.shortcuts import render, redirect
from .forms import EmployeeForm

# Create your views here.
def home(request):
	return render(request, 'main/landing.html')

def apply_job(request):
	if request.method == 'POST':
		form = EmployeeForm(request.POST)
		print('recieved new form')
			# print('form is valid')
		new_emp = form.save(commit=False)
		new_emp.name = new_emp.name.title()
		print('New Employee: ')
		print(f'Name: {new_emp.name}')
		new_emp.save()
		return redirect('success')
	form = EmployeeForm()
	return render(request, 'main/apply.html', {'form': form})


def success(request):
	return render(request, 'main/apply_success.html')