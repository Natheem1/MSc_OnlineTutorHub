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

#EDIT TUTOR PROFILE SIGNAL
def updateTutorUser(sender, instance, created, **kargs):
    tutorprofile = instance 
    user = tutorprofile.user

    if created == False:
        user.first_name = tutorprofile.name
        user.username = tutorprofile.username 
        user.email = tutorprofile.email
        user.save()


post_save.connect(updateTutorUser, sender=TutorProfile)


#EDIT STUDENT PROFILE SIGNAL
def updateStudentUser(sender, instance, created, **kargs):
    studentprofile = instance 
    user = studentprofile.user

    if created == False:
        user.first_name = studentprofile.name
        user.username = studentprofile.username
        user.email = studentprofile.email
        user.save()


post_save.connect(updateStudentUser, sender=StudentProfile)


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