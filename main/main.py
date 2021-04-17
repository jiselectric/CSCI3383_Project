class Graph:
    """
    CSCI3383 Final Project : Implementation of the Graph Library
    
    1. Strongly Connected Components (SCC) for Directed Graphs
    In theory of directed graphs, a graph is said to be strongly connected if every vertex is reachable from every other vertex.
    Hence, the strongly connected components of an arbitrary directed graph form a partition into subgraphs that are themselves strongly connected.
    The time complexity of finding strong connectivity of a graph is in G(|V| + |E|)

    DFS Algorithm can be implemented to ensure the inspect of SCC in linear time.
    In this project, Kosaraju's Algorithm will be used which uses two passes of DFS. The steps of Kosaraju's algorithm are as followed.
    
    1.1) Create an empty stack and finish first DFS traversal. In doing so, after calling a recursive DFS traversal for adjacent vertices of a vertex,
    push the corresponding vertex to stack.

    1.2) Reverse the order of all arcs to obtain the obtain the transpose graph

    1.3) Now pop a vertex in stack, S until the length of S in greater than 0. And then, DFS starting from v prints strongly connected component of v.

    2. Minimum Spanning Tree (MST) for undirected graphs

    A Minimum Spanning Tree (MST) for a weighted, connected and undirected graph is a spanning tree with a combined weight less or equal
    to the weight of other spanning tree. The total sum of the MST is the sum of weights given to each edge of the spanning tree.

    Kruskal’s Algorithm will be implemented to inspect MST.

    2.1) Sort the edges of MST in non-decreasing order of their weights
    2.2) Select the edge with the smallest weight, and check the cycle with the spanning tree formed so far
    2.3) Recursivley repeat step #2 until (V-1) edges in the spanning tree

    3. Single-source shortest paths (SSSP) for weighted directed graphs

    In a Single-source shortest paths problem, main objective is to find the shortest paths weights (and the actual paths) from a particular single-source vertex to all other vertices in a directed weighted graph (if such paths exist).
    There are several efficient algorithms for SSSP problem, for this project Dijkstra algorithm will be implemented. 

    3.1) Create a data structure to keeps track of vertices included in shortest path tree
    3.2) Assign a distance value to all vertices in the input graph
    3.3) Update distance value of all adjacent vertices of 
    """