## Map key and artist name to a categorical value like dictionary

import numpy as np
import pandas as pd

## Definitions
songs = pd.read_csv('data/SpotifyCleaned.csv')

## Extract to-be-hashed values for reference later

unhashed = pd.DataFrame({'artist_name': songs['artist_name'], 'key': songs['key']}) ## Add other categorical values here if need to be hashed

#print(songs.head()) # Original Dataset

## Any Categorical Data Can be converted, just enter it under this section (Automize if you wish)
songs['artist_name'] = songs['artist_name'].astype('category')
songs['key'] = songs['key'].astype('category')

cat_columns = songs.select_dtypes(['category']).columns

songs[cat_columns] = songs[cat_columns].apply(lambda x: x.cat.codes)

# print(songs.head()) # Altered DataSet

print(songs[cat_columns].head()) # Altered Columns
print(unhashed.head()) #Original Columns




## Depricated code, reference if you wish for scuffed mapping
'''
print(songs.head())

allartists, artistcounts = np.unique(songs['artist_name'], return_counts = True)

artistmap = pd.DataFrame(allartists)

print(np.shape(artistmap))
artistmap['artist_num'] = np.arange(1,len(artistmap)+1,1)
artistmap = artistmap.rename({0:'artist_name'}, axis = 1)
artistmap = artistmap.astype(str)
#artistmap['num_songs'] = artistcounts

print(artistmap.head())

kek = list(artistmap['artist_name'])
mymap = map(artistmap['artist_num'], kek)
mydict = dict(mymap)
print(mydict)
'''