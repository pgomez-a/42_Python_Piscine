import types

def ft_map(function_to_apply, iterable):
    """Map the function to all elements of the iterable.
    Args:
      function_to_apply: a function taking an iterable.
      iterable: an iterable object (list, tuple, iterator)
    Return:
      An iterable.
      None if the iterable can not be used by the function.
    """
    if not isinstance(function_to_apply, types.FunctionType):
        raise Exception("function_to_apply is not a function.")
    if not hasattr(iterable, "__iter__"):
        raise Exception("iterable argument is not an iterable.")
    for item in iterable:
        yield function_to_apply(item)
