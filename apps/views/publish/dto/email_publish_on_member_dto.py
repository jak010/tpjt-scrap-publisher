from django import forms


class EmailPublishOnMemberDto(forms.Form):
    receiver = forms.EmailField(required=True)
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
