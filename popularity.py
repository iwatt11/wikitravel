from mwviews.api import PageviewsClient
from datetime import datetime as dt
import datetime


class WikiViews:
    def __init__(self, pages):
        self.p = PageviewsClient()
        self.now = dt.today()
        self.pages = self.str_ops(pages)
        self.views = dict.fromkeys(self.pages, 0)
        self.then = (self.now - datetime.timedelta(days=365)).date()
        self.get_views()
        self.sorted = self.sorted_views()

    @staticmethod
    def str_ops(pages):
        return [x.replace(' ', '_') for x in pages]

    def get_views(self):
        date_views = self.p.article_views('en.wikipedia', self.pages, granularity='monthly',
                                start=self.then.strftime('%Y%m%d'), end=self.now.strftime('%Y%m%d'))
        self.total_views(date_views)
        return self.sorted_views()

    def total_views(self, views):
        for val in views:
            for v in views[val]:
                try:
                    self.views[v] += views[val][v]
                except (KeyError, TypeError):
                    continue

    def sorted_views(self):
        return sorted(self.views.items(), key=lambda x: x[1], reverse=True)
