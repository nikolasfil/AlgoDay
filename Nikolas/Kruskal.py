#!/bin/python3

# Hackerrank Kruskal MST Really Special Subtree
# https://www.hackerrank.com/challenges/kruskalmstrsub?isFullScreen=true


def Kruskal(V, mat):
    # V is a list of sets. Each set contains the vertices that are connected to each other.

    # initializing the sum of the ,minimum spanning tree to 0
    mstsum = 0

    # sorting the edges of the graph based on their weights
    # weight is in the 3rd position of x (0,1,2)
    mat = sorted(mat, key=lambda x: x[2])

    # while there are still edges in the graph
    while len(mat) > 0:
        # Check if the two verices of the current edge are not already in the same set (i.e. they are not already connected)
        if mat[0][0] not in V[mat[0][1] - 1] or mat[0][1] not in V[mat[0][0] - 1]:
            # if they are not in the same set , it means adding the edge won't create a cycle in the minumum spanning tree.
            # merge the sets of the two vertices by taking their union using the | operator
            V[mat[0][0] - 1] = V[mat[0][0] - 1] | V[mat[0][1] - 1]
            
            # set the second vertex's set as the merged set
            V[mat[0][1] - 1] = V[mat[0][0] - 1]

            # update the sets of all vertices in the merged set to the new set .
            # this ensures that all verices connected to the merged set are also part of the same set
            for i in V[mat[0][0] - 1]:
                V[i - 1] = V[mat[0][0] - 1]
                
            # add the weight of the current edge to the sum of the minimum spanning tree
            mstsum += mat[0][2]
        # remove the processed edge from the list to move to the next edge 
        mat.pop(0)
        # print the total weight of the minimum spanning tree
    return mstsum


if __name__=='__main__':
    g_node, g_edge = map(int,input().split())

    # initialize the list of edges
    mat = []
    for m in range(g_edge):
        # from , to , weight
        s = list(map(int, input().split()))
        mat.append(s)

    start = 1
    # Add a set containing only the current vertex i to the list of sets
    # represents the list of sets where each set contains vertices that are connected to each other
    V = [set([i]) for i in range(1,g_node+1)]

    result = Kruskal(V, mat)

    print(result)