import string

def translate(s, old, new):
    '''Translate each character in old to the character at the same position in new'''
    return string.translate(s, string.maketrans(old, new))

def to_ascii(s):
    '''Force a string to convert to ASCII. non-ASCII characters will be droped'''
    try:
        return s.decode('ascii', 'ignore')
    except:
        return s.encode('ascii', 'ignore').decode('ascii','ignore')
