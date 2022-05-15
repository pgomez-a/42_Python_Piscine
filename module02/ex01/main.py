def what_are_the_vars(*args, **kargs):
    """
    Returns an instance of class ObjectC
    """
    object_c = ObjectC()
    for item in range(len(args)):
        try:
            getattr(object_c, "var_" + str(item))
            return None
        except:
            setattr(object_c, "var_" + str(item), args[item])
    for item in kargs:
        try:
            getattr(object_c, item)
            return None
        except:
            setattr(object_c, item, kargs[item])
    return object_c

class ObjectC(object):
    """
    Class made to understand the use of *args, **kargs, getattr and setattr
    """
    def __init__(self):
        return

def doom_printer(obj):
    """
    Prints all the attributes of an ObjectC object
    """
    if obj is None:
        print("Error")
        print("end")
        return
    for attr in dir(obj):
        if attr[0] != "_":
            value = getattr(obj, attr)
            print("{}: {}".format(attr, value))
    print("end")
    return

if __name__ == '__main__':
    obj = what_are_the_vars(7)
    doom_printer(obj)
    obj = what_are_the_vars(None, [])
    doom_printer(obj)
    obj = what_are_the_vars("ft_lol", "HI")
    doom_printer(obj)
    obj = what_are_the_vars()
    doom_printer(obj)
    obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, a=10, var_0="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, "Yes", a=10, var_2 = "world")
    doom_printer(obj)
