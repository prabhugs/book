from django.conf.urls import url

from . import views

app_name = 'questionaire'
urlpatterns = [
               url(r'^$', views.index, name='index'),
               url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
               url(r'^(?P<test_id>[0-9]+)/test/$', views.test, name='test'),
               url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
               url(r'^(?P<question_id>[0-9]+)/answer/$', views.answer, name='answer'),
#               url(r'^list/$', views.list, name='list'),
              ]
