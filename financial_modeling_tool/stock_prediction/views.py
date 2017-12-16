from django.shortcuts import render

# Create your views here.

def register(request):
	return render(request,'register.html')


def login(request):
	return render(request,'login.html')


def logout(request):
	return render(request)


def main(request):
	return render(request)


def classes(request):
	return render(request)


def compare(request):
	return render(request)
