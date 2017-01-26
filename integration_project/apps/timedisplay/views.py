from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse
import datetime

# Create your views here.

def index(request):
    return render(request, 'timedisplay/index.html')

def displayTime(request):

    currentTime = datetime.datetime.now()
    print datetime.datetime
    print "hahah"
    print currentTime
    print "hahah"
    time = {
    "time":currentTime
    }

    return render(request,'timedisplay/index.html',time)

def create(request):
    print(request.method)
    if request.method == "POST":
        print ("*"*50)
        print (request.POST)
        print ("*"*50)
        request.session['name'] = request.POST['first_name']
        return redirect(reverse('my_index'))
    else:
        return redirect(reverse('my_index'))
