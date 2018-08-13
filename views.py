from django.shortcuts import redirect, render
from lists.models import Item, List

def home_page(request):
    """Render home.html"""
    "Testing"
    "todo: todo item"

def home_page(request):
    """Render home.html"""
    "Testing"
    return render(request, 'home.html')