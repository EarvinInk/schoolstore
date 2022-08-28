from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages


# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        c_password = request.POST['c_password']

        if password == c_password:
            if User.objects.filter(username=username):
                messages.info(request, "username allready exists")
                return redirect('credentials:register')


            else:
                user = User.objects.create_user(username=username,
                                                password=password)
                user.save()
                print("user created")
                return redirect('credentials:login')
        else:
            messages.info(request, 'Password dose not match')
            return redirect('credentials:register')
    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid credentials")
            return redirect('credentials:login')

    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('credentials:login')
