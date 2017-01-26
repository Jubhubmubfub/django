from django.shortcuts import render, redirect
from .models import User, UserManager
from django.contrib import messages
from django.core.urlresolvers import reverse
import bcrypt

# Create your views here.
def index(request):
    if 'logged_in' not in request.session:
        request.session['logged_in'] = False
    return render(request, 'login/index.html')

def success(request):
    if request.session['logged_in']:
        return render(request, 'login/success.html')
    print "Not logged in"
    return redirect(reverse('my_index'))

def logout(request):
    request.session['logged_in'] = False
    return redirect(reverse('my_index'))

def register(request):
    user = User.objects.register(request.POST['first_name'],request.POST['last_name'],request.POST['email'],request.POST['password'],request.POST['confirm_pw'])
    if user['error1']:
        messages.add_message(request, messages.INFO, "didn't enter an email")
    if user['error2']:
        messages.add_message(request, messages.INFO, 'email is bad')
    if user['error3']:
        messages.add_message(request, messages.INFO, 'first name must be longer than 1 character')
    if user['error4']:
        messages.add_message(request, messages.INFO, 'last name must be longer than 1 character')
    if user['error5']:
        messages.add_message(request, messages.INFO, "password length must be at least 8 characters")
    if user['error6']:
        messages.add_message(request, messages.INFO, "passwords don't match")
    if user['no_errors']:
        print "**********"
        print "Success!"
        print "**********"
        password = request.POST['password'].encode('utf-8')
        pwhash = bcrypt.hashpw(password, bcrypt.gensalt())
        User.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'], pw_hash=pwhash)
        print User.objects.all()
        request.session['logged_in']=True
        request.session['first_name'] = request.POST['first_name']
        return redirect(reverse('my_success'))
    return redirect(reverse('my_index'))

def login(request):
    user = User.objects.login(request.POST['email'],request.POST['password'])
    if user['error1']:
        messages.add_message(request, messages.INFO, "please enter an email")
    if user['error2']:
        messages.add_message(request, messages.INFO, "please enter a password")
    if user['no_errors']:
        validate = User.objects.filter(email=request.POST['email'])
        if validate:
            print "found a matching email"
            password = request.POST['password'].encode('utf-8')
            pwhash = validate[0].pw_hash.encode('utf-8')
            pw_validate = bcrypt.hashpw(password,pwhash)
            if pw_validate == validate[0].pw_hash:
                request.session['logged_in']= True
                return redirect(reverse('my_success'))
        messages.add_message(request, messages.INFO, "email or password incorrect")
    return redirect(reverse('my_index'))
