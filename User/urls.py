from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

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
    path('councellor',views.councellor,name = 'councellor'),
    path('detect_audio_file',views.detect_audio_file,name = 'detect_audio_file'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)