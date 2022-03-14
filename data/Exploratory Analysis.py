## Just Graphs and visualizaitons to better understand the dataset.

## Just Spaghetti Code

## Imports

from markupsafe import string
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv('data\SpotifyCleaned.csv')
#print(np.shape(data))
#print(list(data.columns))

popularity = data['popularity'] ## Probably the best truth values that we can try to predict
allgenres, genrecounts = np.unique(data['genre'], return_counts = True) # Genre Divison

#print(allgenres)
#print(genrecounts)

'''
# Plots Genre stuff
fig, ax = plt.subplots(figsize = (8,8))
ax.bar(allgenres, genrecounts)
ax.set_xticklabels(allgenres, rotation = 90)
plt.tight_layout()
fig.show()
input('Press <Enter> to exit')
'''

allartists, artistcounts = np.unique(data['artist_name'], return_counts = True)
#
# print(allartists)
artistmap = pd.DataFrame(allartists)

print(np.shape(artistmap))
artistmap['artist_num'] = np.arange(1,13319,1)
artistmap = artistmap.rename({0:'artist_name'}, axis = 1)
artistmap = artistmap.astype(str)
artistmap['num_songs'] = artistcounts
# Boxplot of num_songs

fig, ax = plt.subplots()
hist, bins = np.histogram(artistcounts, bins=10)
logbins = np.logspace(np.log10(bins[0]),np.log10(bins[-1]), len(bins))
ax.hist(artistcounts, bins=logbins)
ax.set_xscale('log')
ax.set_xlabel('Number of Songs per Artist')
ax.set_ylabel('Number of Artists')
ax.set_title('Log Histogram')
fig.show()
input('Press <Enter> to exit')

#print(artistmap.head())

# Plots Artist Stuff
# fig, ax = plt.subplots()
# ax.bar(artistmap['artist_num'], artistcounts)
# plt.tight_layout
# fig.show()
# input('Press <Enter> to exit')