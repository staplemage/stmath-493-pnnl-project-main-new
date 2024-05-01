from Bio.Seq import Seq
import os
import glob
import pathlib
import pickle
import numpy as np

twomers = ["AT", "AC", "AG", "AA", "TA", "TC", "TG", "TT", "CA", "CT", "CG", "CC", "GA", "GT", "GC", "GG"]

def main():
    winDir = "C:\\Users\\patri\\Downloads\\PNNL data\\Bacillus\\testing data"
    linDir = "/home/nprince/Downloads/_From Purvine, Emilie/escherichia"
    
    fullFiles = []
    strainLengths = []
    for root, dirs, files in os.walk(winDir):
        for file in files:
            if file.endswith(".fna"):
                fullFiles.append(os.path.join(root, file))
    print(fullFiles)
    print(len(fullFiles))

    bigList = []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
    for files in fullFiles:
        sequence = []
        count = 0
        reading = open(files)
        # print("SEE ME:" + files)
        seq = Seq(reading.read())
        # print(len(seq))
        hold = []
        for i in range(len(seq) - 2):
            if (count % 4096 == 0 and count > 0):
                # print(len(sequence))
                bigList.append(sequence)
                hold = sequence[(len(sequence) - 128):]
                sequence = []
                sequence = hold
                count += 128
            if seq[i:i+2] in twomers:
                checker = seq[i:i+2]
                sequence.append(twomers.index(checker))
                count += 1
        

    # print(str(bigList))
    f = open("bigListofSeq.txt", "wb") # look into numpy, writeto, readfrom
    pickle.dump(bigList, f)
    print("Done")
    f.close()
    # listToPrint = []

    # need to implement separation into training data and test data, need to take some of them for training and test files 
    # (90% for data, 10% for testing, do that in a way which has some pseudomonas, some in test set) 
    # when creating all the data, save big list with actual heatmaps, and save big list with labels to go with each of them (number each bacteria, for example)
    # look into python path tokenizer
    # redo my file organization, keep log of sorted files, bigList must have parallel list of integer values
main()