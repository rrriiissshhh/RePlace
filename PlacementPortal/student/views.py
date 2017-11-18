from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

from .models import *
from company.models import JAF, Category

HOME_URL = '/'

def auth(user):
    return Student.objects.filter(user=user).exists()

def get_student(user):
    return Student.objects.get(user = user)

@login_required()
def logout(request):
    if auth(request.user):
        auth_logout(request)
    return redirect(HOME_URL)

@login_required()
def home(request):
    if (not auth(request.user)):
        return redirect(HOME_URL)
    student = get_student(request.user)
    data = {'student': student}    
    return render(request, "student/home.html", context=data)

@login_required()
def upload_resume(request):
    if (not auth(request.user)):
        return redirect(HOME_URL)
    if request.method=="POST":
        return redirect('/student/')
    else:
        pass

@login_required()
def my_jobs(request):
    if (not auth(request.user)):
        return redirect(HOME_URL)
    if request.method=="GET":
        selection_list = Application.objects.filter(is_selected=True, student=get_student(request.user))
        data = {'selection_list': selection_list}
        return render(request, "student/my_jobs.html", context=data)
    else:
        jaf = JAF.objects.get(id=request.POST["id"])
        application = Application.objects.get(jaf=jaf, is_selected=True, student=get_student(request.user))
        application.review = request.POST['review']
        application.save();
        return redirect("/student/my_jobs/")

@login_required()
def see_jafs(request):
    student = auth(request.user)
    if not student:
        return redirect(HOME_URL)
    jaf_list = JAF.objects.all()
   
    if request.method=="POST":
        print(request.POST)
        all_categorys = [category.type for category in Category.objects.all()]
        categorys = [key for key in request.POST.keys() if key in all_categorys]
        jaf_list = jaf_list.filter(company__category__type__in=categorys)

        if 'cansign' in request.POST.keys():
            jaf_list = jaf_list.filter(eligibility__department=student.department, eligibility__program=student.program, eligibility__cpi_cutoff__lt=student.cpi)

        if 'signed' in request.POST.keys():
            jaf_list = jaf_list.filter(application__student=student)

    data = {'jaf_list': jaf_list}
    return render(request, "student/jaf_list.html", context=data)
