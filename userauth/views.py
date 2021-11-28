from django.http import request, response,HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages


def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect("/")
            
        else:
            return render(request, "errors/400.html")
    
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
            return render(request, 'errors/400.html')
        if emailtest:
            return render(request, 'errors/400.html')
         
        user = User(email = email, username= username, password =password)
        user.set_password(password)
        user.save()
        return render(request, 'login.html')
    return render(request,'register.html')


    

