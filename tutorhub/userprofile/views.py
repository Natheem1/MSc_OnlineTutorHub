from django.shortcuts import render, redirect 
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib import messages
from users.forms import MyUserCreationForm, TutorProfileForm, StudentProfileForm, TeachSubjectForm, InterestedSubjectForm
from django.db import IntegrityError
from .utils import searchTutors
from users.models import NewUser
from . models import TutorProfile, StudentProfile, MainSubjSkill

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
            messages.success(request, 'Signed In - Welcome to Tutor Hub')
            return redirect('tutor-profiles')
        else:
            messages.error(request,'LOGIN FAILED - USERNAME OR PASSWORD IS INVALID')

    return render(request, 'userprofile/login-signup.html')


#LOGOUT PAGE 
def logoutUser(request):
    logout(request)
    messages.info(request, 'Signed Out Successfully')
    return redirect('login')

#SIGN UP PAGE - STUDENT OR TUTOR
def signupPage(request):
    return render(request, 'userprofile/signup-page.html')

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

                messages.success(request, 'User Successfully Created')

                login(request, user)

                if user.user_type == 'tutor':
                    return redirect('edit-taccount')  # Redirect to tutor profile edit page
                elif user.user_type == 'student':
                    return redirect('edit-saccount')  # Redirect to student profile edit page
        
            except IntegrityError:
                messages.error(request, 'An account email already exists')
        else:
            messages.error(request, 'An Error Has Occurred During Registration')

    context = {'page': page, 'form': form}
    return render(request, 'userprofile/login-signup.html', context)


#ALL TUTOR PROFILES WITH SEARCH FUNCTION - DONE
def tutorProfiles(request):
    tutors, search_query = searchTutors(request)
    
    context = {'tutors': tutors, 'search_query': search_query}
    return render(request, 'userprofile/tutor-profiles.html', context)



#SINGLE TUTOR PROFILE - IN PROGRESS
def tutorProfile(request,pk):
    tutorObj = TutorProfile.objects.get(id=pk)

    mainSubjects = tutorObj.mainsubjskill_set.exclude(subject_description__exact="")
    otherSubjects = tutorObj.mainsubjskill_set.filter(subject_description="")

    context = {'tutorObj': tutorObj, 'mainSubjects': mainSubjects, 
               'otherSubjects': otherSubjects}
    return render(request, 'userprofile/single-tutor.html', context)



#TUTOR ACCOUNCT 'CRUD' - Tutor
@login_required(login_url='login')
def tutorAccount(request):
    account = request.user.tutorprofile

    teachings = account.mainsubjskill_set.all()
    subjects = account.subject_set.all()
    
    context = {'account': account, 'teachings': teachings, 'subjects': subjects}
    return render(request, 'userprofile/tutor-account.html', context)


#EDIT USER PROFILE ACCOUNT - Tutor
@login_required(login_url='login')
def editTAccount(request):
    tutprofile = request.user.tutorprofile
    tutorform = TutorProfileForm(instance=tutprofile)

    if request.method == 'POST':
        tutorform = TutorProfileForm(request.POST, request.FILES, instance=tutprofile)
        if tutorform.is_valid():
            tutorform.save()

            return redirect('tutor-account')
 
    context = {'tutorform': tutorform}
    return render(request, 'userprofile/tutorprofile-form.html', context)

#ADD TEACHING SUBJECTS - Tutor
@login_required(login_url='login')
def addTeachSubject(request):
    tutorprofile = request.user.tutorprofile 
    form = TeachSubjectForm()

    if request.method == 'POST':
        form = TeachSubjectForm(request.POST)
        if form.is_valid():
            addSubject = form.save(commit=False)
            addSubject.owner = tutorprofile
            addSubject.save()
            messages.success(request, 'Subject added successfully')
            return redirect('tutor-account')
        
    context = {'form': form}
    return render(request, 'userprofile/teachingsubjects-form.html', context)

# UPDATE TEACHING SUBJECTS - Tutor
@login_required(login_url='login')
def editTeachSubject(request, pk):
    profile = request.user.tutorprofile 
    subject = profile.mainsubjskill_set.get(id=pk)
    form = TeachSubjectForm(instance=subject)

    if request.method == 'POST':
        form = TeachSubjectForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            messages.success(request, 'Subject Edited successfully')
            return redirect('tutor-account')
        
    context = {'form': form, 'profile':profile, 'subject':subject}
    return render(request, 'userprofile/teachingsubjects-form.html', context)

#DELETE TEACHING SUBJECTS - Tutor
@login_required(login_url='login')
def deleteTeachSubject(request, pk):
    profile = request.user.tutorprofile
    subject = profile.mainsubjskill_set.get(id=pk)

    if request.method == 'POST':
        subject.delete()
        messages.success(request, 'Subject was deleted successfully')
        return redirect('tutor-account')

    context ={'subject': subject}
    return render(request, 'delete-template.html', context)





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


#STUDENT ACCOUNCT 'CRUD' - Student
@login_required(login_url='login')
def studentAccount(request):
    stuaccount = request.user.studentprofile

    interested = stuaccount.interested_subjects.all()
  
    context = {'stuaccount': stuaccount, 'interested':interested}
    return render(request, 'userprofile/student-account.html', context)



#EDIT STUDENT PROFILE ACCOUNT  - Student
@login_required(login_url='login')
def editSAccount(request): 
    stuprofile = request.user.studentprofile
    studentform = StudentProfileForm(instance=stuprofile)

    if request.method == 'POST':
        studentform = StudentProfileForm(request.POST, request.FILES, instance=stuprofile)
        if studentform.is_valid():
            studentform.save()

            return redirect('student-account')

    context = {'studentform': studentform}
    return render(request, 'userprofile/studentprofile-form.html', context)



#ADD INTERESTED SUBJECT - By Student 
@login_required(login_url='login')
def addIntrestedSubject(request):
    studentprofile = request.user.studentprofile
    form = InterestedSubjectForm()

    if request.method == 'POST':
        form = InterestedSubjectForm(request.POST, instance=studentprofile)
        if form.is_valid():
            form.save()  # This saves the selected subjects to the studentprofile
            messages.success(request, 'Subject added successfully')
            return redirect('student-account')

    context = {'form': form}
    return render(request, 'userprofile/interestedsubjects-form.html', context)
