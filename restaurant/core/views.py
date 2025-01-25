from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from core.models import MenuItem, Category
from .forms import SignupForm
from django.contrib.auth import login
from django.contrib import messages

def home(request):
    item_of_the_day = MenuItem.objects.filter(is_item_of_the_day=True).first()
    return render(request, 'home.html', {'item_of_the_day': item_of_the_day})

def menu(request):
    category_id = request.GET.get('category')
    categories = Category.objects.all()
    menu_items = MenuItem.objects.all()
    if category_id:
        menu_items = menu_items.filter(category_id=category_id)
    return render(request, 'menu.html', {'menu_items': menu_items, 'categories': categories})

def menu_view(request):
    menu_items = MenuItem.objects.all()  # Retrieve all menu items
    return render(request, 'core/menu.html', {'menu_items': menu_items})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # Create the user
            user = form.save()
            # Login the user automatically
            login(request, user)
            # Redirect to login page after signup
            messages.success(request, 'Account created successfully. Please log in.')
            return redirect('login')  # Redirect to the login page
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {'form': form})

