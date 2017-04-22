#!/usr/bin/env python
"""
blood.py

Generates random incompatible donor-recipient pairs for kidney donation.
Writes the pairs to a CSV file and prints some statistics to screen.

Classifies according to ABO system only.
Assumes prevalence of blood types as per the following website:
    https://www.giveblood.ie/All_About_Blood/Blood_Group_Basics/
"""
import csv

import numpy as np
import pandas as pd


PAIRS_REQUIRED = 100
FILENAME = "pairs.csv"
TYPES = ["O", "A", "B", "AB"]
PREVALENCE = [0.55, 0.31, 0.11, 0.03]
COMPATIBILITY = pd.DataFrame([[1, 1, 1, 1],
                              [0, 1, 0, 1],
                              [0, 0, 1, 1],
                              [0, 0, 0, 1]], index=TYPES, columns=TYPES)

SIMPLE_PAIRS_P = 0.02 # probability of link existing between a pair


def generate_pairs(types=TYPES, prevalence=PREVALENCE,
                   compatibility=COMPATIBILITY, pairs_required=PAIRS_REQUIRED,
                   filename=FILENAME):
    """Generate incompatible donor-recipient pairs."""
    pairs = []
    
    while len(pairs) < pairs_required:
        donor, recipient = np.random.choice(types, 2, prevalence)
        if not compatibility.loc[donor, recipient]:
            pairs.append((donor, recipient))
            
    if filename: write_lines(pairs, filename)
    
    return pairs


def stats(pairs, types=TYPES, compatibility=COMPATIBILITY, print_stats=True):
    """Generate statistics on pairs list."""
    dim = len(types)
    total = len(pairs)
    pairs_summary = pd.DataFrame(np.zeros((dim, dim)),
                                 index=TYPES, columns=TYPES)
                                 
    for (donor, recipient) in pairs:
        pairs_summary.loc[donor, recipient] += 1
        
    pairs_summary /= total
    donors_summary = np.sum(pairs_summary, axis=0)
    recipients_summary = np.sum(pairs_summary, axis=1)
    
    if print_stats:
        print("\ndonor\\recipient pair frequencies:")
        print(pairs_summary.to_string())
        print("\ndonor frequencies:")
        print(donors_summary.to_string())
        print("\nrecipient frequencies:")
        print(recipients_summary.to_string())
        
    return pairs_summary, donors_summary, recipients_summary


def generate_weighted_matches(n=PAIRS_REQUIRED, p=SIMPLE_PAIRS_P, 
                            filename=FILENAME):
    """Generate random matches between pairs."""
    matches = []
    
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if np.random.rand() < p:
                matches.append((i, j, np.random.rand()))
    
    if filename: write_lines(matches, filename)
    
    return matches


def write_lines(pairs, filename):
    """Write out lines to file in csv format."""
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(pairs)


if __name__ == "__main__":

    print('TEST 1: UNWEIGHTED INCOMPATIBLE PAIR GENERATION BASED ON BLOOD TYPE '
          'PREVALENCE')  
    pairs = generate_pairs()
    #pairs = generate_pairs(filename=None)
    p, d, r = stats(pairs)
    print('\n{} incompatible pairs written to {}'.format(PAIRS_REQUIRED,
                                                       FILENAME))

    print('\n' + '-' * 80)                                                       
    print('TEST 2: WEIGHTED RANDOM INCOMPATIBLE PAIR GENERATION') 
    print('\nnumber of incompatible pairs: {}'.format(PAIRS_REQUIRED))
    fn = "wpairs.csv"
    pairs = generate_weighted_matches(filename=fn)
    print('number of weighted matches: {}'.format(len(pairs)))
    print('\n{} matches written to {}'.format(len(pairs), fn))
