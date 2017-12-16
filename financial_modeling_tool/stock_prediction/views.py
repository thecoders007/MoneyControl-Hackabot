from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.http import HttpResponse
from nasdaq_stock_quote import Share
import requests
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


from nsetools import Nse

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
	nse = Nse()

	top_gainers = nse.get_top_gainers()
	top_losers = nse.get_top_losers()
	r = requests.get('https://www.quandl.com/api/v3/datasets/NSE/NIFTY_50.json?api_key=oqf4vFLPo8MrPBGXVjki')
	nifty = r.json()

	nifty_price = []
	nifty_date = []

	count = 0
	for i in nifty['dataset']['data']:

		nifty_date.append(i[0])	
		nifty_price.append(i[1])

		if count == 30:
			break
		else:
			count = count + 1

	print(nifty_date)

	w_symbol = []
	l_symbol = []
	w_price = []
	l_price = []
	w_hprice = []
	l_hprice = []
	w_lprice = []
	l_lprice = []
	w_oprice = []
	l_oprice = []

	count = 0
	for i in top_gainers:
		w_symbol.append(i['symbol'])
		w_price.append(i['ltp'])
		w_hprice.append(i['highPrice'])
		w_lprice.append(i['lowPrice'])
		w_oprice.append(i['openPrice'])

		if count == 2:
			break
		else:
			count = count + 1


	count = 0
	for i in top_losers:
		l_symbol.append(i['symbol'])
		l_price.append(i['ltp'])
		l_hprice.append(i['highPrice'])
		l_lprice.append(i['lowPrice'])
		l_oprice.append(i['openPrice'])

		if count == 2:
			break
		else:
			count = count + 1

	
	loop1 = zip(w_symbol,w_price,w_hprice,w_lprice,w_oprice)
	loop2 = zip(l_symbol,l_price,l_hprice,l_lprice,l_oprice)

	nifty_date = json.dumps(nifty_date)

	return render(request,'mainpage.html',{'loop1':loop1,'loop2':loop2,
	 'nifty_price' : nifty_price, 'nifty_date' : nifty_date})


def classes(request):
	nse = Nse()
	a = ['ABB','DMART','BHEL','TITAN','TATAPOWER','INDIGO','IDEA','MRF','PNB','GODREJCP','LICHSGFIN','JSWSTEEL']
	price = []
	hprice = []
	lprice = []
	oprice = []
	for i in a:
		 q = nse.get_quote(i)
		 price.append(q['averagePrice'])
		 hprice.append(q['dayHigh'])
		 lprice.append(q['dayLow'])
		 oprice.append(q['closePrice'])
	loop = zip(a,price,hprice,lprice,oprice)



	return render(request,'classes.html',{'loop' : loop})


def compare(request):
	return render(request,'compare.html')



def add_stock(request):
	a = json.loads(request.body.decode('utf-8'))
	print (a)

	r = requests.get('https://www.quandl.com/api/v3/datasets/NSE/'+a['stock']+'.json?api_key=oqf4vFLPo8MrPBGXVjki')
	nifty = r.json()


	nifty_price = []
	nifty_date = []

	count = 0
	for i in nifty['dataset']['data']:

		nifty_date.append(i[0])	
		nifty_price.append(i[1])

		if count == 60:
			break
		else:
			count = count + 1

	pnifty_price = []
	pnifty_date = []

	for i in range(0,29):
		pnifty_date.append(i)
		pnifty_price.append(i)


	json_data = {
		'nifty_price' : nifty_price,
		'nifty_date' : nifty_date,
		'pnifty_price' : pnifty_price,
		'pnifty_date' : pnifty_date
	}


	return JsonResponse({'data':json_data})



@csrf_exempt
def respond_chat(request):
	if request.method == 'POST':
		a = json.loads((request.body.decode("utf-8")))
		print (a)


		# b = (a["result"]["parameters"]["Book"])
		# c = (a["result"]["parameters"]["City"])
		# books = str(Book.objects.filter(book1 = b,city = c))
		# words = books.split()
		# print(a)
		# locname = words[6] 
		# libname = words[7]
		# libname = libname.strip('>]>')
		# print(locname)
		# print(libname)
		# finalstring = "The queried book is available in " + libname + " library at " + locname
		# print(finalstring)
		# return JsonResponse({	
		#       "speech": finalstring,
		#       "messages": [
		#         {
		#           "type": 0,
		#           "speech": finalstring
		#         }]})