from __future__ import unicode_literals
from django.db import models
from ..LoginAndReg.models import User, LoginManager, RegisterManager
# Create your models here.


class Author(models.Model):
	name = models.CharField(max_length=100)
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)

class Book(models.Model):
	title = models.CharField(max_length=100)
	author_id = models.ForeignKey(Author)
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)

class Review(models.Model):
	review = models.TextField()
	rating = models.IntegerField()
	book_id = models.ForeignKey(Book)
	user_id = models.ForeignKey(User, related_name = 'userReviews')
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)

