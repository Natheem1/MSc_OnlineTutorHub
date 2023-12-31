from django.db import models
import uuid
from django.conf import settings
from django.core.validators import MinLengthValidator

# STUDENT PROFILE TABLE
class StudentProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, 
                                       null=True, blank=True)
    email = models.EmailField(max_length=500, blank=False, null=True)
    username = models.CharField(max_length=200, blank=False, null=True)
    name = models.CharField(max_length=200, blank=False, null=True)
    first_name = models.CharField(max_length=300, blank=False, null=True)
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
    Year_group = models.CharField(max_length=200, choices=EDUCATION_LEVEL)
    interested_subjects = models.ManyToManyField('MainSubjSkill',blank=True)

    profile_image = models.ImageField(null=True, blank=True, upload_to='student-profile-img/', 
                                      default="defaultprofileimg/studentdefault.png")
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    parent_name = models.CharField(max_length=150, blank=True, null=True)
    parent_email = models.EmailField(max_length=500, blank=True, null=True)
    parent_phone = models.CharField(max_length=20, blank=True, null=True)
    parent_pro_image = models.ImageField(null=True, blank=True, upload_to='student-parent-profile-img/', 
                                      default="defaultprofileimg/parentm.png")

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
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, 
                                     null=True, blank=True)
    email = models.EmailField(max_length=500, blank=False, null=True)
    username = models.CharField(max_length=100, blank=False, null=True)
    name = models.CharField(max_length=200, blank=False, null=True)
    first_name = models.CharField(max_length=300, blank=False, null=True)
    last_name = models.CharField(max_length=300, blank=True, null=True)
    location = models.CharField(max_length=500, blank=True, null=True)
    short_intro = models.CharField(max_length=200, blank=False, null=True)
    bio = models.TextField(blank=False, null=True, validators=[MinLengthValidator(50, "Bio must be at least 50 characters long.")])
    hourly_rate = models.CharField(max_length=20, blank=True, null=True)
    teaching_subjects = models.ManyToManyField('MainSubjSkill',blank=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='tutor-profile-img/', 
                                      default="defaultprofileimg/default.png")
    profile_image_uploaded = models.BooleanField(default=False)
    
    
    identification = models.ImageField(upload_to='tutor-id/', default="default-image/identification.png")
    identification_uploaded = models.BooleanField(default=False)

    degree = models.ImageField(null=True, blank=True, upload_to='tutor-degree/', default="default-image/degree.png")
    degree_uploaded = models.BooleanField(default=False)
    
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, 
                          unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.username)
    

    

# SUBJECT TABLE - its for the Tutor Table/Model
class MainSubjSkill(models.Model):
    owner = models.ForeignKey(TutorProfile, on_delete=models.CASCADE, null=True, blank=True)
    subject_name = models.CharField(max_length=200, unique=False)
    subject_description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, 
                          primary_key=True, editable=False)
    
    def __str__(self):
        return str(self.subject_name)

    


class Message(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='sent_messages')
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='received_messages')
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    subject = models.CharField(max_length=200, null=True, blank=True)
    body = models.TextField()
    is_read = models.BooleanField(default=False, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.subject

    class Meta:
        ordering = ['is_read', '-created']