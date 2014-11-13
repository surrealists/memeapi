from exceptions import MemeAPIError, MemeAPIBadFormatResponseError
import json
import requests


class MemeAPI:

    def __init__(self):
        self._base_url = 'http://version1.api.memegenerator.net/'

    def _handle_response(self, response):
        if response.status_code != 200:
            raise MemeAPIError()
        try:
            obj = json.loads(response.text)
        except:
            raise MemeAPIBadFormatResponseError()
        return obj

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

    def instances_select_by_popular(self, page_index=None, page_size=None,
                                    url_name=None, days=None,
                                    language_code='en'):
        url = self._base_url + 'Instances_Select_ByPopular'
        params = {}
        if page_index:
            params['pageIndex'] = page_index
        if page_size:
            params['pageSize'] = page_size
        if url_name:
            params['urlName'] = url_name
        if days:
            params['days'] = days
        params['languageCode'] = language_code
        response = requests.get(url, params=params)
        return self._handle_response(response)

    def instance_create(self, username, password, generator_id, image_id,
                        text_0, text_1, language_code='en'):
        url = self._base_url + 'Instance_Create'
        params = {}
        params['username'] = username
        params['password'] = password
        params['generatorID'] = generator_id
        params['imageID'] = image_id
        params['text0'] = text_0
        params['text1'] = text_1
        params['languageCode'] = language_code
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

    def generator_select_by_url_name_or_generator_id(self, url_name,
                                                     generator_id=None):
        url = self._base_url + 'Generator_Select_ByUrlNameOrGeneratorID'
        params = {}
        if generator_id:
            params['generatorID'] = generator_id
        if url_name:
            params['urlName'] = url_name
        response = requests.get(url, params=params)
        return self._handle_response(response)

    def instances_select_by_new(self, page_index=None, page_size=None,
                                url_name=None, language_code='en'):
        url = self._base_url + 'Instances_Select_ByNew'
        params = {}
        if page_index:
            params['pageIndex'] = page_index
        if page_size:
            params['pageSize'] = page_size
        if url_name:
            params['urlName'] = url_name
        params['languageCode'] = language_code
        response = requests.get(url, params=params)
        return self._handle_response(response)

    def instance_select(self, instance_id):
        url = self._base_url + 'Instance_Select'
        params = {'instanceID': instance_id}
        response = requests.get(url, params=params)
        return self._handle_response(response)

    def content_flag_create(self, content_url, reason, email):
        url = self._base_url + 'ContentFlag_Create'
        params = {}
        params['contentUrl'] = content_url
        params['reason'] = reason
        params['email'] = email
        response = requests.get(url, params=params)
        return self._handle_response(response)
