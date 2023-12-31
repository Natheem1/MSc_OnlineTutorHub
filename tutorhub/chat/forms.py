from django.forms import ModelForm
from .models import Room, Topic


class TopicForm(ModelForm):
    class Meta: 
        model = Topic
        fields = '__all__'

    def __init__(self,*args, **kwargs):
        super(TopicForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})



class CreateRoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ['topic', 'name', 'description',]
        exclude = ['host','participants']

        labels = {
            'topic': 'Choose Topic or Create Topic Below ', 'name': 'Create Room Name', 'description': 'Tell us about the Room'
        }

    def __init__(self,*args, **kwargs):
        super(CreateRoomForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})



class UpdateRoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'description']
        exclude = ['host', 'participants']
        labels = {
            'name': 'Create Room Name',
            'description': 'Tell us about the Room'
        }

    def __init__(self,*args, **kwargs):
        super(UpdateRoomForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
