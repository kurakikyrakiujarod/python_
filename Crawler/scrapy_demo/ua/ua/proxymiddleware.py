class ProxyMiddleware(object):
    def process_request(self, request, spider):
        request.meta['proxy'] = 'http://127.0.0.1:25378'
        # request.meta['proxy'] = 'http://user:password@ip:port'
