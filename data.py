#!/usr/bin/env python3
"""
data.py

Generates weighted compatibility data as per the example at:
http://blogs.sas.com/content/operations/2015/02/06/the-kidney-exchange-problem/

Also generate weighted Erdős–Rényi graph.
"""
import csv

import networkx as nx
import numpy as np


PAIRS_COUNT = 100
MATCH_PROBABILITY = 0.02
MATCH_FILENAME = "weights.csv"


def gen_weights(n=PAIRS_COUNT, p=MATCH_PROBABILITY, filename=MATCH_FILENAME):
    """Generate random matches between pairs."""
    weights = []
    index = 1
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                continue
            if np.random.rand() < p:
                weights.append((index, i, j, np.random.rand()))
                index += 1
    
    return weights


def write_weights(weights):
    if filename:
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(weights)


if __name__ == "__main__":
    weights = gen_weights()
