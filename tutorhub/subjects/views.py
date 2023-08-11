from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Subject
from .forms import SubjectForm



def subjects(request):
    subjects = Subject.objects.all()
    context = {'subjects': subjects}
    return render(request, 'subjects/subjects.html', {'subjects':subjects})


def subject(request, pk):
    subjectObj = Subject.objects.get(id=pk)
    tags = subjectObj.tags.all()
    return render(request, 'subjects/single-subject.html', {'subject': subjectObj, 'tags': tags})

def addSubject(request):
    # tutorSubject = request.user.tutorprofile
    form = SubjectForm()

    if request.method == 'POST':
        form = SubjectForm(request.POST, request.FILES)
        if form .is_valid():
            form.save()
            return redirect('subjects')
        
    context = {'form': form}
    return render(request, 'subjects/subject-form.html', context)


def editSubject(request, pk):
    subject = Subject.objects.get(id=pk)
    form = SubjectForm(instance=subject)

    if request.method == 'POST':
        form = SubjectForm(request.POST, request.FILES, instance=subject)
        if form .is_valid():
            form.save()
            return redirect('subjects')
        
    context = {'form': form}
    return render(request, 'subjects/subject-form.html', context)

def deleteSubject(request, pk):
    subject = Subject.objects.get(id=pk)
    if request.method == 'POST':
        subject.delete()
        return redirect('subjects')
    context = {'object': subject}
    return render(request, 'subjects/delete-template.html', context)