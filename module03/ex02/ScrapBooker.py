import numpy as np

class ScrapBooker(object):
    """
    Manipulation and initiation to slicing method on numpy arrays.
    """
    def crop(self, array, dim, position = (0,0)):
        """
        Crops the image as a rectangle via dim arguments (being the new height
        and width of the image) from the coordinates given by position arguments.
        """
        try:
            output = array[position[0]:position[0] + dim[0], position[1]:position[1] + dim[1]]
            return output
        except:
            return None

    def thin(self, array, n, axis):
        """
        Deletes every n-th line pixels along the specified axis 
        0: vertical, 1:horizontal)
        """
        try:
            output = np.delete(array, n - 1, int(not axis))
            return output
        except:
            return None

    def juxtapose(self, array, n, axis):
        """
        Juxtaposes n copies of the image along the specified axis.
        """
        try:
            output = np.copy(array)
            for i in range(n - 1):
                output = np.concatenate((output, array), axis)
            return output
        except:
            return None

    def mosaic(self, array, dim):
        """
        Makes a grid with multiple copies of the array. The dim argument specifies
        the number of repetition along each dimensions.
        """
        try:
            output = self.juxtapose(array, dim[0], 0)
            output = self.juxtapose(output, dim[1], 1)
            return output
        except:
            return None
