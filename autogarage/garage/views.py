from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'garage/index.html')

def appointment(request):
    return render(request,'garage/appointment.html')

def contact(request):
    return render(request,'garage/contact.html')

def edit_profile(request):
    return render(request,'garage/edit_profile.html')

def forgot(request):
    return render(request,'garage/forgot.html')

def login(request):
    return render(request,'garage/login.html')

def map(request):
    return render(request,'garage/map.html')

def register(request):
    return render(request,'garage/register.html')

def service(request):
    return render(request,'garage/service.html')

def verify(request):
    return render(request,'garage/verify.html')
