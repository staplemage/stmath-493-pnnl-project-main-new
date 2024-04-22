from Bio.Seq import Seq

def main():
    # size of chunks to read each DNA file
    CHUNK_SIZE = 1
    # checks for whether program runs!
    print("Testing!")
    print("Must Print!")

    similarityScores = []

    reader1 = open("D:\PycharmProjects\stmath-493-pnnl-project\dna1.txt")
    reader2 = open("D:\PycharmProjects\stmath-493-pnnl-project\dna2.txt")
    read1 = reader1.read()
    read2 = reader2.read()

    buffer1 = chr(CHUNK_SIZE)
    buffer2 = chr(CHUNK_SIZE)

    extraNucleotides = 0
    isDNA1Longer = read1 > read2

    while True:
        readChars1 = reader1.read(CHUNK_SIZE)
        readChars2 = reader2.read(CHUNK_SIZE)

        if (readChars1 == -1 or readChars2 == -1):
            if (readChars1 == -1):
                extraNucleotides += readChars2
                while ((readChars2 == read2.read(buffer2, 0, CHUNK_SIZE) != -1)):
                    extraNucleotides += 1

            elif (readChars2 == -1):
                extraNucleotides += readChars1
                while ((readChars1 == read1.read(buffer1, 0, CHUNK_SIZE) != -1)):
                    extraNucleotides += 1

            break

        similarity = calculateSimilarity(buffer1, buffer2, min(readChars1, readChars2))
        similarityScores.add(similarity)

        print("Comparing:", buffer1, ", ", readChars1, " with ", buffer2, ", ", readChars2, " - Similarity: ",
              similarity)

        averageSimilarity = calculateAverageSimilarity(similarityScores)
        print("Average similarity: ", averageSimilarity)

        if (extraNucleotides > 0):
            if (isDNA1Longer):
                dnaSequenceWithExtra = "DNA 1"
            else:
                dnaSequenceWithExtra = "DNA 2"
            print(dnaSequenceWithExtra + " has " + extraNucleotides + " extra nucleotides.")


def calculateSimilarity(array1, array2, length):
    matches = 0

    for i in range(0, length):
        if (array1[i] == array2[i]):
            matches += 1
    return matches / length * 100


def calculateAverageSimilarity(similarityScores):
    if (similarityScores == -1 or not similarityScores):
        return 0.0

    totalComparisons = len(similarityScores)
    totalMatches = 0

    for score in similarityScores:
        if (score == 100.0):
            totalMatches += 1

    return totalMatches / totalComparisons * 100

main()