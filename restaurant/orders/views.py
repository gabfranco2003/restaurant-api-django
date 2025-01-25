from django.shortcuts import redirect, render, get_object_or_404
from core.models import MenuItem
from .models import Cart, Order
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

def home(request):
    return render(request, 'home.html') 

def menu(request):
    # Fetch all menu items (or apply any other logic as needed)
    menu_items = MenuItem.objects.all()
    return render(request, 'orders/menu.html', {'menu_items': menu_items})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after successful signup
    else:
        form = UserCreationForm()
    return render(request, 'core/signup.html', {'form': form})

def add_to_cart(request, item_id):
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect to login if the user is not authenticated

    # Get the MenuItem object using the item_id
    item = get_object_or_404(MenuItem, id=item_id)

    # Ensure you're passing a User instance, not just a string (username)
    user = request.user  # This is the authenticated User object

    # Get or create a Cart item for the current user and selected MenuItem
    cart_item, created = Cart.objects.get_or_create(customer=user, item=item)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')

def view_cart(request):
    if request.user.is_authenticated:
        # Use the actual User instance from request.user to filter cart items
        user = request.user  # This is the correct User instance, no need to query by username
        cart_items = Cart.objects.filter(customer=user)  # Now filter correctly by the User instance
    else:
        # Optionally, handle anonymous users (not logged in)
        cart_items = Cart.objects.filter(customer=None)  # You could store cart for unauthenticated users if needed
    
    return render(request, 'cart.html', {'cart_items': cart_items})

def place_order(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    cart_items = Cart.objects.filter(customer=request.user)
    
    if not cart_items.exists():
        return redirect('cart')  # Redirect back if cart is empty

    # Calculate the total cost of the cart items
    total = sum(item.item.price * item.quantity for item in cart_items)
    
    # Create an order for the authenticated user
    order = Order.objects.create(customer=request.user, total=total)
    
    # Remove cart items after order is placed
    cart_items.delete()
    
    return redirect('orders')  # Redirect to the orders page

def order_history(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    # Retrieve orders for the authenticated user, ordered by the creation date
    orders = Order.objects.filter(customer=request.user).order_by('-created_at')
    
    return render(request, 'orders.html', {'orders': orders})
