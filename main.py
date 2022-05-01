import numpy as np
import pandas as pd
from scipy.linalg import eig


def getInput():
    # used to take input of graph
    A = np.array([[0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                  [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0],
                  [1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0],
                  [0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                  [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0],
                  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0],
                  [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0],
                  [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0]])
    return A


def powerIteration(A):
    x = np.zeros((1, np.shape(A)[0]), float)
    x[0][0] = 1.0
    close = False
    x_prev = x
    while not close:
        # print(x)
        x = np.matmul(x, A)

        res = np.subtract(x, x_prev)
        errorInArray = 0.0
        for i in range(0, np.size(res)):
            errorInArray += (abs(res[0][i]))
        if errorInArray < 0.00000001:
            close = True
        else:
            x_prev = x

    return x


def rightEigen(A):
    At = A.T
    print(At)
    abc, At = np.linalg.eig(At)
    W, vl = eig(A, left=True, right=False)
    arr1 = vl[:, 0].real
    print(arr1/sum(arr1))



def makePageRank():
    alpha = 0.1
    A = getInput()
    sum = 0
    # step 1 check for rows with no 1's and replace full row with 1/N's
    # step 2 divide each 1 by the number of 1's in the row
    for i in range(0, 8):
        sum = 0
        for j in range(0, 8):
            sum += A[i][j]
        if sum == 0:
            for j in range(0, 8):
                A[i][j] = float(1 / np.shape(A)[0])
        else:
            for j in range(0, 8):
                if A[i][j] == 1:
                    A[i][j] = float(A[i][j] / sum)
    print(A)
    A = A * (1 - alpha)
    A = A + (alpha) / np.shape(A)[0]

    print(A)

    x = powerIteration(A)
    print(x)
    rightEigen(A)
    # print(y)


makePageRank()
