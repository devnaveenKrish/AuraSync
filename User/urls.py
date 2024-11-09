from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"), 
    path('user_login', views.user_login, name="user_login"), 
    path('singup', views.singup, name="singup"), 
    path('user_logout', views.user_logout, name='user_logout'), 
    path('analysis', views.analysis, name='analysis'), 
    path('detect-facial-emotion/', views.detect_facial_emotion, name='detect_facial_emotion'),
    path('detail',views.detail, name='detail'),
    path('trainer_dashboard',views.trainer_dashboard,name = 'trainer_dashboard'),
    path('Analysis_page/<int:user_id>',views.Analysis_page,name = 'Analysis_page'),
    path('trainer',views.trainer,name = 'trainer'),
    path('trainer_assign/<int:trainer_id>',views.trainer_assign,name = 'trainer_assign'),
    path('trainer_disallocate/<int:user_id>', views.trainer_disallocate, name="trainer_disallocate"), 
    
]