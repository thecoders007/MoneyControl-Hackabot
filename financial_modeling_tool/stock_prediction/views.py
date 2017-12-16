from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.http import HttpResponse
from nasdaq_stock_quote import Share
import requests
import json


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
	a =['AAPL','MSFT','YHOO'] 
	# a_prev = []
	# a_volume = []
	# a_perct = []
	# a_high = []
	# a_low = []
	# a_price = []
	# for i in a:
	# 	share = Share(i)
	# 	print share,"asdasdads"
	# 	prev = share.get_prev_close()
	# 	price = share.get_price()
	# 	name = share.get_name()
	# 	volume = share.get_volume()
	# 	perct = share.get_percent_change()
	# 	high = share.get_day_high()
	# 	low = share.get_day_low()
	# 	perct = float(perct)
	# 	perct = perct*100
	# 	perct = str(perct)
	# 	print prev
	# 	# a_prev.append(prev)
	# 	# a_volume.append(volume)
	# 	# a_perct.append(perct)
	# 	# a_high.append(high)
	# 	# a_low.append(low)
	# 	print name

	# print a_prev
	# loop = zip(a,a_prev,a_volume,a_price,a_low,a_high,a_perct)
	# print loop

	prev = []
	high = []
	low = []
	close = []
	volume = []

	for i in a:
			r = requests.get('https://www.quandl.com/api/v3/datasets/EOD/AAPL.json?api_key=oqf4vFLPo8MrPBGXVjki')
			stock_json = r.json()
			# s_json.append(stock_json)
			print stock_json['dataset']['data'][0]
			prev.append(stock_json['dataset']['data'][0][1])
			high.append(stock_json['dataset']['data'][0][2])
			low.append(stock_json['dataset']['data'][0][3])
			close.append(stock_json['dataset']['data'][0][4])
			volume.append(stock_json['dataset']['data'][0][5])

	# print s_json

	# print stock_json

	# s_json.encode("utf-8")
	loop = zip(a,prev,high,low,close,volume)
	print loop

	return render(request,'mainpage.html',{'loop' : loop})


def classes(request):
	return render(request,'classes.html')


def compare(request):
	return render(request,'compare.html')
