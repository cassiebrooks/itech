from django.conf.urls import patterns, url
from quokka import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^about/', views.about, name='about'),
	url(r'^add_answer/$', views.add_answer, name='add_answer'),
]