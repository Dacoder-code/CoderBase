from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import *
from .forms import CreateUserForm
# Create your views here.


def homepage(request):
    if not request.user.is_authenticated:
        return redirect('login_page')
    return render(request, "CoderBase/Index.html")


def signup_view(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_page')

    context = {'form': form}
    return render(request, 'CoderBase/Sign-Up.html', context)


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_page')

        else:
            return render(request, 'CoderBase/Login.html', {
                "message": "Incorrect Username or Password."
            })
    return render(request, 'CoderBase/Login.html')


def logout_view(request):
    logout(request)
    return render(request, 'CoderBase/Login.html', {
        "message": "Logged Out"
    })


def course(request):
    courses = Allcourse.objects.all()
    return render(request, 'CoderBase/Course.html', {'course': courses})


def about(request):
    return render(request, 'CoderBase/About.html')


#def enroll(request, pk):
 #   courses = Allcourse.objects.all()
  #  enrolls = Allcourse.objects.get(id=pk)
   # context = {
    #    'course': courses,
     #   'enroll': enrolls
    #}
    #return render(request, 'CoderBase/Enroll.html', context)
#i was trying to query the database to be able to use the urls with my views
def enroll(request):
    return render(request, 'CoderBase/Enroll.html')