from django.forms import ModelForm, CheckboxSelectMultiple
from django.contrib.auth.forms import UserCreationForm
from .models import NewUser
from userprofile .models import StudentProfile, TutorProfile, MainSubjSkill
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
                   'short_intro', 'bio', 'teaching_level', 
                   'hourly_rate', 'profile_image'] 
        
        widgets = {
            'teaching_level': CheckboxSelectMultiple,
            'teaching_subjects': CheckboxSelectMultiple,
        }
        
    
    def __init__(self,*args, **kwargs):
        super(TutorProfileForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
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
        fields = '__all__'
        exclude = ['owner']
        
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
