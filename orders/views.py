from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Item, Category
# Create your views here.
def index(request):
    return render(request, "orders/index.htm")


def login(request):
    return render(request, "orders/login.htm")


def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "orders/login.htm", {"message": "Invalid credentials."})


def register(request):
    return render(request, "orders/register.htm")


def logout(request):
    logout(request)
    return render(request, "users/login.html", {"message": "Logged out."})
