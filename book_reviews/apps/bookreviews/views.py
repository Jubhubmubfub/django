from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from . import models

# Create your views here.
def index(request):
    return render(request, 'bookreivews/index.html')

def login(request):
    result = User.objects.validateLogin(request)

    if result[0]==False:
        print_messages(request, result[1])
        return redirect(reverse('index'))
    return log_user_in(request,result[1])

def register(request):
    result = User.objects.validateReg(request)

    if result[0]==False:
        print_messages(request, result[1])
        return redirect(reverse('index'))

    return log_user_in(request,result[1])

def success(request):
    if 'user' not in request.session:
        return redirect('/')
    return render(request, 'bookreviews/success.html')

def print_messages(request):
    for message in message_list:
        messages.add_message(request, messages.INFO, message)

def log_user_in(request,user):
    request.session['user'] = {
            'id':user.id,
            'first_name':user.first_name,
            'last_name':user.last_name,
            'email':user.email
    }
    return redirect(reverse('success'))

def logout(request):
    request.session.pop('user')
    return redirect(reverse('index'))
