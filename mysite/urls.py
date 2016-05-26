"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views
#from login.views import *
#import login

urlpatterns = [
    url(r'^practice/', include('practice.urls')),
    url(r'^questionaire/', include('questionaire.urls')),
    #url(r'^', views.index, name='index'),
    url(r'^', include('dashboard.urls')),
    #url(r'^', 'django.contrib.auth.views.login'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page
    url(r'^user/', include('login.urls')),
    #url(r'^register/login/', include('login.urls')),
    #url(r'^register/success/', register_success),
    #url(r'^home/', home),
    #url(r'^logout/', logout_page),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
