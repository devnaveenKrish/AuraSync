from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_login, name="admin_login"),
    path('dashboard', views.admin_index, name='admin_index'), 
    path('logout', views.admin_logout, name='admin_logout'),
    path('psychometric_questions', views.psychometric_questions, name = 'psychometric_qn'),
    path('create_question', views.create_question, name = 'create_question'),
    path('delete_question/<int:qn_id>', views.delete_question, name = 'delete_question'),
    path('edit_question/<int:qn_id>', views.edit_question, name = 'edit_question'),
]