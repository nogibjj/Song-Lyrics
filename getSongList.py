""" Get a list of Songs from a website and export it to a csv"""

from requestCall import requestCall
from bs4 import BeautifulSoup
import pandas as pd


# Get Songs from Website
def findSongs(link):
    wiki = requestCall(link)
    soup = BeautifulSoup(wiki.text, "html.parser")
    # Parse the page for where we know the songs are
    songhtml = soup.find_all("li")[14:580]
    return [
        dict(
            zip(
                ["Artist", "Song"],
                [eachItem.getText() for eachItem in eachSong.find_all("a")[:2]],
            )
        )
        for eachSong in songhtml
    ]

def songsToCSV(songs):
    data = pd.DataFrame(songs)
    data.to_csv("data/songList.csv")
    pass

if __name__ == '__main__':
    link = "https://en.wikipedia.org/wiki/List_of_one-hit_wonders_in_the_United_States"
    songs = findSongs(link)
    songsToCSV(songs)