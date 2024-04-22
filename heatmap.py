import seaborn as sns 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 

#set data varible 
data = np.random.randint(low=1, high=100, size=(10,10))
#put data into dataframe
data_df = pd.DataFrame(data)
#print dataframe
print("data_df print")
print(data_df)

#put dataframe into seaborn heatmap
sns.heatmap(data=data_df, annot=True, fmt="d", cmap = "spring")
#show heatmap
plt.show()