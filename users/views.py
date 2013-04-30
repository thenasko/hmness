from django.shortcuts import redirect
import django.contrib.auth as auth

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
