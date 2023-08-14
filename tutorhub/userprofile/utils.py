from django.db.models import Q
from .models import TutorProfile, MainSubjSkill


def searchTutors(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    subject = MainSubjSkill.objects.filter(subject_name__icontains=search_query)

    tutors = TutorProfile.objects.distinct().filter(
        Q(name__icontains=search_query) |
        Q(short_intro__icontains=search_query) |
        Q(hourly_rate__icontains=search_query) |
        Q(mainsubjskill__in=subject)
    )

    return tutors, search_query 