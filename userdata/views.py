from django.shortcuts import render, redirect
from userdata.forms import RegisterForm, LoginForm
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/products")
        else:
            messages.info(request, 'User not found!')
            return redirect("/login")
    else:
        form = LoginForm(request.POST)
        render(request, 'registration/login.html')
    return render(request, "registration/login.html", {"form": form})


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Registered!')
        return redirect('/login')
    else:
        form = RegisterForm()
    return render(request, "userdata/register.html", {"form": form})
