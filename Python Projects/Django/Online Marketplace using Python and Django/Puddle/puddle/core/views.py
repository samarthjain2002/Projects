from django.shortcuts import render, redirect

# Create your views here.

from item.models import Category, Item

from .forms import SignupForm


def index(request):
    category_id = request.GET.get('category')  # Get category from query parameters
    
    if category_id:
        items = Item.objects.filter(is_sold=False, category_id=category_id)
        categories = None  # Don't pass categories
    else:
        items = Item.objects.filter(is_sold=False)
        categories = Category.objects.all()  # Pass categories only when no filter is applied

    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })


def contact(request):
    return render(request, 'core/contact.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })
