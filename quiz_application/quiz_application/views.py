from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms
#from .forms import UserRegistrationForm
from quiz.models import *

def home(request):
    return render(request, 'home.html')

def dashboard(request):
    cats = Category.objects.all()
   
    return render(request, 'dashboard.html',{'cats':cats})
