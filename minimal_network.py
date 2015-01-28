#find the maximum saving which can be achieved by removing redundant edges whilst ensuring that the network remains connected.  

""" Just a simple application of prim's MST algorithm
"""

from Heap import Heap

def p107(network="p107.network"):
    network=open(network)
    network=[row.split(',') for row in network.read().split('\n')[:-1]]
    edges=Heap(0)
    counter=0
    for i in xrange(len(network)):
        if network[0][i]!='-':
            edges.add((int(network[0][i]),0,i))
    vertices=set([0])
    cost=0
    total_cost=0
    for i in xrange(len(network)):
        for j in xrange(i+1,len(network)):
            if network[i][j]!='-':
                total_cost+=int(network[i][j])
    while len(vertices)<len(network):
        edge=edges.removeMin()
        while edge[2] in vertices:
            edge=edges.removeMin()
        vertices.add(edge[2])
        cost+=edge[0]
        for i in xrange(len(network)):
            if network[edge[2]][i]!='-':
                edges.add((int(network[edge[2]][i]),edge[2],i))
    print total_cost-cost
        
p107()
