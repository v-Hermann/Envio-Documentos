from django import forms


class ApprovalForm(forms.Form):
    status = forms.CharField(max_length=10)


class DisapprovalForm(forms.Form):
    reason = forms.CharField(widget=forms.Textarea)
