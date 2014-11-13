from urllib.parse import urlencode
from exceptions import MemeAPIError
import json
import requests


class MemeAPI:

    def __init__(self):
        self._base_url = 'http://version1.api.memegenerator.net/'

    def _handle_response(self, response):
        if response.status_code != 200:
            raise MemeAPIError(response.content,
                               error_code=response.status_code)

        obj = json.loads(response.text)
        if obj['success']:
            return obj['result']

    def generators_search(self, q, page_index=None, page_size=None):
        url = self._base_url + 'Generators_Search'
        params = {}
        params['q'] = q
        if page_index:
            params['pageIndex'] = page_index
        if page_size:
            params['pageSize'] = page_size
        response = requests.get(url, params=params)
        return self._handle_response(response)

    def generators_select_by_popular(self, page_index=None, page_size=None,
                              days=None):
        url = self._base_url + 'Generators_Select_ByPopular'
        params = {}
        if page_index:
            params['pageIndex'] = page_index
        if page_size:
            params['pageSize'] = page_size
        if days:
            params['days'] = days
        response = requests.get(url, params=params)
        return self._handle_response(response)

    def instances_select_by_popular(self, language_code=None, page_index=None,
                                    page_size=None, url_name=None, days=None):
        url = self._base_url + 'Instances_Select_ByPopular'
        params = {}
        if language_code:
            params['languageCode'] = language_code
        if page_index:
            params['pageIndex'] = page_index
        if page_size:
            params['pageSize'] = page_size
        if url_name:
            params['urlName'] = url_name
        if days:
            params['days'] = days
        response = requests.get(url, params=params)
        return self._handle_response(response)

    def generators_select_by_new(self, page_index=None, page_size=None):
        url = self._base_url + 'Generators_Select_ByNew'
        params = {}
        if page_index:
            params['pageIndex'] = page_index
        if page_size:
            params['pageSize'] = page_size
        response = requests.get(url, params=params)
        return self._handle_response(response)

    def generators_select_by_trending(self):
        url = self._base_url + 'Generators_Select_ByTrending'
        response = requests.get(url)
        return self._handle_response(response)

    def generators_select_related_by_display_name(self, display_name):
        url = self._base_url + 'Generators_Select_Related_ByDisplayName'
        params = {'displayName': display_name}
        response = requests.get(url, params=params)
        return self._handle_response(response)

    #def instance_create():
        #pass

    #def instances_select_by_new():
        #pass

    #def gen_select_by_url_name_or_generator_id():
        #pass

    #def instance_select():
        #pass

    #def content_flag_create():
        #pass
