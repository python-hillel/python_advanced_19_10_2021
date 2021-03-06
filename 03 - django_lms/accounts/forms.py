from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import UserCreationForm

from .models import Profile


class AccountRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]


class AccountUpdateForm(UserChangeForm):
    password = None

    class Meta(UserChangeForm.Meta):
        fields = [
            'first_name',
            'last_name',
            'email',
        ]


class AccountProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['birthday', 'city', 'avatar']

        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }
