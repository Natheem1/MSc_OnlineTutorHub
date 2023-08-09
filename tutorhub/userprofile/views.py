from django.shortcuts import render, redirect 
from django.contrib.auth import login, authenticate, logout
from users.models import NewUser
from . models import TutorProfile, StudentProfile

#LOGIN PAGE
def loginUser(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('subjects')


    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = NewUser.objects.get(username=username)
        except:
            print('USERNAME DOES NOT EXIST')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print('LOGGED IN - WELCOME TO TUTOR HUB')
            return redirect('tutor-profiles')
        else:
            print('LOGIN FAILD - USERNAME OR PASSWORD IS INVALID')

    return render(request, 'userprofile/login-signup.html')


#LOGOUT PAGE 
def logoutUser(request):
    logout(request)
    return redirect('login')

#USER REGISTRATION PAGE
def registerUser(request):
    page = 'register'
    context = {'page': page}
    return render(request, 'userprofile/login-signup.html', context)


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