import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import sys

class ImageProcessor(object):
    """
    Class to load and display images.
    """
    @staticmethod
    def load(path):
        """
        Opens the PNG file specified by the path argument and returns an array with
        the RGB values of the pixels image.
        It displays a message specifying the dimensions of the image.
        """
        try:
            rgb = mpimg.imread(path)
            array = np.array(rgb)
            shape = np.shape(array)
            print("Loading image of dimensions {} x {}".format(shape[0], shape[1]))
            return array
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            print("Exception: {} -- {}".format(exc_type.__name__, exc_value))
            return None

    @staticmethod
    def display(array):
        """
        Takes a numpy array as an argument and display the corresponding RGB image.
        """
        try:
            plt.axis("off")
            plt.imshow(array)
            plt.show()
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            print("Exception: {} -- {}".format(exc_type.__name, exc_value))
        return None
