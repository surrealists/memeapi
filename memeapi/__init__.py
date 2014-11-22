"""
memeapi
-------

memeapi is a library for python that wraps the memegenerator.net API.
"""

__author__ = 'Cristian Cabrera <surrealcristian@gmail.com>'
__version__ = '0.2.0'

from .api import (
    generators_search, generators_select_by_popular, generators_select_by_new,
    generators_select_by_trending, generators_select_related_by_display_name,
    generators_select_by_url_name_or_generator_id, instances_select_by_popular,
    instances_create, instances_select_by_new, instances_select,
    content_flag_create
)
