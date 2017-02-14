from django.shortcuts import render, redirect
from .models import Course
# Create your views here.

def index(request):
<<<<<<< HEAD
  return render(request, 'schooltool/index.html')

def edit_course(request, course_id):
    if request.user.is_staff:
        if request.method == "GET":
            context = {
                "course": Course.objects.get(pk=course_id)
            }
            context["course"].start_date = context["course"].start_date.strftime('%Y-%m-%d')
            context["course"].end_date = context["course"].end_date.strftime('%Y-%m-%d')
            
            return render(request, 'schooltool/edit_course.html', context)

        elif request.method == "POST":
            if request.POST["request"] == "PUT":
                title = request.POST["title"]
                max_students = request.POST["max_students"]
                start_date = request.POST["start_date"]
                end_date = request.POST["end_date"]
                Course.objects.filter(pk=course_id).update(title=title, max_students=max_students, start_date=start_date, end_date=end_date)
                return redirect('/courses/' + course_id + '/edit')
    else:
        return redirect('/courses/' + course_id)
=======
 return render(request, 'schooltool/index.html')

def profile(request):
   context = {"error": False}
   if request.user.is_authenticated:
       return render(request, 'schooltool/secret.html')
   else:
       context["error"] = "Not authenticated"
       return render(request, 'schooltool/signup.html', context)
>>>>>>> 3dd47cc3beeb170caf7ebdb473668dd9e29293ea
