from django import forms


class FileUpload(forms.Form):
    generic_file = forms.ImageField()
