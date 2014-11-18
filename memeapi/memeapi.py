import json
import requests
from .exceptions import MemeAPIError, MemeAPIBadFormatResponseError
from ._compat import integer_types, string_types


valid_language_codes = ('en', 'es', 'ru', '--')


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

        if page_index is not None:
            params['pageIndex'] = page_index

        if page_size is not None:
            params['pageSize'] = page_size

        response = requests.get(url, params=params)
        return self._handle_response(response)

    def generators_select_by_popular(self, page_index=None, page_size=None,
                                     days=None):
        url = self._base_url + 'Generators_Select_ByPopular'
        params = {}

        if page_index is not None:
            params['pageIndex'] = page_index

        if page_size is not None:
            params['pageSize'] = page_size

        if days is not None:
            params['days'] = days

        response = requests.get(url, params=params)
        return self._handle_response(response)

    def generators_select_by_new(self, page_index=None, page_size=None):
        url = self._base_url + 'Generators_Select_ByNew'
        params = {}

        if page_index is not None:
            params['pageIndex'] = page_index

        if page_size is not None:
            params['pageSize'] = page_size

        response = requests.get(url, params=params)
        return self._handle_response(response)

    def generators_select_by_trending(self):
        url = self._base_url + 'Generators_Select_ByTrending'
        response = requests.get(url)
        return self._handle_response(response)

    def generators_select_related_by_display_name(self, display_name):
        url = self._base_url + 'Generators_Select_Related_ByDisplayName'
        params = {}

        params['displayName'] = display_name

        response = requests.get(url, params=params)
        return self._handle_response(response)

    def generators_select_by_url_name_or_generator_id(self, url_name,
                                                      generator_id=None):
        url = self._base_url + 'Generator_Select_ByUrlNameOrGeneratorID'
        params = {}

        params['urlName'] = url_name

        if generator_id is not None:
            params['generatorID'] = generator_id

        response = requests.get(url, params=params)
        return self._handle_response(response)

    def instances_select_by_popular(self, page_index=None, page_size=None,
                                    url_name=None, days=None,
                                    language_code='en'):
        url = self._base_url + 'Instances_Select_ByPopular'
        params = {}

        if page_index is not None:
            params['pageIndex'] = page_index

        if page_size is not None:
            params['pageSize'] = page_size

        if url_name is not None:
            params['urlName'] = url_name

        if days is not None:
            params['days'] = days

        if language_code in valid_language_codes:
            params['languageCode'] = language_code
        else:
            raise Exception("'language_code' is invalid.")

        response = requests.get(url, params=params)
        return self._handle_response(response)

    def instances_create(self, username, password, generator_id, image_id,
                         text_0, text_1, language_code='en'):
        url = self._base_url + 'Instance_Create'
        params = {
            'username': username,
            'password': password,
            'generatorID': generator_id,
            'imageID': image_id,
            'text0': text_0,
            'text1': text_1,
        }

        if language_code in valid_language_codes:
            params['languageCode'] = language_code
        else:
            raise Exception("'language_code' is invalid.")

        response = requests.get(url, params=params)
        return self._handle_response(response)

    def instances_select_by_new(self, page_index=None, page_size=None,
                                url_name=None, language_code='en'):
        url = self._base_url + 'Instances_Select_ByNew'
        params = {}

        if page_index is not None:
            params['pageIndex'] = page_index

        if page_size is not None:
            params['pageSize'] = page_size

        if url_name is not None:
            params['urlName'] = url_name

        if language_code in valid_language_codes:
            params['languageCode'] = language_code
        else:
            raise Exception("'language_code' is invalid.")

        response = requests.get(url, params=params)
        return self._handle_response(response)

    def instances_select(self, instance_id):
        url = self._base_url + 'Instance_Select'
        params = {}

        params['instanceID'] = instance_id

        response = requests.get(url, params=params)
        return self._handle_response(response)

    def content_flag_create(self, content_url, reason, email):
        url = self._base_url + 'ContentFlag_Create'
        params = {
            'contentUrl': content_url,
            'reason': reason,
            'email': email,
        }

        response = requests.get(url, params=params)
        return self._handle_response(response)
