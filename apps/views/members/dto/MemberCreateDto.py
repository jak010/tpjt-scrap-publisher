from django import forms


class MemberCreateFormDto(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)

    @property
    def get_email(self):
        return self.cleaned_data['email']

    @property
    def get_password(self):
        return self.cleaned_data['password']
