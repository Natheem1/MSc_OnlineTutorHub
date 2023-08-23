from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib import messages
from users.forms import MyUserCreationForm, TutorProfileForm, StudentProfileForm, TeachSubjectForm, InterestedSubjectForm, StudentProfileParentForm, TutorIDForm, TutorDegreeForm, MessageForm, MessageReplyForm
from django.db import IntegrityError
from .utils import searchTutors, paginateTutorProfiles, paginateStudentProfiles, searchStudents
from users.models import NewUser
from . models import TutorProfile, StudentProfile, MainSubjSkill, Message

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


#ALL TUTOR PROFILES WITH SEARCH & PAGE NUMBER FUNCTIONS - DONE
def tutorProfiles(request):
    tutors, search_query = searchTutors(request)
    page_number_range, tutors = paginateTutorProfiles (request, tutors, 3)
    
    context = {'tutors': tutors, 'search_query': search_query, 'page_number_range': page_number_range}
    return render(request, 'userprofile/tutorprofile/tutor-profiles.html', context)



#SINGLE TUTOR PROFILE - IN PROGRESS
def tutorProfile(request,pk):
    tutorObj = TutorProfile.objects.get(id=pk)

    mainSubjects = tutorObj.mainsubjskill_set.exclude(subject_description__exact="")
    otherSubjects = tutorObj.mainsubjskill_set.filter(subject_description="")

    context = {'tutorObj': tutorObj, 'mainSubjects': mainSubjects, 
               'otherSubjects': otherSubjects}
    return render(request, 'userprofile/tutorprofile/single-tutor.html', context)



#TUTOR ACCOUNCT 'CRUD' - Tutor
@login_required(login_url='login')
def tutorAccount(request):
    account = request.user.tutorprofile

    teachings = account.mainsubjskill_set.all()
    subjects = account.subject_set.all()
    
    context = {'account': account, 'teachings': teachings, 'subjects': subjects}
    return render(request, 'userprofile/tutorprofile/tutor-account.html', context)




#EDIT USER PROFILE ACCOUNT - Tutor
@login_required(login_url='login')
def editTAccount(request):
    tutprofile = request.user.tutorprofile
    tutorform = TutorProfileForm(instance=tutprofile)

    if request.method == 'POST':
        tutorform = TutorProfileForm(request.POST, request.FILES, instance=tutprofile)
        if tutorform.is_valid():
            tutor_profile = tutorform.save(commit=False)
            
            if tutorform.cleaned_data['revert_profileimage']:
                tutor_profile.profile_image_uploaded = False
                tutor_profile.profile_image = tutor_profile._meta.get_field('profile_image').get_default()
            
            tutor_profile.save()

            return redirect('tutor-account')
 
    context = {'tutorform': tutorform}
    return render(request, 'userprofile/tutorprofile/tutorprofile-form.html', context)


#TUTOR ID FORM
@login_required(login_url='login')
def editTutorId(request):
    tutprofile = request.user.tutorprofile
    tutoridform = TutorIDForm(instance=tutprofile)

    if request.method == 'POST':
        tutoridform = TutorIDForm(request.POST, request.FILES, instance=tutprofile)
        if tutoridform.is_valid():
            tutoridform.save()

            return redirect('tutor-account')
        
    context = {'tutoridform': tutoridform}
    return render(request, 'userprofile/tutorprofile/tutorid-form.html', context)

#VIEW TUTOR ID DOCUMENT 
@login_required(login_url='login')
def viewTutorId(request):
    tutorid = request.user.tutorprofile

    context = {'tutorid':tutorid}
    return render(request, 'userprofile/tutorprofile/viewtutorid.html', context) 

#TUTOR DEGREE FORM
@login_required(login_url='login')
def editTutorDegree(request):
    tutprofile = request.user.tutorprofile
    tutordegreeform = TutorDegreeForm(instance=tutprofile)

    if request.method == 'POST':
        tutoridform = TutorDegreeForm(request.POST, request.FILES, instance=tutprofile)
        if tutoridform.is_valid():
            tutoridform.save()

            return redirect('tutor-account')
        
    context = {'tutordegreeform': tutordegreeform}
    return render(request, 'userprofile/tutorprofile/tutordegree-form.html', context)

#VIEW TUTOR DEGREE DOCUMENT 
@login_required(login_url='login')
def viewTutorDegree(request):
    tutordegree = request.user.tutorprofile

    context = {'tutordegree':tutordegree}
    return render(request, 'userprofile/tutorprofile/viewtutordegree.html', context) 


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
    return render(request, 'userprofile/tutorprofile/teachingsubjects-form.html', context)

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
    return render(request, 'userprofile/tutorprofile/teachingsubjects-form.html', context)

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






