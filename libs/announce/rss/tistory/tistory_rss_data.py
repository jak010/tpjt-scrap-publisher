from __future__ import annotations

from .sub_data.summary_detail import SummaryDetail


class TistoryRssData:
    def __init__(self, entry):
        self.entry = entry

    def __str__(self):
        return self.get_id

    @property
    def get_author(self):
        return self.entry['author']

    @property
    def get_author_detail(self):
        return self.entry['get_author_detail']

    @property
    def get_authors(self):
        return self.entry['authors']

    @property
    def get_comments(self):
        return self.entry['comments']

    @property
    def get_id(self):
        return self.entry['id']

    @property
    def get_link(self):
        return self.entry['link']

    @property
    def get_links(self):
        return self.entry['links']

    @property
    def get_published(self):
        return self.entry['published']

    @property
    def get_published_parsed(self):
        return self.entry['published_parsed']

    @property
    def get_summary(self):
        return self.entry['summary']

    @property
    def get_summary_detail(self) -> SummaryDetail:
        return SummaryDetail(self.entry['summary_detail'])

    @property
    def get_tags(self):
        return self.entry['tags']

    @property
    def get_title(self):
        return self.entry['title']

    @property
    def get_title_detail(self):
        return self.entry['title_detail']
