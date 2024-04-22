from Bio import SeqIO
filename = "C:\\Users\\ylime\\Downloads\\mtdownload1531_2024.01.09_19.55\\_From Purvine, Emilie\\RefSeq_data\\salmonella\\ncbi_dataset\\data\\GCF_000006945.2\\GCF_000006945.2_ASM694v2_genomic.fna"
sequences = [i for i in SeqIO.parse("C:\\Users\\ylime\\Downloads\\mtdownload1531_2024.01.09_19.55\\_From Purvine, Emilie\\RefSeq_data\\salmonella\\ncbi_dataset\\data\\GCF_000006945.2\\GCF_000006945.2_ASM694v2_genomic.fna","fasta")]
#"C:\\Users\\ylime\\Downloads\\mtdownload1531_2024.01.09_19.55\\_From Purvine, Emilie\\RefSeq_data\\salmonella\\ncbi_dataset\\data\\GCF_000006945.2\\GCF_000006945.2_ASM694v2_genomic.fna"
import numpy as np
#for seq_record in SeqIO.parse("C:\\Users\\ylime\\Downloads\\mtdownload1531_2024.01.09_19.55\\_From Purvine, Emilie\\RefSeq_data\\salmonella\\ncbi_dataset\\data\\GCF_000006945.2\\GCF_000006945.2_ASM694v2_genomic.fna","fasta"):
    #ID = print(seq_record.id) #print record id
    #length = print(len(seq_record)) #length of each sequences

#NC_003197.2 Salmonella enterica
#NC_021870.1 Salmonella bongori
#NC_000913.3 E. coli

data = SeqIO.parse("C:\\Users\\ylime\\Downloads\\mtdownload1531_2024.01.09_19.55\\_From Purvine, Emilie\\RefSeq_data\\salmonella\\ncbi_dataset\\data\\GCF_000006945.2\\GCF_000006945.2_ASM694v2_genomic.fna","fasta")

#prints out the set
record_iterator = data
#first_record = next(record_iterator)
#second_record = next(record_iterator)
#print("first record: ", first_record) #first set
#print("second record: ", second_record) #second set
count = list(SeqIO.parse("C:\\Users\\ylime\\Downloads\\mtdownload1531_2024.01.09_19.55\\_From Purvine, Emilie\\RefSeq_data\\salmonella\\ncbi_dataset\\data\\GCF_000006945.2\\GCF_000006945.2_ASM694v2_genomic.fna","fasta"))

#iterate through sequences
for i in range(0,len(count)):
    #print([i], count[i].description)
    if "complete" in count[i].description:
        #print([i], count[i].description)
        if "plasmid" not in count[i].description:
            print([i], count[i].description)
    else:
        continue

#print(len(count))
#function to count the number of bases in a set
def count_base(seq):
    base_counts = {}
    for base in seq:
        if base in base_counts:
            base_counts[base] += 1
        else:
            base_counts[base] = 1
    return base_counts

#bases count of first record
#first_count = count_base(first_record)
#print("first_base: ", first_count)

#bases count of second record
#second_count = count_base(second_record)
#print("second_base: ", second_count)

#function to count proportion of gc content
def calculate_gc_content(seq):
    """
    Take DNA sequence as input and calculate the GC content.
    """
    no_of_g = seq.count("G")
    no_of_c = seq.count("C")
    total = no_of_g + no_of_c
    gc = total / len(seq) * 100

    return gc

#gc content for first record
#first_gc=calculate_gc_content(first_record)
#print("first gc content: ", first_gc)

#gc content for first record
#second_gc=calculate_gc_content(second_record)
#print("second gc content: ", second_gc)

#function to build k-mers
def build_kmers(sequence, ksize):
    kmers = []
    n_kmers = len(sequence) - ksize + 1

    for i in range(n_kmers):
        kmer = sequence[i:i + ksize]
        kmers.append(kmer)

    return kmers

#2-mers from first record
#km2_1st = build_kmers(first_record, 2)
#2-mers from second record
#km2_2nd = build_kmers(second_record,2)

#count dimer
#from collections import Counter
#dimer_1st = Counter(km2_1st)
#dimer_2nd = Counter(km2_2nd)
#print(dimer_1st)

#extracting sequences of interest in files
seq1 = sequences[0]
print(seq1.name)

gene_of_interest=[]
for sequence in sequences:
    if sequence.name=='NC_003197.2':
        gene_of_interest.append(sequence)

#saving a sequence to an output file
#SeqIO.write(gene_of_interest,"C:\\Users\\Tammy\\OneDrive\\Desktop\\salmonella\\NC_003197.fna",'fasta')
