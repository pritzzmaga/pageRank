import numpy as np
import pandas as pd
from scipy.linalg import eig
import networkx as nx


def getInput(n_getInput, k_getInput):
    # used to take input of graph
    """
    Gets input from user and makes an Adjacency Matrix

    Parameters
    ---------
    n_getInput : int
        Number of Nodes in the Graph
    k_getInput : int
        Number of Edges in the Graph

    Returns
    ---------
    A : numpy array of order nxn
        Adjacency Matrix representing a Web Graph
    """
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
    """
    Gives the Power Iterated Answer for PageRank Algorithm


    Parameters
    ---------
    A_powerIteration : Adjacency Matrix
        The Web Graph, to find PageRank of

    Returns
    ---------
    x : numpy array of order 1xn
        The Probability Vector found through PowerIteration
    """
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
    """
    Returns the Right Eigen Vector found through Linear Algebra

    
    Parameters
    ---------
    A_eigen : Adjacency Matrix
        The Web Graph, to find PageRank of

    Returns
    ---------
    ans : numpy array of order 1xn
        The Probability Vector found through Linear Algebra
    """
    At = A_eigen.T

    abc, At = np.linalg.eig(At)
    W, vl = eig(A_eigen, left=True, right=False)
    arr1 = vl[:, 0].real
    ans = arr1 / sum(arr1)
    return ans


def makePageRank(n, A_alpha, alpha):
    """
    Driver Function for PageRank
    Parameters
    ---------
    n : int
        The number Nodes in the PageRank Algo
    A_alpha : Adjacency Matrix
        The Web Graph, to find PageRank of
    alpha : float
        Random Teleportation Factor    

    Returns
    ---------
        Doesn't Return but Prints the PageRanks through Power Iteration and Eigen Vector Methods
    """
    # alpha = 0.1

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

    x = powerIteration(A_alpha)
    print("The probability transition matrix from power iteration method is: ")
    print(x[0])
    ans = rightEigen(A_alpha)
    print("The probability transition matrix from eigenvector method is: ")
    print(ans)
    # print(y)


def makePageRankAlphaZero(n, A_zero_alpha, G, k):
    """
    PageRank Algo With no Random Teleportaion Factor
    Parameters
    ---------
    n : int
        The number Nodes in the PageRank Algorithm
    A_zero_alpha : Adjacency Matrix
        The Web Graph, to find PageRank of
    G : Adjcency Matrix
        The Web Graph as a Digraph to check for Strong Connectivity
    k : int
        The Number of Edges in the PageRank Algorithm    

    Returns
    ---------
        Doesn't Return but Prints the PageRanks with no Random Teleportation
    """
    ansList = []
    print(A_zero_alpha)
    if nx.is_strongly_connected(G):

        for i in range(0, n):
            ansList.append(sum(A_zero_alpha[i]) / k)
        print("The probability transition matrix when alpha is 0 is: ")
        print(ansList)
    else:
        print("Not Strongly Connected")
    return


if __name__ == '__main__':
    n = int(input("Enter the number of nodes: "))
    k = int(input("Enter the number of connections: "))
    A, G = getInput(n, k)
    A_dummy = A

    makePageRankAlphaZero(n, A, G, k)
    makePageRank(n, A_dummy, 0.1)
