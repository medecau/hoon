def readf(file, create=False):
    '''Read file contents.
    Parameter create sets wether to create a new file or not.'''
    if create:
        mode = 'r+'
    else:
        mode = 'r'
    return open(file, mode).read()

def writef(file, arg, create=True):
    '''Write contents to file.
    Parameter create sets wether to create a new file or not.'''
    if create:
        mode = 'w+'
    else:
        mode = 'w'
    open(file, mode).write(arg)

def appendf(file, arg, create=True):
    '''Write contents to file.
    Parameter create sets wether to create a new file or not.'''
    if create:
        mode = 'a+'
    else:
        mode = 'a'
    open(file,'a+').write(arg)

def readurl(url):
    '''Return URL contents.'''
    import urllib2
    return urllib2.open(url).read()
