from __future__ import unicode_literals
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
import bcrypt, re
import south

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def validateReg(self,request):
        errors = self.validate_inputs(request)
        if errors:
            return (False,errors)
        user_list = User.objects.filter(email=request.POST['email'])
        if len(user_list)>0:
            errors.append("Email already exists")
            return (False, errors)
        else:
            pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())

            user = self.create(first_name=request.POST['first_name'],alias=request.POST['alias'],email=request.POST['email'].lower(),pw_hash=pw_hash)
            return (True,user)


    def validateLogin(self, request):
        try:
            user = User.objects.get(email=request.POST['email'].lower())
            password = request.POST['password'].encode()

            if bcrypt.hashpw(password,user.pw_hash.encode()):
                return (True,user)
        except ObjectDoesNotExist:
            pass
        return (False,["Email/Password doesn't match"])

    def validate_inputs(self, request):
        errors = []
        if len(request.POST['first_name']) < 3 or len(request.POST['alias']) < 3:
            errors.append("Please enter a first name/alias that is longer than 2 characters")
        if not EMAIL_REGEX.match(request.POST['email']):
            errors.append("Invalid email entered")
        if len(request.POST['password']) < 8:
            errors.append("Password must be at least 8 characters")
        if len(request.POST['password']) < 8 or request.POST['password'] != request.POST['confirm_pw']:
            errors.append("Passwords must match and be at least 8 characters.")
        return errors

class BookManager(models.Manager):
    def validate_inputs(self,request):
        errors = []
        author = request.POST['author']
        if len(request.POST['title'])<1:
            errors.append("Please enter a title")
        if len(request.POST['author']) < 1:
            author = request.POST['author_list']
        if len(request.POST['review']) < 1:
            errors.append("Please enter a review")
        if errors:
            return (False,errors)
        else:
            book = {
            'user': request.session['user']['id'],
            'title' : request.POST['title'],
            'author_list' : request.POST['author_list'],
            'author' : author,
            'rating' : request.POST['rating'],
            'review' : request.POST['review']
            }
        return (True,book)


class ReviewManager(models.Manager):
    def validate_inputs(self,request):
        errors = []
        if len(request.POST['review']) < 1:
            errors.append("Please enter a review")
            return (False,errors)
        else:
            return (True,errors)


class User(models.Model):
    first_name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    pw_hash = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()

class Review(models.Model):
    review = models.CharField(max_length=1000)
    rating = models.IntegerField()
    book = models.ForeignKey(Book, related_name='reviews')
    user = models.ForeignKey(User, related_name='reviews')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ReviewManager()
