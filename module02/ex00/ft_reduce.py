import types

def ft_reduce(function_to_apply, iterable):
    """Apply function of two arguments cumulatively.
    Args:
      function_to_apply: a function taking an iterable.
      iterable: an iterable object (list, tuple, iterator).
    Return:
      A value, of same type of elements in the iterable parameter.
      None if the iterable can not be used by the function.
    """
    if not isinstance(function_to_apply, types.FunctionType):
        raise Exception("function_to_apply is not a function.")
    if not hasattr(iterable, "__iter__"):
        raise Exception("iterable argument is not an iterable.")
    tmp_value = iterable[0]
    for pos in range(1, len(iterable)):
        try:
            tmp_value = function_to_apply(tmp_value, iterable[pos])
        except:
            return None
    return tmp_value
