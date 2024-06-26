# petstore/views.py

from django.shortcuts import render

def index(request):
    return render(request, 'petstore/index.html')
