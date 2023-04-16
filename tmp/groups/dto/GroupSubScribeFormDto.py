from django import forms


class GroupSubScribeFormDto(forms.Form):
    author = forms.CharField(max_length=12, required=True)

    sub_domain = forms.CharField(max_length=12, required=True)
    domain = forms.CharField(max_length=12, required=True)
    top_level_domain = forms.CharField(max_length=12, required=True)

    @property
    def get_author(self):
        return self.cleaned_data['author']

    @property
    def get_sub_domain(self):
        return self.cleaned_data['sub_domain']

    @property
    def get_domain(self):
        return self.cleaned_data['domain']

    @property
    def get_top_level_domain(self):
        return self.cleaned_data['top_level_domain']
