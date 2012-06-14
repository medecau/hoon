import urllib

def request(url, data):
    """
        Makes a simple request. If no data it's a GET else it's a POST.
        Returns a string.
    """
    if data is not None:
        post_data = urllib.urlencode(data)
    else:
        post_data = None
    return urllib.urlopen(url, post_data).read()