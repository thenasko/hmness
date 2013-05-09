from django.contrib import messages

from annoying.utils import HttpResponseReload

def follow(request, origin, target):
    origin.follow(target)

    messages.success(request, "You just followed someone!")

    return HttpResponseReload(request)

def unfollow(request, origin, target):
    origin.unfollow(target)

    messages.warning(request, "You just unfollowed someone!")
    
    return HttpResponseReload(request)
