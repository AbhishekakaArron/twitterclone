from django.http import response,HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from .forms import UserRegisterForm
from django.contrib import messages

# def index(request):
#     print(request.user)
#     if request.user.is_anonymous:
#         return redirect("/login") 
#     return render(request, 'twitterhome/home.html')


def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect("/")
            
        else:
            messages.error(request, "Bad Credentials!!")
            return HttpResponse('bad request')
    
    return render(request, "login.html")


def logoutUser(request):
    logout(request)
    messages.info(request, 'logged out successfully')
    return render(request, "login.html")


def registerUser(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')
    if username and password and email:
        usertest = User.objects.filter(username=username).exists()
        emailtest = User.objects.filter(email=email).exists()
        if usertest:
            return HttpResponse('username already exists')
        if emailtest:
            return HttpResponse('email already exists')
         
        user = User(email = email, username= username, password =password)
        user.set_password(password)
        user.save()
        return render(request, 'login.html')
    return render(request,'register.html')


def handle400(request, exception):
    return(render(request, "400.html", status=400))