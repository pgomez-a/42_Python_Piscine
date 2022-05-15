import copy

class Vector:
    def __init__(self, vector_list):
        """Initializes Vector class"""
        self.vector_list = vector_list.copy() 
        if len(vector_list) > 1:
            self.shape = (len(vector_list), 1)
        else:
            self.shape = (1, len(vector_list[0]))
        return

    def dot(self, other):
        """Produce a dot product between two Vectors of same shape"""
        if self.shape != other.shape:
            print("TypeError: Vectors are not of same shape.")
            return False
        product = 0
        for row in range(len(self.vector_list)):
            for column in range(len(self.vector_list[row])):
                product += self.vector_list[row][column] * other.vector_list[row][column]
        return product

    def T(self):
        """Returns the transpose Vector"""
        transpose = list()
        if self.shape[0] == 1:
            for row in self.vector_list:
                for column in row:
                    transpose.append([column])
        else:
            col_to_row = list()
            for row in self.vector_list:
                for column in row:
                    col_to_row.append(column)
            transpose.append(col_to_row)
        return Vector(transpose)

    def __str__(self):
        """Shows the content of the Vector object"""
        txt = ""
        txt += "Vector(" + str(self.vector_list) + ")"
        return txt

    def __repr__(self):
        """Prints the content of the Vector object"""
        return "Vector(" + str(self.vector_list) + ")"

    def __add__(self, other):
        """Addition for 2 Vectors of the same shape"""
        if self.shape != other.shape:
            print("TypeError: Vectors are not of same shape.")
            return False
        output = copy.deepcopy(self.vector_list)
        for row in range(len(output)):
            for column in range(len(output[row])):
                output[row][column] += other.vector_list[row][column]
        return output

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        """Substraction for 2 Vectors of same shape"""
        if self.shape != other.shape:
            print("TypeError: Vectors are not of same shape.")
            return False
        output = copy.deepcopy(self.vector_list)
        for row in range(len(output)):
            for column in range(len(output[row])):
                output[row][column] -=  other.vector_list[row][column]
        return output

    def __rsub(self, other):
        return self - other

    def __mul__(self, scalar):
        """Multiplication for Vector and scalar"""
        if type(scalar) != int and type(scalar) != float:
            print("TypeError: Vector can only mul scalar.")
            return False
        output = copy.deepcopy(self.vector_list)
        for row in range(len(output)):
            for column in range(len(output[row])):
                output[row][column] *= scalar
        return output

    def __rmul__(self, scalar):
        """Reverse multiplication for Vector and scalar"""
        return self * scalar

    def __truediv__(self, scalar):
        """Division for Vector and scalar"""
        if type(scalar) != int and type(scalar) != float:
            print("TypeError: Vector can only truediv scalar.")
            return False
        if scalar == 0.0:
            print("ZeroDivisionError: division by zero.")
            return False
        output = copy.deepcopy(self.vector_list)
        for row in range(len(output)):
            for column in range(len(output[row])):
                output[row][column] /= scalar
        return output

    def __rtruediv__(self, scalar):
        """Reverse ficision for Vector and scalar"""
        print("NotImplementedError: Division of a scalar by a Vector is not defined here.")
        return False
