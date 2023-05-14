from __future__ import annotations

from django.core.exceptions import PermissionDenied
from django.views.generic import TemplateView


class MemberProfileView(TemplateView):
    template_name = "pages/profile.html"

    def get(self, *args, **kwargs):
        if not self.request.user:
            raise PermissionDenied()

        return self.render_to_response(context={
            'member': {
                'email': self.request.user.email,
                'last_login': self.request.user.last_login,
                'date_of_join': self.request.user.date_of_join
            }
        })
