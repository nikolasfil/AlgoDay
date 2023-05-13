#!/bin/python3

# BFS shortest reach 
# Hackerrank
# https://www.hackerrank.com/challenges/bfsshortreach/problem?isFullScreen=true

import sys
from queue import Queue


class Node:
    def __init__(self):
        self.distance = -1
        self.children = []
        self.visited = False


def bfs(n_numberOfNodes, m_numberOfEdges, edges, s_startingNode):
    """Breadth-first search algorithm to calculate the shortest distances from a source node to all other nodes in an undirected graph."""
    
    # edges = [(start, end), ...] a list of tuples representing the edges between nodes. Each tuple contains two integers representing the indices (1-based) of the connected nodes.
    # s_startingNode = source node

    # initializes a list that sores n_numberOfNodes instances of Node class
    # Each Node represents a node in the graph and has two attributes : children to store all the neighboring nodes and distance: the shortest distance from the source code .
    
    nodes = [Node() for _ in range(n_numberOfNodes)]

    # iterates over the edges list and creates the necessary connections between nodes.
    for edge in edges:
        # I retrieves the corresponding Node objects from the nodes list based on the indices specified in the edges list.
        # for each edge, it adds the second node to the children list of the first node and vice versa since the graph is undirected.
        first, second = [nodes[i - 1] for i in edge]
        first.children.append(second)
        second.children.append(first)

    # initializes the top variable with the Node object corresponding to the source node (s_startingNode - 1 index) from the nodes list. It sets the distance of the source node to 0.
    top = nodes[s_startingNode - 1]
    top.distance = 0

    # creates a Queue object called queue to perform the BFS traversal. It adds the top node to the queue.
    queue = Queue()
    queue.put(top)

    # enters a while loop that continues until the queue is empty.
    while not queue.empty():
        # retrieves the first node from the queue and iterates over its children.
        node = queue.get()
        for child in node.children:
            # if the child node has not been visited or if the distance of the child node is greater than the distance of the current node plus 6 (the distance to reach the child node can be improved)
            if (not child.visited) or (child.distance > node.distance + 6):
                # updates the distance of the child node and adds it to the queue.
                child.distance = node.distance + 6
                child.visited = True
                # it adds the child node to the queue for further exploration in subsequent iterations of the loop
                queue.put(child)

    # removes the source node from the list of nodes and returns the distances of all the nodes in the graph.
    del nodes[s_startingNode - 1]
    return [node.distance for node in nodes]


if __name__ == "__main__":
    q_testCases = int(input().strip())
    for _ in range(q_testCases):
        n_numberOfNodes, m_numberOfEdges = [int(x) for x in input().strip().split(" ")]
        edges = []
        
        for _ in range(m_numberOfEdges):
            # 
            edges.append(list(map(int, input().rstrip().split())))
        
        
        s_startingNode = int(input().strip())

        result = bfs(n_numberOfNodes, m_numberOfEdges, edges, s_startingNode)
        print(" ".join(map(str, result)))
