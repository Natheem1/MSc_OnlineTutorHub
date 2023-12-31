from django.db import models
import uuid
from userprofile.models import TutorProfile, StudentProfile

# SUBJECTS TABLE
class Subject(models.Model):
    owner = models.ForeignKey(TutorProfile, null=True, blank=True, on_delete=models.SET_NULL)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    subject_image = models.ImageField(null=True, blank=True, upload_to='subject-image/' ,default="default-image/default-img.png")
    tags = models.ManyToManyField('Tag', blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    # String representation of the subject.
    def __str__(self):
        return self.title

    # Meta class for ordering subjects by creation date.
    class Meta:
        ordering = ['created']

    #Vote Calculation
    @property 
    def getVoteCount(self):
        reviews = self.review_set.all()
        upVotes = reviews.filter(value='up').count()
        totalVotes = reviews.count()

        ratio = (upVotes / totalVotes) * 100
        self.vote_total = totalVotes
        self.vote_ratio = ratio
        self.save()



# REVIEW TABLE 
class Review(models.Model):
    
    owner = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    # Vote type choices: up (positive) or down (negative).
    VOTE_TYPE = (
        ('up', 'Positive Vote'),
        ('down', 'Negative Vote'),
    )
    value = models.CharField(max_length=20, choices=VOTE_TYPE)

    # String representation of the review (its vote type)
    def __str__(self):
        return self.value


# TAG TABLE
class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    # String representation of the tag.
    def __str__(self):
        return self.name