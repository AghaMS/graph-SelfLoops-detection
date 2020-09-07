#!/usr/bin/env python
# coding: utf-8

# A simple function to detect self-loops in graphs

def Self_Loops(G):
    '''
    Detect self loops in a network
    '''
    bold_start = '\033[1m'
    bold_end   = '\033[0m'
    
    nodes_in_selfloops = []
    for u, v in G.edges():
        if u == v:
            nodes_in_selfloops.append(u)

    if len(nodes_in_selfloops) > 0:
        print(bold_start,"Warning: Graph has self-loops. The nodes with self loops are:",bold_end, nodes_in_selfloops)
 
