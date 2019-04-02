from playlist import Playlist
from song import Song
import os
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
import datetime
class MusicCrawler:
    def __init__(self,path):
        self.path=path

    def generate_playlist(self):
        pl=Playlist("New playlist")
        source_dir =os.path.expanduser(self.path)
        for name in os.listdir(source_dir):  
            if name[-4:].lower() != ".mp3":  # ignore non-mp3 files
                continue

            path = os.path.join(source_dir, name)
            print(path)
            iaudio = EasyID3(path) 
            # if 'TALB' in iaudio:
            #     print('a')
            #     Alb  = iaudio.get('TALB', 'No album title') 
            if 'album' not in iaudio.keys():
                album='No information for the album'
                title=iaudio['title'][0]
                artist=iaudio['artist'][0]
                audio = MP3(path)
                secs=int(audio.info.length)
                duration=str(datetime.timedelta(seconds=secs))
                s=Song(title,artist,album,duration)
                pl.add_song(s)
        return pl




def main():
    crawler = MusicCrawler("~\python\week5\music")
    my_pl=crawler.generate_playlist()
    my_pl.pprint_playlist()


if __name__=='__main__':
    main()