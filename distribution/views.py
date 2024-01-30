from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import *
from django.db import IntegrityError
from django.contrib import messages
from . models import *
from analyzer. models import *


def index(request):
    return render(request,'index.html')


def register_distri(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        contact = request.POST['contact']
        dateofbirth = request.POST['dateofbirth']
        address = request.POST['address']
        password = request.POST['password']
        try:
            dis_register(username=username, email=email, contact=contact, dateofbirth=dateofbirth, address=address,
                   password=password).save()
            messages.info(request, "successfully registered")
            return redirect('/login_distri/')
        except IntegrityError as e:
            messages.info(request, "name already exists")
            return redirect('/register_distri/')
    return render(request, 'distri/dis_register.html')


def login_distri(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            r = dis_register.objects.get(email=email, password=password)
            request.session['distri'] = r.email

            if r is not None:
                messages.info(request, 'welcome')
                return redirect('/home_disrtibution/')
        except dis_register.DoesNotExist as e:
            messages.info(request, 'name does not exists')
            return redirect('/login_distri/')

    else:
        return render(request, 'distri/dis_register.html')


def home_disrtibution(request):
    return render(request,'distri/dis_home.html')


def register_form(request):
    if request.method=="POST":
        name = request.POST['name']
        print(name)
        contactno =request.POST['contactno']
        email = request.POST['email']
        dateofbirth =request.POST['dateofbirth']
        age =request.POST['age']
        gender =request.POST['gender']
        address = request.POST['address']
        print(address)
        city=request.POST['city']
        organisation=request.POST['organisation']
        state=request.POST['state']
        education=request.POST['education']
        year_of_experience=request.POST['year_of_experience']
        try:
            distributor_form(name=name, contactno=contactno, email=email, dateofbirth=dateofbirth, age=age,
                 gender=gender, address=address,city=city,organisation=organisation,
                 education=education,state=state,year_of_experience=year_of_experience).save()
            messages.info(request, "successfully registered")
            return redirect('/register_form/')
        except:
            pass
    return render(request,'distri/distributor_form.html')


def admin_view_distributor(request):
    if 'distri' in request.session:
        values = distributor_form.objects.filter(approve=True)

        # print(values.name)
        return render(request, 'distri/show_approve.html', {'values': values})


def view_tablet1(request):
    if 'distri' in request.session:
        values = reserch1.objects.filter(pack1=True)

        # print(values.name)
        return render(request, 'distri/tablet1.html', {'values': values})


def view_tablet2(request):
    if 'distri' in request.session:
        values = reserch2.objects.filter(pack2=True)

        # print(values.name)
        return render(request, 'distri/tablet2.html', {'values': values})


def view_tablet3(request):
    if 'distri' in request.session:
        values = reserch3.objects.filter(pack3=True)

        # print(values.name)
        return render(request, 'distri/tablet3.html', {'values': values})


def view_tablet4(request):
    if 'distri' in request.session:
        values = reserch4.objects.filter(pack4=True)

        # print(values.name)
        return render(request, 'distri/tablet4.html', {'values': values})


def view_tablet5(request):
    if 'distri' in request.session:
        values = reserch5.objects.filter(pack5=True)

        # print(values.name)
        return render(request, 'distri/tablet5.html', {'values': values})


def dis_logout(request):
    if 'distri' in request.session:
        request.session.pop('distri',None)
        messages.success(request,'logout already successfully')
        return redirect('/')
    else:
        messages.success(request, 'session logged out')
        return redirect('/dis_logout/')





