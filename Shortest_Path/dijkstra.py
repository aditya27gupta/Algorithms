"""
Dijkshtra's Algorithm:
    Set initial distances for all vertices: 0 for the source vertex, and infinity for all the other.
    Choose the unvisited vertex with the shortest distance from the start to be the current vertex. So the algorithm will always start with the source as the current vertex.
    For each of the current vertex's unvisited neighbor vertices, calculate the distance from the source and update the distance if the new, calculated, distance is lower.
    We are now done with the current vertex, so we mark it as visited. A visited vertex is not checked again.
    Go back to step 2 to choose a new current vertex, and keep repeating these steps until all vertices are visited.
    In the end we are left with the shortest path from the source vertex to every other vertex in the graph.
"""
