from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Property(models.Model):
    description = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User)

class Event(models.Model):
    comment = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    property = models.ForeignKey(Property)

class Note(models.Model):
    comment = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    event = models.ForeignKey(Event)

class File(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    note = models.ForeignKey(Note)

class Alert(models.Model):
    when = models.DateTimeField()
    event = models.ForeignKey(Event)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
