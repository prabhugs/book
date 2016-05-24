#from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import patterns, include, url
from . import views

#urlpatterns = [
#    url(r'^$', views.register, name='register'),
#    url(r'^login/', views.login, name='login'),
#    url(r'^register/success/', views.register_success, name='register_success'),
#]

urlpatterns = patterns('',
    url(r'^register/$', views.register, name='register'),
    url(r'^register/success/', views.register_success, name='register_success'),
    url(r'^login/$', 'django.contrib.auth.views.login'),

    url(r'^logout/$', views.logout_page, name='logout'),
#    url(r'^accounts/login/$', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page
#    url(r'^register/$', register),
#    url(r'^register/success/$', register_success),
#    url(r'^home/$', home),
)
