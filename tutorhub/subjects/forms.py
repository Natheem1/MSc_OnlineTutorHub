from django.forms import ModelForm, widgets
from django import forms
from .models import Subject, Review

class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = ['title', 'subject_image','description',  'tags']

        labels = {
            'title': 'Subject Ad Title', 'subject_image': 'Subject Ad Image - Add to Attract Students', 
            'description': 'Subject Ad Description - Tell Us About Your Subject And Really Sell Your Self', 
            'tags': 'Subject Features - HOLD Ctrl or Cmd ⌘ To Select Items'
        }

        

    
    def __init__(self, *args, **kwargs):
        super(SubjectForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            if name != 'tags':
                field.widget.attrs.update({'class': 'input'})
            else:
                field.widget.attrs.update({'class': 'column-checkbox'})


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value', 'body']

        labels = {
            'value': 'Vote your Experience',
            'body': 'Comment your Experience',
        }

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})