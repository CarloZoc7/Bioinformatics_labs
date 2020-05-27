"""
Assignment 2: Local alignment
A local alignment approach tries to identify the most similar subsequences that maximize the scoring of their matching parts and the changes needed to transfer one subsequence into the other. The dynamic programming approach tabularizes optimal subsolutions in matrix S, where an entry Si,j represents the maximal similarity score for any local alignment of the (sub)prefixes ax..i with by..j, where x,y>0 are so far unknown and have to be identified via traceback.
To better clarify how local alignment works, take a look here: http://rna.informatik.uni-freiburg.de/Teaching/index.jsp?toolName=Smith-Waterman
Then, write a Python program that given two sequences (passed as first and second argument from command line) and match, mismatch and gap cost (passed as third, fourth, fifth argument from command line).
1. Compute matrix D and output it on the terminal, along with the final alignment score (remember that the maximum value you can have in the matrix is 0!!)
2. Output the final alignment (if two sequences have more than one alignment with the same score, provide one of them)
3. Check your alignment on Freiburg website
4. Local alignment has a lot of concepts similar to global alignment, so you can reuse a lot of code you have previously written for global alignment!
Usage should be something like this:
python local_alignment.py AATCG AACG 1 -1 -2
Output:
Local alignment score: 2.0
[[0. 0. 0. 0. 0.]
[0. 1. 1. 0. 0.]
[0. 1. 2. 0. 0.]
[0. 0. 0. 1. 0.]
[0. 0. 0. 1. 0.]
[0. 0. 0. 0. 2.]]
Final alignment:
AA
||
AA
"""

import pandas as pd
import numpy as np
import sys


if len(sys.argv) < 6:
    print("Error with the number of arguments in command line!\n")
    exit(-1)

sequence_1 = sys.argv[1]
sequence_2 = sys.argv[2]
match = int(sys.argv[3])
mismatch = int(sys.argv[4])
gap = int(sys.argv[5])

n_rows = len(sequence_1) + 1
n_cols = len(sequence_2) + 1

gl_alignment = []

for i in range(n_rows):
    tmp = []
    for j in range(0, n_cols):
        if i == 0:
            tmp.append(0)
        elif j == 0:
            tmp.append(0)
    gl_alignment.append(tmp)

sequence_1 = list(sequence_1)
sequence_2 = list(sequence_2)

print(sequence_1)
print(sequence_2)

gl_alignment = pd.DataFrame(data=gl_alignment)

for i, base_1  in zip(range(1, n_rows), sequence_1):
    for j, base_2 in zip(range(1, n_cols), sequence_2):
            candidates = [0]
            # sim(i-1, j-1) + sim(X,Y)
            if base_1 == base_2:
                candidates.append(gl_alignment.iloc[i-1, j-1] + match)
            else:
                candidates.append(gl_alignment.iloc[i-1, j-1] + mismatch)
            # sim(i-1, j) + gap
            candidates.append(gl_alignment.iloc[i-1, j] + gap)
            # sim(i, j-1) + gap
            candidates.append(gl_alignment.iloc[i, j-1] + gap)

            max_score = max(candidates)

            gl_alignment.iloc[i, j] = max_score

print(gl_alignment)

# alignment scores