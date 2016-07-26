from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Icon(models.Model):
    name = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Color(models.Model):
    name = models.CharField(max_length=25)
    color = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Property(models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=50)
    icon_type = models.ForeignKey(Icon)
    icon_color = models.ForeignKey(Color)
    address = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User)

class Event(models.Model):
    name = models.CharField(max_length=25)
    comment = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    property = models.ForeignKey(Property)

class Note(models.Model):
    name = models.CharField(max_length=25)
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
