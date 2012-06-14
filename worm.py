import urllib
import string
import json
import hashlib

def cute(t):
    """
        some humans like it this way
    """
    return json.dumps(t, indent=2)

def translate(s, old, new):
    '''
        Translate each character in old to the character
        at the same positionin new
    '''
    return string.translate(s, string.maketrans(old, new))

def to_ascii(s):
    '''
        Force a string to convert to ASCII.
        non-ASCII characters will be droped
    '''
    try:
        return s.decode('ascii', 'ignore')
    except:
        return s.encode('ascii', 'ignore').decode('ascii','ignore')
def read(file, create=False):
    '''
        Read file contents.
        Parameter create sets wether to create a new file or not.'''
    if create:
        mode = 'r+'
    else:
        mode = 'r'
    return open(file, mode).read()

def write(file, arg, create=True):
    '''
        Write contents to file.
        Parameter create sets wether to create a new file or not.
    '''
    if create:
        mode = 'w+'
    else:
        mode = 'w'
    open(file, mode).write(arg)

def append(file, arg, create=True):
    '''
        Write contents to file.
        Parameter create sets wether to create a new file or not.
    '''
    if create:
        mode = 'a+'
    else:
        mode = 'a'
    open(file,'a+').write(arg)

def sm(a=None, b=None, isjunk=None):
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
    return sm(a, b).ratio()

def qratio(a, b):
    '''
        Return an upper bound on ratio() very quickly.
    '''
    return sm(a, b).real_quick_ratio()

def get_opcodes(a, b):
    '''
        Get a list of tuples describing how to turn a into b.
    '''
    return sm(a, b).get_opcodes()

def qmatch(a, b, ratio=1):
    '''
        Fast test the similarity of two sequences by testing with
        real_quick_ratio() first.
    '''
    smo = sm(a, b)
    if smo.real_quick_ratio()<ratio:
        return False
    else:
        if smo.ratio()<ratio:
            return False
        else:
            return True

def hash(algorithm='sha1'):
    '''
        Generic constructor. algorithm parameter defaults to sha1.
        Returns hash object.
    '''
    return hashlib.new(algorithm)

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

class Fibonacci(object):
    a, o=0, 1
    def __init__(self):
        pass
    def next(self):
        self.a, self.o = self.o, self.a+self.o
        return self.o

def fib_seq(num):
    '''
        Returns the fibonacci sequence in a list up to num
    '''
    seq=[]
    f=Fibonacci()
    for i in range(num):
        seq.append(f.next())
    return seq

def is_prime(num):
    '''
        Checks for the primality of a number
    '''
    from math import ceil
    from math import sqrt
    if (num%2 == 0 and num>2) or num < 2 or type(num) is not int:
        return False
    else:
        l=int(ceil(sqrt(num)))
        for i in xrange(3, l+1, 2):
            if num%i==0:
                return False
        return True

def next_prime(num):
    '''
        Returns the next prime
    '''
    if num > 2:
        if num%2==0:
            num-=1
        else:
            pass
        while True:
            num+=2
            if is_prime(num):
                return num
            else:
                continue
    elif num == 2:
        return 3
    else:
        return 2

def get_factors(num, short=False):
    '''
        Calculates the factors of num
    '''
    from math import ceil
    from math import sqrt
    factors=[]
    square=sqrt(num)
    if square == int(square):
        factors.append(int(square))
    for f in xrange(1,int(ceil(square))):
        if num%f==0:
            factors.extend([f, int(num/f)])
    if short:
        factors.sort()
        return factors[1:-1]
    else:
        return factors

def obj(name='anonymous'):
    '''
        Returns a new object
        TODO: change the type and allow for isinstance() to work properly
    '''
    return type(str(name), (object, ), {})

