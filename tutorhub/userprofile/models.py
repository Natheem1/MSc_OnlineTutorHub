from django.db import models
import uuid
from django.conf import settings

# STUDENT PROFILE TABLE
class StudentProfile(models.Model):
    studentuser = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, 
                                       null=True, blank=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    first_name = models.CharField(max_length=300, blank=True, null=True)
    last_name = models.CharField(max_length=300, blank=True, null=True)
    short_goal = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    EDUCATION_LEVEL = (
        ('Year 7', 'Year 7 KS3'),
        ('Year 8', 'Year 8 KS3'),
        ('Year 9', 'Year 9 KS3'),
        ('Year 10', 'Year 10 KS4'),
        ('Year 11', 'Year 11 KS4'),
        ('Year 12', 'Year 12 KS5'),
        ('Year 13', 'Year 13 KS5'),
    )
    education = models.CharField(max_length=200, choices=EDUCATION_LEVEL)
    interested_subjects = models.ManyToManyField('Subject',blank=True)

    profile_image = models.ImageField(null=True, blank=True, upload_to='profiles/', 
                                      default="profiles/default.png")
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    parent_name = models.CharField(max_length=150, blank=True, null=True)
    parent_email = models.EmailField(max_length=500, blank=True, null=True)
    parent_phone = models.CharField(max_length=20, blank=True, null=True)

    PREFERRED_AVAILABILITY_CHOICES = [
        ('Weekday mornings', 'Weekday mornings'),
        ('Weekday afternoons', 'Weekday afternoons'),
        ('Weekday evenings', 'Weekday evenings'),
        ('Weekends mornings', 'Weekends mornings'),
        ('Weekends afternoons', 'Weekends afternoons'),
        ('Weekends evenings', 'Weekends evenings'),
    ]

    preferred_availability = models.CharField(
        max_length=100, choices=PREFERRED_AVAILABILITY_CHOICES, blank=True, null=True
    )

    def __str__(self):
        return str(self.username)
    



# TUTOR PROFILE TABLE
class TutorProfile(models.Model):
    tutoruser = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, 
                                     null=True, blank=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    first_name = models.CharField(max_length=300, blank=True, null=True)
    last_name = models.CharField(max_length=300, blank=True, null=True)
    location = models.CharField(max_length=500, blank=True, null=True)
    short_intro = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    teaching_level = models.ManyToManyField('TeachingLevel', blank=False) 
    hourly_rate = models.CharField(max_length=20, blank=True, null=True)
    teaching_subjects = models.ManyToManyField('Subject',blank=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='profiles/', 
                                      default="profiles/default.png")
    
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, 
                          unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.username)
    



# SUBJECT TABLE - its for the Tutor Table/Model
class Subject(models.Model):
    subject_name = models.CharField(max_length=60, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, 
                          primary_key=True, editable=False)
    
    def __str__(self):
        return str(self.subject_name)




# TEACHING LEVEL TABLE - - its for the Tutor Table/Model
class TeachingLevel(models.Model):
    teaching_level = models.CharField(max_length=60, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, 
                          primary_key=True, editable=False)
    
    def __str__(self):
        return str(self.teaching_level)