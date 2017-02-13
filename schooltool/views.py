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
