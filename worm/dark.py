import json

def cute(t):
    """
        some humans like it this way
    """
    return json.dumps(t, indent=2)

def obj(name='anonymous'):
    '''
    Returns a new object
    TODO: change the type and allow for isinstance() to work properly
    '''
    return type(str(name), (object, ), {})
