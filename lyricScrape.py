# Import necessary modules
from requestCall import requestCall
import re
import random
from bs4 import BeautifulSoup
import time
from datasets import Dataset
import pandas as pd


# Make a list of song information including artist and lyrics
def getLyrics(songs):
    for eachRow in songs.index:
        eachSong = songs.loc[eachRow,:]
        try:
            print(f'google searching{eachSong}')
            lyricSearch = requestCall(
                f"https://www.google.com/search?q={eachSong['Artist']} {eachSong['Song']} lyrics")
            pass
        except AssertionError as e:
            print(f'Error, status code is: {e}')
            continue
        lyricSoup = BeautifulSoup(lyricSearch.text, "html.parser")
        lyrics = lyricSoup.find("div", {"data-lyricid": re.compile(".*[Ll]yric.*")})
        if lyrics != None:
            songs.loc[eachRow, "Lyrics"] = re.sub(
                "(\w?[a-z0-9?])([A-Z]\w?)",
                "\g<1>\n\g<2>",
                lyrics.getText().split("Source")[0],
            )
        time.sleep(random.uniform(0,.5))
        pass
    return songs


if __name__ == "__main__":
    start_time = time.time()
    songs = pd.read_csv('data/songList.csv', index_col = 0)
    songs = songs.loc[:100,:]
    songs = getLyrics(songs)
    # Exclude songs for now that couldn't be found on Google
    # songswlyrics = [eachSong for eachSong in songs if "Lyrics" in eachSong.keys()]
    songswlyrics = songs.dropna()

    print(songswlyrics.head())

    # Create a Hugging Face Dataset from Songs w/ Lyrics
    dataset = Dataset.from_pandas(songswlyrics)

    # Push dataset to Hugging Face
    dataset.push_to_hub("nick-carroll1/lyrics_dataset")
    print(time.time()-start_time)
