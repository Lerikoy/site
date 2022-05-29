from django.urls import path
from . import views

urlpatterns = [
    # post views
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    # re_path(r'^login/$', views.user_login, name='login'),
    # re_path(r'^logout/$', views.logout, name='logout'),
    # re_path(r'^logout-then-login/$', 'django.contrib.auth.views.logout_then_login', name='logout_then_login'),
    # re_path(r'^$', views.dashboard, name='dashboard'),
]