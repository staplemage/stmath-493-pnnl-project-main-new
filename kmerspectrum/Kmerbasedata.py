import matplotlib.pyplot as plt
import numpy as np
from Bio import SeqIO
#This is the code for generating a python function k_mer_frequency which will return the frequencies and frequency counts (multiplicity)
def k_mer_frequency(seq, k):
    L: int = len(seq)
    frequencies = {}
    # iterate over the number of k-mers in seq
    for n in range(L - k + 1):
        kmer: str = seq[n:n+k]
        frequencies[kmer] = frequencies.get(kmer, 0) + 1
    # Count how many times each frequency occurs
    frequency_counts = {}
    for frequency in frequencies.values():
        frequency_counts[frequency] = frequency_counts.get(frequency, 0) + 1
    return frequency_counts

# this is the code to open the file 1 and pass the inputs of sequence to above python function
with open("/Users/sony/Downloads/kmerplots/GCF_000007805.1_ASM780v1_genomic.fna") as handle1:
    for record in SeqIO.parse(handle1, "fasta"):
        print(record.seq)
sequence1: str = record.seq
k_value_1 = 7
result1 = k_mer_frequency(sequence1, k_value_1)

# this is the code to open the file 2 and pass the inputs of sequence to above python function
with open("/Users/sony/Downloads/kmerplots/GCF_000026105.1_ASM2610v1_genomic.fna") as handle2:
    for record in SeqIO.parse(handle2, "fasta"):
        print(record.seq)
sequence2: str = record.seq
k_value_2 = 7
result2 = k_mer_frequency(sequence2, k_value_2)

colors1 = np.random.rand(30)
colors2 = np.random.rand(1803)

x1 = list(result1.keys())
y1 = list(result1.values())

x2 = list(result2.keys())
y2 = list(result2.values())
#for y in y2:
#    print(y, end=",")

#44-47 and 51-52 line code is for generating a single one view graph to compare 2 files
#fig = plt.figure()
#ax1 = fig.add_subplot(111)
#ax1.scatter(x1, y1, c='b', marker="s", label='pseudomonas syringae')
#ax1.scatter(x2, y2, c='r', marker="o", label='pseudomonas entomophila')

# lines 50-54 and 57 and 59-64 are for generating two separate k-mer spectrums one for each file
plt.scatter(x1, y1, c=colors1)
plt.colorbar()
plt.xlabel('Frequency1')
plt.ylabel('Repetition1')
plt.title('pseudomonas syringae Frequency vs Repetition of k-mers'+ " " + str(k_value_1))
plt.title('pseudomonas entomophila vs pseudomonas syringae'+ " " + str(k_value_2) +'-mer spectrum')
plt.legend(loc='upper left')
plt.show()

plt.scatter(x2, y2, c=colors2)
plt.colorbar()
plt.xlabel('Frequency')
plt.ylabel('Repetition')
plt.title('pseudomonas entomophila Frequency vs Repetition of k-mers'+ " " + str(k_value_2))
plt.show()





