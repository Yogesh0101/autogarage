from django.conf.urls import url
from . import views

urlpatterns={
    url(r'^$', views.index, name='index'),
    url(r'^login', views.login, name='login'),
    url(r'^index', views.index, name='index'),
    url(r'^profile', views.profile, name='profile'),
    url(r'^setting', views.setting, name='setting'),
    url(r'^view_garage', views.view_garage, name='view_garage'),
    url(r'^add_garage', views.add_garage, name='add_garage'),
    url(r'^adsreq', views.adsreq, name='adsreq'),
    url(r'^advertise', views.advertise, name='advertise'),
    url(r'^calendar', views.calendar, name='calendar'),
    url(r'^garage_request',views.garage_request, name='garage_request'),
    url(r'^messages', views.messages, name='messages'),
    url(r'^users', views.users, name='users'),
}