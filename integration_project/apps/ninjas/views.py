from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'ninjas/index.html')

def show(request, ninja_color):
    print "hello world"
    if ninja_color == "blue":
        ninja = "leonardo"
    elif ninja_color == "purple":
        ninja = "donatello"
    elif ninja_color == "orange":
        ninja = "michelangelo"
    elif ninja_color == "red":
        ninja = "raphael"
    elif ninja_color != "red" and ninja_color != "blue" and ninja_color != "purple" and ninja_color != "orange":
        ninja = "notapril"

    context = {
        'ninja': ninja
    }
    return render(request, 'ninjas/show.html', context)
