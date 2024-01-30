from django.shortcuts import render
from django.shortcuts import *
from django.contrib import messages
from . models import *
from distribution.models import *
from research.models import *
from inventory.models import *

# Create your views here.


def index(request):
    return render(request,'index.html')


def tech_admin(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        print(email)
        if email == "admin@gmail.com" and password == "admin":
            print(email)
            request.session['admin'] = "admin@gmail.com"
            messages.info(request, "Successfully Registered ")
            return render(request,'admin/admin_home.html')
        elif email != "admin@gmail.com":
            messages.error(request, "Wrong Mail id")
            return render (request,'admin/register.html')
        elif password != "admin":
            messages.error(request,"wrong password")
            return render (request, 'admin/register.html')
        else:
            return render(request,'admin/register.html')
    return render(request,'admin/register.html')


def admin_home(request):
    return render(request,'admin/admin_home.html')


def approve_distributor(request):
    if 'admin' in request.session:
        values = distributor_form.objects.filter(approve=False)
        print(values)
        return render(request, 'admin/approve_distributor.html', {'values': values})
    # else:
    #     return redirect('/approve_distributor/')


def approve_true(request,id):
    if "admin" in request.session:
        values = distributor_form.objects.get(id=id)
        values.approve = True
        values.save()
        messages.info(request, "successfully approved")
        return redirect('/approve_distributor/')

def approve_research(request):
    if 'admin' in request.session:
        values = form.objects.filter(admin_approve=False)
        print(values)
        return render(request, 'admin/approve_research.html', {'values': values})
    # else:
    #     return redirect('/approve_distributor/')


def send_research(request,id):
    if "admin" in request.session:
        values = form.objects.get(id=id)
        values.admin_approve = True
        values.save()
        messages.info(request, "successfully approved")
        return redirect('/approve_research/')

def inventory_approve(request):
    if 'admin' in request.session:
        values = invo_register_form.objects.filter(app=False)
        print(values)
        return render(request, 'admin/approve_inventory.html', {'values': values})



def send_inventory(request,id):
    if "admin" in request.session:
        values = invo_register_form.objects.get(id=id)
        values.app = True
        values.save()
        messages.info(request, "successfully approved")
        return redirect('/inventory_approve/')





def admin_logout(request):
    if 'admin' in request.session:
        request.session.pop('admin',None)
        messages.success(request,'logout already successfully')
        return redirect('/')
    else:
        messages.success(request, 'session logged out')
        return redirect('/admin_logout/')
