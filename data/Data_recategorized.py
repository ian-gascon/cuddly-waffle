## Map key and artist name to a categorical value like dictionary

import numpy as np
import pandas as pd

## Definitions
songs = pd.read_csv('data/SpotifyCleaned.csv')

print(songs.head())

allartists, artistcounts = np.unique(songs['artist_name'], return_counts = True)

artistmap = pd.DataFrame(allartists)

print(np.shape(artistmap))
artistmap['artist_num'] = np.arange(1,len(artistmap)+1,1)
artistmap = artistmap.rename({0:'artist_name'}, axis = 1)
artistmap = artistmap.astype(str)
artistmap['num_songs'] = artistcounts