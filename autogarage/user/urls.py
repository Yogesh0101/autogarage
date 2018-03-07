from django.conf.urls import url
from . import views

urlpatterns={
    url(r'^$', views.index, name='idex'),
    url(r'^index', views.index, name='idex'),
    url(r'^autogarage', views.autogarage, name='autogarage'),
    url(r'^book', views.book, name='book'),
    url(r'^contact', views.contact, name='contact'),
    url(r'^edit_profile', views.edit_profile, name='edit_profile'),
    url(r'^forgot', views.forgot, name='forgot'),
    url(r'^login', views.login, name='login'),
    url(r'^map', views.map, name='map'),
    url(r'^notification', views.notification, name='notification'),
    url(r'^profile', views.profile, name='profile'),
    url(r'^register', views.register, name='register'),
    url(r'^search', views.search, name='search'),
    url(r'^verify', views.verify, name='verify'),



}