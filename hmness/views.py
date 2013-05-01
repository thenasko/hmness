from django.shortcuts import render
from django.contrib.auth.models import User
import django.contrib.auth as auth


from users.models import UserProfile

def home(request):
    context = {
        'active_page': 'home',
        'users': User.objects.all(),
        }
    return render(request, "home.html", context)

def contact(request):
    context = {
        'active_page': 'contact',
        }
    return render(request, "contact.html", context)

def about(request):
    context = {
        'active_page': 'about',
        }
    return render(request, "about.html", context)
