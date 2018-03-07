from django.conf.urls import url
from . import views

urlpatterns={
    url(r'^$', views.index, name='index'),
    url(r'^index', views.index, name='index'),
    url(r'^appointment', views.appointment, name='appointment'),
    url(r'^contact', views.contact, name='contact'),
    url(r'^edit_profile', views.edit_profile, name='edit_profile'),
    url(r'^forgot', views.forgot, name='forgot'),
    url(r'^login', views.login, name='login'),
    url(r'^map', views.map, name='map'),
    url(r'^register', views.register, name='register'),
    url(r'^service', views.service, name='service'),
    url(r'^verify', views.verify, name='verify'),
}