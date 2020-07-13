"""
Matrix class written by Daniel Wang encapsulating most of the aspects of matrices. Not like Numpy,
this provides more functions and more user-friendly.
In 4 words: 闲着无聊
"""

import numpy as np
from numpy import array as arr


class Matrix():
    num_of_matrix = 0

    def __init__(self, shape, *mat):
        mat = mat[0]
        if mat:
            if isinstance(type(mat), type(arr)):
                self.mat = mat
            else:
                self.mat = arr(mat)
        else:
            self.mat = self.identity(3)
        self.nrows = len(mat)
        self.ncols = len(mat[0])

        Matrix.num_of_matrix += 1
        self.my_num = Matrix.num_of_matrix

    def get_mat(self):
        return self.mat

    def set_mat(self, other):
        assert len(other) > 0 and len(other[0]) > 0
        self.mat = other

    mat = property(get_mat, set_mat)

    def __str__(self):
        return "Matrix" + str(self.mat)

    def __mul__(self, other):
        return self.__internal_dot(other)

    def __add__(self, other):
        return self.__internal_add(other)

    def __abs__(self):
        return self.det()

    # Make the object from this class subscriptable
    def __getitem__(self, item):
        return self.mat[item]

    def __len__(self):
        return len(self.mat)

    def dot(self, nm, inplace=False):
        result = self.__internal_dot(nm)
        if inplace:
            self.mat = result
        return result

    def add(self, nm, inplace=False):
        result = self.__internal_add(nm)
        if inplace:
            self.mat = result
        return result

    def inv(self):
        row = len(self.mat)
        col = len(self.mat[0])
        # Make sure it's a square
        assert row == col
        return self.__internal_inv()

    def det(self):
        row = len(self.mat)
        col = len(self.mat[0])
        # Make sure it's a square
        assert row == col
        # Edge cases
        if 997 < row < 1000000:
            import sys
            sys.setrecursionlimit(row + 2)
        elif row > 1000000:
            raise Exception("Row/Col number exceeded")
        return self.__internal_det(list(self.mat))

    """
    Using matplotlib to plot matrix
    """

    def matplot(self):
        pass

    # This means a private method
    def __internal_dot(self, nm):
        if isinstance(nm, (int, float, bool)):
            return self.mat * nm
        else:
            assert len(self.mat[0]) == len(nm)

            matcher = len(self.mat[0])

            nrow_of_mat = len(self.mat)
            ncol_of_new_mat = len(nm[0])

            new_mat = self.zero(nrow_of_mat, ncol_of_new_mat, frame=True)
            for row in range(nrow_of_mat):
                for col in range(ncol_of_new_mat):
                    nsum = 0
                    for match in range(matcher):
                        nsum += nm[match][col] * self.mat[row][match]
                    new_mat[row][col] = nsum
            return new_mat

    def __internal_add(self, nm):
        if isinstance(nm, (int, float, bool)):
            return self.mat + nm
        else:
            assert len(self.mat) == len(nm) and len(self.mat[0]) == len(nm[0])
            for row in range(len(nm)):
                for col in range(len(nm[0])):
                    nm[row][col] += self.mat[row][col]
            return nm

    def __internal_inv(self):
        pass

    """
    Precondition: 
    1. Squre matrix
    
    Postcondition:
    mat object is not changed    
    """

    def __internal_det(self, nm):
        sum = 0
        if len(nm) == 2:
            return nm[0][0] * nm[1][1] - nm[0][1] * nm[1][0]
        for col in range(len(nm[0])):
            sum += (-1) ** (2 + col) * nm[0][col] * self.__internal_det(np.delete(np.delete(nm, 0, 0), col, 1))
        return sum

    # def __construct_nm(self, nm, col):
    #     changed_matrix = Matrix.zero(len(nm) - 1, len(nm[0]) - 1)
    #     for r in range(1, len(nm)):
    #         for c in range(0, len(nm[0])):
    #             if c != col:
    #                 changed_matrix = nm[r][c]
    #     return changed_matrix

    @staticmethod
    def identity(*dimension):
        assert 0 < len(dimension) < 3
        a = Matrix.zero(*dimension)
        row, col = Matrix.getrc(*dimension)
        for i in range(row):
            for j in range(col):
                if i == j:
                    a[i] = 1
        return a

    @staticmethod
    def zero(*dimension, frame=False):
        assert 0 < len(dimension) < 3
        row, col = Matrix.getrc(*dimension)
        if frame:
            var = None
        else:
            var = 0
        return arr([[var for _ in range(col)] for _ in range(row)])

    @staticmethod
    def getrc(*dimension):
        if len(dimension) > 1:
            row, col = dimension
        else:
            col = row = dimension[0]
        return row, col
