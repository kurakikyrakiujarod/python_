# -*- coding: utf-8 -*-
# from fake_useragent import UserAgent
from ua.settings import USER_AGENTS
from random import choice


class UserAgentDownloadMiddleware(object):
    def process_request(self, request, spider):
        request.headers.setdefault(b'User-Agent', choice(USER_AGENTS))
        # request.headers.setdefault(b'User-Agent', UserAgent().chrome)
