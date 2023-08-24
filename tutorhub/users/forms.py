from django.forms import ModelForm, CheckboxSelectMultiple, Select
from django.contrib.auth.forms import UserCreationForm
from .models import NewUser
from userprofile .models import StudentProfile, TutorProfile, MainSubjSkill, Message
from django import forms

class MyUserCreationForm(UserCreationForm):
    USER_TYPE_CHOICES = [
        ('tutor', 'Tutor'),
        ('student', 'Student'),
    ]

    user_type = forms.ChoiceField(
        choices=USER_TYPE_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'radio-buttons'}),
    )

    class Meta:
        model = NewUser
        fields = ('first_name','email', 'username','user_type', 'password1', 'password2')
        labels = {
            'first_name': 'Name',
        }

    def __init__(self,*args, **kwargs):
        super(MyUserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class TutorProfileForm(ModelForm):
    revert_profileimage = forms.BooleanField(label='Remove Profile Image Set to Default', required=False)


    class Meta:
        model = TutorProfile
        fields = ['name', 'username','email', 'first_name', 'last_name', 'location',
                   'short_intro', 'bio',  
                   'hourly_rate', 'profile_image'] 
        
        labels = {
            'bio': 'Bio - Minimum 50 Character Long'
        }
        
        widgets = {
            'teaching_level': CheckboxSelectMultiple(attrs={'class': 'column-checkbox'}),
            'teaching_subjects': CheckboxSelectMultiple,
            'profile_image': forms.ClearableFileInput(attrs={'clear_checkbox_label': ''})
        }
        
    
    def __init__(self,*args, **kwargs):
        super(TutorProfileForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            if name != 'teaching_level':
                field.widget.attrs.update({'class': 'input'})



class TutorIDForm(ModelForm):
    class Meta:
        model = TutorProfile
        fields = ['identification']
        
    
    def __init__(self,*args, **kwargs):
        super(TutorIDForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class TutorDegreeForm(ModelForm):
    class Meta:
        model = TutorProfile
        fields = ['degree']

    def __init__(self,*args, **kwargs):
        super(TutorDegreeForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class StudentProfileForm(ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['name', 'username', 'email', 'first_name', 'last_name', 'short_goal',
                   'bio', 'Year_group', 'profile_image', 'preferred_availability']
        
    
    def __init__(self,*args, **kwargs):
        super(StudentProfileForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})



class StudentProfileParentForm(ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['parent_pro_image','parent_name', 'parent_email', 'parent_phone']
        
    
    def __init__(self,*args, **kwargs):
        super(StudentProfileParentForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})



class TeachSubjectForm(ModelForm):
    class Meta:
        model = MainSubjSkill
        fields = ['subject_name', 'subject_description']
        
        labels = {
            'subject_name': 'Subject Title ', 'subject_description': 'Subject Description - Tell Us Something About The Subject You Teach'
        }
        
    def __init__(self,*args, **kwargs):
        super(TeachSubjectForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class InterestedSubjectForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['interested_subjects']  # Only the interested_subjects field

        widgets = {
            'interested_subjects': CheckboxSelectMultiple,
        }

    def __init__(self, *args, **kwargs):
        super(InterestedSubjectForm, self).__init__(*args, **kwargs)
        # Customize the form as needed
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['subject', 'body',]

        labels = {
            'subject': 'Reason For Messaging', 'body': 'Write Your Message Below'
        }


    def __init__(self,*args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

class MessageReplyForm(ModelForm):
    class Meta:
        model = Message
        fields = ['body']

        labels = {
            'body': 'Write Your Message Below'
        }

    def __init__(self,*args, **kwargs):
        super(MessageReplyForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
