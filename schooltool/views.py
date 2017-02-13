from django.shortcuts import render

# Create your views here.

def index(request):
  return render(request, 'schooltool/index.html')

def profile(request):
    # context = {"error": False}
    # if request.user.is_authenticated:
    #     context = {
    #         "users": User.objects.filter(user_id = request.user.id).select_related()
    #     }
        return render(request, 'schooltool/profile.html')
    # else:
    #     context["error"] = "Not authenticated"
    #     return render(request, 'schooltool/signup.html', context)
