from django.urls import path
from . import views

urlpatterns = [
    path('', views.psychometric, name='psychometric'),
    path('test', views.psychometric_questions, name='psychometric_questions'),
]