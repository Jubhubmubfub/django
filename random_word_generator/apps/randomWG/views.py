from django.shortcuts import render,redirect
import string
from random import randint

# Create your views here.


def index(request):
    print ("*"*50)
    print ("*"*50)
    if 'attempt' not in request.session:
        request.session['attempt'] = 0
        print request.session['attempt']
    return render(request, 'randomWG/index.html')





def generate_word(request):
    if request.method == "POST":
        string = "0123456789abcdefghjijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        newstring = ""
        request.session['random_word'] = ""
        for i in range(1,15):
            x = randint(0,len(string)-1)
            newstring += string[x]
        request.session['random_word'] = newstring
        request.session['attempt'] += 1
        return redirect('/')
    else:
        return redirect('/')
