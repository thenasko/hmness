from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
import django.contrib.auth as django_auth

from django.http import Http404
from django.template import RequestContext

from annoying.utils import HttpResponseReload
from annoying.decorators import render_to

from actstream.models import following, followers

from users.forms import LoginForm
from users.forms import SignupForm

from connections.views import follow as connections_follow
from connections.views import unfollow as connections_unfollow


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
        return HttpResponseReload(request)

def logout(request):
    django_auth.logout(request)
    return redirect('home')

def signup(request):
    return redirect('users:register')

def register(request):
    if request.method == 'POST': # If the form has been submitted...
        form = SignupForm(request.POST) # A form bound to the POST data
        if form.is_valid():
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            user = User.objects.create_user(username, email,password)      
            user = django_auth.authenticate(username=username,
                                        password=password)
            django_auth.login(request, user)
            return redirect('home')
            # TODO: Redirect to the page this came from
    else:
        form = SignupForm()
    return render(request,'auth.html',{'loginform':LoginForm,'signupform': form})
     

def auth(request):
    if request.user.is_authenticated():
        return redirect('home')

    context = {
        'active_page': '',
        'loginform': LoginForm,
        'signupform': SignupForm,
        }
    return render(request, "auth.html", context)

def user(request, username, active_tab='activity'):
    user_to_show = get_object_or_404(User, username=username)

    # If edit tab is requested, check whether user should have access
    if (active_tab == 'edit') and (request.user.id != user.id):
        return redirect('users:user', username = username)

    context = {
        'active_page': '',
        'active_tab': active_tab,
        'user_to_show': user_to_show,
        'following': following(user_to_show),
        'followers': followers(user_to_show),
        }
    return render(request, "user.html", context)

def follow(request, username):
    if request.user.is_authenticated():
        user = get_object_or_404(User, username=username)
        return connections_follow(request, request.user.get_profile(), user.get_profile())
    else:
        raise Http404

def unfollow(request, username):
    if request.user.is_authenticated():
        user = get_object_or_404(User, username=username)
        return connections_unfollow(request, request.user.get_profile(), user.get_profile())
    else:
        raise Http404
