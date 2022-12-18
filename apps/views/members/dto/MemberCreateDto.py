from django import forms


class MemberCreateFormDto(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()

    @property
    def get_email(self):
        return self.cleaned_data['email']

    @property
    def get_password(self):
        return self.cleaned_data['password']
