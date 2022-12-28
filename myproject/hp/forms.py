from django import forms
class hp(forms.Form):
    title = forms.CharField()
    body = forms.CharField()