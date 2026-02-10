import pandas as pd

song_df = pd.read_csv('./data/song.csv')
ost_df = pd.read_csv('./data/movies_processed_final.csv')

song_df['movie_id'] = None

for i in range(len(song_df)):
    title = str(song_df.loc[i, 'track_name']).lower()

    for j in range(len(ost_df)):
        track_list = str(ost_df.loc[j, 'track_list']).lower()

        if title in track_list:
            song_df.loc[i, 'movie_id'] = ost_df.loc[j, 'imdb_id']
            break

