from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.hashers import make_password
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    fullname = forms.CharField(required=True)

    class Meta:
        model = CustomUser
        fields = ('fullname', 'email')
        labels = {
            'fullname': 'Nome completo',
        }


class CustomUserChangeForm(UserChangeForm):
    password = forms.CharField(widget=forms.PasswordInput(), required=False)

    class Meta:
        model = CustomUser
        fields = ('fullname', 'email', 'password')

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password:
            # hash the password before saving
            return make_password(password)
        else:
            # if the password is not provided, return the existing password
            return self.instance.password
