from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Feature
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.

def index(request):
    feature1 = Feature()
    feature1.id, feature1.name, feature1.details, feature1.is_true = 1, "Fast", "Our service is very quick and responsive", True
    feature2 = Feature()
    feature2.id, feature2.name, feature2.details, feature2.is_true = 1, "Reliable", "Our service is reliable, robust and fault tolerant", True
    feature3 = Feature()
    feature3.id, feature3.name, feature3.details, feature3.is_true = 1, "Easy to Use", "Our service is easy to use and understand", False
    feature4 = Feature()
    feature4.id, feature4.name, feature4.details, feature4.is_true = 1, "Affordable", "Our service is very affordable with multiple price ranges", True

    features = [feature1, feature2, feature3, feature4]

    features = Feature.objects.all()

    return render(request, "index.html", {"features": features})

def index1(request):
    name = "Sam"
    return render(request, 'index1.html', {'name': name})

def counter(request):
    text = request.POST['text']
    number = len(text.split())
    return render(request, 'counter.html', {"number": number})

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already used")
                return redirect("register")
            elif User.objects.filter(username=username).exists():
                messages.info(request, "User already exists")
                return redirect("register")
            else:
                user = User.objects.create_user(username = username, email = email, password = password1)
                user.save()
                return redirect("login")
        else:
            messages.info(request, "Password not the same")
            return redirect("register")
    else:
        return render(request, "register.html")
    
def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Credentials Invalid")
            return redirect("login")
    else:
        return render(request, "login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')