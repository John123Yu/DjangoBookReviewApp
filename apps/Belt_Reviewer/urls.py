from django.conf.urls import url, include # Notice we added include
from . import views

urlpatterns = [
	url(r'^books$', views.index, name = "index"),
	url(r'^books/new$', views.createDisplay, name = "createDisplay"),
	url(r'^bookscreate$', views.create, name = "create"),
	url(r'^books(?P<id>\d+)$', views.show, name = "show"),
	url(r'^books(?P<id>\d+)/showuser$', views.showUser, name = "showUser"),
	url(r'^books(?P<id>\d+)/delete$', views.delete, name = "delete"),
	url(r'^bookslogout$', views.logout, name = "logout"),
	url(r'^booksNewReview$', views.newReview, name = "newReview")

]