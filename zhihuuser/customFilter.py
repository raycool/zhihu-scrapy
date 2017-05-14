from scrapy.dupefilters import RFPDupeFilter


class SeenUserIDFilter(RFPDupeFilter):
    def __init__(self, path,debug):
        self.IDURL_seen = set()
        super(SeenUserIDFilter, self).__init__(path,debug)


    def request_seen(self, request):
        if request.url in self.IDURL_seen:
            return True
        else:
            self.IDURL_seen.add(request.url)
