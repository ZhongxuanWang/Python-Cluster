"""
Matrix class written by Daniel Wang encapsulating most of the aspects of matrices. Not like Numpy,
this provides more functionalities and convenient access to code.
"""

import numpy as np
from numpy import array as arr


class Matrix(object):
    num_of_matrix = 0

    def __init__(self, *mat):
        if mat:
            assert len(mat) > 0 and len(mat[0]) > 0
            self.mat = arr(mat)
        else:
            self.mat = self.identity(3)
        self.nrows = len(mat)
        self.ncols = len(mat[0])

        Matrix.num_of_matrix += 1
        self.my_num = Matrix.num_of_matrix

    def __str__(self):
        return "Matrix" + str(self.mat[0])

    def __mul__(self, other):
        return self.internal_dot(other)

    def __add__(self, other):
        return self.internal_add(other)

    def dot(self, nm):
        mat = self.internal_dot(nm)

    def add(self, nm):
        mat = self.internal_add(nm)

    """
    Using matplotlib to plot graph
    """
    def matplot(self):
        pass

    """
    Using seaborn to plot matrix
    """
    def seaplot(self):
        pass



    def internal_dot(self, nm):
        if isinstance(nm, (int, float, bool)):
            return self.mat[0] * nm
        else:
            # self.mat =
            pass

    def internal_add(self, nm):
        if isinstance(nm, (int, float, bool)):
            return self.mat[0] + nm # TODO what happened???
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
    def zero(frame=False, *dimension):
        assert 0 < len(dimension) < 3
        if frame:
            var = None
        else:
            var = 0
        return arr([[var] for _ in range(dimension[0])] for _ in range(dimension[len(dimension) - 1]))
