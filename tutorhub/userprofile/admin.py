from django.contrib import admin
from .models import StudentProfile, TutorProfile, MainSubjSkill, Message

admin.site.register(StudentProfile)
admin.site.register(TutorProfile)
admin.site.register(MainSubjSkill)
admin.site.register(Message)
