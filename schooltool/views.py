from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
# Create your views here.

def index(request):
  return render(request, 'schooltool/index.html')


def signup(request):
    context = {"error": False}
    if request.method == "GET":
        return render(request, 'schooltool/signup.html', context)
    elif request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        if 'is_staff' in request.POST:
          is_staff = True
        else:
          is_staff = False
        try:
            user = User.objects.create_user(username=username, password=password, is_staff=is_staff)
            print(user)
            if user is not None:
                return login(request)
        except:
            context["error"] = f"User {username} already exists"
            return render(request, 'schooltool/signup.html', context)
