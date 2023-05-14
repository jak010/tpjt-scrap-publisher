from django import forms

from django.contrib.auth import get_user_model

Member = get_user_model()


class MemberSignUpForm(forms.Form):
    email = forms.EmailField(
        max_length=255,
        label="Email",
        widget=forms.EmailInput(attrs={
            "placeholder": "Eemail Input Here",
        })
    )

    password = forms.CharField(
        max_length=255,
        label="Password",
        widget=forms.PasswordInput(attrs={
            'placeholder': "Password input",
        })
    )


class MemberLoginForm(forms.Form):
    email = forms.EmailField(
        max_length=255,
        label="Email",
        widget=forms.EmailInput(attrs={
            "placeholder": "Eemail Input Here",
        })

    )

    password = forms.CharField(
        max_length=255,
        label="Password",
        widget=forms.PasswordInput(attrs={
            'placeholder': "Password input",
        })
    )
