import numpy as np
import pandas as pd
from scipy.linalg import eig
import networkx as nx


def getInput(n_getInput, k_getInput):
    # used to take input of graph
    G = nx.MultiDiGraph()
    A = np.zeros((n_getInput, n_getInput), float)
    print("Enter the Edges:")
    for i in range(0, k_getInput):
        x, y = input().split(',')
        G.add_edge(int(x), int(y))
        A[int(x) - 1][int(y) - 1] = float(1.0)
    return A, G

    # A = [[0.0, 1.0, 0.0, 0.0],
    #      [1.0, 0.0, 1.0, 0.0],
    #      [0.0, 1.0, 0.0, 1.0],
    #      [0.0, 0.0, 1.0, 0.0]]
    # return A


def powerIteration(A_powerIteration):
    x = np.zeros((1, np.shape(A_powerIteration)[0]), float)
    x[0][0] = 1.0
    close = False
    x_prev = x
    while not close:
        # print(x)
        x = np.matmul(x, A_powerIteration)

        res = np.subtract(x, x_prev)
        errorInArray = 0.0
        for i in range(0, np.size(res)):
            errorInArray += (abs(res[0][i]))
        if errorInArray < 0.00000001:
            close = True
        else:
            x_prev = x

    return x


def rightEigen(A_eigen):
    At = A_eigen.T

    abc, At = np.linalg.eig(At)
    W, vl = eig(A_eigen, left=True, right=False)
    arr1 = vl[:, 0].real
    print(arr1 / sum(arr1))


def makePageRank(n, A_alpha, alpha):
    # alpha = 0.1
    print(A_alpha)
    sum = 0
    # step 1 check for rows with no 1's and replace full row with 1/N's
    # step 2 divide each 1 by the number of 1's in the row
    for i in range(0, n):
        sum = 0
        for j in range(0, n):
            sum += A_alpha[i][j]
        if sum == 0:
            for j in range(0, n):
                A_alpha[i][j] = float(1 / n)
        else:
            for j in range(0, n):
                if A_alpha[i][j] == 1:
                    A_alpha[i][j] = float(A_alpha[i][j] / sum)
    # print(A)
    A_alpha = A_alpha * (1 - alpha)
    A_alpha = A_alpha + (alpha) / n

    print(A_alpha)
    print("alpha is ")
    print(alpha)

    # x = powerIteration(A)
    # print(x)
    rightEigen(A_alpha)
    # print(y)


def makePageRankAlphaZero(n, A_zero_alpha, G, k):
    ansList = []
    print(A_zero_alpha)
    if nx.is_strongly_connected(G):
        print("strongly connectted")
        for i in range(0, n):
            ansList.append(sum(A_zero_alpha[i])/k)
        print(ansList)
    else:
        print("not strongly connected")


if __name__ == '__main__':
    n = int(input("Enter the number of nodes: "))
    k = int(input("Enter the number of connections: "))
    A, G = getInput(n, k)
    A_dummy = A

    makePageRankAlphaZero(n, A, G, k)
    makePageRank(n, A_dummy, 0.1)


