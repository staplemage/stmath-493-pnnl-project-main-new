import seaborn as sns 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
from Bio.Seq import Seq
sequence = []

#open file 
reader1 = open("depicting twomer sequence.txt")
# read file 
data = reader1.read()
#converter 
def convert_strings_to_floats(input_array):
	output_array = []
	for element in input_array:
		converted_float = float(element)
		output_array.append(converted_float)
	return output_array
input_array = [data]
output_array = convert_strings_to_floats(input_array)
#print array 
print(output_array)
