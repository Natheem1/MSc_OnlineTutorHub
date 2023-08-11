from django.urls import path 
from . import views


urlpatterns = [
    path('', views.subjects, name="subjects"),
    path('subject/<str:pk>/', views.subject, name="subject"),

    path('add-subject/', views.addSubject, name="add-subject"),

    path('edit-subject/<str:pk>/', views.editSubject, name="edit-subject"),
    path('delete-subject/<str:pk>/', views.deleteSubject, name="delete-subject"),
]