#ALL STUDENT PROFILES WITH SEARCH & PAGE NUMBER FUNCTIONS - DONE
def studentProfiles(request):
    students, search_qurey = searchStudents(request)
    page_number_range, students = paginateStudentProfiles (request, students, 3)

    context = {'students': students, 'search_query': search_qurey, 'page_number_range':page_number_range}
    return render (request, 'userprofile/studentprofile/student-profiles.html', context)


#SINGLE STUDENT PROFILE
def studentProfile(request,pk):
    studentObj = StudentProfile.objects.get(id=pk)
    context = {'studentObj': studentObj}
    return render(request, 'userprofile/studentprofile/single-student.html', context)


#STUDENT ACCOUNCT 'CRUD' - Student
@login_required(login_url='login')
def studentAccount(request):
    stuaccount = request.user.studentprofile

    interested = stuaccount.interested_subjects.all()
  
    context = {'stuaccount': stuaccount, 'interested':interested}
    return render(request, 'userprofile/studentprofile/student-account.html', context)



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
    return render(request, 'userprofile/studentprofile/studentprofile-form.html', context)


#EDIT STUDENT PROFILE PARENT ACCOUNT  - Student
@login_required(login_url='login')
def editSPAccount(request): 
    stuprofile = request.user.studentprofile
    studentparentform = StudentProfileParentForm(instance=stuprofile)

    if request.method == 'POST':
        studentparentform = StudentProfileParentForm(request.POST, request.FILES, instance=stuprofile)
        if studentparentform.is_valid():
            studentparentform.save()

            return redirect('student-account')

    context = {'studentparentform':studentparentform}
    return render(request, 'userprofile/studentprofile/studentparent-form.html', context)



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
    return render(request, 'userprofile/studentprofile/interestedsubjects-form.html', context)




#MESSAGE FUNCTIONS 

#MESSAGE INBOX 
@login_required(login_url='login')
def inbox(request):
    current_user = request.user  
   
   # Checks if the user is a student or tutor and then redirects them 
    if current_user.user_type == 'student':
        profilepk = current_user.studentprofile.pk
    else:
        profilepk = None

    messageRequests = current_user.received_messages.all()
    unreadCount = messageRequests.filter(is_read=False).count()

    context = {'messageRequests':messageRequests,'unreadCount': unreadCount, 'profilepk':profilepk }
    return render(request, 'userprofile/inbox.html', context)


# MESSAGE VIEW 
@login_required(login_url='login')
def viewMessage(request, pk):
    current_user = request.user
    message = current_user.received_messages.get(id=pk)
    if message.is_read == False:
        message.is_read = True
        message.save()

    context = {'message': message}
    return render(request, 'userprofile/message.html', context)

#CREATE MESSGE as a Tutor (User)
def createMessageTutor(request,pk):
    sender= request.user
    trecipient = TutorProfile.objects.get(id=pk)
    form = MessageForm()

    if not sender.is_authenticated:
        messages.error(request, 'You Must be Signed In or Registered To Send Messages')
        return redirect('signup') 

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = sender
            message.recipient = trecipient.user

            if sender:
                message.name = sender.username
                message.email = sender.email
            message.save()

            messages.success(request, 'Message Sent Successfully')

            return redirect('tutor-profile', pk=trecipient.id)

    context = {'trecipient':trecipient, 'form':form}
    return render (request, 'userprofile/message-form.html', context)

#CREATE MESSGE as a Student to Students 
def createMessageStudent(request, pk):
    sender = request.user 
    srecipient = StudentProfile.objects.get(id=pk)
    form = MessageForm

    if not sender.is_authenticated:
        messages.error(request, 'You Must Be Signed In or Registered To Send Messages')
        return redirect('signup')
    
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = sender
            message.recipient = srecipient.user

            if sender:
                message.name = sender.username
                message.email = sender.email
            message.save()

            messages.success(request, 'Message Sent Successfully')

            return redirect('student-profile', pk=srecipient.id)

    context = {'srecipient':srecipient, 'form':form}
    return render (request, 'userprofile/message-form.html', context)

# MESSAGE DIRECT REPLY 

def replyMessage(request,pk):
    sender = request.user
    original_message = Message.objects.get(id=pk)



    # Set initial data for the reply form
    initial_data = {'subject': f"Re: {original_message.subject}"}
    form = MessageReplyForm(initial=initial_data)


    if request.method == 'POST':
        form = MessageReplyForm(request.POST)
        if form.is_valid():
            reply_message = form.save(commit=False)
            reply_message.sender = sender
            reply_message.recipient = original_message.sender

            if sender:
                reply_message.name = sender.username
                reply_message.email = sender.email
                reply_message.subject = f"Re: {original_message.subject}"
            reply_message.save()

            messages.success(request, 'Reply Sent Successfully')

            return redirect('inbox')
                


    context = {'original_message': original_message, 'form': form}
    return render(request, 'userprofile/replymessage-form.html', context)

