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
    """
    Returns a list of search results by the a search keyword.
    """
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
    """
    Returns the most popular generators for the last n days. 
    """
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
    """
    Returns the most recently created generators. This list gets updated
    whenever the website moderators approve another batch of generators to
    appear on the website.
    Some generators may not be approved due to poor quality, nsfw content,
    etc, so this list is highly selective.
    """

    url = _base_url + 'Generators_Select_ByNew'
    params = {}

    if page_index is not None:
        params['pageIndex'] = page_index

    if page_size is not None:
        params['pageSize'] = page_size

    response = requests.get(url, params=params)
    return _handle_response(response)


def generators_select_by_trending():
    """
    Returns recently trending generators. 
    """
    url = _base_url + 'Generators_Select_ByTrending'
    response = requests.get(url)
    return _handle_response(response)


def generators_select_related_by_display_name(display_name):
    """
    Returns generators that are related to a particular generator, a sort of 'see also' list.
    """
    url = _base_url + 'Generators_Select_Related_ByDisplayName'
    params = {}

    params['displayName'] = display_name

    response = requests.get(url, params=params)
    return _handle_response(response)


def generators_select_by_url_name_or_generator_id(url_name, generator_id=None):
    """
    Returns information about a specific generator, either by its generator_id or by its url_name.
    """
    url = _base_url + 'Generator_Select_ByUrlNameOrGeneratorID'
    params = {}

    params['urlName'] = url_name

    if generator_id is not None:
        params['generatorID'] = generator_id

    response = requests.get(url, params=params)
    return _handle_response(response)


def instances_select_by_popular(page_index=None, page_size=None, url_name=None,
                                days=None, language_code='en'):
    """
    Returns the most popular instances for a particular period (days == None
    for all time, days = 1 for the last day, days = 7 for the last week) 
    for a particular generator (url_name != None) or for all generators 
    (url_name] == None). 
    Only shows moderator approved content. 
    """
    
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
    """
    Creates a captioned image. 
    Images created with this method are created in the database and may appear
    on the website.
    User credentials of an ordinary user must be provided to create images.
    Sign up on http://memegenerator.net/ to create your user. 
    """
    
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
    """
    Returns recently created instances, for a particular generator
    (url_name] != None) or for all generators (url_name == None).
    Only shows moderator approved content. 
    """
    
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
    """
    Select an instance by its instanceID. 
    """
    url = _base_url + 'Instance_Select'
    params = {}

    params['instanceID'] = instance_id

    response = requests.get(url, params=params)
    return _handle_response(response)


def content_flag_create(content_url, reason, email):
    """
    Flag content for removal, for cases of harassment etc.
    """
    url = _base_url + 'ContentFlag_Create'
    params = {
        'contentUrl': content_url,
        'reason': reason,
        'email': email,
    }

    response = requests.get(url, params=params)
    return _handle_response(response)
