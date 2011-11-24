import hashlib

def hash(algorithm='sha1'):
    '''Generic constructor. algorithm parameter defaults to sha1.
    Returns hash object.'''
    return hashlib.new(algorithm)

def digest(s, algorithm='sha1'):
    '''Return the digest of the string passed in arg. This string may contain
    non-ASCII characters, including null bytes.
    
    algorithm parameter defaults to sha1.'''
    h=hashlib.new(algorithm)
    h.update(s)
    return h.digest()

def hexdigest(s, algorithm='sha1'):
    '''Like digest() except the digest is returned as a string of double
    length, containing only hexadecimal digits.
    
    algorithm parameter defaults to sha1.'''
    h=hashlib.new(algorithm)
    h.update(s)
    return h.hexdigest()
