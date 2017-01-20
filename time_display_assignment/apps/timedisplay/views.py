from django.shortcuts import render, redirect, HttpResponse
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
        return redirect('/')
    else:
        return redirect('/')
