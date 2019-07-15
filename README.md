PyAlgorithm version 0.1.2
---------------------------------------------------
Creator: Zihao Liu

Description
---------------------------------------------------
PyAlgorithm is a fun open source project that provides algorithmic library for python >= 2.7. Its goal is to cover as much fundamental algorithms in computer science as possible in Python, and therefore provide easy to use programming tools for application developer or contestants from coding challenge. 

You can find information about both using PyAlgorithm and contributing to the project in the wiki: https://github.com/ZihaoAllen/PyAlgorithm/wiki

Several paradigms currently included are:

- Divide-And-Conquer:
    - Merge sort
    - Count Inversion
    - Integer multiplication
    - Closest points in 2D plane
    - Randomized Quick Sort


- Selection Algorithm
    - Randomized Selection
    - Deterministic Selection


- Graph Algorithm:
    - Graph Representation (Adjacency List)
    - Randomized Contraction Algorithm to find the minimum cut in Undirected Graph
    - Breath First Search
    - Shortest Path without weights on path using Breath First Search
    - Find connected components in undirected graph using Breath First Search
    - Depth First Search
    - Topological sort in DAG using Depth First Search
    - Finding strongest connected components in DAG using Depth First Search
    - Dijkstra's Shortest Path algorithm in directed graph without heap optimization O(mn)
    - Dijkstra's Shortest Path algorithm in directed graph with heap optimization O(mlogn)
        

- Greedy Algorithm:
    - Greedy Scheduling problem
    - MST with Prim's Algorithm (no heap optimization)
    - MST with Prim's Algorithm (heap optimization)
    - MST with Kruskal's Algorithm
    - MST with Kruskal's Algorithm (Union-Find optimization)
    - Greedy k max spacing clustering algorithm
    - Greedy Huffman codes algorithm (heap optimization)

- Dynamic Programming:
    - Weighted Independent Set problem
    - Knapsack Problem

- Utility Data Structure include:
    - Heap:
        - insert a value (O(logN))
        - extract min/max (not simutaneously) (O(logN)
        - remove an element from heap (O(logN) with internal bookkeeping)
    - Union-Find:
        - find(node) find a leader for the node
        - union(component1, component2) merge two component with each other

Requirements
---------------------------------------------------
- Python >= 2.6, Python 3 has not been tested yet


Installation
---------------------------------------------------
Get the source and run
    
    $ python setup.py install
    $ python
    $ >> from PyAlgorithm.Data_Structure import heap
    $ >> h = heap.Heap(True)      # construct a min heap
    $ >> from PyAlgorithm.Graph_Algorithm import graph
    $ >> g = graph.Graph()     # construct a graph

Usage
---------------------------------------------------
    $ from PyAlgorithm.section_name import method_name

Testing
---------------------------------------------------
Go to PyAlgorithm/testing, run 

    $ python data_structure_unittest.py (or other desired test code)

Note that test code for graph is not included right now


Project Wiki
---------------------------------------------------
https://github.com/ZihaoAllen/PyAlgorithm/wiki

License
---------------------------------------------------
PyAlgorithm is distributed under the MIT License. See the bundled LICENSE for more details