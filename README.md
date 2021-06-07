# CSCI3383_Project


![graph 0a3b0feb](https://user-images.githubusercontent.com/35610628/120974519-322bd300-c7ab-11eb-8871-7097fa30f2ff.png)

### Description 
  - an Object-Oriented programming (OOP) design and implementation of graph library

### Objective
  - familiarize with advanced graph operations and algorithms such as Kosaraju, Kruskal, and Dijkstra algorithm
  - wrtie compact and concise API with the help of object-oriented programming

### Stack
  - Python (jupyter)

### Program Overview

  1. Kosaraju's Algorithm for Strongly Connected Components

  ![img1 daumcdn](https://user-images.githubusercontent.com/35610628/120975276-ff360f00-c7ab-11eb-8507-51fb6df21078.png)
  
  - Kosaraju's Algorithm is a DFS based algorithm used to find Strongly Connected Components in a graph

  Steps <br/>
    1. Traverse through the original graph using DFS <br/>
    2. Reverse the original graph using an adjacency list <br/>
    3. Traverse through the reversed graph using DFS, when DFS-traversal if finisehd, all nodes visited will form SCC <br/>

  2. Kruskal's Algorithm for Minimum Spanning Tree of an Undirected Edge-weighted Graph

  ![image](https://user-images.githubusercontent.com/35610628/120975819-a2872400-c7ac-11eb-8bb1-522f8bf99758.png)
  
  - Kruskal's Algorithm is a greedy algorithm in graph theory as in each step it adds the next lowest-weight edge that will not form a cycle to the minimum spanning forest.

  Steps <br/>
    1. Sort every edges of graph in non-descending order <br/>
    2. Select the smalles edge and check whether it forms a cycle with the spanning tree. If not, include the edge <br/>
    3. Repeat the previous step untill there exists (V-1) edges in the spanning tree <br/>
    
    
   3. Dijkstra's Algorithm for Single-Source Shortest Paths

  ![EKu1v4e](https://user-images.githubusercontent.com/35610628/120976664-82a43000-c7ad-11eb-8e31-4a500248f0dc.png)
  
  - Dijkstra's Algorithm is a dynamic programming algorithm in graph theory for finding the shortest paths between nodes in a graph

  Steps <br/>
    1. Sort every edges of graph in non-descending order <br/>
    2. Select the smalles edge and check whether it forms a cycle with the spanning tree. If not, include the edge <br/>
    3. Repeat the previous step untill there exists (V-1) edges in the spanning tree <br/>
    
    
