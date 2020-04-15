import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

# Read data from file 'filename.csv'
# (in the same directory that your python process is based)
data = pd.read_csv("E5_Analysis.csv")
df = pd.DataFrame(data)

#extract each feautre as patial dataframe
#Generate blank array for inserting temperary column
blank = np.zeros(15)

#Break out data into amplitude, maximum, height (peak to peak), and minimum datsframes

amp = df.iloc[:,::4]
df.insert(1,"temp",blank,True)
max = df.iloc[:,::4]
df.insert(1,"temp",blank,True)
height = df.iloc[:,::4]
df.insert(1,"temp",blank,True)
min = df.iloc[:,::4]

# print time average
print(amp.mean())
print(max.mean())
print(height.mean())
print(min.mean())



#g=sns.swarmplot(x=data[0,:],y=data[1,:],palette='pastel')
#g.tick_params('x',labelrotation=60)
#plt.show(g)
