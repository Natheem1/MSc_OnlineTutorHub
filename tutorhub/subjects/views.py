from django.shortcuts import render
# from django.http import HttpResponse


def subjects(request):
    return render(request, 'subjects.html')


def subject(request, pk):
    return render(request, 'single-subject.html')