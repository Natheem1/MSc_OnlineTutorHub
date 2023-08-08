from django.contrib import admin
from .models import Subject, Review, Tag

# Register your models here.
admin.site.register(Subject)
admin.site.register(Review)
admin.site.register(Tag)