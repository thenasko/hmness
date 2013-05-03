from django.shortcuts import render, redirect, get_object_or_404
from django.template import RequestContext
from django.shortcuts import render_to_response

from pins.models import PIN

def pin(request, pin_id):
    pin = get_object_or_404(PIN, id=pin_id)
    context = {
        'active_page': '',
        'pin': pin,
        }
    return render(request, "pin.html", context)
