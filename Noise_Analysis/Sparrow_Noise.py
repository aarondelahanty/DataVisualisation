import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

# Read data from file 'filename.csv'
# (in the same directory that your python process is based)
data = pd.read_csv("E5_Analysis.csv")
df = pd.DataFrame(data)


#Break out data into amplitude, maximum, height (peak to peak), and minimum datsframes

amp = df.iloc[:,::4]
amp_avg = amp.mean()
amp_avg = amp_avg.transpose()
# df.insert(1,"temp",blank,True)
max = df.iloc[:,1::4]
max_avg = max.mean()
max_avg = max_avg.transpose()
# df.insert(1,"temp",blank,True)
height = df.iloc[:,2::4]
height_avg = height.mean()
height_avg = height_avg.transpose()
# df.insert(1,"temp",blank,True)
min = df.iloc[:,3::4]
min_avg = pd.DataFrame(min.mean())
min_avg = min_avg.melt()
min_avg.columns = ['electrode','voltage']
min_avg['electrode'] = np.arange(1,61)
# print each subdataframe
print(amp_avg)
print(max_avg)
print(height_avg)
print(min_avg)

f, axes = plt.subplots(2,2)

g=sns.swarmplot(x = None, y=amp_avg, ax=axes[0,0], palette='pastel',)
# g.tick_params('x',labelrotation=60)

h=sns.swarmplot(x = None, y=max.mean(),ax=axes[0,1], palette='pastel')
# h.tick_params('x',labelrotation=60)
#
i=sns.swarmplot(x=[""]*len(min_avg), y=min_avg['voltage'],ax=axes[1,0], palette='Blues', hue = min_avg['electrode'])
# i.tick_params('x',labelrotation=60)
#
j=sns.swarmplot(x = None, y=height.mean(),ax=axes[1,1], palette='pastel')
# j.tick_params('x',labelrotation=60)

plt.show()
