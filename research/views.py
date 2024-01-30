from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import *
from django.db import IntegrityError
from django.contrib import messages
from . models import *
from analyzer.models import *


def index(request):
    return render(request,'index.html')


def register_research(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        contact = request.POST['contact']
        dateofbirth = request.POST['dateofbirth']
        address = request.POST['address']
        password = request.POST['password']
        try:
            research_register(username=username, email=email, contact=contact, dateofbirth=dateofbirth, address=address,
                   password=password).save()
            messages.info(request, "successfully registered")
            return redirect('/login_research/')
        except IntegrityError as e:
            messages.info(request, "name already exists")
            return redirect('/register_research/')
    return render(request, 'research/register.html')


def login_research(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            r = research_register.objects.get(email=email, password=password)
            request.session['research'] = r.email
            print(request.session['research'])
            if r is not None:
                messages.info(request, 'welcome')
                return redirect('/home_research/')
        except research_register.DoesNotExist as e:
            messages.info(request, 'name does not exists')
            return redirect('/login_research/')

    else:
        return render(request, 'research/register.html')


def home_research(request):
    return render(request,'research/new.html')




def registration(request):
    if request.method=="POST":
        name = request.POST['name']
        contactno =request.POST['contactno']
        email = request.POST['email']
        dateofbirth =request.POST['dateofbirth']
        age =request.POST['age']
        gender =request.POST['gender']
        address = request.POST['address']
        city=request.POST['city']
        organisation=request.POST['organisation']
        state=request.POST['state']
        Degree=request.POST['Degree']
        year_of_experience=request.POST['year_of_experience']
        print(year_of_experience)
        try:
            form(name=name, contactno=contactno, email=email, dateofbirth=dateofbirth, age=age,
                 gender=gender, address=address,city=city,organisation=organisation,
                 Degree=Degree,state=state,year_of_experience=year_of_experience).save()
            messages.info(request, "successfully registered")
            return redirect('/home_research/')
        except:
            pass
    return render(request, 'research/register_form.html')
def view_admin_research(request):
    values = form.objects.filter(admin_approve=True)
    if 'research' in request.session:
        values = form.objects.filter(admin_approve=True)
    return render(request, 'research/view_admin_approve.html', {'values': values})


def report1(request):
    values = reserch1.objects.filter(accept=True)
    if 'research' in request.session:
        values = reserch1.objects.filter(accept=True)
    return render(request, 'research/report1.html', {'values': values})



def report2(request):
    values = reserch2.objects.filter(accept1=True)
    if 'research' in request.session:
        values = reserch2.objects.filter(accept1=True)
    return render(request, 'research/report2.html', {'values': values})

def report3(request):
    values = reserch3.objects.filter(accept2=True)
    if 'research' in request.session:
        values = reserch3.objects.filter(accept2=True)
    return render(request, 'research/report3.html', {'values': values})

def report4(request):
    values = reserch4.objects.filter(accept3=True)
    if 'research' in request.session:
        values = reserch4.objects.filter(accept3=True)
    return render(request, 'research/report4.html', {'values': values})

def report5(request):
    values = reserch5.objects.filter(accept4=True)
    if 'research' in request.session:
        values = reserch5.objects.filter(accept4=True)
    return render(request, 'research/report5.html', {'values': values})

def send_invo1(request):
    if 'research' in request.session:
        values = reserch1.objects.filter(send1=False)
        print(values)
        return render(request, 'research/report1.html', {'values': values})



def view_invo1(request,id):
    if "research" in request.session:
        values = reserch1.objects.get(id=id)
        values.send1 = True
        values.save()
        messages.info(request, "successfully sent to inventory Team")
        return redirect('/send_invo1/')


def send_invo2(request):
    if 'research' in request.session:
        values = reserch2.objects.filter(send2=False)
        print(values)
        return render(request, 'research/report2.html', {'values': values})


def view_invo2(request, id):
    if "research" in request.session:
        values = reserch2.objects.get(id=id)
        values.send2 = True
        values.save()
        messages.info(request, "successfully sent to inventory Team")
        return redirect('/send_invo2/')


def send_invo3(request):
    if 'research' in request.session:
        values = reserch3.objects.filter(send3=False)
        print(values)
        return render(request, 'research/report3.html', {'values': values})


def view_invo3(request, id):
    if "research" in request.session:
        values = reserch3.objects.get(id=id)
        values.send3 = True
        values.save()
        messages.info(request, "successfully sent to inventory Team")
        return redirect('/send_invo3/')


def send_invo4(request):
    if 'research' in request.session:
        values = reserch4.objects.filter(send4=False)
        print(values)
        return render(request, 'research/report4.html', {'values': values})


def view_invo4(request, id):
    if "research" in request.session:
        values = reserch4.objects.get(id=id)
        values.send4 = True
        values.save()
        messages.info(request, "successfully sent to inventory Team")
        return redirect('/send_invo4/')


def send_invo5(request):
    if 'research' in request.session:
        values = reserch5.objects.filter(send5=False)
        print(values)
        return render(request, 'research/report5.html', {'values': values})


def view_invo5(request, id):
    if "research" in request.session:
        values = reserch5.objects.get(id=id)
        values.send5 = True
        values.save()
        messages.info(request, "successfully sent to inventory Team")
        return redirect('/send_invo5/')









def research_logout(request):
    if 'research' in request.session:
        request.session.pop('research',None)
        messages.success(request,'logout already successfully')
        return redirect('/')
    else:
        messages.success(request, 'session logged out')
        return redirect('/research_logout/')






