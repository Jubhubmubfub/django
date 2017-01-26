# from __future__ import unicode_literals
# from django.core.exceptions import ObjectDoesNotExist
# from django.db import models
# import bcrypt, re
#
# EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
#
# class UserManager(models.Manager):
#     def validateReg(self,request):
#         errors = self.validate_inputs(request)
#
#         if len(errors) > 0:
#             return (False,errors)
#
#         pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
#
#         user = self.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'],pw_hash=pw_hash)
#         return (True,user)
#
#
#     def validateLogin(self, request):
#         try:
#             user = Users.object.get(email=request.POST['email'])
#             password = request.POST['password'].encrypt()
#
#             if bcrypt.hashpw(password,user.pw_hash.encode()):
#                 return (True,user)
#         except ObjectDoesNotExist:
#             pass
#         return (False,["Email/Password doesn't match"])
#
#     def validate_inputs(self, request):
#         errors = []
#         if len(request.POST['first_name']) < 3 or len(request.POST['last_name']) < 3:
#             errors.append("Please enter a first/last name that is longer than 2 characters")
#         if not EMAIL_REGEX.match(request.POST['email']):
#             errors.append("Invalid email entered")
#         if len(request.POST['password']) < 8:
#             errors.append("Password must be at least 8 characters")
#         if len(request.POST['password']) < 8 or request.POST['password'] != request.POST['confirm_pw']:
#             errors.append("Passwords must match and be at least 8 characters.")
#         return errors
#
# class BookManager(models.Manager):
#     def validate_inputs(self,request):
#         errors = []
#         if len(request.POST['title']) < 1:
#             errors.append("Please enter a title")
#         if len(request.POST['author']) < 1:
#             errors.append("Please input an author")
#         if len(request.POST['review']) < 1:
#             errors.append("Please choose a rating")
#         if len(request.POST['review']) < 1:
#             errors.append("Please enter a review")
#         return errors
#
# class ReviewManager(models.Manager):
#     def validate_inputs(self,request):
#         errors = []
#         if len(request.POST['review']) < 1:
#             errors.append("Please enter a review")
#         return errors
#
# class User(models.Model):
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     email = models.EmailField(max_length=255)
#     pw_hash = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add = True)
#     updated_at = models.DateTimeField(auto_now = True)
#     objects = UserManager()
#
# class Review(models.Model):
#     review = models.TextField(max_length=1000)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     objects = ReviewManager()
#
# class Book(models.Model):
#     title = models.CharField(max_length=100)
#     author = models.CharField(max_length=100)
#     review = models.ForeignKey(models.Review)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     objects = BookManager()
