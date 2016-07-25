from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import datetime

# Create your models here.

def clean_date(date, checkdate=datetime.date.today()):

    if date > checkdate:

        raise ValidationError("The date cannot be in the past!")
        
    return date

def clean_email(email):

	if User.objects.filter(email=email).count():
		raise ValidationError("This email address is taken.")
		return date
