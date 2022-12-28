from django import forms


class aksesorisForms(forms.Form):
    email = forms.CharField(max_length=225)
    password = forms.CharField(max_length=200)