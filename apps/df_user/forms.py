from django import forms

class ForgetForm(forms.Form):
    email = forms.EmailField(required=True)

class ModifyForm(forms.Form):
    password1 = forms.CharField(required=True, min_length=5)
    password2 = forms.CharField(required=True, min_length=5)