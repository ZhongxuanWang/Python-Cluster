"""
Matrix class written by Daniel Wang encapsulating most of the aspects of matrices. Not like Numpy,
this provides more functionalities and convenient access to code.
In 4 words: 闲着无聊
"""

import numpy as np
from numpy import array as arr


class Matrix(object):
    num_of_matrix = 0

    def __init__(self, *mat):
        # ATTENTION: What you get from mat is a tuple formatted variable! to access it, using [index]
        if mat:
            self.mat = mat[0]
        else:
            self.mat = self.identity(3)
        self.nrows = len(mat[0])
        self.ncols = len(mat[0][0])

        Matrix.num_of_matrix += 1
        self.my_num = Matrix.num_of_matrix

    def getmat(self):
        return self.__mat

    def setmat(self, other):
        assert len(other) > 0 and len(other[0]) > 0
        self.__mat = other

    mat = property(getmat, setmat)

    def __str__(self):
        return "Matrix" + str(self.mat)

    def __mul__(self, other):
        return self.__internal_dot(other)

    def __add__(self, other):
        return self.__internal_add(other)

    # Make the object from this class subscriptable
    def __getitem__(self, item):
        return self.mat[item]

    def __len__(self):
        return len(self.mat)

    def dot(self, nm):
        mat = self.__internal_dot(nm)

    def add(self, nm):
        mat = self.__internal_add(nm)

    """
    Using matplotlib to plot matrix
    """

    def matplot(self):
        pass

    """
    Using seaborn to plot matrix
    """

    def seaplot(self):
        pass

    # This means a private method
    def __internal_dot(self, nm):
        if isinstance(nm, (int, float, bool)):
            return self.mat * nm
        else:
            assert len(self.mat[0]) == len(nm)

            matcher = len(self.mat[0])

            nrow_of_mat = len(self.mat)
            ncol_of_mat = len(self.mat[0])

            ncol_of_new_mat = len(nm[0])

            new_mat = self.zero(ncol_of_new_mat, nrow_of_mat, frame=True)
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
            # self.mat =
            pass

    @staticmethod
    def identity(*dimension):
        assert 0 < len(dimension) < 3
        a = arr([])
        if len(dimension) == 1:
            for i in range(dimension[0]):
                for j in range(dimension[0]):
                    if i == j:
                        a[i].append(1)
                    else:
                        a[i].append(0)
            return a
        elif len(dimension) == 2:
            for i in range(dimension[0]):
                for j in range(dimension[1]):
                    if i == j:
                        a[i].append(1)
                    else:
                        a[i].append(0)
            return a

    @staticmethod
    def zero(*dimension, frame=False):
        assert 0 < len(dimension) < 3
        if frame:
            var = None
        else:
            var = 0
        return arr([[var for _ in range(dimension[0])] for _ in range(dimension[len(dimension) - 1])])
