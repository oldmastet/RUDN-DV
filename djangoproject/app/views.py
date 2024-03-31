from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def start (request):
    return render (request, 'start.html')