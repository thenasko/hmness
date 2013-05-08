from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
import django.contrib.auth as django_auth

from users.forms import LoginForm
from users.forms import SignupForm

from django.template import RequestContext
from django.shortcuts import render_to_response


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

def user(request, username):
    user = get_object_or_404(User, username=username)
    c_in_only, c_out_only, c_in_out = user.get_profile().connections_pack
    context = {
        'active_page': '',
        'user': user,
        'connections_in_only': c_in_only,
        'connections_out_only': c_out_only,
        'connections_in_out': c_in_out,
        'connections_in_count': len(c_in_only) + len(c_in_out),
        'connections_out_count': len(c_out_only) + len(c_in_out),
        }
    return render(request, "user.html", context)
