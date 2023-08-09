from users.models import NewUser
from django.db.models.signals import post_save, post_delete
from django.conf import settings
from .models import StudentProfile, TutorProfile

#CREATE PROFILE SINGAL 
def createProfile(sender, instance, created, **kargs):
    if created and isinstance(instance, NewUser):
        user = instance
        if user.user_type == 'student':
            stuprofile = StudentProfile.objects.create(
                user=user,
                username=user.username,
                email=user.email,
                name=user.first_name,
            )
            print('STUDENT PROFILE CREATE BY SIGNAL TRIGGERED')

        elif user.user_type == 'tutor':
            tutprofile = TutorProfile.objects.create(
                user=user,
                username=user.username,
                email=user.email,
                name=user.first_name,
            )
            print('TUTOR PROFILE CREATED BY SIGNAL TRIGGERED')

post_save.connect(createProfile, sender=settings.AUTH_USER_MODEL)


#DELETE PROFILE SIGNAL
def deleteUser(sender, instance, **kargs):
    try:
        print("USER DETETED")
        user = instance.user
        user.delete()
    except NewUser.DoesNotExist:
        print("USER DELETED FROM NEWUSER TABLE AND NO LONGER EXISTS Deleted")
        print("SIGN UP AGAIN")


post_delete.connect(deleteUser, sender=TutorProfile)
post_delete.connect(deleteUser, sender=StudentProfile)