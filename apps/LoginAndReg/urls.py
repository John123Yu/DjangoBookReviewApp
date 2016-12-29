from django.conf.urls import url, include # Notice we added include
from . import views

urlpatterns = [
	url(r'^$', views.index, name = "index"),
	url(r'^users$', views.register, name = "register"),
	url(r'^login$', views.login, name = "login"),
	url(r'^success$', views.success, name = "success")
	]
# 	url(r'^emails$', views.create),
# 	url(r'^success$', views.success),
# 	url(r'^emails/(?P<id>[0-9]*)/delete', views.destroy)
# ]