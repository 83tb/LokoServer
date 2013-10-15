# Create your views here.

from django.shortcuts import render_to_response

try:
    from LokoServer.io import openLock, closeLock
except:
    pass









from LokoApp.models import Queue

def open(request):

    Queue.objects.create(command="open")
    return render_to_response("open.html")

def close(request):


    Queue.objects.create(command="close")
    return render_to_response("close.html")

def index(request):
    return render_to_response("index.html")
