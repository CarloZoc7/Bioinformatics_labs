"""
Assignment 1: Random fasta file generator
Write a python program that generates a fasta file containing reads with the following characteristics:
-Read id is in the following format: >read_id_X where X is a progressive number starting from 0.
-Sequences have length 50 bp
-Bases are randomly generated using a A,T,C,G alphabet, but probability of each base for each read should be given from the command line as a set of numbers (probA, probT, probC, probG)
- The number of reads should be passed as an argument from the command line
-The name of the fasta file should be passed as an argument from the command line
Example:
python read_generator simulatedfasta.fa 100 30 30 30 10
"""
import numpy as np
import sys


if len(sys.argv) != 7:
    print('Error with the number of arguments! \n')
    exit(-1)

name_file = sys.argv[1]
numReads = int(sys.argv[2])
probA = int(sys.argv[3])/100
probT = int(sys.argv[4])/100
probC = int(sys.argv[5])/100
probG = int(sys.argv[6])/100

with open(name_file, 'w') as f:
    sequence = ''
    for i in range(0, numReads):
        f.write('>read_id_%d\n'%i)
        sequence = np.random.choice(['A', 'T', 'C', 'G'], 50, p=[probA, probT, probC, probG])
        sequence = ''.join([element for element in sequence])
        sequence = sequence + '\n'
        f.write(sequence)

print('Program finish with success! \n')