"""
Under the assumption that both input sequences a and b stem from the same origin, a global alignment tries to identify
matching parts and the changes needed to transfer one sequence into the other. The changes are scored and an optimal set
 of changes is identified, which defines an alignment. The dynamic programming approach tabularizes optimal subsolutions
  in matrix D, where an entry Di,j represents the best score for aligning the prefixes a1..i with b1..j.
To better clarify how global alignment works, take a look here:
 http://rna.informatik.uni-freiburg.de/Teaching/index.jsp?toolName=Needleman-Wunsch
Then, write a Python program that given two sequences (passed as first and second argument from command line) and match,
mismatch and gap costs (passed as third, fourth, fifth argument from command line):
1. Compute matrix D and output it on the terminal, along with the final alignment score
2. Output the final alignment (if two sequences have more than one alignment with the same score, provide one of them
e.g. check website for ‘AACCG’ and ‘AACG’)
3. Check your alignment on Freiburg website
Usage should be something like this:
python global_alignment.py AACCG AACG 1 -1 -2
Output:
Global alignment score: 2.0 [[ 0. -2. -4. -6. -8.]
                            [ -2. 1. -1. -3. -5.]
                            [ -4. -1. 2. 0. -2.]
                            [ -6. -3. 0. 3. 1.]
                            [ -8. -5. -2. 1. 2.]
                            [-10. -7. -4. -1. 2.]]
Final alignment: AACCG ||| | AAC-G
"""
import numpy as np
import pandas as pd
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

print("match=", match, " mismatch=", mismatch, "gap=", gap)

for i in range(n_rows):
    tmp = []
    tot_i = 0
    tot_j = 0
    for j in range(0, n_cols):
        if i == 0 and j == 0:
            tmp.append(0)
        else:
            if i == 0:
                tot_i = gap * j
                tmp.append(tot_i)
            elif j == 0:
                tot_j = tot_j + gap * i
                tmp.append(tot_j)
    gl_alignment.append(tmp)

sequence_1 = list(sequence_1)
sequence_2 = list(sequence_2)

print(sequence_1)
print(sequence_2)

gl_alignment = pd.DataFrame(data=gl_alignment)

for i, base_1  in zip(range(1, n_rows), sequence_1):
    for j, base_2 in zip(range(1, n_cols), sequence_2):
            candidates = []
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



# show matrix
print(gl_alignment)

# to finish for best alignment score




