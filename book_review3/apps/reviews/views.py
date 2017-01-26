from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Book, Review
# from sets import Set

# Create your views here.
def index(request):
    return render(request, 'reviews/index.html')

def register(request):
    result = User.objects.validateReg(request)
    if result[0]==False:
        print_messages(request, result[1])
        return redirect('/')
    return log_user_in(request,result[1])

def add_review(request,book_id):
    books = Book.objects.all()
    book = Book.objects.get(id=book_id)
    reviews = Review.objects.filter(book__id=book_id)
    context = {
        'books':books,
        'book':book,
        'reviews':reviews
    }
    return render(request, 'reviews/book.html',context)

def delete_review(request,review_id):
    review = Review.objects.get(id=review_id)
    context = {
        'review':review
    }
    return render(request,'reviews/delete_review.html',context)

def destroy_review(request,review_id):
    Review.objects.get(id=review_id).delete()
    return redirect('/success')

def append_review(request,book_id):
    result = Review.objects.validate_inputs(request)
    if result[0]==False:
        print_messages(request,result[1])
    else:
        book = Book.objects.get(id=book_id)
        user = User.objects.get(id=request.session['user']['id'])
        newReview = Review.objects.create(review=request.POST['review'],rating=request.POST['rating'],book=book, user=user)
    return redirect('/add_review/{}'.format(book_id))

def user_reviews(request,user_id):
    user = User.objects.get(id=user_id)
    # reviews = list(set(Review.objects.filter(user__id=user_id)))
    reviews = Review.objects.all().filter(user__id=user_id).values('book__id','book__title').distinct()

    print "REVIEWS IS =========>",reviews
    # for review in reviews:
    #     print review.review
    count = len(reviews)
    context = {
        'user':user,
        'reviews':reviews,
        'count':count,
    }
    return render(request,'reviews/user_reviews.html',context)

def success(request):
    if 'user' not in request.session:
        return redirect('/')
    review_list = Review.objects.all().order_by('-created_at')
    book_list = Book.objects.all().order_by('-created_at')[:3]
    book_list2 = Book.objects.all()
    user_list = User.objects.all()[:3]
    print book_list[0].title
    context = {
        'users': user_list,
        'books': book_list,
        'books2': book_list2,
        'reviews': review_list
    }
    return render(request, 'reviews/home.html',context)

def login(request):
    result = User.objects.validateLogin(request)

    if result[0]==False:
        print_messages(request, result[1])
        return redirect('/')
    return log_user_in(request,result[1])

def add_book_review(request):
    books = Book.objects.values('author').distinct()
    context = {
        'books':books
    }
    return render(request, 'reviews/add_book.html',context)

def multiple_book_check(request,book):
    errors = []
    review_list = Review.objects.filter(user_id=request.session['user']['id'])
    print "PRINTING LIST OF REVIEWS BY THIS USER=====>",review_list
    if len(review_list)<1:
        return (True, book)
    else:
        for review in review_list:
            if review.book.title.lower()==book['title'].lower():
                errors.append("You already wrote a review for that book")
                return (False,errors)
            else:
                return (True, book)

def add_book(request,book):
    #check if user already created a review for that book

    user = User.objects.get(id=request.session['user']['id'])
    #gets a list of books the user has reviewed
    review_list = Review.objects.filter(user_id=request.session['user']['id'])
    #check if a book title that was entered matches any of these books
    result = multiple_book_check(request,book)
    if result[0]==True:
        newBook = Book.objects.create(title=book['title'], author=book['author'])
        # print "THIS IS THE review WE JUST WROTE====>",book['review']
        newReview = Review.objects.create(review=book['review'],rating=book['rating'],book=newBook,user=user)
        print "NEW BOOK IS============",newBook
        return redirect('/success')
    else:
        print_messages(request,result[1])
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
    messages.add_message(request, messages.INFO, "successfully logged in! VALID EMAIL {}".format(user.email))
    return redirect('/success')

def logout(request):
    request.session.pop('user')
    return redirect('/')
