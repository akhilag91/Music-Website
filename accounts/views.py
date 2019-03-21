# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect

# Create your views here.
from django.contrib.auth import login as auth_login

from django.contrib.auth.forms import UserCreationForm
from .forms import signupform


def signup(request):
    if request.method == "POST":
        form = signupform(request.POST)
        if form.is_valid():
            user = form.save()      
            auth_login(request,user)
            return redirect('home')
    else:
        form = signupform()
    return render(request,'signup.html',{"form":form})