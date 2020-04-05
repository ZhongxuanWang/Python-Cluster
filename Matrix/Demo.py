"""
This Demo is for matrix class written by Daniel Wang for interpretation
"""

from Matrix import Matrix
import numpy as np


def main():
    mat1 = Matrix(np.array([[1, 2, -3], [4, 0, -2]]))
    mat2 = Matrix(np.array([[5, -4, 2, 0], [-1, 6, 3, 1], [7, 0, 5, 8]]))

    mat3 = Matrix(np.array([[-1, 3, 1], [2, 5, 0], [3, 1, -2]]))
    mat4 = Matrix(np.array([[5, -4, 2], [-1, 3, 1], [7, 0, 8]]))

    mat5 = Matrix([[2, 0], [-7, 5]])

    print("Printing out the content")
    print(mat1, "\n", mat2)

    print("Dot product - with real number directly")
    print(mat1 * 5)

    print("Dot product - with matrix directly")
    print(mat1 * mat2)
    print(mat3 * mat4)

    print("Determinant")
    print(abs(mat3))

    print("Identities")
    print(Matrix.identity(3))

    print("Zero")
    print(Matrix.zero(3, 4))


if __name__ == '__main__':
    main()
