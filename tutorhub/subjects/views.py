from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from .models import Subject, Tag
from .forms import SubjectForm, ReviewForm
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required
from .utils import searchsubjects



def subjects(request):
    subjects, search_query = searchsubjects(request)

    page = request.GET.get('page') 
    results = 6
    paginator = Paginator(subjects, results)

    try:
        subjects = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        subjects = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        subjects = paginator.page(page)
    
    context = {'subjects': subjects, 'search_qurey': search_query, 'paginator': paginator}
    return render(request, 'subjects/subjects.html', {'subjects':subjects})


def subject(request, pk):
    subjectObj = Subject.objects.get(id=pk)

    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.subject = subjectObj
        review.owner = request.user.studentprofile
        review.save()

        subjectObj.getVoteCount

        messages.success(request, 'Review Successful Submitted')
        return redirect('subject', pk=subjectObj.id)

    tags = subjectObj.tags.all()

    user_type = request.user.user_type if request.user.is_authenticated and request.user.user_type == 'tutor' else None

    return render(request, 'subjects/single-subject.html', {'subject': subjectObj, 'tags': tags, 'form': form, 'user_type': user_type})

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