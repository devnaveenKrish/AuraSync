from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_login, name="admin_login"),
    path('dashboard', views.admin_index, name='admin_index'), 
    path('logout', views.admin_logout, name='admin_logout'),
]