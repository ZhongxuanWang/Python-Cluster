"""
Matrix class written by Daniel Wang encapsulating most of the aspects of matrices. Not like Numpy,
this provides more functionalities and convenient access to code.
"""

import copy
import numpy as np
from numpy import array as arr


class Matrix(object):
    num_of_matrix = 0

    def __init__(self, *mat):
        if mat:
            assert len(mat) > 0 and len(mat[0]) > 0
            self.mat = mat
        else:
            self.mat = self.identity(3)
        self.nrows = len(mat)
        self.ncols = len(mat[0])

        Matrix.num_of_matrix += 1
        self.my_num = Matrix.num_of_matrix

    def __str__(self):
        return "Matrix" + str(self.mat[0])

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
            return self.mat[0] * nm
        else:
            assert len(self.mat[0]) == len(nm)
            matcher = self.mat[0]
            nrow = len(self.mat)
            ncol = len(nm[0])
            new_mat = self.zero(nrow, ncol, frame=True)
            for row in range(nrow):
                for col in range(ncol):
                    sum = 0
                    for row2 in range(nrow):
                        for match in range(matcher):
                            sum += self.mat[row2][match] * nm[row2][match]

                    new_mat[row][col] = sum
            return new_mat

    def __internal_add(self, nm):
        if isinstance(nm, (int, float, bool)):
            return self.mat[0] + nm  # TODO what happened???
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
