from django.shortcuts import render, redirect
import django.contrib.auth as auth

def home(request):
    context = {
        'active_page': 'home',
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

def login(request):
    if (request.POST and
        'username' in request.POST and
        'password' in request.POST):
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,
                                 password=password)
        if user is None:
            # TODO: Add a 'invalid login' error message
            return redirect('home');
        else:
            auth.login(request, user)
            # TODO: Redirect to the page this came from
            return redirect('home');
    else:
        # TODO: Add a 'invalid login' error message
        return redirect('home');

def logout(request):
    auth.logout(request)
    return redirect('home')
