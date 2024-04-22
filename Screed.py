import screed #python library for readting FASTA and FASQ file formats
with screed.open("C:\\Users\\Tammy\\OneDrive\\Desktop\\salmonella\\ncbi_dataset\\data\\GCF_000006945.2\\GCF_0000069452_ASM694v2_genomic.fna") as seqfile:
    for read in seqfile:
        seq = read.sequence
        #name = read.name
        #print(name) #prints the name of each bacteria in the file
        #print("length: ", len(seq))

#does not take the titles out
def readFastaFile(inputfile):
    """
    Reads and returns file as FASTA format with special characters removed.
    """
    with screed.open(inputfile) as seqfile:
        for read in seqfile:
            seq = read.sequence
    return seq

den1 = readFastaFile("C:\\Users\\Tammy\\OneDrive\\Desktop\\salmonella\\ncbi_dataset\\data\\GCF_000006945.2\\GCF_0000069452_ASM694v2_genomic.fna")

#function to count the bases
def count_base(seq):
    base_counts = {}
    for base in seq:
        if base in base_counts:
            base_counts[base] += 1
        else:
            base_counts[base] = 1
    return base_counts

count = count_base(den1)
print("bases:", count)

#takes the number g and number of c and add them together and then devided by the len(seq)
def calculate_gc_content(seq):
    """
    Take DNA sequence as input and calculate the GC content.
    """
    no_of_g = seq.count("G")
    no_of_c = seq.count("C")
    total = no_of_g + no_of_c
    gc = total / len(seq) * 100

    return gc

gc_content = calculate_gc_content(den1)
print("GC content: ", gc_content)

#builds K-mers
def build_kmers(sequence, ksize):
    kmers = []
    n_kmers = len(sequence) - ksize + 1

    for i in range(n_kmers):
        kmer = sequence[i:i + ksize]
        kmers.append(kmer)

    return kmers

# Dimer
km2 = build_kmers(den1, 2)

#count dimer
from collections import Counter
dimer = Counter(km2)
print("dimer:", dimer)

# Trimer
km3 = build_kmers(seq, 3)

# Count trimer
trimer = Counter(km3)
print(trimer)
