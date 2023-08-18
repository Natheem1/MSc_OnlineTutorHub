from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
    path('signup/', views.signupPage, name="signup"),
    


    path('tutor-profiles/', views.tutorProfiles, name="tutor-profiles"),
    path('student-profiles/', views.studentProfiles, name="student-profiles"),

    path('tutor/<str:pk>/', views.tutorProfile, name="tutor-profile"),
    path('student/<str:pk>/', views.studentProfile, name="student-profile"),

    path('tutor-account/', views.tutorAccount, name="tutor-account"),
    path('student-account/', views.studentAccount, name="student-account"),

    path('edit-tutor/account/', views.editTAccount, name="edit-taccount"),
    path('edit-tutor/id/account', views.editTutorId, name="edit-tidaccount"),
    path('edit-tutor/degree/account', views.editTutorDegree, name="edit-tdegreeaccount"),
    path('view-tutor-id/', views.viewTutorId,name="view-tutorid" ),
    path('view-tutor-degree/', views.viewTutorDegree,name="view-tutordegree" ),

    path('edit-student/account/', views.editSAccount, name="edit-saccount"),
    path('edit-studentparent/account/', views.editSPAccount, name="edit-spaccount"),


    path('add-teaching/subject/', views.addTeachSubject, name="add-teach-subject"),
    path('edit-teaching/subject/<str:pk>/', views.editTeachSubject, name="edit-teach-subject"),
    path('delete-teaching/subject/<str:pk>/', views.deleteTeachSubject, name="delete-teach-subject"),

    path('add-interested/subject/', views.addIntrestedSubject, name="add-interested-subject"),



    path('inbox/', views.inbox, name="inbox"),
    path('message/<str:pk>/', views.viewMessage, name="message"),
    path('send-message/<str:pk>/', views.createMessageTutor, name="create-message"),

    path('send-message-students/<str:pk>/', views.createMessageStudent, name="create-message-students"),

    path('reply-message/<str:pk>/', views.replyMessage, name="reply-message"),

]