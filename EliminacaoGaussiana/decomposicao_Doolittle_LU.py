import numpy as np


def LUDecompDoolittle(a, b):
    n, m = a.shape
    lower = [[0 for x in range(n)]
             for y in range(n)]
    upper = [[0 for x in range(n)]
             for y in range(n)]

    # Decomposing matrix into Upper
    # and Lower triangular matrix
    for i in range(n):

        # Upper Triangular
        for k in range(i, n):

            # Summation of L(i, j) * U(j, k)
            sum = 0
            for j in range(i):
                sum += (lower[i][j] * upper[j][k])

            # Evaluating U(i, k)
            upper[i][k] = a[i][k] - sum

        # Lower Triangular
        for k in range(i, n):
            if (i == k):
                lower[i][i] = 1  # Diagonal as 1
            else:

                # Summation of L(k, j) * U(j, i)
                sum = 0
                for j in range(i):
                    sum += (lower[k][j] * upper[j][i])

                # Evaluating L(k, i)
                lower[k][i] = int((a[k][i] - sum) /
                                  upper[i][i])

    # Substituição
    # LUx=b =>  Ly=b,  Ux=y
    y = np.zeros(n)
    # Ly=b
    y[0] = b[0]
    for i in range(1, n, 1):
        # Vetorizei aqui!
        y[i] = (b[i] - np.dot(upper[i, :i], y[:i]))

    # Ux=y
    x = np.zeros(n)
    x[n-1] = y[n-1]/upper[n-1, n-1]
    for i in range(n-2, -1, -1):
        # Vetorizei aqui!
        x[i] = (y[i] - np.dot(upper[i, i+1:], x[i+1:]))/upper[i, i]
    # setw is for displaying nicely
    # print("Lower Triangular\t\tUpper Triangular")

    # Displaying the result :
    # for i in range(n):

        # Lower
    #    for j in range(n):
    #        print(lower[i][j], end="\t")
    #    print("", end="\t")

        # Upper
    #    for j in range(n):
    #        print(upper[i][j], end="\t")
    #    print("")
