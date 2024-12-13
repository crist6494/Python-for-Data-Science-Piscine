def ft_filter(function, collection):
    """
    Return an iterator yielding those items of collection):
    for which function(item) is true.
    If function is None, return the items that are true.
    """
    for i in collection:
        if (function or bool)(i):
            yield i
