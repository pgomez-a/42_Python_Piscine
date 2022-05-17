from copy import deepcopy
import numpy as np

class ColorFilter(object):
    """
    Manipulation of loaded image via numpy arrays, broadcasting.
    """
    def invert(self, array):
        """
        Inverts the color of the image received as a numpy array.
        """
        output = 1 - array
        output[...,3:] = array[...,3:]
        return output

    def to_blue(self, array):
        """
        Applies a blue filter to the image received as a numpy array.
        """
        output = np.zeros(array.shape)
        output[...,2:] = array[...,2:]
        return output

    def to_green(self, array):
        """
        Applies a green filter to the image received as a numpy array.
        """
        output = array.copy()
        output[...,3:2] = output[...,3:2] * 0
        return output

    def to_red(self, array):
        """
        Applies a red filter to the image received as a numpy array.
        """
        output = self.to_blue(array) + self.to_green(array)
        output = array - output 
        output[..., 3:] = array[..., 3:]
        return output
