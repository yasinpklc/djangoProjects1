from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from Library.models import Category,Library
from home.models import Settings


# Create your views here.
def index(request):
    setting = Settings.objects.get(pk=1)
    category = Category.objects.all()
    sliderdata = Library.objects.all().order_by('?')[0:6]
    newLibrary= Library.objects.order_by('-create_at')[0:4]
    context= {'setting': setting, 'page': 'home','sliderdata': sliderdata,'newLibrary':newLibrary,'category':category}

    return render(request,'index.html',context)
def hakkimizda(request):
    setting = Settings.objects.get(pk = 1)
    categorydata = Category.objects.all()
    sliderdata = Library.objects.all().order_by('?')[0:6]
    category = Category.objects.all()
    context = {'setting':setting, 'page': 'hakkimizda','categorydata': categorydata,'sliderdata': sliderdata,'category':category}
    return render(request, 'hakkimizda.html', context)

def oduncverme(request):
    setting = Settings.objects.get(pk = 1)
    categorydata = Category.objects.all()
    sliderdata = Library.objects.all().order_by('?')[0:6]
    category = Category.objects.all()
    context = {'setting':setting, 'page': 'oduncverme','categorydata': categorydata,'sliderdata': sliderdata,'category':category}
    return render(request, 'oduncverme.html', context)

def iletisim(request):
    setting = Settings.objects.get(pk = 1)
    categorydata = Category.objects.all()
    sliderdata = Library.objects.all().order_by('?')[0:6]
    category = Category.objects.all()
    context = {'setting':setting, 'page': 'iletisim','categorydata': categorydata,'sliderdata': sliderdata,'category':category}
    return render(request, 'iletisim.html', context)

def sikcasorulansorular(request):
    setting = Settings.objects.get(pk = 1)
    categorydata = Category.objects.all()
    sliderdata = Library.objects.all().order_by('?')[0:6]
    category = Category.objects.all()
    context = {'setting':setting, 'page': 'sikcasorulansorular','categorydata': categorydata,'sliderdata': sliderdata,'category':category}
    return render(request, 'sikcasorulansorular.html', context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/login/')
    category = Category.objects.all()
    context = {'category': category, }
    return render(request, 'login.html', context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')