import types

def ft_filter(function_to_apply, iterable):
    """Filter the result of function apply to all elements of the iterable.
    Args:
      function_to_apply: a function taking an iterable.
      iterable: an iterable object (list, tuple, iterator)
    Return:
      An iterable.
      None if the iterable can not be used by the funtion.
    """
    if function_to_apply != None and not isinstance(function_to_apply, types.FunctionType):
        raise Exception("function_to_apply is not a function.")
    if not hasattr(iterable, "__iter__"):
        raise Exception("iterable argument is not an iterable")
    for item in iterable:
        if (function_to_apply == None and item) or function_to_apply(item):
            yield item
