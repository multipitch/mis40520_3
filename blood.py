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
import random

import numpy as np
import pandas as pd


PAIRS_REQUIRED = 1000
FILENAME = "pairs.csv"
TYPES = ["O", "A", "B", "AB"]
PREVALENCE = [0.55, 0.31, 0.11, 0.03]
COMPATIBILITY = pd.DataFrame([[1, 1, 1, 1],
                              [0, 1, 0, 1],
                              [0, 0, 1, 1],
                              [0, 0, 0, 1]], index=TYPES, columns=TYPES)


def generate_pairs(types=TYPES, prevalence=PREVALENCE,
                   compatibility=COMPATIBILITY, pairs_required=PAIRS_REQUIRED,
                   filename=FILENAME):
    """Generate incompatible donor-recipient pairs."""
    pairs = []
    while len(pairs) < pairs_required:
        donor, recipient = np.random.choice(types, 2, prevalence)
        if not compatibility.loc[donor, recipient]:
            pairs.append((donor, recipient))
    if filename:
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(pairs)
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
        print("\ndonor\\recipient pairs:")
        print(pairs_summary.to_string())
        print("\ndonors:")
        print(donors_summary.to_string())
        print("\nrecipients:")
        print(recipients_summary.to_string())
    return pairs_summary, donors_summary, recipients_summary


if __name__ == "__main__":  
    pairs = generate_pairs()
    #pairs = generate_pairs(filename=None)
    p, d, r = stats(pairs)
