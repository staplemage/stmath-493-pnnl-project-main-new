import seaborn as sns 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
from Bio.Seq import Seq
from array import array
sequence = []
output_array = []

#string to float method
def convert_strings_to_floats(data):
    output_array = []
    for element in data:
        converted_float = float(element)
        output_array.append(converted_float)
    return output_array

def main():
    #reader
<<<<<<< HEAD
    reader1 = open("C:\\Users\\patri\\Desktop\\school etc\\PNNL Project\\stmath-493-pnnl-project\\GCF_000026105.1_ASM2610v1_genomic_sorted_p_and_p")
=======

    reader1 = open("pseudomonas aeruginosa.txt")

>>>>>>> d3febb0ec2c4002f7e0af512b822462489da3eb1
    #data reader 
    input = reader1.read()
    data = input.split(',')
    output_array = convert_strings_to_floats(data)
    res = np.array(output_array)
    res = res[0:20*20]
    data_df = pd.DataFrame(res.reshape(20,20))
    print(data_df)
    #produce heatmap

    sns.heatmap(data_df, annot=True)
    #plt.show()
    plt.savefig("Plot_1.png")

    sns.heatmap(data_df, annot=True, cmap="spring")
    #plt.show()
    plt.savefig("pseudomonas entomophila pp")
main()


