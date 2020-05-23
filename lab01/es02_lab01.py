"""
Assignment 2: Statistics extraction
Write a python program for extracting statistics from fasta files. The program must take as first argument from the
command line the name of the input fasta file to be analyzed and write to an output text file (whose name is passed as
second argument from the command line) a summary of the computed statistics.
The following are the expected output statistics:
-Statistics of single bases across all the reads: Number of A,T,C,G
-Number of reads having at least one low complexity sequence: AAAAAA, TTTTTT, CCCCCC or GGGGGG.
- Number of reads having a number of GC couples (so called GC content) higher than a threshold GC_THRESHOLD passed as
third argument from the command line
-For each read having a GC content higher than GC_THRESHOLD, report its read_id and the number of GC couples
"""

import sys

if len(sys.argv) != 4:
    print('Error number of parameters!')
    exit(-1)

file_in = sys.argv[1]
file_out = sys.argv[2]
threshold_GC = int(sys.argv[3])

count_A = 0
count_C = 0
count_G = 0
count_T = 0

count_low_complexity = 0

count_GC = 0

f_in = open(file_in, 'r')
f_out = open(file_out, 'w')

for i, lines in enumerate(f_in):
    if lines.startswith('>') is False:
        for i in range(0, len(lines)):
            element = lines[i]
            if element == 'A':
                count_A = count_A + 1
            if element == 'C':
                count_C = count_C + 1
            if element == 'T':
                count_T = count_T + 1
            if element == 'G':
                count_G = count_G + 1

        for str_low in ['AAAAA', 'TTTTTT', 'CCCCCC', 'GGGGGG']:
            check = lines.find(str_low)
            if check > -1:
                count_low_complexity = count_low_complexity + 1


        for j in range(0, len(lines)-1):
            couple_elements = lines[j] + lines[j+1]
            if couple_elements == 'GC':
                    count_GC = count_GC + 1

        if count_GC >= threshold_GC:
            f_out.write('>read_is_{:d} contains GC {:d} reads \n'.format(i, count_GC))
        count_GC = 0

f_out.write('Number of low complexity %d \n' % count_low_complexity)
f_out.write('Number of A %d \n' % count_A)
f_out.write('Number of C %d \n' % count_C)
f_out.write('Number of G %d \n' % count_G)
f_out.write('Number of T %d \n' % count_T)

f_in.close()
f_out.close()

print('End program with success!')