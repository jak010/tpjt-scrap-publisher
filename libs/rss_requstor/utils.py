from .tistory_rss import TistoryRss, TistoryRssData

from apps.views.publish.dto.email_publish_on_member_dto import EmailPublishOnMemberDto


def rss_factory(email_publish_on_member_dto: EmailPublishOnMemberDto):
    if email_publish_on_member_dto.get_domain == "tistory":
        tistory_rss = TistoryRss(sub_domain=email_publish_on_member_dto.sub_domain)
        return TistoryRssData(tistory_rss.get_entires[0])
