from django.shortcuts import render, HttpResponse, redirect
from models import User
from django.contrib import messages
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
    
    return render (request, 'LoginAndReg/index.html')

def register(request):
	error_messages = {}
	if request.method == "POST":
		result = User.registerMgr.userRegister(request.POST['first_name'], request.POST['last_name'], request.POST['email'], request.POST['password'], request.POST['confirm_password'], request.POST['birthday'])
		if result[0]:
		    request.session['login'] = result[1].id
		    return redirect(reverse('beltReviewer:index'))
		else:
		    error_messages = result[1]
		    return render(request, 'LoginAndReg/index.html',  error_messages )
	else:
		pass

def login(request):
	error_messages = {}
	if request.method == "POST":
		result = User.loginMgr.login(request.POST['email'], request.POST['password'])
		if result[0]:
			user = User.loginMgr.get(email = request.POST['email'])
			request.session['login'] = user.id
			# messages.info(request, 'Three Credits remain')
			# messages.error(request, "Entered BLA BLA BLA")

			return redirect(reverse('beltReviewer:index'))
		else:
			error_messages = result[1]
			return render(request, 'LoginAndReg/index.html',  error_messages )
	else:
		return redirect ('/')

def success(request):
    
    return render (request, 'LoginAndReg/success.html')
