# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import Owner
from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.

def logout(request):
    request.session.flush()
    return redirect('/')

def index(request):
    return render(request, 'login_app/index.html')

def register(request):
    results = Owner.objects.registerVal(request.POST)
    if results['status'] == False:
        Owner.objects.createOwner(request.POST)
        messages.success(request, 'Your user has been created. Please log in')
    else:
        for error in results['errors']:
            messages.error(request, error)

    return redirect('/')

def login(request):
    results = Owner.objects.loginVal(request.POST)
    if results['errors']:
        for error in results['errors']:
            messages.error(request, error)
        return redirect('/')
    else:
        request.session['first_name'] = results['user'].first_name
        request.session['last_name'] = results['user'].last_name
        request.session['email'] = results['user'].email
        request.session['id'] = results['user'].id
        return redirect('/dashboard')
