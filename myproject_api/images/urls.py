from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^create/$', views.image_create, name='create'),
]