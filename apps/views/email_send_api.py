from django.views import View
from django.http.response import JsonResponse

from ..models import EmailHistory
from ..orm import Member


class EmailSendView(View):
    """ Email 전송하기 """

    def post(self, *args, **kwargs):
        post_id = self.request.POST.get("post_id", None)
        receiver = self.request.POST.get("receiver", None)

        if receiver is not None:
            try:
                receive_of_member = Member.objects.get(email=receiver)
            except Member.DoesNotExist:
                return JsonResponse(status=400, data={
                    "desg": "Does Not Exist Member"
                })

            email_history = EmailHistory(
                sender="admin",
                receiver=receive_of_member
            )

            email_history.save()

        return JsonResponse(status=201, data={
            "desg": "Success"
        })
