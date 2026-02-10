import pandas as pd

song_df = pd.read_csv('./data/song_track.csv')
ost_df = pd.read_csv('./data/movies_processed_final.csv')

ost_df["track_title"] = ost_df["track_list"].astype(str).str.split("@")
ost_titles = ost_df["track_title"].explode().str.lower().str.strip().dropna().unique()

song_df = song_df.dropna(subset=["track_name"])
song_df["title_key"] = song_df["track_name"].str.lower().str.strip()

ost_song_df = song_df[song_df["title_key"].isin(ost_titles)].copy()
ost_song_df = ost_song_df.drop(columns=["title_key"])

ost_song_df.to_csv('././data/song.csv', index=False)