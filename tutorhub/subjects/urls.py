from django.urls import path 
from . import views


urlpatterns = [
    path('', views.subjects, name="subjects"),
    path('subject/<str:pk>', views.subject, name="subject"),
]