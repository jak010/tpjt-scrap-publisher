class SummaryDetail:
    def __init__(self, summary_detail):
        self.summary_detail = summary_detail

    @property
    def base(self):
        return self.summary_detail['base']

    @property
    def language(self):
        return self.summary_detail['lanugae']

    @property
    def value(self):
        return self.summary_detail['value']