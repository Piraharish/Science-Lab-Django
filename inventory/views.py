from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import *
from django.db import IntegrityError
from django.contrib import messages
from . models import *
from distribution.models import *
from analyzer. models import *

import random
def index(request):
    return render(request,'index.html')


def register_invo(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        contact = request.POST['contact']
        dateofbirth = request.POST['dateofbirth']
        address = request.POST['address']
        password = request.POST['password']
        try:
            inve_register(username=username, email=email, contact=contact, dateofbirth=dateofbirth, address=address,
                   password=password).save()
            messages.info(request, "successfully registered")
            return redirect('/login_invo/')
        except IntegrityError as e:
            messages.info(request, "name already exists")
            return redirect('/register_invo/')
    return render(request, 'inventory/register.html')


def login_invo(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            r = inve_register.objects.get(email=email, password=password)
            request.session['invo'] = r.email

            if r is not None:
                messages.info(request, 'welcome')
                return redirect('/home_invo/')
        except inve_register.DoesNotExist as e:
            messages.info(request, 'name does not exists')
            return redirect('/login_invo/')

    else:
        return render(request, 'inventory/register.html')


def home_invo(request):
    return render(request,'inventory/invo_home.html')


def inventory_registration(request):
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
            invo_register_form(name=name, contactno=contactno, email=email, dateofbirth=dateofbirth, age=age,
                 gender=gender, address=address,city=city,organisation=organisation,
                 education=education,state=state,year_of_experience=year_of_experience).save()
            messages.info(request, "successfully registered")
            return redirect('/home_invo/')
        except:
            pass
    return render(request,'inventory/registration.html')


def admin_to_inventory(request):
    if 'invo' in request.session:
        values = invo_register_form.objects.filter(app=True)
        print(values)
        return render(request, 'inventory/admin_approve.html',{'values':values})


def view_distributor(request):
    if 'invo' in request.session:
        values = distributor_form.objects.filter(approve=True)
        print(values)
        # print(values.name)
        return render(request, 'inventory/view_distributor.html', {'values': values})


def view_report1 (request):
    if 'invo' in request.session:
        values = reserch1.objects.filter(send1=True)
        print(values)
        # print(values.name)
        return render(request, 'inventory/view_report1.html', {'values': values})


def view_report2 (request):
    if 'invo' in request.session:
        values = reserch2.objects.filter(send2=True)
        print(values)
        # print(values.name)
        return render(request, 'inventory/view_report2.html', {'values': values})


def view_report3 (request):
    if 'invo' in request.session:
        values = reserch3.objects.filter(send3=True)

        # print(values.name)
        return render(request, 'inventory/view_report3.html', {'values': values})


def view_report4 (request):
    if 'invo' in request.session:
        values = reserch4.objects.filter(send4=True)
        print(values)
        # print(values.name)
        return render(request, 'inventory/view_report4.html', {'values': values})


def view_report5 (request):
    if 'invo' in request.session:
        values = reserch5.objects.filter(send5=True)
        print(values)
        # print(values.name)
        return render(request, 'inventory/view_report5.html', {'values': values})


def send_to_packing1(request, id):
    st = reserch1.objects.get(id=id)
    r = random.randint(1000,2000)
    st.packing_id1 = r
    st.save()
    return redirect('/view_report1/')


def send_to_packing2(request, id):
    st = reserch2.objects.get(id=id)
    r = random.randint(1000, 2000)
    st.packing_id2 = r
    st.save()
    return redirect('/view_report2/')


def send_to_packing3 (request,id):
    st = reserch3.objects.get(id=id)
    r = random.randint(1000, 2000)
    st.packing_id3 = r
    st.save()
    return redirect('/view_report3/')


def send_to_packing4(request, id):
    st = reserch4.objects.get(id=id)
    r = random.randint(1000, 2000)
    st.packing_id4 = r
    st.save()
    return redirect('/view_report4/')


def send_to_packing5(request, id):
    st = reserch5.objects.get(id=id)
    r = random.randint(1000, 2000)
    st.packing_id5 = r
    st.save()
    return redirect('/view_report5/')


def send1_to_distributor(request):
    if 'invo' in request.session:
        values = reserch1.objects.filter(pack1=False, accept=True)
        print(values)
        return render(request, 'inventory/send_report1.html', {'values': values})


def view_distributor1 (request,id):
    if "invo" in request.session:
        values = reserch1.objects.get(id=id)
        values.pack1 = True
        values.save()
        messages.info(request, "successfully approved")
        return redirect('/send1_to_distributor/')


def send2_to_distributor(request):
    if 'invo' in request.session:
        values = reserch2.objects.filter(pack2=False, accept1=True)
        print(values)
        return render(request, 'inventory/send_report2.html', {'values': values})


def view_distributor2 (request,id):
    if "invo" in request.session:
        values = reserch2.objects.get(id=id)
        values.pack2 = True
        values.save()
        messages.info(request, "successfully approved")
        return redirect('/send2_to_distributor/')


def send3_to_distributor(request):
    if 'invo' in request.session:
        values = reserch3.objects.filter(pack3=False,accept2=True)
        print(values)
        return render(request, 'inventory/send_report3.html', {'values': values})


def view_distributor3 (request,id):
    if "invo" in request.session:
        values = reserch3.objects.get(id=id)
        values.pack3 = True
        values.save()
        messages.info(request, "successfully approved")
        return redirect('/send3_to_distributor/')

def send4_to_distributor(request):
    if 'invo' in request.session:
        values = reserch4.objects.filter(pack4=False,accept3=True)
        print(values)
        return render(request, 'inventory/send_report4.html', {'values': values})


def view_distributor4 (request, id):
    if "invo" in request.session:
        values = reserch4.objects.get(id=id)
        values.pack4 = True
        values.save()
        messages.info(request, "successfully approved")
        return redirect('/send4_to_distributor/')


def send5_to_distributor (request):
    if 'invo' in request.session:
        values = reserch5.objects.filter(pack5=False,accept4=True)
        print(values)
        return render(request, 'inventory/send_report5.html', {'values': values})


def view_distributor5 (request, id):
    if "invo" in request.session:
        values = reserch5.objects.get(id=id)
        values.pack5 = True
        values.save()
        messages.info(request, "successfully approved")
        return redirect('/send5_to_distributor/')


def invo_logout(request):
    if 'invo' in request.session:
        request.session.pop('invo',None)
        messages.success(request,'logout already successfully')
        return redirect('/')
    else:
        messages.success(request, 'session logged out')
        return redirect('/invo_logout/')










