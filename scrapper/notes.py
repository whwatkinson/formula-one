from requests import get


from bs4 import BeautifulSoup
from diskcache import Cache

url = 'https://en.wikipedia.org/wiki/2020_Formula_One_World_Championship'
cache = Cache("tmp")


@cache.memoize()
def cache_get(url):
    return get(url)


def parse_url_to_soup(valid_url: str) -> BeautifulSoup:
    """
    Parses an URL's HTML.
    :param valid_url: a vlaid URL
    :return: A BeautifulSoup Object
    """

    response = cache_get(valid_url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup
