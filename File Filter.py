from pathlib import Path
import os

#bacillus = "C:\\Users\\Tammy\\OneDrive - UW\\STMATH 493\\_From Purvine, Emilie\\RefSeq_data\\ncbi_dataset\\data"
#escherichia = r"C:\Users\Tammy\OneDrive - UW\STMATH 493\_From Purvine, Emilie\RefSeq_data\escherichia\ncbi_dataset\data"
#lactobacillus = r"C:\Users\Tammy\OneDrive - UW\STMATH 493\_From Purvine, Emilie\RefSeq_data\lactobacillus\ncbi_dataset\data"
#pseudonomas = r"C:\Users\Tammy\OneDrive - UW\STMATH 493\_From Purvine, Emilie\RefSeq_data\pseudomonas\ncbi_dataset\data"
#samonella = r"C:\Users\Tammy\OneDrive - UW\STMATH 493\_From Purvine, Emilie\RefSeq_data\salmonella\ncbi_dataset\data"
#streptococcus = r"C:\Users\Tammy\OneDrive - UW\STMATH 493\_From Purvine, Emilie\RefSeq_data\Streptococcus\ncbi_dataset\data"

#data = [bacillus,escherichia,lactobacillus,pseudonomas,samonella,streptococcus]

location = r'C:\Users\Tammy\OneDrive - UW\STMATH 493\_From Purvine, Emilie\unzipped'

#stores filenames of complete sequences that are not plasmid or chromosomes
files = []
for i in Path(location).glob('**/*.fna'):
    if "complete" in i.read_text():
        if 'plasmid' and 'chromosome' not in i.read_text():
            files.append(i.name)


print(files)
#print(len(files))