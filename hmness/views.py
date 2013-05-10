from django.shortcuts import render
from django.contrib.auth.models import User
import django.contrib.auth as auth
from pins.models import PIN

from annoying.decorators import render_to

from users.models import UserProfile

@render_to('home.html')
def home(request):
    return {
        'active_page': 'home',
        'users': User.objects.all(),
        'pins': PIN.objects.all(),
        }

@render_to('contact.html')
def contact(request):
    return {
        'active_page': 'contact',
        }

@render_to('about.html')
def about(request):
    return {
        'active_page': 'about',
        }
