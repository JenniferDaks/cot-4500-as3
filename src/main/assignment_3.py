import numpy as np


def euler_method(a_val, b_val, n_val, initial_val, function_val):
    h = (b_val - a_val) / n_val
    t = a_val
    w = initial_val
    for i in range(1, n_val+1):
        y = w
        w = w + (h * eval(function_val))
        t = a_val + (i * h)
    print("%.5f" % w)


def runge_kutta(function2_val, a2_val, b2_val, n2_val, initial_val2):
    h = (b2_val - a2_val) / n2_val
    t_i = a2_val
    y_i = initial_val2
    for i in range(1, n2_val+1):
        t = t_i
        y = y_i
        k1 = h * eval(function2_val)

        t = t_i + (h / 2)
        y = y_i + ((1 / 2) * k1)
        k2 = h * eval(function2_val)

        t = t_i + (h / 2)
        y = y_i + ((1 / 2) * k2)
        k3 = h * eval(function2_val)

        t = t_i + h
        y = y_i + k3
        k4 = h * eval(function2_val)

        y_i = y_i + (1 / 6) * (k1 + (2 * k2) + (2 * k3) + k4)
        t_i = t_i + h

    print("%.5f" % y_i)


def gaussian_elimination(m1, m2):
    rows = len(m1)
    for i in range(1, rows):
        x = m1[0][0] / m1[i][0]
        m1[i] = m1[i] - m1[0]/x
        m2[i] = m2[i] - m2[0]/x


if __name__ == "__main__":
    # 1. Euler Method with the following details
    #         Function: t – y**2
    #         Range: 0 < t < 2
    #         Iterations: 10
    #         Initial Point: f(0) = 1
    function = "t - y**2"
    a = 0
    b = 2
    N = 10
    initial_value = 1
    euler_method(a, b, N, initial_value, function)

    # 2. Runge-Kutta with the following details:
    #         Function: t - y**2
    #         Range: 0 < t < 2
    #         Iterations: 10
    #         Initial Point: f(0) = 1
    function2 = "t - y**2"
    a2 = 0
    b2 = 2
    N2 = 10
    initial_value2 = 1
    runge_kutta(function2, a2, b2, N2, initial_value2)

    # 3. Use Gaussian elimination and backward substitution
    # solve the following linear system of equations written
    # in augmented matrix format.
    #     [  2 -1  1  |  6 ]
    #     [  1  3  1  |  0 ]
    #     [ -1  5  4  | -3 ]
    #matrix1 = np.array([[2, -1, 1], [1, 3, 1], [-1, 5, 4]])
    #matrix2 = np.array([[6], [0], [-3]])
    #gaussian_elimination(matrix1, matrix2)

    # 4. Implement LU Factorization for the following matrix and do the following:
    #     1  1  0  3
    #     2  1 −1  1
    #     3 −1 −1  2
    #    −1  2  3 −1
    # a. Print out the matrix determinant.
    # b. Print out the L matrix.
    # c. Print out the U matrix.

    # 5. Determine if the following matrix is diagonally dominate.
    #     9   0   5   2   1
    #     3   9   1   2   1
    #     0   1   7   2   3
    #     4   2   3  12   2
    #     3   2   4   0   8

    # 6. Determine if the matrix is a positive definite.
    #     2  2  1
    #     2  3  0
    #     1  0  2
