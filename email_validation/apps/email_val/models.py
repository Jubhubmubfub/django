from __future__ import unicode_literals

from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your models here.

class UserManager(models.Manager):
    def login(self,email):
        print "Running a login function!"
        print "If successful login occurs, maybe return {'theuser':user} where user is a user object?"
        print "If unsuccessful, maybe return { 'errors':['login unsuccessful'] }"
        if len(email) < 1:
            return {'valid':False,'error':"Must enter an email"}
        elif not EMAIL_REGEX.match(email):
            return {'valid':False,'error':"Invalid email"}
        else:
            return {'email':email, 'error':"", 'valid':True}
    def register(self,postData):
        print ("Register a user here")
        print ("If successful, maybe return {'theuser':user} where user is a user object?")
        print ("If unsuccessful do something like this? return {'errors':['User first name too short', 'Last name too short']}")
        pass
class User(models.Model):
    email = models.EmailField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
