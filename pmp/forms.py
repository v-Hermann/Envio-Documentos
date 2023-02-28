from django import forms
from django.core.exceptions import ValidationError

class FileUpload(forms.Form):
    generic_file = forms.ImageField()