from django.shortcuts import render
from . models import TutorProfile, StudentProfile

#ALL TUTOR PROFILES
def tutorProfiles(request):
    tutors = TutorProfile.objects.all()
    context = {'tutors': tutors}
    return render(request, 'userprofile/tutor-profiles.html', context)

#SINGLE TUTOR PROFILE
def tutorProfile(request,pk):
    tutorObj = TutorProfile.objects.get(id=pk)
    context = {'tutorObj': tutorObj}
    return render(request, 'userprofile/single-tutor.html', context)

#ALL STUDENT PROFILES 
def studentProfiles(request):
    students = StudentProfile.objects.all()
    context = {'students': students}
    return render (request, 'userprofile/student-profiles.html', context)

#SINGLE STUDENT PROFILE
def studentProfile(request,pk):
    studentObj = StudentProfile.objects.get(id=pk)
    context = {'studentObj': studentObj}
    return render(request, 'userprofile/single-student.html', context)