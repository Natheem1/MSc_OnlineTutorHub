from django.contrib import admin
from .models import StudentProfile, TeachingLevel, TutorProfile, MainSubjSkill, Message

admin.site.register(StudentProfile)
admin.site.register(TutorProfile)
admin.site.register(MainSubjSkill)
admin.site.register(TeachingLevel)
admin.site.register(Message)
