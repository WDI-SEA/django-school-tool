from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User


# Create your views here.

def index(request):
  return render(request, 'schooltool/index.html')

def login(request):
    context = {"Error": False}
    if request.method == "GET":
        return render(request, 'schooltool/login.html')
    if request.method == "POST":
        email = request.post["email"]
        password = request.post["password"]
        user = auth.authenticated(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            context = {"Error": "User not authenticated"}
            return redirect('login')
