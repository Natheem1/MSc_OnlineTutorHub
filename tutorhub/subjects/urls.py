from django.urls import path 
from . import views

# Responsible for defining the URL patterns and routing the incoming HTTP requests 
# to specific view functions within the app.

urlpatterns = [
    path('subjects/', views.subjects, name="subjects"),
    path('subject/<str:pk>', views.subject, name="subject"),

]