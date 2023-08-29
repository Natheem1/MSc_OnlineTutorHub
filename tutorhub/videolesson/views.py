from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Video Lesson Main Dashboard 
@login_required
def VideoLessonDashboard(request):
    tutor = request.user.tutorprofile 

    context = {'tutor': tutor}
    return render(request, 'videolesson/videodashboard.html', context)

# Join Video Lesson 
@login_required
def JoinLesson(request):
    
    if request.method == 'POST':
        roomID = request.POST.get('roomID')
        return redirect("/createlesson?roomID=" + roomID)
    
    return render(request, 'videolesson/joinmeeting.html')


# Video Lesson - ZegoCloud
@login_required
def CreateVideoLesson(request):
    user = request.user

    context = {'user':user}
    return render(request, 'videolesson/createmeeting.html', context)