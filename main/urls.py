from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index_view, name='index_view'),
	#url(r'^(?P<input>\w+)/$', views.index_view),
	#url(r'^(?P<text>.+)/json$', views.text_json_view),
	#url(r'^(?P<text>.+)/$', views.text_result_view, name='url_link_for_intext'),
	url(r'^(?P<input>.+)/json$', views.json_view),
	url(r'^(?P<input>.+)/$', views.result_view, name='url_link'),
]