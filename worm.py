import urllib
import string
import json
import hashlib

def cute(thing, indent=2):
    """
        some humans like it this way
    """
    if type(thing) in [type(str()), type(unicode())]:
        thing = json.loads(thing)
    return json.dumps(thing, indent)

def translate(s, old, new):
    '''
        Translate each character in old to the character
        at the same positionin new
    '''
    return s.translate(string.maketrans(old, new))

def toascii(s):
    '''
        Force a string to convert to ASCII.
        non-ASCII characters will be droped
        TODO: check for better solutions
    '''
    try:
        return s.decode('ascii', 'ignore')
    except:
        return s.encode('ascii', 'ignore').decode('ascii','ignore')
def read(f, create=False):
    '''
        Read file contents.
        Parameter create sets wether to create a new file or not.'''
    if create:
        mode = 'r+'
    else:
        mode = 'r'
    return open(f, mode).read()

def write(f, arg, create=True):
    '''
        Write contents to file.
        Parameter create sets wether to create a new file or not.
    '''
    if create:
        mode = 'w+'
    else:
        mode = 'w'
    open(f, mode).write(arg)

def append(f, arg, create=True):
    '''
        Write contents to file.
        Parameter create sets wether to create a new file or not.
    '''
    if create:
        mode = 'a+'
    else:
        mode = 'a'
    open(f, mode).write(arg)

def sequence_matcher(a=None, b=None, isjunk=None):
    '''
        Short for the SequenceMatcher constructor.
        isjunk is moved to the right so it\'s not required
        when providing a and b parameters.
    '''
    import difflib
    return difflib.SequenceMatcher(isjunk, a, b)

def ratio(a, b):
    '''
        Return a measure of the sequences' similarity.
    '''
    return sequence_matcher(a, b).ratio()

def qratio(a, b):
    '''
        Return an upper bound on ratio() very quickly.
    '''
    return sequence_matcher(a, b).real_quick_ratio()

def opcodes(a, b):
    '''
        Get a list of tuples describing how to turn a into b.
    '''
    return sequence_matcher(a, b).get_opcodes()

def qmatch(a, b, ratio=1):
    '''
        Fast test the similarity of two sequences by testing with
        real_quick_ratio() first.
    '''
    smo = sequence_matcher(a, b)
    if smo.real_quick_ratio()<ratio:
        return False
    else:
        if smo.ratio()<ratio:
            return False
        else:
            return True

def digest(s, algorithm='sha1'):
    '''
        Return the digest of the string passed in arg. This string may contain
        non-ASCII characters, including null bytes.

        algorithm parameter defaults to sha1.
    '''
    h = hashlib.new(algorithm)
    h.update(s)
    return h.digest()

def hexdigest(s, algorithm='sha1'):
    '''
        Like digest() except the digest is returned as a string of double
        length, containing only hexadecimal digits.

        algorithm parameter defaults to sha1.
    '''
    h = hashlib.new(algorithm)
    h.update(s)
    return h.hexdigest()

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

def obj(name='anonymous'):
    '''
        Returns a new object
        TODO: change the type and allow for isinstance() to work properly
    '''
    return type(str(name), (object, ), {})

