# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..login_app.models import Owner
from django.shortcuts import render, redirect
from models import Trip

# Create your views here.
def dashboard(request):
    if 'email' not in request.session:
        return redirect('/')
    context = {
        'friend_users': Owner.objects.exclude(id=request.session['id'])
    }
    myself = Owner.objects.get(id = request.session['id']),
    context = {
        'cur_user': Owner.objects.get(id = request.session['id']),
        'trips':Trip.objects.all()
    }
    return render(request, 'main_app/dashboard.html', context)


def make_plan_page(request):
    return render(request, 'main_app/make_plan_page.html')

def create(request):
    Trip.objects.create(trip_name = request.POST['trip_name'], start_date = request.POST['start_date'], end_date = request.POST['end_date'], plan = request.POST['plan'])
    return redirect('/dashboard')

def addOwner(request, id):
    trip = Trip.objects.get(id = id)
    owner = Owner.objects.get(id = request.session['id'])
    owner.trips.add(trip)
    return redirect('/dashboard')

def removeOwner(request, id):
    trip = Trip.objects.get(id = id)
    owner = Owner.objects.get(id = request.session['id'])
    owner.trips.remove(trip)
    return redirect('/dashboard')

def trip_view(request):
    return render(request, 'main_app/trip_view.html')



def trip_view(request, id):
    context = {
        'trips': Trip.objects.filter(id=id)
    }

    return render(request, 'main_app/trip_view.html', context)
