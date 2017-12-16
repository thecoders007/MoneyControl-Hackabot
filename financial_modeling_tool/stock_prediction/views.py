from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.http import HttpResponse


# Create your views here.

def register(request):
	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		password1 = request.POST['password1']
		password2 = request.POST['password2']


		
		if password1 != password2:
			return HttpResponse("Enter Password Correctly")
			
		user = User.objects.create(username=email,first_name=name,email=email)
		user.set_password(password1)
		
		
		user.save()
		user = authenticate(username = email, password = password1)
		if user:
			auth_login(request, user)
			return redirect('/main/')
		
	else:

		return render(request,"register.html")




def login(request):
	if request.method == 'POST':
		email = request.POST['email']
		password = request.POST['password']
		user = authenticate(username = email, password = password)
		if user:
			auth_login(request, user)
			return redirect('/main/')
		else:
			return render(request, 'login.html',{'context' : 'Wrong username or password'})

	else:	
		return render(request, 'login.html')
	


def logout(request):
	if request.user.is_authenticated():
		auth_logout(request)
	else:
		return HttpResponse("invalid")
	return render(request,'login.html')
	


def main(request):
	return render(request,'disease.html')


def classes(request):
	return render(request)


def compare(request):
	return render(request)
