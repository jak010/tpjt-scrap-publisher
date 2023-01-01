from django import forms

from django.core import validators


class MultipleEmailFields(forms.Field):
    def to_python(self, value):
        if not value:
            return []
        return [email.strip() for email
                in value.split(",")]

    def validate(self, value):
        super().validate(value)
        for email in value:
            validators.EmailValidator(email)


class EmailPublishOnMemberDto(forms.Form):
    receiver = MultipleEmailFields(required=True)
    subject = forms.CharField(max_length=256, required=True)
    sub_domain = forms.CharField(required=True)
    domain = forms.CharField(required=True)
    top_level_domain = forms.CharField(required=True)

    @property
    def get_receiver(self):
        return self.cleaned_data['receiver']

    @property
    def get_sub_domain(self):
        return self.cleaned_data['sub_domain']

    @property
    def get_domain(self):
        return self.cleaned_data['domain']

    @property
    def get_top_level_domain(self):
        return self.cleaned_data['top_level_domain']

    @property
    def get_subject(self):
        return self.cleaned_data['subject']
