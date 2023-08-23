from django.db.models import Q
from .models import Tag, Subject
from django.core.paginator import Paginator


# Subject Page Numbers
def paginateSubjects(request, subjects, results):

    page = request.GET.get('page', 1)
    paginator = Paginator(subjects, results)

    page_number_range = paginator.page_range 
    subjects = paginator.get_page(page) 

    return page_number_range, subjects



# Subject Search Function 
def searchsubjects(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    tags = Tag.objects.filter(name__icontains=search_query)

    subjects = Subject.objects.distinct().filter(
        Q(title__icontains=search_query) |
        Q(description__icontains=search_query) |
        Q(owner__name__icontains=search_query) |
        Q(tags__in=tags)
    )

    return subjects, search_query 