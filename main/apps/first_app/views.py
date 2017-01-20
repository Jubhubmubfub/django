from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'first_app/index.html')

def show(request):
    print (request.method)
    return render(request, 'first_app/show_users.html')
