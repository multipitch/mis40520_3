#!/usr/bin/env python3
"""
results.py

Analysis of results from mosel model "kidney.mos"
Generates a plot showing donation chains.
"""
import csv

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


WEIGHTS_FILE = "weights.csv"
MATCHES_FILE = "matches.csv"


def csv_to_list(filename, delimiter=",", header=False):
    """Read contents of a csv file and return as a list of tuples."""
    with open(filename, "r") as f:
        reader = csv.reader(f, delimiter=delimiter)
        if header: return list(reader)[1:]   
        return list(reader)


# Get data from input and output files
raw_weights = csv_to_list(WEIGHTS_FILE)
raw_matches = csv_to_list(MATCHES_FILE, delimiter="\t", header=True)

# Compile an edgelist
edgelist = []
for line in raw_weights:
    edgelist.append((int(line[1]), int(line[2]), float(line[3])))

# Generate a graph from the results
G = nx.DiGraph()
G.add_weighted_edges_from(edgelist)
nx.set_edge_attributes(G, 'matching', 0)
nx.set_node_attributes(G, 'matching', 0)
matches = []
ec = [] # Edge colours for plot
for line in raw_matches:
    u = int(line[0])
    v = int(line[1])
    m = int(line[2])
    matches.append((u, v, m))
    ec.append(m)
    G[u][v]['matching'] = m
    G.node[u]['matching'] = m


# Define node colours and labels for plot
nc = []
labels = {}
for n in G.nodes():
    color = None
    for m in matches:
        if m[0] == n:
            color = m[2]
            labels[m[0]] = m[0]
            break
    nc.append(color)

# Plot results
layout = nx.spring_layout(G)
n1 = nx.draw_networkx_nodes(G, layout, node_size=20, cmap=plt.get_cmap("jet"),
                            node_color="gray")
n1.set_edgecolor("gray")
n2 = nx.draw_networkx_nodes(G, layout, node_size=400,
                            cmap=plt.get_cmap("jet"), node_color=nc)
n2.set_edgecolor("black")

nx.draw_networkx_edges(G, pos=layout, edge_color="gray", width=1,
                       arrows=False)
nx.draw_networkx_edges(G, pos=layout, edgelist=matches, width=3,
                       cmap=plt.get_cmap("jet"), edge_color=ec,
                       arrows=False)
nx.draw_networkx_labels(G, layout, labels)
plt.tick_params(top="off", bottom="off", left="off", right="off",
                labelleft="off",labelbottom="off")
plt.axis=("off")
plt.tight_layout()
plt.savefig("plot.pdf", format="pdf")

