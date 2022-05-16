import copy
import math

class TinyStatistician(object):
    @staticmethod
    def mean(x):
        """
        Computes the mean of a given non-empty list or array x.
        """
        if len(x) == 0:
            return None
        mean = 0.0
        for item in x:
            mean += item
        return float(mean / len(x))

    @staticmethod
    def median(x):
        """
        Computes the median of a given non-empty list or array x.
        """
        if len(x) == 0:
            return None
        sorted_x = copy.deepcopy(x)
        sorted_x.sort()
        pos = len(sorted_x) * 0.5
        if  pos - int(pos) == 0.0:
            return float((sorted_x[int(pos) - 1] + sorted_x[int(pos)]) / 2)
        return float(sorted_x[int(pos)])

    @staticmethod
    def quartiles(x):
        """
        Computes the 1st and 3rd quartiles of a given non-empty array x.
        """
        if len(x) == 0:
            return None
        quartiles = list()
        sorted_x = copy.deepcopy(x)
        sorted_x.sort()
        pos = len(sorted_x) * 0.25
        if pos - int(pos) == 0.0:
            quartiles.append(float((sorted_x[int(pos) - 1] + sorted_x[int(pos)]) / 2))
        else:
            quartiles.append(float(sorted_x[int(pos)]))
        pos = len(sorted_x) * 0.75
        if pos - int(pos) == 0.0:
            quartiles.append(float((sorted_x[int(pos) - 1] + sorted_x[int(pos)]) / 2))
        else:
            quartiles.append(float(sorted_x[int(pos)]))
        return quartiles

    @staticmethod
    def var(x):
        """
        Computes the variance of a given non-empty list or array x.
        """
        if len(x) == 0:
            return None
        mean = TinyStatistician.mean(x)
        variance = 0.0
        for item in x:
            variance += (item - mean)**2
        return float(variance / len(x))

    @staticmethod
    def std(x):
        """
        Computes the standard deviation of a given non-empty list or array x.
        """
        if len(x) == 0:
            return None
        return float(math.sqrt(TinyStatistician.var(x)))
