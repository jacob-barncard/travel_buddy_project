# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
import bcrypt
from django.db import models
from django.contrib import messages

# Create your models here.

class OwnerManager(models.Manager):

    def createOwner(self, postData):
        password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
        self.create(first_name = postData['first_name'], last_name = postData['last_name'], email = postData['email'], password = password)


    def registerVal(self, postData):
        results = {'errors':[], 'status': False}

        if len(postData['first_name']) < 2:
            results['status'] = True
            results['errors'].append('First name is too short ')

        if len(postData['last_name']) < 2:
            results['status'] = True
            results['errors'].append('Last name is too short ')

        if not re.match(r"[^@]+@[^@]+\.[^@]+", postData['email']):
            results['status'] = True
            results['errors'].append('Email is not valid ')

        if len(postData['password']) < 8:
            results['status'] = True
            results['errors'].append('Password is too short ')

        if postData['password'] != postData['c_password']:
            results['status'] = True
            results['errors'].append('Password does not match ')

        user = self.filter(email = postData['email'])

        if len(user) > 0:
            results['status'] = True
            results['errors'].append('User already exists in database ')

        return results

    def loginVal(self, postData):
        results = {'errors':[], 'user': None}
        email_matches = self.filter(email = postData['email'])
        if len(email_matches) == 0:
            results['errors'].append('Email is not registered')
        else:
            results['user'] = email_matches[0]
            if not bcrypt.checkpw(postData['password'].encode(), results['user'].password.encode()):
                results['errors'].append('Please check your email and password and try again')
                results['status'] = True
        return results


class Owner(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    friends = models.ManyToManyField('self')
    objects = OwnerManager()
