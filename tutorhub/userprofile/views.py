from django.shortcuts import render
from . models import TutorProfile, StudentProfile

#ALL TUTOR PROFILES
def tutorProfiles(request):
    tutors = TutorProfile.objects.all()
    context = {'tutors': tutors}
    return render(request, 'userprofile/tutor-profiles.html', context)

#ALL STUDENT PROFILES 
def studentProfiles(request):
    students = StudentProfile.objects.all()
    context = {'students': students}
    return render (request, 'userprofile/student-profiles.html', context)
