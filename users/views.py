from django.shortcuts import render, redirect
import django.contrib.auth as django_auth
from django.contrib import messages

from users.forms import LoginForm

def login(request):
    if (request.POST and
        'username' in request.POST and
        'password' in request.POST):
        username = request.POST['username']
        password = request.POST['password']
        user = django_auth.authenticate(username=username,
                                        password=password)
    else:
        user = None

    if user is None:
        messages.error(request,
                       'The username or password you provided does not match our records.')
        return redirect('users:auth');
    else:
        django_auth.login(request, user)
        # TODO: Redirect to the page this came from
        return redirect('home');

def logout(request):
    django_auth.logout(request)
    return redirect('home')

def auth(request):
    if request.user.is_authenticated():
        return redirect('home')

    context = {
        'active_page': '',
        'loginform': LoginForm,
        }
    return render(request, "auth.html", context)

def user(request, username):
    context = {
        'active_page': '',
        'username': username,
        }
    return render(request, "user.html", context)
