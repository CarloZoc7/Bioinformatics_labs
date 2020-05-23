""""
Assignment 4: Consensus Region
Write a python program that reconstructs the consensus regions on a specific chromosome starting from a tab-separated
file called alignments.txt made up of three columns: the read ID, the sequence of the read and the alignment position
of the read onto the reference genome. An example of alignments.txt is available in the following.
Exploiting the sequence and the alignment position of each read, build the consensus regions on the selected chromosome.
 Please note that all reads have the same length and that multiple consensus regions are allowed for the same chromosome.
"""
import sys
import numpy as np
import pandas as pd

dataset = pd.DataFrame(columns=('Read', 'Start_point'))
tmp = {}
with open('alignments.txt', 'r') as file:

    for i, row in enumerate(file.readlines()):
        data = row.split('\t')
        tmp = {'Read': data[1],
               'Start_point': int(data[2])
               }
        dataset = dataset.append(tmp, ignore_index=True)

dataset.sort_values(by=['Start_point'], inplace=True)
print(dataset)

len_read = len(dataset['Read'][0])
print('Len of reads: ', len_read)

print('\n')
print('First situation:\n')
for i, reads in enumerate(dataset.values):
    if i != 0:
            # stampo n spazi
            space_distance = ''
            for space in range(reads[1]):
                # concateno gli spazi pari a dove inizia il file di lettura
                space_distance = space_distance + ' '
            # stampo il tutto
            print(space_distance + reads[0])
    else:
        # prima lettura
        print(reads[0])

    prec = reads[1]


counter_bases = {}

for i, reads in enumerate(dataset.values):
    if i != 0:
        if prec + len_read >= reads[1]:

            for j, element in enumerate(reads[0]):
               start_read = reads[1]
               #controllo su lunghezza:
               if start_read + j < len(final_genome):
                    key = start_read + j # position is the key

                    # adding element to the list of possible bases
                    if key not in counter_bases.keys():
                        counter_bases[key] = [final_genome[key], element]
                    else:
                        counter_bases[key].append(element)


               else:
                   # aggiungo le rimanenti basi
                   final_genome = final_genome + element

        else:
            distance = ''
            difference = reads[1] - (prec + len_read)
            for i in range(difference):
                distance = distance + ' '
            final_genome = final_genome + distance + reads[0]
    else:
        # prima lettura
        final_genome = reads[0]
    prec = reads[1]

print('RESULT:')

for key in counter_bases.keys():
    bases = counter_bases[key]
    key_bases, counter = np.unique(bases, return_counts=True)

    result_count = pd.DataFrame(index=key_bases, data=counter)
    result_base = result_count.idxmax()

    final_list = list(final_genome)
    final_list[key] = result_base[0]
    final_genome = ''.join(final_list)

print(final_genome)

