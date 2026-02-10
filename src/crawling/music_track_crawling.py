import requests
import pandas as pd
from bs4 import BeautifulSoup

movie_df = pd.read_csv('../../data/movies_processed.csv')

j = 0
all_data = []
for i, row in enumerate(movie_df[20000:25000].itertuples(index=False), start=20000):
    j+=1
    movie_id = row.imdb_id
    url = f'https://m.imdb.com/title/{movie_id}/soundtrack/' 
    print (movie_id)

    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, 'html.parser')

    target_data = soup.find_all(class_='ipc-metadata-list-item__label ipc-btn--not-interactable')

    result_list = []
    for item in target_data:
        result_list.append(item.get_text(strip=True))

    all_data.append({
        'index': i,            
        'movie_id': movie_id,   
        'track_list': "@ ".join(result_list) 
    })
    if j==10:
        df = pd.DataFrame(all_data)
        df.to_csv('movie_list.csv', index=False, encoding='utf-8-sig')
        j=0

df = pd.DataFrame(all_data)

df.to_csv('movie_list.csv', index=False, encoding='utf-8-sig')