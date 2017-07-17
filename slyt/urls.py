from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^(?P<pk>[\w{}.-]{1,40})/$', views.stik_redirect, name='stik_redirect'),
]