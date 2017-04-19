from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.dictionary, name='index'),
    #url(r'^$', views.response, name='response'),
]