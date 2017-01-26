from django.shortcuts import render, redirect
from .models import User, UserManager
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your views here.
def index(request):
    if 'email' not in request.session:
        request.session['email']= ""
    if 'error' not in request.session:
        request.session['error'] = ""
    return render(request, 'email_val/index.html')

def success(request):
    context = {
            'emails': User.objects.all()
    }
    return render(request, 'email_val/success.html',context)

def process(request):
    user = User.objects.login(request.POST['email'])
    print user
    if user['valid'] == False:
        request.session['error']= user['error']
        return redirect('/')
    else:
        User.objects.create(email=user['email'])
        request.session['email']=user['email']
        return redirect('/success')
    # valid = True
    # if len(request.POST['email']) < 1:
    #     print "must enter an email"
    #     valid = False
    #     request.session['error'] = "Must enter an email"
    # elif not EMAIL_REGEX.match(request.POST['email']):
    #     valid = False
    #     request.session['error'] = "Invalid email"
    #     print "email not valid"
    # elif valid:
    #     User.objects.create(email=request.POST['email'])
    #     request.session['email'] = request.POST['email']
    #     request.session['error'] = ""
    #     return redirect('/success')
    # return redirect('/')

def delete(request,id):
    User.objects.filter(id=id).delete()
    return redirect('/success')
