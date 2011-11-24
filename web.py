def readurl(url):
    '''Return URL contents.'''
    import urllib2
    return urllib2.open(url).read()
