import numpy as np
import pandas as pd
import networkx as nx
import matplotlib as plt

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
    return ansList #this is the root set



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
    A = np.matrix()


scanFile()
rootList = findRootSet('War')
baseList = findBaseSet(rootList)