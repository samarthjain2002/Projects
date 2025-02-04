from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

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

    return render(request, "index.html", {"features": features})

def index1(request):
    name = "Sam"
    return render(request, 'index1.html', {'name': name})

def counter(request):
    text = request.POST['text']
    number = len(text.split())
    return render(request, 'counter.html', {"number": number})