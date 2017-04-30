# mis40520_3
Assignment 3

data.py
Creates a random set of weighted compatibility data and outputs to a csv file.
Written in python3.
Can be run from the terminal as follows:
$ ./data.py
or
$ python3 data.py


kidney.mos
Solves the kidney exchange problem, reading in 'weights.csv' and generating
a set of matched pairs, 'matches.csv'.
Written in mosel.
To run from the terminal, run e.g.:
$ mosel kidney.mos # run with default options
$ mosel kidney.mos fin='myinput.csv' fout='myoutput.csv' L = 123 # customised

makefile
Runs the chain data.py > kidney.mos > results.py (run 'make' from the terminal).
Can also be used to clean the working directory (run 'make clean').
For GNU/Linux only.

results.py
Reads in from 'weights.csv' and 'matches.csv' and creates a simple plot
using networkx and matplotlib.  Also generated .gexf files that can be read
by Gephi, which is used to generate more detailed plots.
The output file 'results.gexf' contains the edge weights and matchinhgs.
The output file 'results_reweighted.gexf' changes the edge weights so a single,
low weight value is used for unused edges and a single, high weight value is
used for edges in matchings - this aids plot clarity in Gephi.
Written in python3.
Can be run from the terminal as follows:
$ ./results.py
or
$ python3 results.py

