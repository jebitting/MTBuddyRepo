# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import bcrypt, re
EMAILREG = re.compile(r'^[a-zA-Z0-9.-_+]+@[a-zA-Z0-9.-_]+\.[a-zA-Z]*$')
# NAMEREG
# PASSREG
# OTHERREG

class userMTB_Manager(models.Manager):
    def hashpass(self, password):
        return bcrypt.hashpw(password, bcrypt.gensalt())

    def check_create(self, data):
        # error checking for the new user account
        errors = []
        if len(data['first_name']) < 2:
            errors.append(['first_name', "Error: First Name must be greater than 2 characters.  Please try again."])
        if len(data['last_name']) < 2:
            errors.append(['last_name', "Error: Last Name must be greater than 2 characters.  Please try again."])
        if not re.match(EMAILREG, data['email']):
            errors.append(['email', "Error:  Email is not a valid address.  Please try again."])
        if len(data['password']) < 8:
            errors.append(['password', "Password must be at lease eight characters.  Please try again."])
        if not data['password'] == data['confirmpass']:
            errors.append(['confirmpass', "Passwords do not match"])
        # what to do with the errors that were discovered
        if errors:
            return [False, errors]
        # if everything is good, proceed
        else:
            curent_user = userMTB.objects.filter(email=data['email'])
            if curent_user:
                errors.append(['curent_user', "User already exists, please try again."])
                return [False, errors]
            newUser = userMTB(first_name=data['first_name'], last_name=data['last_name'], email=data['email'])
            # how to handle the hashed password
            hashpass = bcrypt.hashpw(data['password'].encode(), bcrypt.gensalt())
            print hashpass, "hashed password"
            newUser.hashpass = self.hashpass(data['password'].encode())
            print newUser.hashpass
            newUser.save()
            print newUser
            return [True, newUser]

    def check_log(self, data):
        errors = []
        curent_user = userMTB.objects.filter(email=data['email'])
        if not curent_user:
            errors.append(['account', "Email or password incorrect"])
        elif not bcrypt.checkpw(data['password'].encode(), curent_user[0].hashpw.encode()):
            errors.append(['account', "Email or password incorrect"])
        if errors:
            return [False, errors]
        else:
            print current_user[0]
            return [True, curent_user[0]]

class trip_Manager(models.Manager):
    # validations for trip informaton
    pass

class traveling_Manager(models.Manager):
    # validations for accompanying travelers
    pass

class userMTB(models.Model):
    first_name = models.CharField(max_length=45, blank=False)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=200)
    # password or hashed password
    # password = models.CharField(max_length=255)
    hashpass = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = userMTB_Manager()
    def __str__(self):
        return '--> NEW USER - ID: %s | Name: %s %s | Email: %s' % (self.id, self.first_name, self.last_name, self.email)

class trip(models.Model):
    destination = models.CharField(max_length=45)
    description = models.TextField(max_length=500)
    traveler = models.ForeignKey(userMTB)
    #check on reverse lookup (related_name ="") and if necessary
    start_date = models.DateTimeField
    end_date = models.DateTimeField
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    # objects = trips_Manager()

class traveling(models.Model):
    traveling_user = models.ForeignKey(userMTB)
    traveling_trip = models.ForeignKey(trip)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    # objects = traveling_Manager()
