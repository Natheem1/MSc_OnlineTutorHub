from django.contrib import admin
from .models import StudentProfile, TeachingLevel, TutorProfile, Subject

admin.site.register(StudentProfile)
admin.site.register(TutorProfile)
admin.site.register(Subject)
admin.site.register(TeachingLevel)
