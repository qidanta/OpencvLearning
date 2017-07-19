def some(iterable, target):
    '''has target, if one element in iterable is true will be true
    no target, if one element  in iterable equal target will be true

    - Params:
    @iterable: a obj could be iterable
    @target: compare element in obj with target

    - Returns:
    true of false
    '''
    if target:
        for element in iterable:
            if element == target:
                return True
        return False
    else:
        for element in iterable:
            if element:
                return True
        return False

def each(iterable, target):
    '''has target, if all element in iterable is false will be true
    no target, if all element  in iterable does not equal target will be true

    - Params:
    @iterable: a obj could be iterable
    @target: compare element in obj with target

    - Returns:
    true of false
    '''
    if target:
        for element in iterable:
            if element == target:
                return False
        return True
    else:
        for element in iterable:
            if not element:
                return False
        return True