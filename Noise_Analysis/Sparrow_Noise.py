import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

# Read data from file 'filename.csv'
# (in the same directory that your python process is based)
data = pd.read_csv("N4_Analysis.csv")
df = pd.DataFrame(data)

#define electrode sizes (are in square um), need to confirm reference sizes
ref = 200 * 50
large = 11 * 11
med = 7 * 7
small = 3.5 * 2.5

#Break out data into amplitude, maximum, height (peak to peak), and minimum dataframes

amp = df.iloc[:,::4]
amp_time = df.iloc[:,0:2]
amp_time.columns = ['time', 'voltage']
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
# Electrodes are numbered in visual reading order of MC_Rack layout top left to bottom right
height_avg['size'] = [ref,ref,ref,med,med,med,med,ref,ref,med,med,med,med,ref,large,large,large,large,large,large,large,large,large,large,large,large,large,large,large,large,ref,ref,ref,small,small,small,small,ref,ref,small,small,small,small,ref,small,small,small,small,small,small,small,small,small,small,small,small,small,small,small,small]
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


## 4 Panel plot, ultimately I think only
# f, axes = plt.subplots(2,2)
#
# g=sns.swarmplot(x=amp_avg['electrode'], y=amp_avg['voltage'], ax=axes[0,0], palette='pastel',)
# g.set_title('amplitude')
#
# h=sns.swarmplot(x=max_avg['electrode'], y=max_avg['voltage'], ax=axes[0,1], palette='pastel')
# h.set_title('maximum')
#
# i=sns.swarmplot(x=min_avg['electrode'], y=min_avg['voltage'], ax=axes[1,0], palette='pastel')
# i.set_title('minimum')
# #
# j=sns.swarmplot(x=height_avg['electrode'], y=height_avg['voltage'], ax=axes[1,1], palette='pastel')
# j.set_title('height')
# plt.show()


#Single plot of main plot of interest, peak to peak
# Threshold in uV
threshold = 100

k=sns.swarmplot(x=height_avg['size'], y=height_avg['voltage'], palette='pastel', hue = height_avg['size'])
k.set(xticks = [], title = 'Time Averaged Peak to Peak Amplitude',xlabel = "Electrode Area", ylabel = "Recorded Voltage [uV]")
# k.legend_.remove()
#k.axhline(threshold)
k.legend_.set_title('Electrode Area [um$^2$]')

# Add data labels (for readabiltiy only add electode ID if above voltage threshold)

def label_point(x, y, val, ax):
    xplot = 0
    a = pd.concat({'x': x, 'y': y, 'val': val}, axis=1)
    for i, point in a.iterrows():
        #need to convert x-position to swarm bin for plotting
        if x[i] <= small:
            xplot = 0
        elif x[i] <= med:
            xplot = 1
        elif x[i] <= large:
            xplot = 2
        else:
            xplot = 3
        if y[i] > threshold:
            k.text(xplot, point['y'], int(point['val']))
            print("Electrode number", int(point['val']), "exceeds ", threshold, "uV threshold")

label_point(height_avg['size'], height_avg['voltage'],height_avg['electrode'], plt.gca())
plt.show()

#Plot looking at time stabilisation
print(amp_time)
l = sns.scatterplot(x = amp_time["time"], y= amp_time["voltage"])
plt.show(l)
