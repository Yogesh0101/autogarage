from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'user/index.html')

def autogarage(request):
    return render(request,'user/autogarage.html')

def book(request):
    return render(request,'user/book.html')

def contact(request):
    return render(request,'user/contact.html')

def edit_profile(request):
    return render(request,'user/edit_profile.html')

def forgot(request):
    return render(request,'user/forgot.html')

def login(request):
    return render(request,'user/login.html')

def map(request):
    return render(request,'user/map.html')

def notification(request):
    return render(request,'user/notification.html')

def profile(request):
    return render(request,'user/profile.html')

def register(request):
    return render(request,'user/register.html')

def search(request):
    return render(request,'user/search.html')

def verify(request):
    return render(request,'user/verify.html')
