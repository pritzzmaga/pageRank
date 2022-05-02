import networkx as nx
import numpy as np

web_graph = nx.read_gpickle('web_graph.gpickle')


def rootSet(query):
    n = len(web_graph.nodes)
    rootset = []
    for node in web_graph.nodes:
        nodeContent = web_graph.nodes[node]['page_content'].lower().split(", ;:")
        if query in nodeContent:
            print(nodeContent)
            rootset.append(node)
    return rootset


def makeBaseSet(rootset):
    baseSet = list(rootset)

    for edge in web_graph.edges:
        if edge[0] in rootset:
            if edge[1] not in baseSet:
                baseSet.append(edge[1])
        elif edge[1] in rootset:
            if edge[0] not in baseSet:
                baseSet.append(edge[0])
    return baseSet


def makeAdjacencyMatrix(baseSet):
    subgraph = nx.subgraph(web_graph, sorted(baseSet))
    adjacencyMatrix = nx.to_numpy_array(subgraph)
    return adjacencyMatrix


def findHandA(adjacencyMatrix, baseSet):
    n = len(baseSet)
    hubValues = np.ones(n) / n
    authValues = np.ones(n) / n

    for i in range(2022):
        hubValues = np.dot(adjacencyMatrix, authValues)
        authValues = np.dot(adjacencyMatrix.T, hubValues)
        hubSum = sum(hubValues)
        authSum = sum(authValues)
        hubValues /= hubSum
        authValues /= authSum

    HubScores = []
    AuthorityScores = []
    for i in range(len(baseSet)):
        HubScores.append((baseSet[i], hubValues[i]))
        AuthorityScores.append((baseSet[i], authValues[i]))

    HubScores.sort(key=lambda x: x[0])
    AuthorityScores.sort(key=lambda x: x[0])

    print("\nHub Scores: ")
    for i in range(len(baseSet)):
        print("Node", HubScores[i][0], " : ", HubScores[i][1])

    print("\nAuthority Scores: ")
    for i in range(len(baseSet)):
        print("Node", AuthorityScores[i][0], " : ", AuthorityScores[i][1])


query = input("Enter a query word: ")
query = query.lower()
rootset = rootSet(query)
baseset = makeBaseSet(rootset)
adj=makeAdjacencyMatrix(baseset)
print(rootset)
print(baseset)
findHandA(adj,baseset)
