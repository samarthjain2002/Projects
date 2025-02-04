from django.shortcuts import render

# Create your views here.

def index(request):
    name = "Sam"
    return render(request, 'index1.html', {'name': name})