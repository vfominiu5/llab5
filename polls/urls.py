from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^articles/$', views.index, name='index'),
    url(r'^articles/(?P<id>(\d+))$', views.article, name='article'),
    url(r'^mems/$', views.mems, name='mems')
]