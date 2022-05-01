import numpy as np
import pandas as pd
import networkx as nx
import matplotlib as plt
from scipy.linalg import eig


def scanFile():
    web_graph = nx.read_gpickle("web_graph.gpickle")
    web_graph
    node_index = 20
    web_graph.nodes[node_index]['page_content']
    print(web_graph[10])
    pos = {i: web_graph.nodes[i]['pos'] for i in range(len(web_graph.nodes))}
    print(web_graph)

    print(web_graph.nodes[30]['page_content'])


def findRootSet(query):
    web_graph = nx.read_gpickle("web_graph.gpickle")
    ansList = []
    for i in range(0, len(web_graph.nodes)):
        if query.lower() in web_graph.nodes[i]['page_content'].lower():
            ansList.append(i)

    print(ansList)
    return ansList  # this is the root set


def findBaseSet(rootList):
    baseList = []
    web_graph = nx.read_gpickle("web_graph.gpickle")
    for i in rootList:
        if i not in baseList:
            baseList.append(i)
        for j in web_graph[i]:
            if j not in baseList:
                baseList.append(j)

    baseList.sort()
    print(baseList)
    return baseList


def makeAdjacencyMatrix(baseList):
    web_graph = nx.read_gpickle("web_graph.gpickle")
    A_index = {}
    A = np.zeros((len(baseList), len(baseList)), float)
    count = 0
    for i in baseList:
        A_index[i] = count
        count += 1
    for i in baseList:
        for j in web_graph[i]:
            if j in baseList:
                A[A_index[i]][A_index[j]] = 1

    return A


def findAandH(A):
    AT = A.T
    # hw, hv = np.linalg.eig(np.matmul(A, AT))
    hw, hv = eig(np.matmul(A, AT), left=False, right=True)
    ma = 0
    ind = 0
    for i in range(0, len(hw)):
        if hw[i] > ma:
            ind = i
            ma = hw[i]
    h = hv[:, ind].real

    print(h * h / sum(h * h))
    print(abs(sum(h * h / sum(h * h))))

    aw, av = eig(np.matmul(AT, A), left=False, right=True)
    ma = 0
    ind = 0
    for i in range(0, len(aw)):
        if aw[i] > ma:
            ind = i
            ma = aw[i]
    a = av[:, ind].real

    print(a * a / sum(a * a))
    print(abs(sum(a * a / sum(a * a))))


if __name__ == '__main__':
    scanFile()
    rootList = findRootSet('War')
    baseList = findBaseSet(rootList)
    A = makeAdjacencyMatrix(baseList)
    findAandH(A)
