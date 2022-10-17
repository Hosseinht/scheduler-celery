from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
)
from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()


class UserForm(UserCreationForm):
    username = forms.EmailField(max_length=254, required=True,
                                widget=forms.TextInput(attrs={
                                    'placeholder': '*Email..'}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': '*Password..', }))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': '*Confirm Password..', }))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',)


class AuthForm(AuthenticationForm):
    username = forms.EmailField(max_length=254, required=True,
                                widget=forms.TextInput(attrs={'placeholder': '*Email..', }))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': '*Password..', }))

    class Meta:
        model = User
        fields = ('username', 'password',)
