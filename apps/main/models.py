from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Icon(models.Model):
    name = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name

class Color(models.Model):
    name = models.CharField(max_length=25)
    color = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return "{}-{}".format(self.name, self.color)

class Property(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField(max_length=255, null=True)
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
    name = models.CharField(max_length=25, null=True)
    comment = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    event = models.ForeignKey(Event)

def directory_path(prop_id,event_id, note_id, filename):
    return 'property_{0}/event_{1}/note_{2}/{3}'.format(prop_id,event_id, note_id, filename)

class File(models.Model):
    # upload_to=directory_path
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    note = models.ForeignKey(Note)

class Alert(models.Model):
    when = models.DateTimeField()
    comment = models.CharField(max_length=50)
    event = models.ForeignKey(Event)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
