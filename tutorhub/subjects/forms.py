from django.forms import ModelForm, widgets
from django import forms
from .models import Subject 

class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = ['title', 'subject_image','description',  'tags']

        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

    
    def __init__(self, *args, **kwargs):
        super(SubjectForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})