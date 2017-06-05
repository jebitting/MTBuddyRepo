# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import userMTB, trip, traveling

def dashboard(request):
    return render(request, 'mtbuddy/dashboard.html')

def register(request):
    if request.method == "POST":
        print request.POST
        if request.POST["process"] == "register":
            response = userMTB.objects.check_create(request.POST)
        elif request.POST["process"] == "login":
            response = userMTB.objects.check_log(request.POST)
        if not response[0]:
            for message in response[1]:
                messages.error(request, message[1])
            return redirect('mtbuddy:dashboard')
        else:
            request.session['user'] = {
            "id": response[1].id,
            "first_name": response[1].first_name,
            "last_name": response[1].last_name,
            }
            return redirect('mtbuddy:dashboard')
    return redirect('mtbuddy:landing')

def login(request):
    print ">>>> at login"
    return redirect('mtbuddy:landing')

def landing(request):
    print ">>>> at landing"
    # pass lookup from tables information about logged in traveler trips
    # trips = trip.objects.filter(traveler=userMTB)
    Context = {
    "trips": trip.objects.all()
    # select all from trip
    }
    return render(request, 'mtbuddy/landing.html')

def create(request):
    print ">>>> at create"
    return render(request, 'mtbuddy/create.html')

def delete(request, id):
    print ">>>> at delete"
    # add lookup from tables about existing trip information
    # delete from table
    return redirect('mtbuddy:dashboard')

def logout(request):
    print ">>>> at logout"
    # log user out and close session
    return render(request, 'mtbuddy/logout.html')
    # return redirect('mtbuddy: dashboard')
