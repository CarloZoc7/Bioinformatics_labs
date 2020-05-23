"""
Assignment 3: Fasta comparison
Write a python program to compare two fasta files. The two fasta files are passed as first and second argument from the
command line.
The two fasta files have the following characteristics:
-The fasta format of the two files is correct (no need to check the format)
-Each read takes up a single line
-Each input file does not contain duplicated reads (i.e. identical reads)
The program must write as output a third fasta file containing only the reads that are in common between the input
files. The read ids in the output file should be composed by the read id of the first file concatenated with the read id
 of the second file.
"""

import sys

if len(sys.argv) != 4:
    print('Error number of parameters!')
    exit(-1)

file_1 = sys.argv[1]
file_2 = sys.argv[2]
file_out = sys.argv[3]

f1 = open(file_1, 'r')
f2 = open(file_2, 'r')
f_out = open(file_out, 'w')

list_f1 = list()
list_f2 = list()

for line_f1, line_f2 in zip(f1, f2):
    if line_f1.startswith('>') is False:
        list_f1.append(line_f1)
        list_f2.append(line_f2)


for i, line_f1 in enumerate(list_f1):
    for j, line_f2 in enumerate(list_f2):
        if line_f1 == line_f2:
                f_out.write('>read_id_{:d} - read_id_{:d}\n'.format(i+1, j+1))

f1.close()
f2.close()
f_out.close()
