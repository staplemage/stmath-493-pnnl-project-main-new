from Bio.Seq import Seq

twomers = ["AT", "AC", "AG", "AA", "TA", "TC", "TG", "TT", "CA", "CT", "CG", "CC", "GA", "GT", "GC", "GG"]
twomer_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def main():
    #forms sequences from FASFA/text files
    reading1 = open("C:\\Users\\patri\\Desktop\\school etc\\PNNL Project\\stmath-493-pnnl-project\\usable complete sequences\\Pseudomonas\\aeruginosa\\GCF_000006765.1_ASM676v1_genomic.fna")
    seq1 = Seq(reading1.read())
    print("The length of the first sequence is", len(seq1))

    reading2 = open("C:\\Users\\patri\\Desktop\\school etc\\PNNL Project\\stmath-493-pnnl-project\\usable complete sequences\\Pseudomonas\\syringae\\GCF_000007805.1_ASM780v1_genomic.fna")
    seq2 = Seq(reading2.read())
    print("The length of the second sequence is", len(seq2))

    # print(len(seq1))

    #establishes overlap variable
    overlap = 0


    # for loop comparison between two different strands
    for i in range(400):#len(seq1) - 2):
        #takes two adjacent nucleotides from strands
        checker1 = seq1[i:i+2]
        checker2 = seq2[i:i+2]
        #print(checker1)
        if (checker1 == checker2):
            overlap += 1 # logs the overlap between twomers
            switch(checker1) # runs switch to determine which matches the matching twomers to arrays
    print("The overlap of twomers in the same position is of count: ", overlap)
    for i in range(0,16):
        print(twomers[i], ": ", twomer_count[i])
    accuracy = (overlap / 400) * 100 #len(seq1)) * 100
    print("Percentage match: ", format(accuracy, ".2f"), "%")
def switch(input):
    if input == "AT":
        twomer_count[0] += 1
    elif input == "AC":
        twomer_count[1] += 1
    elif input == "AG":
        twomer_count[2] += 1
    elif input == "AA":
        twomer_count[3] += 1
    elif input == "TA":
        twomer_count[4] += 1
    elif input == "TC":
        twomer_count[5] += 1
    elif input == "TG":
        twomer_count[6] += 1
    elif input == "TT":
        twomer_count[7] += 1
    elif input == "CA":
        twomer_count[8] += 1
    elif input == "CT":
        twomer_count[9] += 1
    elif input == "CG":
        twomer_count[10] += 1
    elif input == "CC":
        twomer_count[11] += 1
    elif input == "GA":
        twomer_count[12] += 1
    elif input == "GT":
        twomer_count[13] += 1
    elif input == "GC":
        twomer_count[14] += 1
    elif input == "GG":
        twomer_count[15] += 1


main()