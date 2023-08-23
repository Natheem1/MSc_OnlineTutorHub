from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Subject, Tag, Review
from .forms import SubjectForm, ReviewForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .utils import searchsubjects, paginateSubjects
from datetime import timedelta
from django.utils import timezone



def subjects(request):
    subjects, search_query = searchsubjects(request)
    page_number_range, subjects = paginateSubjects(request, subjects, 6)
    
    context = {'subjects': subjects, 'search_qurey': search_query, 'page_number_range': page_number_range}
    return render(request, 'subjects/subjects.html', context)



def subject(request, pk):
    subjectObj = Subject.objects.get(id=pk)

    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.subject = subjectObj
        review.owner = request.user.studentprofile

        # Checks if the user has submitted a review for the specific subject in the last 2 hours
        last_review = Review.objects.filter(owner=request.user.studentprofile, subject=subjectObj).order_by('-created').first()
        if last_review:
            time_since_last_review = timezone.now() - last_review.created
            if time_since_last_review < timedelta(hours=2):
                messages.error(request, 'You Already Submitted a Review - Wait 5 hours ')
                return redirect('subjects')  

        review.save()

        subjectObj.getVoteCount

        messages.success(request, 'Review Successfully Submitted')
        return redirect('subject', pk=subjectObj.id)

    tags = subjectObj.tags.all()

    tutorprofile = subjectObj.owner

    user_type = request.user.user_type if request.user.is_authenticated and request.user.user_type == 'tutor' else None

    return render(request, 'subjects/single-subject.html', {'subject': subjectObj, 'tags': tags,
                                                             'form': form, 'user_type': user_type, 'tutorprofile': tutorprofile})


@login_required(login_url='login')
def addSubject(request):
    tutorprofile = request.user.tutorprofile
    form = SubjectForm()

    if request.method == 'POST':
        form = SubjectForm(request.POST, request.FILES)
        if form .is_valid():
            subject = form.save(commit=False)
            subject.owner = tutorprofile
            subject.save()
            return redirect('tutor-account')
        
    context = {'form': form}
    return render(request, 'subjects/subject-form.html', context)


@login_required(login_url='login')
def editSubject(request, pk):
    tutorprofile = request.user.tutorprofile
    subject = tutorprofile.subject_set.get(id=pk)
    form = SubjectForm(instance=subject)

    if request.method == 'POST':
        form = SubjectForm(request.POST, request.FILES, instance=subject)
        if form .is_valid():
            form.save()
            return redirect('tutor-account')
        
    context = {'form': form}
    return render(request, 'subjects/subject-form.html', context)

@login_required(login_url='login')
def deleteSubject(request, pk):
    tutorprofile = request.user.tutorprofile
    subject = tutorprofile.subject_set.get(id=pk)
    if request.method == 'POST':
        subject.delete()
        return redirect('tutor-account')
    context = {'object': subject}
    return render(request, 'delete-template.html', context)