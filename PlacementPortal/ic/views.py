#for basic rendering of html pages
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect

#for authentication login and logout
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from company.models import JAF
from student.models import Student, Application

from .models import *
from company.models import *


def auth(user):
	return IC.objects.filter(user=user).exists()


# Create your views here.
def login(request):
	if request.POST :
		user = authenticate(username=request.POST['username'], password=request.POST['password'])
		if user is not None and auth(user):  # A backend authenticated the credentials
			if user.is_active:
				auth_login(request, user)
				return HttpResponseRedirect('/ic/home/')
		return render(request, "ic/login.html",context={'error':'invalid credentials'})
	else:
		if(request.user.is_authenticated() and auth(request.user)):
			return HttpResponseRedirect('/ic/home/')
		else:
			return render(request, "ic/login.html",context={'error':''})

@login_required()
def logout(request):
	if (not auth(request.user)):
		return redirect('/replace')
	auth_logout(request)
	return redirect('/replace')

@login_required(login_url='/ic/login/')
def home(request):
	if (not auth(request.user)):
		return redirect('/replace')
	jaf_list = list(JAF.objects.all())
	for jaf in jaf_list:
		jaf.student_count  = Application.objects.filter(jaf = jaf).count()
	verified_students = Student.objects.filter(resume_verified = True)
	unverified_students = Student.objects.filter(resume_verified = False)
	data = {'jaf_list':jaf_list, 'verified_students':verified_students, 'unverified_students':unverified_students}
	return render(request, "ic/home.html", context = data)

@login_required(login_url='/ic/login/')
def view_jaf(request,pk):
	if (not auth(request.user)):
		return redirect('/replace')
	jaf = JAF.objects.get(pk = pk)
	if (jaf is None):
		return redirect('/replace')
	application_list = Application.objects.filter(jaf = jaf)
	eligibility_list = Eligibility.objects.filter(jaf = jaf)
	test_list = JAFTest.objects.filter(jaf = jaf)
	jaf.student_count = application_list.count()
	data = {'jaf':jaf, 'application_list':application_list, 'eligibility_list':eligibility_list, 'test_list': test_list}
	return render(request, "ic/jaf.html", context = data)