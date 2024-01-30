from django.shortcuts import render
from django.shortcuts import *
from django.db import IntegrityError
from django.contrib import messages
from . models import *
# from analyzer. models import register
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import AdaBoostClassifier
from sklearn.datasets import make_classification
import warnings
warnings.filterwarnings('ignore')
data = pd.read_csv('test1.csv')


def index(request):
    return render(request,'index.html')


def register_analyse(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        contact = request.POST['contact']
        dateofbirth = request.POST['dateofbirth']
        address = request.POST['address']
        password = request.POST['password']
        try:
            register(username=username, email=email, contact=contact, dateofbirth=dateofbirth, address=address,
                   password=password).save()
            messages.info(request, "successfully created")
            return redirect('/login/')
        except IntegrityError as e:
            messages.info(request, "name already exists")
            return redirect('/register_analyse/')
    return render(request, 'analyzer/register.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            r = register.objects.get(email=email, password=password)
            request.session['analyzer'] = r.email
            print(request.session['analyzer'])
            if r is not None:
                messages.info(request, 'welcome')
                return redirect('/home/')
        except register.DoesNotExist as e:
            messages.info(request, 'name does not exists')
            return redirect('/login/')

    else:
        return render(request, 'analyzer/register.html')


def home(request):
    return render(request,'analyzer/ana_home.html')

def analyze1(request):
    if request.method=="POST":
        Disease = request.POST['Disease']
        symptoms = request.POST['symptoms']
        tablet = request.POST['tablet']
        composition = request.POST['composition']
        price = request.POST['price']
        Medicine = request.POST['Medicine']
        side_effect = request.POST['side_effect']
        sevearity = request.POST['sevearity']
        reserch1(Disease=Disease,symptoms=symptoms,tablet=tablet,composition=composition,price=price,Medicine=Medicine,
                 side_effect=side_effect,sevearity=sevearity).save()
        messages.info(request, "successfully registered")
        return redirect('/home/')
    return render(request,'analyzer/research_medi.html')

def analyze2(request):
    if request.method=="POST":
        Disease = request.POST['Disease']
        symptoms = request.POST['symptoms']
        tablet = request.POST['tablet']
        composition = request.POST['composition']
        price = request.POST['price']
        Medicine = request.POST['Medicine']
        side_effect = request.POST['side_effect']
        sevearity = request.POST['sevearity']
        reserch2(Disease=Disease, symptoms=symptoms, tablet=tablet, composition=composition, price=price,
                 Medicine=Medicine,
                 side_effect=side_effect, sevearity=sevearity).save()
        messages.info(request, "successfully registered")
        return redirect('/home/')


    return render(request,'analyzer/research2.html')

def analyze3(request):
    if request.method=="POST":
        Disease = request.POST['Disease']
        symptoms = request.POST['symptoms']
        tablet = request.POST['tablet']
        composition = request.POST['composition']
        price = request.POST['price']
        Medicine = request.POST['Medicine']

        side_effect = request.POST['side_effect']
        sevearity = request.POST['sevearity']
        reserch3(Disease=Disease, symptoms=symptoms, tablet=tablet, composition=composition, price=price,
                 Medicine=Medicine,
                 side_effect=side_effect, sevearity=sevearity).save()
        messages.info(request, "successfully registered")
        return redirect('/home/')



    return render(request,'analyzer/research3.html')

def analyze4(request):
    if request.method=="POST":
        Disease = request.POST['Disease']
        symptoms = request.POST['symptoms']
        tablet = request.POST['tablet']
        composition = request.POST['composition']
        price = request.POST['price']
        Medicine = request.POST['Medicine']

        side_effect = request.POST['side_effect']
        sevearity = request.POST['sevearity']
        reserch4(Disease=Disease, symptoms=symptoms, tablet=tablet, composition=composition, price=price,
                 Medicine=Medicine,
                 side_effect=side_effect, sevearity=sevearity).save()
        messages.info(request, "successfully registered")
        return redirect('/home/')



    return render(request,'analyzer/research4.html')


def analyze5(request):
    if request.method=="POST":
        Disease = request.POST['Disease']
        symptoms = request.POST['symptoms']
        tablet = request.POST['tablet']
        composition = request.POST['composition']
        price = request.POST['price']
        Medicine = request.POST['Medicine']
        side_effect = request.POST['side_effect']
        sevearity = request.POST['sevearity']
        reserch5(Disease=Disease, symptoms=symptoms, tablet=tablet, composition=composition, price=price,
                 Medicine=Medicine,
                 side_effect=side_effect, sevearity=sevearity).save()
        messages.info(request, "successfully registered")
        return redirect('/home/')


    return render(request,'analyzer/research5.html')


def send_company(request):
    if 'analyzer' in request.session:
        values = forms.objects.filter(view=False,solution__isnull=True,solution1__isnull=True, solution2__isnull=True,
                                      solution3__isnull =True,solution4__isnull =True)
        return render(request,'analyzer/view',{'values': values})
    else:
        return redirect('/send_company/')

def move_company (request,id):
    if "analyzer" in request.session:
        values = forms.objects.get(id=id)
        values.view = True
        values.save()
        messages.info(request, "successfully sent")
        return redirect('/send_company/')

def table1(request):
    values = reserch1.objects.all()
    if 'analyzer' in request.session:
        values = reserch1.objects.all()
        return render(request,'analyzer/table1.html',{'values':values})
    return render(request, 'analyzer/table1.html', {'values': values})


def algo(datas,r):
    print('hi')
    # print(datas.isnull().sum())
    # df = pd.DataFrame(pd.read_excel("research.xlsx"))
    # read_file = pd.read_excel("research.xlsx")
    # read_file.to_csv("research.csv", header=True, index=False)
    # df = pd.DataFrame(pd.read_csv("test1.csv"))
    data = pd.read_csv('test1.csv')
    print(data.isnull().sum())
    data_x = data.iloc[:, :-1]
    data_y = data.iloc[:, -1]
    string_datas = [i for i in data_x.columns if data_x.dtypes[i] == np.object_]

    LabelEncoders = []
    for i in string_datas:
        newLabelEncoder = LabelEncoder()
        data_x[i] = newLabelEncoder.fit_transform(data_x[i])
        LabelEncoders.append(newLabelEncoder)
    ylabel_encoder = None
    if type(data_y.iloc[1]) == str:
        ylabel_encoder = LabelEncoder()
        data_y = ylabel_encoder.fit_transform(data_y)

    model = AdaBoostClassifier()
    model.fit(data_x, data_y)

    value = {data_x.columns[i]: datas[i] for i in range(len(datas))}
    l = 0
    for i in string_datas:
        z = LabelEncoders[l]
        value[i] = z.transform([value[i]])[0]
        l += 1
    value = [i for i in value.values()]
    predicted = model.predict([value])
    print(12334455)
    if ylabel_encoder:
        predicted = ylabel_encoder.inverse_transform(predicted)
    return predicted[0]

def get_input1 (request, id):
    get = reserch1.objects.get(id=id)
    r=get.id
    inputvar = []
    get.save()

    a = get.Disease
    b = get.symptoms
    c = get.tablet
    d = get.composition
    e = get.price
    l = get.Medicine
    h = get.side_effect
    k = get.sevearity
    print(a)
    print(b)
    inputvar.append(a)
    inputvar.append(b)
    inputvar.append(c)
    inputvar.append(d)
    inputvar.append(e)
    inputvar.append(l)
    inputvar.append(h)
    inputvar.append(k)

    print('input:', inputvar)
    f=algo(inputvar,r)
    print('OUTPUT:',f)
    st = reserch1.objects.filter(id=r).update(solution=f)

    return redirect('/home/')

def table2(request):
    values = reserch2.objects.all()
    if 'analyzer' in request.session:
        values = reserch2.objects.all()
        return render(request,'analyzer/table2.html',{'values':values})
    return render(request, 'analyzer/table2.html', {'values': values})

def algo1(datas,r):
    # print(datas)
    # df = pd.DataFrame(pd.read_excel("test2.xlsx"))
    # read_file = pd.read_excel("test2.xlsx")
    # read_file.to_csv("test2.csv", header=True, index=False)
    # df = pd.DataFrame(pd.read_csv("test2.csv"))
    data = pd.read_csv('test2.csv')
    print(data.isnull().sum())
    data_x = data.iloc[:, :-1]
    data_y = data.iloc[:, -1]
    string_datas = [i for i in data_x.columns if data_x.dtypes[i] == np.object_]
    print('hi')

    LabelEncoders = []
    for i in string_datas:
        newLabelEncoder = LabelEncoder()
        data_x[i] = newLabelEncoder.fit_transform(data_x[i])
        LabelEncoders.append(newLabelEncoder)
    ylabel_encoder = None
    if type(data_y.iloc[1]) == str:
        ylabel_encoder = LabelEncoder()
        data_y = ylabel_encoder.fit_transform(data_y)

    model = AdaBoostClassifier()
    model.fit(data_x, data_y)

    value = {data_x.columns[i]: datas[i] for i in range(len(datas))}
    l = 0
    for i in string_datas:
        z = LabelEncoders[l]
        value[i] = z.transform([value[i]])[0]
        l += 1
    value = [i for i in value.values()]
    predicted = model.predict([value])
    print(12334455)
    if ylabel_encoder:
        predicted = ylabel_encoder.inverse_transform(predicted)
    return predicted[0]

def get_input2(request, id):
    get = reserch2.objects.get(id=id)
    r=get.id
    inputvar = []
    get.save()

    a = get.Disease
    b = get.symptoms
    c = get.tablet
    d = get.composition
    e = get.price
    l = get.Medicine
    h = get.side_effect
    k = get.sevearity
    print(a)
    print(b)
    inputvar.append(a)
    inputvar.append(b)
    inputvar.append(c)
    inputvar.append(d)
    inputvar.append(e)
    inputvar.append(l)
    inputvar.append(h)
    inputvar.append(k)

    print('input:', inputvar)
    f=algo1(inputvar,r)
    print('OUTPUT:',f)
    st = reserch2.objects.filter(id=r).update(solution1=f)

    return redirect('/home/')

def table3(request):
    values = reserch3.objects.all()
    if 'analyzer' in request.session:
        values = reserch3.objects.all()
        return render(request,'analyzer/table3.html',{'values':values})
    return render(request, 'analyzer/table3.html', {'values': values})

def algo2(datas,r):
    # print(datas)
    # df = pd.DataFrame(pd.read_excel("research3.xlsx"))
    # read_file = pd.read_excel("research3.xlsx")
    # read_file.to_csv("research3.csv", header=True, index=False)
    # df = pd.DataFrame(pd.read_csv("research3.csv"))
    data = pd.read_csv('research3.csv')
    data_x = data.iloc[:, :-1]
    data_y = data.iloc[:, -1]
    string_datas = [i for i in data_x.columns if data_x.dtypes[i] == np.object_]

    LabelEncoders = []
    for i in string_datas:
        newLabelEncoder = LabelEncoder()
        data_x[i] = newLabelEncoder.fit_transform(data_x[i])
        LabelEncoders.append(newLabelEncoder)
    ylabel_encoder = None
    if type(data_y.iloc[1]) == str:
        ylabel_encoder = LabelEncoder()
        data_y = ylabel_encoder.fit_transform(data_y)

    model = AdaBoostClassifier()
    model.fit(data_x, data_y)

    value = {data_x.columns[i]: datas[i] for i in range(len(datas))}
    l = 0
    for i in string_datas:
        z = LabelEncoders[l]
        value[i] = z.transform([value[i]])[0]
        l += 1
    value = [i for i in value.values()]
    predicted = model.predict([value])
    print(12334455)
    if ylabel_encoder:
        predicted = ylabel_encoder.inverse_transform(predicted)
    return predicted[0]

def get_input3(request, id):
    get = reserch3.objects.get(id=id)
    r=get.id
    inputvar = []
    get.save()

    a = get.Disease
    b = get.symptoms
    c = get.tablet
    d = get.composition
    e = get.price
    l = get.Medicine
    h = get.side_effect
    k = get.sevearity
    print(a)
    print(b)
    inputvar.append(a)
    inputvar.append(b)
    inputvar.append(c)
    inputvar.append(d)
    inputvar.append(e)
    inputvar.append(l)
    inputvar.append(h)
    inputvar.append(k)

    print('input:', inputvar)
    f=algo2(inputvar,r)
    print('OUTPUT:',f)
    st = reserch3.objects.filter(id=r).update(solution2=f)

    return redirect('/home/')

def table4(request):
    values = reserch4.objects.all()
    if 'analyzer' in request.session:
        values = reserch4.objects.all()
        return render(request,'analyzer/table4.html',{'values':values})
    return render(request, 'analyzer/table4.html', {'values': values})

def algo3(datas,r):
    # print(datas)
    # df = pd.DataFrame(pd.read_excel("research4.xlsx"))
    # read_file = pd.read_excel("research4.xlsx")
    # read_file.to_csv("research4.csv", header=True, index=False)
    # df = pd.DataFrame(pd.read_csv("research4.csv"))
    data = pd.read_csv('research4.csv')
    data_x = data.iloc[:, :-1]
    data_y = data.iloc[:, -1]
    string_datas = [i for i in data_x.columns if data_x.dtypes[i] == np.object_]

    LabelEncoders = []
    for i in string_datas:
        newLabelEncoder = LabelEncoder()
        data_x[i] = newLabelEncoder.fit_transform(data_x[i])
        LabelEncoders.append(newLabelEncoder)
    ylabel_encoder = None
    if type(data_y.iloc[1]) == str:
        ylabel_encoder = LabelEncoder()
        data_y = ylabel_encoder.fit_transform(data_y)

    model = AdaBoostClassifier()
    model.fit(data_x, data_y)

    value = {data_x.columns[i]: datas[i] for i in range(len(datas))}
    l = 0
    for i in string_datas:
        z = LabelEncoders[l]
        value[i] = z.transform([value[i]])[0]
        l += 1
    value = [i for i in value.values()]
    predicted = model.predict([value])
    print(12334455)
    if ylabel_encoder:
        predicted = ylabel_encoder.inverse_transform(predicted)
    return predicted[0]

def get_input4(request, id):
    get = reserch4.objects.get(id=id)
    r=get.id
    inputvar = []
    get.save()

    a = get.Disease
    b = get.symptoms
    c = get.tablet
    d = get.composition
    e = get.price
    l = get.Medicine
    h = get.side_effect
    k = get.sevearity
    print(a)
    print(b)
    inputvar.append(a)
    inputvar.append(b)
    inputvar.append(c)
    inputvar.append(d)
    inputvar.append(e)
    inputvar.append(l)
    inputvar.append(h)
    inputvar.append(k)

    print('input:', inputvar)
    f=algo3(inputvar,r)
    print('OUTPUT:',f)
    st = reserch4.objects.filter(id=r).update(solution3=f)

    return redirect('/home/')

def table5(request):
    values = reserch5.objects.all()
    if 'analyzer' in request.session:
        values = reserch5.objects.all()
        return render(request,'analyzer/table5.html',{'values':values})
    return render(request, 'analyzer/table5.html', {'values': values})

def algo4(datas,r):
    # print(datas)
    # df = pd.DataFrame(pd.read_excel("research5.xlsx"))
    # read_file = pd.read_excel("research5.xlsx")
    # read_file.to_csv("research5.csv", header=True, index=False)
    # df = pd.DataFrame(pd.read_csv("research5.csv"))
    data = pd.read_csv('research5.csv')
    data_x = data.iloc[:, :-1]
    data_y = data.iloc[:, -1]
    string_datas = [i for i in data_x.columns if data_x.dtypes[i] == np.object_]

    LabelEncoders = []
    for i in string_datas:
        newLabelEncoder = LabelEncoder()
        data_x[i] = newLabelEncoder.fit_transform(data_x[i])
        LabelEncoders.append(newLabelEncoder)
    ylabel_encoder = None
    if type(data_y.iloc[1]) == str:
        ylabel_encoder = LabelEncoder()
        data_y = ylabel_encoder.fit_transform(data_y)

    model = AdaBoostClassifier()
    model.fit(data_x, data_y)

    value = {data_x.columns[i]: datas[i] for i in range(len(datas))}
    l = 0
    for i in string_datas:
        z = LabelEncoders[l]
        value[i] = z.transform([value[i]])[0]
        l += 1
    value = [i for i in value.values()]
    predicted = model.predict([value])
    print(12334455)
    if ylabel_encoder:
        predicted = ylabel_encoder.inverse_transform(predicted)
    return predicted[0]

def get_input5(request, id):
    get = reserch5.objects.get(id=id)
    r=get.id
    inputvar = []
    get.save()

    a = get.Disease
    b = get.symptoms
    c = get.tablet
    d = get.composition
    e = get.price
    l = get.Medicine
    h = get.side_effect
    k = get.sevearity
    print(a)
    print(b)
    inputvar.append(a)
    inputvar.append(b)
    inputvar.append(c)
    inputvar.append(d)
    inputvar.append(e)
    inputvar.append(l)
    inputvar.append(h)
    inputvar.append(k)

    print('input:', inputvar)
    f=algo4(inputvar,r)
    print('OUTPUT:',f)
    st = reserch5.objects.filter(id=r).update(solution4=f)

    return redirect('/home/')

def view_analyze1(request):
    if 'analyzer' in request.session:
        values = reserch1.objects.filter(accept=False)
        return render(request,'analyzer/view1.html',{'values': values})
    else:
        return redirect('/view_analyze1/')
def send_analyze1(request,id):
    if "analyzer" in request.session:
        print('hi')
        values = reserch1.objects.get(id=id)
        values.accept= True
        values.save()
        print('hi')
        messages.info(request, "successfully sent")
        return redirect('/view_analyze1/')


def reject_analyze1(request):
    if 'analyzer' in request.session:
        values = reserch1.objects.filter(reject=False)
        return render(request, 'analyzer/view1.html', {'values': values})
    else:
        return redirect('/reject_analyze1/')


def delete_analyze1(request, id):
    if "analyzer" in request.session:
        print('hi')
        values = reserch1.objects.get(id=id)
        values.reject = True
        values.save()
        print('hi')
        messages.info(request, "successfully sent")
        return redirect('/reject_analyze1/')


def view_analyze2(request):
    if 'analyzer' in request.session:
        values = reserch2.objects.filter(accept1=False)
        return render(request,'analyzer/view2.html',{'values': values})
    else:
        return redirect('/view_analyze2/')
def send_analyze2(request,id):
    if "analyzer" in request.session:
        print('hi')
        values = reserch2.objects.get(id=id)
        values.accept1= True
        values.save()
        print('hi')
        messages.info(request, "successfully sent")
        return redirect('/view_analyze2/')
def reject_analyze2(request):
    if 'analyzer' in request.session:
        values = reserch2.objects.filter(reject1=False)
        return render(request, 'analyzer/view2.html', {'values': values})
    else:
        return redirect('/reject_analyze2/')


def delete_analyze2(request, id):
    if "analyzer" in request.session:
        print('hi')
        values = reserch2.objects.get(id=id)
        values.reject1 = True
        values.save()
        print('hi')
        messages.info(request, "successfully sent")
        return redirect('/reject_analyze2/')


def view_analyze3(request):
    if 'analyzer' in request.session:
        values = reserch3.objects.filter(accept2=False)
        return render(request,'analyzer/view3.html',{'values': values})
    else:
        return redirect('/view_analyze3/')
def send_analyze3(request,id):
    if "analyzer" in request.session:
        print('hi')
        values = reserch3.objects.get(id=id)
        values.accept2= True
        values.save()
        print('hi')
        messages.info(request, "successfully sent")
        return redirect('/view_analyze3/')
def reject_analyze3(request):
    if 'analyzer' in request.session:
        values = reserch3.objects.filter(reject2=False)
        return render(request, 'analyzer/view3.html', {'values': values})
    else:
        return redirect('/reject_analyze3/')


def delete_analyze3(request, id):
    if "analyzer" in request.session:
        print('hi')
        values = reserch3.objects.get(id=id)
        values.reject2 = True
        values.save()
        print('hi')
        messages.info(request, "successfully sent")
        return redirect('/reject_analyze3/')

def view_analyze4(request):
    if 'analyzer' in request.session:
        values = reserch4.objects.filter(accept3=False)
        return render(request,'analyzer/view4.html',{'values': values})
    else:
        return redirect('/view_analyze4/')
def send_analyze4(request,id):
    if "analyzer" in request.session:
        print('hi')
        values = reserch4.objects.get(id=id)
        values.accept3= True
        values.save()
        print('hi')
        messages.info(request, "successfully sent")
        return redirect('/view_analyze4/')
def reject_analyze4(request):
    if 'analyzer' in request.session:
        values = reserch4.objects.filter(reject3=False)
        return render(request, 'analyzer/view4.html', {'values': values})
    else:
        return redirect('/reject_analyze4/')


def delete_analyze4(request, id):
    if "analyzer" in request.session:
        print('hi')
        values = reserch4.objects.get(id=id)
        values.reject3 = True
        values.save()
        print('hi')
        messages.info(request, "successfully sent")
        return redirect('/reject_analyze4/')

def view_analyze5(request):
    if 'analyzer' in request.session:
        values = reserch5.objects.filter(accept4=False)
        return render(request,'analyzer/view5.html',{'values': values})
    else:
        return redirect('/view_analyze5/')
def send_analyze5(request,id):
    if "analyzer" in request.session:
        print('hi')
        values = reserch5.objects.get(id=id)
        values.accept4= True
        values.save()
        print('hi')
        messages.info(request, "successfully sent")
        return redirect('/view_analyze5/')
def reject_analyze5(request):
    if 'analyzer' in request.session:
        values = reserch5.objects.filter(reject4=False)
        return render(request, 'analyzer/view5.html', {'values': values})
    else:
        return redirect('/reject_analyze5/')


def delete_analyze5(request, id):
    if "analyzer" in request.session:
        print('hi')
        values = reserch5.objects.get(id=id)
        values.reject4 = True
        values.save()
        print('hi')
        messages.info(request, "successfully sent")
        return redirect('/reject_analyze5/')



def logout(request):
    if 'analyzer' in request.session:
        request.session.pop('analyzer',None)
        messages.success(request,'logout already successfully')
        return redirect('/')
    else:
        messages.success(request, 'session logged out')
        return redirect('/logout')




