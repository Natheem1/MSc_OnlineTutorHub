from django.urls import path
from . import views

urlpatterns = [
    path('tutor-profiles/', views.tutorProfiles, name="tutor-profiles"),
    path('student-profiles', views.studentProfiles, name="student-profiles"),

    path('tutor/<str:pk>', views.tutorProfile, name="tutor"),
    path('student/<str:pk>', views.studentProfile, name="student"),
]