from django import forms

from django.contrib.auth import get_user_model

Member = get_user_model()


class GroupCreateForm(forms.Form):
    group_name = forms.CharField(
        max_length=255,
        label="Name",
        widget=forms.TextInput(attrs={
            "placeholder": "Group Name",
        })
    )

    group_description = forms.CharField(
        max_length=255,
        label="Description",
        widget=forms.TextInput(attrs={
            "placeholder": "Group Description",
        })
    )
