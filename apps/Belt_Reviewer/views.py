from django.shortcuts import render, HttpResponse, redirect
from models import Book, Review, Author
from ..LoginAndReg.models import User, LoginManager, RegisterManager
from django.core.urlresolvers import reverse
from django.db.models import Count 

def index(request):
	user = User.registerMgr.get(id = request.session['login'])
	context = {
        'book_reviews' : Review.objects.all(),
        'user_name': user.firstName,
        'books': Book.objects.all()
    }
	print context['books']
	return render(request, 'Belt_Reviewer/index.html', context)

def createDisplay(request):
	context = {
		'authors': Author.objects.all()
	}
	return render(request, 'Belt_Reviewer/addnew.html', context)

def create(request):
	author = Author(name = request.POST['author'])
	author.save()
	book = Book(title = request.POST['title'], author_id = author)
	book.save()
	user = User.registerMgr.get(id = request.session['login'])
	review = Review(review = request.POST['review'], rating = request.POST['rating'], book_id = book, user_id = user)
	review.save()
	return redirect(reverse('beltReviewer:index'))

def newReview(request):
	book = Book.objects.get(id = request.POST['title'])
	user = User.registerMgr.get(id = request.session['login'])
	review = Review(review = request.POST['review'], rating = request.POST['rating'], book_id = book, user_id_id = user.id)
	review.save()
	url = "/BeltReviewer/books" + str(book.id)
	return redirect(url)
	# return redirect(reverse('beltReviewer:index'))

def show(request, id):
	book = Book.objects.get(id = id)
	context = {
		'book_reviews': Review.objects.filter(book_id = book),
		'book': book
	}
	return render(request, 'Belt_Reviewer/show1.html', context)

def showUser(request, id):
	user = User.registerMgr.filter(id = id)
	context = {
		'users': user.annotate(reviewcount = Count('userReviews')),
		'books': Book.objects.filter(review__user_id = user)
	}
	return render(request, 'Belt_Reviewer/showuser.html', context)

def delete(request, id):
	review = Review.objects.filter(id = id)
	book = Book.objects.get(review = review)
	review.delete()
	url = "/BeltReviewer/books" + str(book.id)
	return redirect(url)
	# return redirect(reverse('beltReviewer:index'))

def logout(request):
    request.session['login'] = 0
    return redirect(reverse('login:index'))



