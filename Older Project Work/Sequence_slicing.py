from Bio import SeqIO
import screed
lacto_amy = SeqIO.parse(r"C:\Users\Tammy\OneDrive - UW\STMATH 493\_From Purvine, Emilie\unzipped\lactobacillus\ncbi_dataset\data\GCF_000194115.1\GCF_000194115.1_ASM19411v1_genomic.fna","fasta")
lacto_acid = SeqIO.parse(r"C:\Users\Tammy\OneDrive - UW\STMATH 493\_From Purvine, Emilie\unzipped\lactobacillus\ncbi_dataset\data\GCF_000389675.2\GCF_000389675.2_ASM38967v2_genomic.fna","fasta")
pseu_syr = SeqIO.parse(r"C:\Users\Tammy\OneDrive - UW\STMATH 493\_From Purvine, Emilie\unzipped\pseudomonas\ncbi_dataset\data\GCF_000007805.1\GCF_000007805.1_ASM780v1_genomic.fna","fasta")
pseu_ent = SeqIO.parse(r"C:\Users\Tammy\OneDrive - UW\STMATH 493\_From Purvine, Emilie\unzipped\pseudomonas\ncbi_dataset\data\GCF_000026105.1\GCF_000026105.1_ASM2610v1_genomic.fna","fasta")
#iterators
lacto_amy_iterator = lacto_amy
first_lacto_amy = next(lacto_amy_iterator)

lacto_acid_iterator = lacto_acid
first_lacto_acid = next(lacto_acid_iterator)

pseu_syr_iterator = pseu_syr
first_pseu_syr = next(pseu_syr_iterator)

pseu_ent_iterator = pseu_ent
first_pseu_ent = next(pseu_ent_iterator)

#function for slicing sequences from 0 to N
def seq_slicing(seq,N):
    seq = seq[0:N]
    return seq

#prints out the first 400 characters of the sequence
ad_lacto_amy = seq_slicing(first_lacto_amy,400)
ad_lactor_acid = seq_slicing(first_lacto_acid,400)
#exporting adjusted files
#SeqIO.write(adjusted,"adjusted.fna","fasta")
#adjusted = SeqIO.parse("C:\\Users\\Tammy\\OneDrive\\Desktop\\salmonella\\ncbi_dataset\\data\\GCF_000006945.2\\GCF_0000069452_ASM694v2_genomic.fna","fasta")


def calculate_gc_content(seq):
    """
    Take DNA sequence as input and calculate the GC content.
    """
    no_of_g = seq.count("G")
    no_of_c = seq.count("C")
    total = no_of_g + no_of_c
    gc = total / len(seq) * 100

    return gc


def calculate_at_content(seq):
    """
    Take DNA sequence as input and calculate the GC content.
    """
    no_of_a = seq.count("A")
    no_of_t = seq.count("T")
    total = no_of_a + no_of_t
    at = total / len(seq) * 100

    return at

#gc/at results
print("lacto_amy at", calculate_at_content(ad_lacto_amy))
print("lacto_amy gc",calculate_gc_content(ad_lacto_amy))
print("lacto_acid at",calculate_at_content(ad_lactor_acid))
print("lacto_acid gc",calculate_gc_content(ad_lactor_acid))

#calculate purine
def count_purine(seq):
    no_of_a = seq.count("A")
    no_of_g = seq.count("G")
    total = no_of_a + no_of_g
    purine = total/len(seq)*100
    return purine

def count_pyrimidine(seq):
    no_of_c = seq.count("C")
    no_of_t = seq.count("T")
    total = no_of_c + no_of_t
    pyrimidine = total/len(seq)*100
    return pyrimidine

#result for purine nad pyrimidine
print("lacto amy purine", count_purine(ad_lacto_amy))
print("lacto amy pyrimidine", count_pyrimidine(ad_lacto_amy))
print("lacto acid purine", count_purine(ad_lactor_acid))
print("lacto acid pyrimidine", count_pyrimidine(ad_lactor_acid))
print("pseu_syr purine ",count_purine(first_pseu_syr))
print("pseu_syr pyrimidine ",count_pyrimidine(first_pseu_syr))
print("pseu_ent purine ",count_purine(first_pseu_ent))
print("pseu_ent pyrimidine ",count_pyrimidine(first_pseu_ent))

def build_kmers(sequence, ksize):
    kmers = []
    n_kmers = len(sequence) - ksize + 1

    for i in range(n_kmers):
        kmer = sequence[i:i + ksize]
        kmers.append(kmer)

    return kmers

dimer_acid = build_kmers(ad_lactor_acid.seq,2)

from collections import Counter
dimer = Counter(dimer_acid)
