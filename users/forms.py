from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Email address', help_text='Your SHU email address.')
    username = forms.CharField(label='Student ID', help_text='Your SHU username')
    first_name = forms.CharField(max_length=50)  # Required
    last_name = forms.CharField(max_length=50)  # Required
    groups = Group.objects.all()
    group_data = []

    for group in groups:
        group_id = group.id
        group_name = group.name
        group_tuple = (group_id, group_name)
        group_data.append(group_tuple)

    group = forms.ChoiceField(choices=group_data, label='Course')

    class Meta:
        model = User

        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', ]
