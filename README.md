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
    
    Steps
      1. Traverse through the original graph using DFS
      2. Reverse the original graph using an adjacency list 
      3. Traverse through the reversed graph using DFS, when DFS-traversal if finisehd, all nodes visited will form SCC

