from django.shortcuts import render

# Used for testing function and URL routes setup
from django.http import HttpResponse

# Dummy view functions for testing URL routes and setup.

def subjects(request):
    return HttpResponse("Search all Subjects here ")


def subject(request, pk):
    return HttpResponse("Single Subject" + "  " + str(pk))