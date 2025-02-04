from django.shortcuts import render

# Create your views here.

def index1(request):
    name = "Sam"
    return render(request, 'index1.html', {'name': name})

def counter(request):
    text = request.POST['text']
    number = len(text.split())
    return render(request, 'counter.html', {"number": number})