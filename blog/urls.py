from django.conf.urls import url
from . import views


urlpatterns = [
    url('home/', views.home, name='blog-home'),
    url('about/', views.about, name='blog-about'),
]
