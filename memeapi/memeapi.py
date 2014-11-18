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

        if isinstance(q, string_types):
            params['q'] = q
        else:
            raise Exception("'q' must be string.")

        if page_index is not None:
            if isinstance(page_index, integer_types):
                params['pageIndex'] = page_index
            else:
                raise Exception("'page_index' must be integer.")

        if page_size is not None:
            if isinstance(page_size, integer_types):
                params['pageSize'] = page_size
            else:
                raise Exception("'page_size' must be integer.")

        response = requests.get(url, params=params)
        return self._handle_response(response)

    def generators_select_by_popular(self, page_index=None, page_size=None,
                                     days=None):
        url = self._base_url + 'Generators_Select_ByPopular'
        params = {}

        if page_index is not None:
            if isinstance(page_index, integer_types):
                params['pageIndex'] = page_index
            else:
                raise Exception("'page_index' must be integer.")

        if page_size is not None:
            if isinstance(page_size, integer_types):
                params['pageSize'] = page_size
            else:
                raise Exception("'page_size' must be integer.")

        if days is not None:
            if isinstance(days, integer_types):
                params['days'] = days
            else:
                raise Exception("'days' must be integer.")

        response = requests.get(url, params=params)
        return self._handle_response(response)

    def instances_select_by_popular(self, page_index=None, page_size=None,
                                    url_name=None, days=None,
                                    language_code='en'):
        url = self._base_url + 'Instances_Select_ByPopular'
        params = {}

        if page_index is not None:
            if isinstance(page_index, integer_types):
                params['pageIndex'] = page_index
            else:
                raise Exception("'page_index' must be integer.")

        if page_size is not None:
            if isinstance(page_size, integer_types):
                params['pageSize'] = page_size
            else:
                raise Exception("'page_size' must be integer.")

        if url_name is not None:
            if isinstance(url_name, string_types):
                params['urlName'] = url_name
            else:
                raise Exception("'url_name' must be string.")

        if days is not None:
            if isinstance(days, integer_types):
                params['days'] = days
            else:
                raise Exception("'days' must be integer.")

        if language_code in valid_language_codes:
            params['languageCode'] = language_code
        else:
            raise Exception("'language_code' is invalid.")

        response = requests.get(url, params=params)
        return self._handle_response(response)

    def instance_create(self, username, password, generator_id, image_id,
                        text_0, text_1, language_code='en'):
        url = self._base_url + 'Instance_Create'
        params = {}

        if isinstance(username, string_types):
            params['username'] = username
        else:
            raise Exception("'username' must be string.")

        if isinstance(password, string_types):
            params['password'] = password
        else:
            raise Exception("'password' must be string.")

        if isinstance(generator_id, integer_types):
            params['generatorID'] = generator_id
        else:
            raise Exception("'generator_id' must be integer.")

        if isinstance(image_id, integer_types):
            params['imageID'] = image_id
        else:
            raise Exception("'image_id' must be integer.")

        if isinstance(text_0, string_types):
            params['text0'] = text_0
        else:
            raise Exception("'text_0' must be string.")

        if isinstance(text_1, string_types):
            params['text1'] = text_1
        else:
            raise Exception("'text_1' must be string.")

        if language_code in valid_language_codes:
            params['languageCode'] = language_code
        else:
            raise Exception("'language_code' is invalid.")

        response = requests.get(url, params=params)
        return self._handle_response(response)

    def generators_select_by_new(self, page_index=None, page_size=None):
        url = self._base_url + 'Generators_Select_ByNew'
        params = {}

        if page_index is not None:
            if isinstance(page_index, integer_types):
                params['pageIndex'] = page_index
            else:
                raise Exception("'page_index' must be integer.")

        if page_size is not None:
            if isinstance(page_size, integer_types):
                params['pageSize'] = page_size
            else:
                raise Exception("'page_size' must be integer.")

        response = requests.get(url, params=params)
        return self._handle_response(response)

    def generators_select_by_trending(self):
        url = self._base_url + 'Generators_Select_ByTrending'
        response = requests.get(url)
        return self._handle_response(response)

    def generators_select_related_by_display_name(self, display_name):
        url = self._base_url + 'Generators_Select_Related_ByDisplayName'
        params = {}

        if isinstance(display_name, string_types):
            params['displayName'] = display_name
        else:
            raise Exception("'display_name' must be string.")

        response = requests.get(url, params=params)
        return self._handle_response(response)

    def generator_select_by_url_name_or_generator_id(self, url_name,
                                                     generator_id=None):
        url = self._base_url + 'Generator_Select_ByUrlNameOrGeneratorID'
        params = {}

        if isinstance(url_name, string_types):
            params['urlName'] = url_name
        else:
            raise Exception("'url_name' must be string.")

        if generator_id is not None:
            if isinstance(generator_id, integer_types):
                params['generatorID'] = generator_id
            else:
                raise Exception("'generator_id' must be integer.")

        response = requests.get(url, params=params)
        return self._handle_response(response)

    def instances_select_by_new(self, page_index=None, page_size=None,
                                url_name=None, language_code='en'):
        url = self._base_url + 'Instances_Select_ByNew'
        params = {}

        if page_index is not None:
            if isinstance(page_index, integer_types):
                params['pageIndex'] = page_index
            else:
                raise Exception("'page_index' must be integer.")

        if page_size is not None:
            if isinstance(page_size, integer_types):
                params['pageSize'] = page_size
            else:
                raise Exception("'page_size' must be integer.")

        if url_name is not None:
            if isinstance(url_name, string_types):
                params['urlName'] = url_name
            else:
                raise Exception("'url_name' must be string.")

        if language_code in valid_language_codes:
            params['languageCode'] = language_code
        else:
            raise Exception("'language_code' is invalid.")

        response = requests.get(url, params=params)
        return self._handle_response(response)

    def instance_select(self, instance_id):
        url = self._base_url + 'Instance_Select'
        params = {}

        if isinstance(instance_id, integer_types):
            params['instanceID'] = instance_id
        else:
            raise Exception("'instance_id' must be integer.")

        response = requests.get(url, params=params)
        return self._handle_response(response)

    def content_flag_create(self, content_url, reason, email):
        url = self._base_url + 'ContentFlag_Create'
        params = {}

        if isinstance(content_url, string_types):
            params['contentUrl'] = content_url
        else:
            raise Exception("'content_url' must be string.")

        if isinstance(reason, string_types):
            params['reason'] = reason
        else:
            raise Exception("'reason' must be string.")

        if isinstance(email, string_types):
            params['email'] = email
        else:
            raise Exception("'email' must be string.")

        response = requests.get(url, params=params)
        return self._handle_response(response)
