from django.shortcuts import render,get_object_or_404
from .models import *
from django.http import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def login(request):
    if request.method=='POST':
        mobile=request.POST['mobile']
        password=request.POST['password']

        try:
            auser=auth.authenticate(mobile=mobile,password=password)
            if auser is not None:
                auth.login(request,'adminpanel/index.html')
            else:
                return render(request,'adminpanel/login.html')
        except auth.ObjectNotExist:
            print("invalid user")
    else:
        return render(request,'adminpanel/login.html')


def index(request):
    return render(request,'adminpanel/index.html')

def add_garage(request):
    return render(request,'adminpanel/add_garage.html')

def view_garage(request):
    return render(request,'adminpanel/view_garage.html')

def adsreq(request):
    return render(request,'adminpanel/adsreq.html')

def advertise(request):
    return render(request,'adminpanel/advertise.html')

def calendar(request):
    return render(request,'adminpanel/calendar.html')

def garage_request(request):
    return render(request,'adminpanel/garage_request.html')
    
def messages(request):
    return render(request,'adminpanel/messages.html')

def users(request):
    return render(request,'adminpanel/users.html')

def profile(request):
    return render(request,'adminpanel/profile.html')

def setting(request):
    return render(request,'adminpanel/setting.html')