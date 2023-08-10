from django.shortcuts import render, redirect 
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from users.forms import MyUserCreationForm
from django.db import IntegrityError
# from django.contrib.auth.forms import UserCreationForm
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

        # try:
        #     user = NewUser.objects.get(username=username)
        # except NewUser.DoesNotExist:
        #     messages.error(request,'LOGIN FAILED - USERNAME DOES NOT EXIST')

        user = authenticate(request, username=username, password=password)
        # print("User authentication result:", user)

        if user is not None:
            login(request, user)
            messages.success(request, 'LOGGED IN - WELCOME TO TUTOR HUB')
            return redirect('tutor-profiles')
        else:
            messages.error(request,'LOGIN FAILED - USERNAME OR PASSWORD IS INVALID')

    return render(request, 'userprofile/login-signup.html')


#LOGOUT PAGE 
def logoutUser(request):
    logout(request)
    messages.info(request, 'You have been Logged out')
    return redirect('login')

#USER REGISTRATION PAGE
def registerUser(request):
    page = 'register'
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)

        if form.is_valid():
            try:
                user = form.save(commit=False)
                user.email = user.email.lower()
                # user.username = user.username.lower()
                user.save()

                messages.success(request, 'User Was Successful Created')

                login(request, user)
                return redirect('subjects')
            except IntegrityError:
                messages.error(request, 'An account with this email already exists')
        else:
            messages.error(request, 'An Error Has Occurred During Registration')

    context = {'page': page, 'form': form}
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