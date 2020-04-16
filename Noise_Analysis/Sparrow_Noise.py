import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

# Read data from file 'filename.csv'
# (in the same directory that your python process is based)
data = pd.read_csv("E5_Analysis.csv")
df = pd.DataFrame(data)


#Break out data into amplitude, maximum, height (peak to peak), and minimum dataframes

amp = df.iloc[:,::4]
amp_avg = pd.DataFrame(amp.mean())
amp_avg = amp_avg.melt()
amp_avg.columns = ['electrode','voltage']
print(amp_avg['electrode'])
amp_avg['electrode'] = np.arange(1,62)
# df.insert(1,"temp",blank,True)
max = df.iloc[:,1::4]
max_avg = pd.DataFrame(max.mean())
max_avg = max_avg.melt()
max_avg.columns = ['electrode','voltage']
max_avg['electrode'] = np.arange(1,61)
# df.insert(1,"temp",blank,True)
height = df.iloc[:,2::4]
height_avg = pd.DataFrame(height.mean())
height_avg = height_avg.melt()
height_avg.columns = ['electrode','voltage']
height_avg['electrode'] = np.arange(1,61)
# df.insert(1,"temp",blank,True)
min = df.iloc[:,3::4]
min_avg = pd.DataFrame(min.mean())
min_avg = min_avg.melt()
min_avg.columns = ['electrode','voltage']
min_avg['electrode'] = np.arange(1,61)
# print each subdataframe
# print(amp_avg)
# print(max_avg)
# print(height_avg)
# print(min_avg)

f, axes = plt.subplots(2,2)

g=sns.swarmplot(x=amp_avg['electrode'], y=amp_avg['voltage'], ax=axes[0,0], palette='pastel',)
g.set_title('amplitude')

h=sns.swarmplot(x=max_avg['electrode'], y=max_avg['voltage'], ax=axes[0,1], palette='pastel')
h.set_title('maximum')

i=sns.swarmplot(x=min_avg['electrode'], y=min_avg['voltage'], ax=axes[1,0], palette='pastel')
i.set_title('minimum')
#
j=sns.swarmplot(x=height_avg['electrode'], y=height_avg['voltage'], ax=axes[1,1], palette='pastel')
j.set_title('height')

plt.show()
