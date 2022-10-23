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
    dfwolyrics = dfwolyrics.iloc[-10:,:]
    songs = scrape.getLyrics(dfwolyrics)
    songs.to_json('mydata.json', indent=2)
    # print(songs.tail())
    # songswlyrics = songs.dropna()
    # print(songswlyrics.tail())
    # dfwlyrics = dfwlyrics.reset_index()
    # dfwlyrics = dfwlyrics.merge(songswlyrics, how='outer', on=['Artist', 'Song', 'Lyrics'])
    # print(dfwlyrics.tail())




if __name__ == '__main__':
    addData()

#dataset.push_to_hub("nick-carroll1/lyrics_dataset")
