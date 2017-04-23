#!/usr/bin/env python3
"""
results.py

Analysis of results from mosel model "kidney.mos"
"""
import csv

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


WEIGHTS_FILE = "weights.csv"
MATCHES_FILE = "matches.csv"

def csv_to_list(filename, delimiter=',', header=False):
    with open(filename, 'r') as f:
        reader = csv.reader(f, delimiter=delimiter)
        return list(reader)[1:]

raw_weights = csv_to_list(WEIGHTS_FILE)
raw_matches = csv_to_list(MATCHES_FILE, delimiter='\t')

edgelist = []
for line in raw_weights:
    edgelist.append((int(line[1]), int(line[2]), float(line[3])))

matches = []
for line in raw_matches[1:]:
    matches.append((int(line[0]), int(line[1]), int(line[2])))

G = nx.DiGraph()
G.add_weighted_edges_from(edgelist)
nx.set_edge_attributes(G, 'matching', 0)
for match in matches:
    try:
        G[match[0]][match[1]]['matching'] = match[2]    
    except:
        print("Error: Following match not in weighted edge list: {}".format(
            match[0:2]))
    # Something not right here - edges should exist for each match

layout = nx.spring_layout(G)
nodes = nx.draw_networkx_nodes(G, layout)
nodes.set_edgecolor("k")
nx.draw_networkx_edges(G, pos=layout, edge_color='gray')
plt.savefig('plot.pdf', format='pdf')

