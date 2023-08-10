from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import NewUser

class MyUserCreationForm(UserCreationForm):
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