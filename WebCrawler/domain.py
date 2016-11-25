from urllib.parse import urlparse


def get_dname(url):
    try:
        results = get_subdname(url).split('.')
        return results[-2] + '.' + results[-1]
    except:
        return ''


def get_subdname(url):
    try:
        return urlparse(url).netloc
    except:
        return ''
