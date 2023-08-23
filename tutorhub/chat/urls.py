from django.urls import path 
from . import views 

urlpatterns = [
    path('chat/', views.AllChatRooms, name="all-rooms"),
    path('room/<str:pk>', views.room, name="room"),

    path('studentchat-user/<str:pk>/', views.StudentChatUser, name="studentchat-profile"),
    

    path('create-topic/', views.createTopic, name="create-topic"),

    path('create-rooom/', views.createRoom, name="create-room"),
    path('update-room/<str:pk>', views.updateRoom, name="update-room"),
    path('delete-room/<str:pk>', views.deleteRoom, name="delete-room"),
    path('delete-message/<str:pk>', views.deleteMessage, name="delete-message"),

    path('topics/', views.topicsPage, name="topics"),
    path('activity/', views.activityPage, name="activity"),
]