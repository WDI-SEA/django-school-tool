from django.shortcuts import render
from .models import Course

# Create your views here.

def index(request):
  return render(request, 'schooltool/index.html')

def courses(request):
  context = {
    "courses" :  Course.objects.all()
  }
  return render(request, 'schooltool/courses.html', context)

  return render(request, 'schooltool/index.html')

def profile(request):
  context = {"error": False}
  if request.user.is_authenticated:
    return render(request, 'schooltool/secret.html')
  else:
    context["error"] = "Not authenticated"
    return render(request, 'schooltool/signup.html', context)
