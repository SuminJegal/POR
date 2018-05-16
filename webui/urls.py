from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='default'),
    url('home_v2', views.home_v2, name='home_v2'),
    url('home', views.home, name='home'),
]
