from django.shortcuts import render

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
