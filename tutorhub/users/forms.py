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