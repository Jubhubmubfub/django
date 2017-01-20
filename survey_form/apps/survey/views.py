from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'survey/index.html')

def post(request):
    return render(request, 'survey/post.html') 

def submit(request):
    if request.method == "POST":
        request.session['name'] = request.POST['name']
        request.session['dojo_locations'] = request.POST['dojo_locations']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']

    return redirect('/post')
