import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Read data from file 'filename.csv'
# (in the same directory that your python process is based)
data = pd.read_csv("CO_import.csv")
# Preview the first 5 lines of the loaded data
data.head()
print(data)
plt.clf()
f, axes = plt.subplots(1,3)


g=sns.swarmplot(x=data['date'],y=data['dia'], hue=data['well'], ax=axes[0],palette='pastel')
g.tick_params('x',labelrotation=60)


h=sns.boxplot(x=data['date'],y=data['dia'],ax=axes[1], hue=data['well'],palette='pastel')
h.tick_params('x',labelrotation=60)

i=sns.swarmplot(y=data['dia'],x=[""]*len(data), ax=axes[2], hue=data['date'],palette='Blues')
plt.show(f)
