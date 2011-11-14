def sm(a=None, b=None, isjunk=None, autojunk=True):
    '''Short for the SequenceMatcher constructor. isjunk is moved to the right
    so it\'s not required when providing a and b parameters.'''
    import difflib
    return difflib.SequenceMatcher(None, a, b)

def ratio(a, b):
    '''Return a measure of the sequences' similarity.'''
    return sm(a, b).ratio()

def qratio(a, b):
    '''Return an upper bound on ratio() very quickly.'''
    return sm(a, b).real_quick_ratio()

def get_opcodes(a, b):
    '''Get a list of tuples describing how to turn a into b.'''
    return sm(a, b).get_opcodes()

def qmatch(a, b, ratio=1):
    '''Fast test the similarity of two sequences by testing with
    real_quick_ratio() first.'''
    smo=sm(a, b)
    if smo.real_quick_ratio()<ratio:
        return False
    else:
        if smo.ratio()<ratio:
            return False
        else:
            return True