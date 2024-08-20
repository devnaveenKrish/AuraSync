from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"), 
    path('user_login', views.user_login, name="user_login"), 
    path('singup', views.singup, name="singup"), 
    path('user_logout', views.user_logout, name='user_logout'), 
    path('analysis', views.analysis, name='analysis')
]