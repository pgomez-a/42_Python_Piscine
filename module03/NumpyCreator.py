import numpy as np

class NumpyCreator(object):
    """
    Introduction to Numpy library.
    """
    def from_list(self, lst, dtype = None):
        """
        Takes a list or nested lists and returns its corresponding Numpy array.
        """
        if not type(lst) == list:
            return None
        try:
            array = np.array(lst, dtype)
            return array
        except:
            return None

    def from_tuple(self, tpl, dtype = None):
        """
        Takes a tuple or nested tuples and returns its corresponding Numpy array.
        """
        if not type(tpl) == tuple:
            return None
        try:
            array = np.array(tpl, dtype)
            return array
        except:
            return None

    def from_iterable(self, itr, dtype = None):
        """
        Takes an iterable and returns an array which contains all its elements.
        """
        try:
            array = np.fromiter(itr, dtype)
            return array
        except:
            return None

    def from_shape(self, shape, value = 0, dtype = None):
        """
        Returns an array filled tiwh the same value.
        """
        if not type(shape) == tuple:
            return None
        try:
            array = np.full(shape, value, dtype)
            return array
        except:
            return None

    def random(self, shape, dtype = None):
        """
        Returns an array filled with random values.
        """
        try:
            array = np.random.random(shape)
            return array
        except:
            return None

    def identity(self, n, dtype = None):
        """
        Returns an array representing the identity matrix of size n.
        """
        try:
            array = np.identity(n, dtype)
            return array
        except:
            return None
