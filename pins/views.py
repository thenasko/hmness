from django.shortcuts import render, redirect, get_object_or_404
from django.template import RequestContext
from django.http import Http404

from annoying.decorators import render_to

from pins.models import PIN

from connections.views import follow as connections_follow
from connections.views import unfollow as connections_unfollow


@render_to('pin.html')
def pin(request, pin_id):
    pin = get_object_or_404(PIN, id=pin_id)
    return {
        'active_page': '',
        'pin': pin,
        }

def follow(request, pin_id):
    if request.user.is_authenticated():
        pin = get_object_or_404(PIN, id=pin_id)
        return connections_follow(request, request.user.get_profile(), pin)
    else:
        raise Http404

def unfollow(request, pin_id):
    if request.user.is_authenticated():
        pin = get_object_or_404(PIN, id=pin_id)
        return connections_unfollow(request, request.user.get_profile(), pin)
    else:
        raise Http404
