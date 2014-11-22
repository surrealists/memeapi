import json
import requests
from .exceptions import BadStatusError, NotJSONError, LanguageCodeError
from ._compat import integer_types, string_types


_valid_language_codes = ('en', 'es', 'ru', '--')
_base_url = 'http://version1.api.memegenerator.net/'


def _handle_response(response):
    if response.status_code != 200:
        raise BadStatusError(
            'MemeGenerator API returned a %s status code.' %
            (response.status_code,)
        )
    try:
        obj = json.loads(response.text)
    except:
        raise NotJSONError('Response was not valid JSON.')
    return obj


def generators_search(q, page_index=None, page_size=None):
    url = _base_url + 'Generators_Search'
    params = {}

    params['q'] = q

    if page_index is not None:
        params['pageIndex'] = page_index

    if page_size is not None:
        params['pageSize'] = page_size

    response = requests.get(url, params=params)
    return _handle_response(response)


def generators_select_by_popular(page_index=None, page_size=None, days=None):
    url = _base_url + 'Generators_Select_ByPopular'
    params = {}

    if page_index is not None:
        params['pageIndex'] = page_index

    if page_size is not None:
        params['pageSize'] = page_size

    if days is not None:
        params['days'] = days

    response = requests.get(url, params=params)
    return _handle_response(response)


def generators_select_by_new(page_index=None, page_size=None):
    url = _base_url + 'Generators_Select_ByNew'
    params = {}

    if page_index is not None:
        params['pageIndex'] = page_index

    if page_size is not None:
        params['pageSize'] = page_size

    response = requests.get(url, params=params)
    return _handle_response(response)


def generators_select_by_trending():
    url = _base_url + 'Generators_Select_ByTrending'
    response = requests.get(url)
    return _handle_response(response)


def generators_select_related_by_display_name(display_name):
    url = _base_url + 'Generators_Select_Related_ByDisplayName'
    params = {}

    params['displayName'] = display_name

    response = requests.get(url, params=params)
    return _handle_response(response)


def generators_select_by_url_name_or_generator_id(url_name, generator_id=None):
    url = _base_url + 'Generator_Select_ByUrlNameOrGeneratorID'
    params = {}

    params['urlName'] = url_name

    if generator_id is not None:
        params['generatorID'] = generator_id

    response = requests.get(url, params=params)
    return _handle_response(response)


def instances_select_by_popular(page_index=None, page_size=None, url_name=None,
                                days=None, language_code='en'):
    url = _base_url + 'Instances_Select_ByPopular'
    params = {}

    if page_index is not None:
        params['pageIndex'] = page_index

    if page_size is not None:
        params['pageSize'] = page_size

    if url_name is not None:
        params['urlName'] = url_name

    if days is not None:
        params['days'] = days

    if language_code in _valid_language_codes:
        params['languageCode'] = language_code
    else:
        raise LanguageCodeError('Invalid language code.')

    response = requests.get(url, params=params)
    return _handle_response(response)


def instances_create(username, password, generator_id, image_id, text_0,
                     text_1, language_code='en'):
    url = _base_url + 'Instance_Create'
    params = {
        'username': username,
        'password': password,
        'generatorID': generator_id,
        'imageID': image_id,
        'text0': text_0,
        'text1': text_1,
    }

    if language_code in _valid_language_codes:
        params['languageCode'] = language_code
    else:
        raise LanguageCodeError('Invalid language code.')

    response = requests.get(url, params=params)
    return _handle_response(response)


def instances_select_by_new(page_index=None, page_size=None, url_name=None,
                            language_code='en'):
    url = _base_url + 'Instances_Select_ByNew'
    params = {}

    if page_index is not None:
        params['pageIndex'] = page_index

    if page_size is not None:
        params['pageSize'] = page_size

    if url_name is not None:
        params['urlName'] = url_name

    if language_code in _valid_language_codes:
        params['languageCode'] = language_code
    else:
        raise LanguageCodeError('Invalid language code.')

    response = requests.get(url, params=params)
    return _handle_response(response)


def instances_select(instance_id):
    url = _base_url + 'Instance_Select'
    params = {}

    params['instanceID'] = instance_id

    response = requests.get(url, params=params)
    return _handle_response(response)


def content_flag_create(content_url, reason, email):
    url = _base_url + 'ContentFlag_Create'
    params = {
        'contentUrl': content_url,
        'reason': reason,
        'email': email,
    }

    response = requests.get(url, params=params)
    return _handle_response(response)
