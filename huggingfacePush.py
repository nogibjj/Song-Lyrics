from datasets import Dataset, load_dataset
import pandas as pd
import lyricScrape as scrape


def addData():
    dataset = load_dataset("nick-carroll1/lyrics_dataset")
    dataset = dataset['train']
    dfwlyrics = dataset.to_pandas()
    dfwolyrics = pd.read_csv('data/songList.csv', index_col = 0)
    dfwlyrics = dfwlyrics.set_index(['Artist', 'Song'])
    dfwolyrics = dfwolyrics.set_index(['Artist', 'Song'])
    dfwolyrics = dfwolyrics.loc[dfwolyrics.index[~dfwolyrics.index.isin(dfwlyrics.index)]].reset_index()
    songs = scrape.getLyrics(dfwolyrics)
    return songs

def to_json(songs):
    songs.to_json('mydata.json', indent=2)
    # print(songs.tail())
    # songswlyrics = songs.dropna()
    # print(songswlyrics.tail())
    # dfwlyrics = dfwlyrics.reset_index()
    # dfwlyrics = dfwlyrics.merge(songswlyrics, how='outer', on=['Artist', 'Song', 'Lyrics'])
    # print(dfwlyrics.tail())

def from_json(file):
    dataset = load_dataset("nick-carroll1/lyrics_dataset")
    dataset = dataset['train']
    dfwlyrics = dataset.to_pandas()
    songs = pd.read_json(file)
    songswlyrics = songs.dropna()
    dfwlyrics = dfwlyrics.merge(songswlyrics, how='outer', on=['Artist', 'Song', 'Lyrics'])
    dataset = Dataset.from_pandas(dfwlyrics)
    dataset = dataset.remove_columns('__index_level_0__')
    return dataset


def upload(dataset, location):
    dataset.push_to_hub(location)


if __name__ == '__main__':
    songs = addData()
    to_json(songs)
    file = 'mydata.json'
    dataset = from_json(file)
    location = "nick-carroll1/lyrics_dataset"
    upload(dataset, location)
