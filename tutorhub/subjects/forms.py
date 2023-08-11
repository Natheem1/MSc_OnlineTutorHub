from django.forms import ModelForm, widgets
from django import forms
from .models import Subject 

class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = ['title', 'subject_image','description',  'tags']

    #     widgets = {
    #         'tags': forms.CheckboxSelectMultiple(),
    #     }

    
    # def _init_(self, *args, **kwargs):
    #     super(SubjectForm, self)._init_(*args, **kwargs)

    #     for name, field in self.fields.items():
    #         field.widget.attrs.update({'class': 'input'})