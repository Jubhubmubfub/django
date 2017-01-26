from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if 'counter' not in request.session:
        request.session['counter']= 0
    return render(request, 'survey/index.html')

def post(request):
    return render(request, 'survey/post.html')

def submit(request):
    print "**************"
    if request.method == "POST":
        request.session['name'] = request.POST['name']
        request.session['dojo_locations'] = request.POST['dojo_locations']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']
        request.session['counter'] += 1

    return redirect('/post')
