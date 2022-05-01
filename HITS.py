import numpy as np
import pandas as pd
import networkx as nx
import matplotlib as plt

def scanFile():
    web_graph = nx.read_gpickle("web_graph.gpickle")
    web_graph
    node_index = 20
    web_graph.nodes[node_index]['page_content']
    pos = {i: web_graph.nodes[i]['pos'] for i in range(len(web_graph.nodes))}
    print(web_graph)

    print(web_graph.nodes[15]['page_content'])

def findRootSet(query):
    web_graph = nx.read_gpickle("web_graph.gpickle")
    ansList = []
    for i in range(0, len(web_graph.nodes)):
        if query in web_graph.nodes[i]:
            ansList.append(i)

scanFile()
findRootSet()