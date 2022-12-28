from django import forms
class casing(forms.Form):
    title = forms.CharField()
    body = forms.CharField()