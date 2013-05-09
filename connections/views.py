from annoying.utils import HttpResponseReload

def follow(request, origin, target):
    origin.follow(target)

    return HttpResponseReload(request)

def unfollow(request, origin, target):
    origin.unfollow(target)

    return HttpResponseReload(request)
