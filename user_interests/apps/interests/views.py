from django.shortcuts import render, redirect
from .models import User, Interest

# Create your views here.
def index(request):
    if 'error' not in request.session:
        request.session['error'] = ""
    return render(request, 'interests/index.html')

def users(request):
    context = {
        'users':User.objects.all(),
        'interests':Interest.objects.all()
    }
    return render(request, 'interests/users.html', context)

def user_interests(request,user_id):
    users = User.objects.filter(id=user_id)
    if len(users) < 1:
        return redirect('/')
    interests = users[0].interests.all()
    context = {
        'user': users[0],
        'interests':interests
    }
    return render(request, 'interests/user_interests.html', context)

def process(request):
    print "PROCESS IS HAPPENING**************"
    user = User.objects.filter(first_name=request.POST['first_name'])
    print "THIS IS THE USER",user
    users = User.objects.all()
    print "THESE ARE THE USERS",users
    if len(user) < 1:
        print "CREATING IS STARTING"
        #user
        user_list = User.objects.filter(first_name = request.POST['first_name'])
        if not user_list:
            user = User.objects.create(first_name= request.POST['first_name'])
        else:
            user = user_list[0]
        #interest
        name = request.POST['interest']
        interest_list = Interest.objects.filter(name=name)
        if not interest_list:
            interest = Interest.objects.create(name=name)
        else:
            interest = interest_list[0]

        user.interests.add(interest)
        request.session['error']=""
        print "CREATING IS OVER"
        return redirect('/users')
    else:
        return redirect('/')
