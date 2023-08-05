from django.shortcuts import render
# from django.http import HttpResponse


subjectsList = [
    {
        'id': '1',
        'title': 'Mathematics',
        'description': 'Study of numbers, quantities, and shapes'
    },
    {
        'id': '2',
        'title': 'English Literature',
        'description': 'Exploration of written works in the English language'
    },
    {
        'id': '3',
        'title': 'Biology',
        'description': 'Study of living organisms and their interactions'
    }
]

def subjects(request):
    msg = 'Hello, your are on the Subjects page '
    return render(request, 'subjects/subjects.html', {'message':msg, 'subjects':subjectsList})


def subject(request, pk):
    subjectId = None
    for i in subjectsList:
        if i['id'] == pk:
            subjectId = i 
    return render(request, 'subjects/single-subject.html', {'subject': subjectId})