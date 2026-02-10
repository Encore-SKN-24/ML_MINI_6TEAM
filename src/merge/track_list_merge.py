import pandas as pd

movie_df = pd.read_csv('././data/raw/movies_processed_final.csv')
music_df = pd.read_csv('././data/raw/music_list.csv')

movie_df = movie_df.merge(
    music_df[['movie_id', 'track_list']],
    left_on='imdb_id',
    right_on='movie_id',
    how='left'
).drop(columns=['movie_id'])
print(movie_df)

movie_df = movie_df.dropna(subset=['track_list'])

movie_df = movie_df.drop(columns=['track_list_x'])
movie_df = movie_df.drop(columns=['track_list_y'])

movie_df.to_csv('././data/raw/movies_processed_final.csv', index=False)

