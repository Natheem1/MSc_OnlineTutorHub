from django.urls import path 
from .import views 

urlpatterns = [
    path('videodashboard/', views.VideoLessonDashboard, name='video-dashboard'),
    path('joinlesson/', views.JoinLesson, name='join-lesson'),
    
    path('createlesson/', views.CreateVideoLesson, name='create-lesson'),
]