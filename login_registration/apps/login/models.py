from __future__ import unicode_literals

from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
    def register(self, first_name, last_name, email, password, confirm_pw):
        error1 = False
        error2 = False
        error3 = False
        error4 = False
        error5 = False
        error6 = False
        no_errors= False
        if len(email) < 1:
            error1 = True
        elif not EMAIL_REGEX.match(email):
            error2 = True
        if len(first_name) < 2:
            error3 = True
        if len(last_name) < 2:
            error4 = True
        if len(password) < 8:
            error5 = True
        elif password != confirm_pw:
            error6 = True
        else:
            no_errors = True
        return {'error1':error1,'error2':error2,'error3':error3,'error4':error4,'error5':error5,'error6':error6,'no_errors':no_errors}

    def login(self, email,password):
        error1 = False
        error2 = False
        no_errors = False
        if len(email) < 1:
            error1 = True
        if len(password) < 1:
            error2 = True
        else:
            no_errors = True
        return {'error1':error1,'error2':error2, 'no_errors':no_errors}

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    pw_hash = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
