from django.shortcuts import render,redirect
from django.conf import urls

# Create your views here.
def index(request):
    return render(request,'index.html')
