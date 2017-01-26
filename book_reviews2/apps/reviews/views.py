from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Book, Review

# Create your views here.
def index(request):
    return render(request, 'reviews/index.html')

def register(request):
    result = User.objects.validateReg(request)
    if result[0]==False:
        print_messages(request, result[1])
        return redirect('/')
    return log_user_in(request,result[1])

def success(request):
    if 'user' not in request.session:
        return redirect('/')
    review_list = Review.objects.all
    book_list = Book.objects.all()
    context = {
        # 'books': book_list,
        # 'reviews': review_list
    }
    return render(request, 'reviews/home.html',context)

def login(request):
    result = User.objects.validateLogin(request)

    if result[0]==False:
        print_messages(request, result[1])
        return redirect('/')
    return log_user_in(request,result[1])

def add_book_review(request):
    return render(request, 'reviews/add_book.html')

def add_book(request,book):
    user_list = User.objects.filter(id=request.session['user']['id'])
    if user_list:
        user = user_list[0]
    else:
        print ""
    newBook = Book.objects.create(title=book['title'], author=book['author'],rating=book['rating'])
    print "THIS IS THE REVIEW WE JUST WROTE====>",book['review']
    newReview = Review.objects.create(review=book['review'],book=newBook,user=user)
    print "NEW BOOK IS============",newBook
    return redirect('/success')

def create_book(request):
    result = Book.objects.validate_inputs(request)
    if result[0]==True:
        print "NO ERRORS"
        print "result[1] is==========>",result[1]
        return add_book(request,result[1])
    print_messages(request,result[1])
    return redirect('/add_book_review')

def print_messages(request, message_list):
    for message in message_list:
        messages.add_message(request, messages.INFO, message)

def log_user_in(request,user):
    request.session['user'] = {
            'id':user.id,
            'first_name':user.first_name,
            'alias':user.alias,
            'email':user.email,
    }
    return redirect('/success')

def logout(request):
    request.session.pop('user')
    return redirect('/')
