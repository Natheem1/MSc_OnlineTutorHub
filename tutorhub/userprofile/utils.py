from django.db.models import Q
from .models import TutorProfile, MainSubjSkill, StudentProfile
from django.core.paginator import Paginator




# Profiles Pagination Tutor Profile Page 
def paginateTutorProfiles(request, profiles, results):

    page = request.GET.get('page', 1)
    paginator = Paginator(profiles, results)

    page_number_range = paginator.page_range 
    paginated_profiles = paginator.page(page)

    return page_number_range, paginated_profiles


# Profiles Pagination student Profile Page 
def paginateStudentProfiles(request, profiles, results):

    page = request.GET.get('page', 1)
    paginator = Paginator(profiles, results)

    page_number_range = paginator.page_range 
    paginated_profiles = paginator.page(page)

    return page_number_range, paginated_profiles


# Tutor Search 
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


# Student Profile Search
def searchStudents(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    interested_subjects = MainSubjSkill.objects.filter(subject_name__icontains=search_query)

    students = StudentProfile.objects.distinct().filter(
        Q(name__icontains=search_query) |
        Q(short_goal__icontains=search_query) |
        Q(Year_group__icontains=search_query) |
        Q(interested_subjects__in=interested_subjects)
    )

    return students, search_query
