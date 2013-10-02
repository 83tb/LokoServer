# Create your views here.

from django.shortcuts import render_to_response

try:
    from LokoServer.io import openLock, closeLock
except:
    pass


def open(request):
    try:
        openLock()
    except: pass

    return render_to_response("open.html")

def close(request):

    try:
        closeLock()
    except: pass

    return render_to_response("close.html")

def index(request):
    return render_to_response("index.html")
