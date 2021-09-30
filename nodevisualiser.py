import string
import random
import pyvis as py
from pyvis.network import Network
import pandas as pd
import networkx as nx
from random import randint, seed, choice

# Seed random
seed(randint(0,1000))

# Node sets
nodeList = []
targetNodeList = []
weightList = []

# Random node generation functions
def generateGNode():
    global nodeList

    gNode = 'G' + str(randint(0,400))
    nodeList.append(gNode)

def generateDNode():
    global nodeList
    dNode = 'D' + str(randint(0,10))
    nodeList.append(dNode)

def nameNNode():
    global nodeList
    nNode = 'N0'
    nodeList.append(nNode)

def generateNodeList():
    global nodeList
    for i in range(0,250):
        generateGNode()

    for i in range(0,10):
        generateDNode()
    
    nameNNode()

def generateTargetNode():
    targetNode = random.choice(nodeList)
    targetNodeList.append(targetNode)

generateNodeList()

for x in nodeList:
    generateTargetNode()
    weightList.append('1')

# Build nodeData set
nodeData = {'source': nodeList, 'target': targetNodeList, 'weight': weightList}

# Create DataFrame
nodes = pd.DataFrame(data = nodeData)

# Testing
g = nx.from_pandas_edgelist(
    nodes,
    source = 'source',
    target = 'target',
    edge_attr = 'weight')

# Graphing
net = Network(notebook = True)
net.from_nx(g)
net.show('nodeNetwork.html')