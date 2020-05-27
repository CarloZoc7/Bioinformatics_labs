"""
After implementing a simplified form of global and local alignment, let's now try to use BWA, a widespread alignment
tool and practice with its output formats.
Before proceeding with this assignment, follow the instructions in the LAB2_Tips file to install the tool and download
reference files for chromosome 10 and chromosome 18.
Remember to download mate_1.fq and mate_2.fq files from the Teaching Portal.

BWA
1. Create a bwa index for the reference sequence (chr10 and chr18). This process requires some minutes to be performed.
Remember that indexing must be performed just once, when you have a new sample from the same species to process you can
start directly from step 2.
mkdir path_to_folder_where_BWA_index_will_be_created
bwa index -p path_to_folder_where_BWA_index_will_be_created path_to_reference_sequence/reference_chr10_chr18.fa
2. Perform the alignment of mate_1.fq and mate_2.fq
bwa mem path_to_folder_where_BWA_index_has_been_created path_to_reads_file/mate_1.fq path_to_reads_file/mate_2.fq > path_to_place_results/results.sam
"""