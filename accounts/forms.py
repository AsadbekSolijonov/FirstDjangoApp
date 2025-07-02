from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from accounts.models import CustomUser, Profile


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'phone', 'email']


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['phone', 'username', 'email', 'first_name', 'last_name']


class ProfileChangeForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image', )
