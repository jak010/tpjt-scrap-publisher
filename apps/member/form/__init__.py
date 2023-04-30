from django import forms

from django.contrib.auth import get_user_model

Member = get_user_model()


class MemberCreateForm(forms.Form):
    email = forms.EmailField(max_length=255)
    password = forms.CharField(max_length=255)


class MemberLoginForm(forms.Form):
    email = forms.EmailField(max_length=255)
    password = forms.CharField(max_length=255)
