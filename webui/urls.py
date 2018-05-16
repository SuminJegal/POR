from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home_v2, name='home_v2'),
]
