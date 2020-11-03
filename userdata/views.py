from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegisterForm, LoginForm
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
            return redirect("/registration")
    else:
        form = LoginForm(request.POST)
        render(request, 'authentication/login.html')
    return render(request, "authentication/login.html", {"form": form})


def register(response):
    if response.method == 'POST':
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form = RegisterForm()
    return render(response, 'registration/register.html', {'form': form})

# def registration(response):
#     if response.method == "POST":
#         form = RegisterForm(response.POST)
#         if form.is_valid():
#             form.save()
#         return redirect("/login")
#     else:
#         form = RegisterForm()
#     return render(response, 'registration/registration.html', {"form": form})

    # if request.method == "POST":
    #     form = RegisterForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request, 'Successfully Registered!')
    #     return redirect('/login')
    # else:
    #     form = RegisterForm()
    # return render(request, "registration/registration.html", {"form": form})
