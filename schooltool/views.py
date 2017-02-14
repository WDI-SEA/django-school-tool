from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Course, Staff, Student
# Create your views here.

def index(request):
  context = {
    "courses": Course.objects.all()
  }
  return render(request, 'schooltool/index.html', context)

def create_course(request):
	if request.method == "GET":
		context = {
			"courses": Course.objects.all()
			# "courses": Course.objects.filter(user_id = request.user.id).select_related()
		}
		return render(request, 'schooltool/create_course.html', context)
	elif request.method == "POST":
		# if request.user.is_authenticated:
			new_course = Course()
			new_course.title = request.POST["title"]
			new_course.start_date = request.POST["start_date"]
			new_course.end_date = request.POST["end_date"]
			new_course.user_id = request.user.id
			new_course.save()
			return redirect('index')
		# else:
		# 	return redirect('/create_course')

def login(request):
    context = {"Error": False}
    if request.method == "GET":
        return render(request, 'schooltool/login.html')
    if request.method == "POST":
        username = request.post["username"]
        password = request.post["password"]
        user = auth.authenticated(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            context = {"Error": "User not authenticated"}
            return redirect('login')

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

def profile(request):
	context = {"error": False}
	if request.user.is_authenticated:
		return render(request, 'schooltool/secret.html')
	else:
		context["error"] = "Not authenticated"
		return render(request, 'schooltool/signup.html', context)
