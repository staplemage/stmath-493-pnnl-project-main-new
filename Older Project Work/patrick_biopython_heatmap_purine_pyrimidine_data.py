from Bio.Seq import Seq

twomers = ["AT", "AC", "AG", "AA", "TA", "TC", "TG", "TT", "CA", "CT", "CG", "CC", "GA", "GT", "GC", "GG"]
twomer_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
sequence = []

def main():
    #forms sequences from FASFA/text files
    reading = open("GCF_000026105.1_ASM2610v1_genomic.fna")
    seq = Seq(reading.read())
    global sequence

    # for loop comparison between two different strands
    for i in range(len(seq) - 2):
        #takes two adjacent nucleotides from strands
        checker = seq[i:i+2]
        switch(checker) # runs switch to determine which matches the matching twomers to arrays
        #print(checker)

    for i in range(0,16): # prints results out
        print(twomers[i], ": ", twomer_count[i])
    
    # bubble_sort(sequence)
    # print(sequence)
    f = open("GCF_000026105.1_ASM2610v1_genomic_sorted_p_and_p", "x")
    f.write(str(sequence[0]))
    for i in range(1, len(sequence)):
        f.write(", ")
        f.write(str(sequence[i]))
    f.close()

def switch(input): # artificial switch statement given lack of switch in python
    if input == "AT":
        sequence.append(1)
        twomer_count[0] += 1
    elif input == "AC":
        sequence.append(45)
        twomer_count[1] += 1
    elif input == "AG":
        sequence.append(45)
        twomer_count[2] += 1
    elif input == "AA":
        sequence.append(1)
        twomer_count[3] += 1
    elif input == "TA":
        sequence.append(1)
        twomer_count[4] += 1
    elif input == "TC":
        sequence.append(45)
        twomer_count[5] += 1
    elif input == "TG":
        sequence.append(45)
        twomer_count[6] += 1
    elif input == "TT":
        sequence.append(1)
        twomer_count[7] += 1
    elif input == "CA":
        sequence.append(45)
        twomer_count[8] += 1
    elif input == "CT":
        sequence.append(45)
        twomer_count[9] += 1
    elif input == "CG":
        sequence.append(90)
        twomer_count[10] += 1
    elif input == "CC":
        sequence.append(90)
        twomer_count[11] += 1
    elif input == "GA":
        sequence.append(45)
        twomer_count[12] += 1
    elif input == "GT":
        sequence.append(45)
        twomer_count[13] += 1
    elif input == "GC":
        sequence.append(90)
        twomer_count[14] += 1
    elif input == "GG":
        sequence.append(90)
        twomer_count[15] += 1

def bubble_sort(seq):
    n = len(seq)
    for i in range(n):
        already_sorted = True

        for j in range(n - i - 1):
            if seq[j] < seq[j + 1]:
                seq[j], seq[j + 1] = seq[j + 1], seq[j]
                already_sorted = False
        if already_sorted:
            break
    return seq
main()