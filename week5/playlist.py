from song import Song
import pprint
import datetime
import matplotlib.pyplot as plt
from tabulate import tabulate
from random import *
import json,io
import os
import mutagen
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3


class Playlist:
    songs=[]
    temp_songs=[]
    index_of_song=-1
    count_songs_left=0
    def __init__(self,name,repeat=False,shuffle=False):
        self.name=name
        self.repeat=repeat
        self.shuffle=shuffle
        #print('constructor. Name:',self.name,'repeat:',str(self.repeat),'shuffle: ',str(self.shuffle))
    def __str__(self):
        s='name: '+self.name+' repeat: '+str(self.repeat)+' shuffle: '+str(self.shuffle)
        return s
    def add_song(self,song):
        self.songs.append(song)
        self.temp_songs.append(song)
        self.count_songs_left+=1
    def remove_song(self,song):
        self.songs.remove(song)
    def total_length(self):
        total_len=0
        for el in self.songs:
            total_len+=el.length_seconds()
        print(total_len)
        return str(datetime.timedelta(seconds=total_len))
    def count_artists(self,artist):
        count=0
        for el in self.songs :
            if el.artist==artist:
                count+=1
        return count
    def artists(self):
        hist={}
        for el in self.songs:
            if el.artist not in hist.keys():
                hist[el.artist]=self.count_artists(el.artist)
        plt.bar(list(hist.keys()), hist.values(), color='g')
        plt.show()
    def print_songs(self):
        for el in self.songs:
            print(el)
    def next_song(self):
        n=len(self.songs)
        if self.shuffle==False:
            if self.index_of_song==-1:
                self.index_of_song+=1
                return self.songs[self.index_of_song]
            elif self.index_of_song<n-1:
                self.index_of_song+=1
                return self.songs[self.index_of_song]
            elif self.index_of_song==n-1 and self.repeat==False:
                s="end of playlist"
                return s
            elif self.index_of_song==n-1 and self.repeat==True:
                self.index_of_song=0
                return self.songs[self.index_of_song]
        else:
            # if self.count_songs_left>0:
            #     self.temp_songs=self.songs
            #     # self.c=[1,2,3,4,5];
            #     # print(self.c)# vinagi e [1,2,3,4,5]
            #     # self.c.pop(0)
            #     print(len(self.songs))# i to se promenq zaedno sus self.temp_songs
            #     print(len(self.temp_songs))######?? vseki put se namalqva i ne se vliqe ot gornoto ravenstvo
            #     ind=randint(0, self.count_songs_left-1)
            #     song_to_play=self.temp_songs[ind]
            #     self.temp_songs.remove(song_to_play)
            #     self.count_songs_left=self.count_songs_left-1
            #     return song_to_play
            # elif self.count_songs_left==0:
            #     self.count_songs_left=len(self.songs)
            #     self.temp_songs=self.songs
            #     print(len(self.temp_songs))######?? vseki put se namalqva i ne se vliqe ot gornoto ravenstvo
            #     ind=randint(0, self.count_songs_left-1)
            #     song_to_play=self.temp_songs[ind]
            #     self.temp_songs.remove(song_to_play)
            #     self.count_songs_left=self.count_songs_left-1
            if self.count_songs_left==0 and self.repeat==True:
                #self.temp_songs=self.songs
                for el in self.songs:
                    self.temp_songs.append(el)#taka self.songs ne se promenq, a po goniq nachin se
                self.count_songs_left=len(self.songs)
            if self.count_songs_left==0 and self.repeat==False:
                 s="end of playlist"
                 return s
            print(len(self.temp_songs),len(self.songs))
            ind=randint(0, self.count_songs_left-1)
            song_to_play=self.temp_songs[ind]
            self.temp_songs.remove(song_to_play)
            self.count_songs_left=self.count_songs_left-1
            return song_to_play
    def pprint_playlist(self):
        arr=[]
        for el in self.songs:
            sub_arr=[el.artist,el.title,el._length]
            arr.append(sub_arr)
        print(tabulate(arr, headers=['Artist', 'Song','Length'], tablefmt='orgtbl'))
    def save(self):
        arr=[]
        for el in self.songs:
            arr.append(el.__dict__)
        name=self.name
        name=name.replace(' ','-')
        s=name+'.json'
        path_to_folder=os.path.expanduser(os.path.join("~\python\week5\playlist-data/" + s))
        print(path_to_folder)
        with open(path_to_folder, "w") as write_file:
            json.dump(arr, write_file)

    @staticmethod
    def load(path):
        songs_from_file=[]
        path_to_folder=os.path.expanduser("~\python\week5\playlist-data/Rock-and-metal-playlist.json" )
        with open(path_to_folder, 'r') as f:
            data = json.load(f)
        for song in data:
            s=Song(song['title'],song['artist'],song['album'],song['_length'])
            songs_from_file.append(s)
        path=path.replace('-',' ')
        path=path.split('.')[0]
        pl=Playlist(path)
        return pl




def main():
    print(mutagen.File("Rammstein - Du Hast (Official Video).mp3"))
    audio = MP3("Rammstein - Du Hast (Official Video).mp3")
    print(audio.info.length)

    iaudio = EasyID3("Rammstein - Du Hast (Official Video).mp3")
    print(iaudio)
    print(iaudio['title'] )


    code_songs = Playlist(name="Rock and metal playlist", repeat=False, shuffle=False)
    s = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
    s1 = Song(title="Du Hast", artist="Rammastein", album="Sehnsucht", length="3:56")
    s2 = Song(title="Ich Will", artist="Rammastein", album="Mutter", length="4:06")
    s3 = Song(title="Sonne", artist="Rammastein", album="Mutter", length="4:13")
    gn1 = Song(title="Welcome To The Jungle", artist="Guns N' Roses", album="Appetite for destruction", length="4:40")
    gn2 = Song(title="Paradise City", artist="Guns N' Roses", album="Appetite for destruction", length="6:49")
    code_songs.add_song(s)
    code_songs.add_song(s1)
    code_songs.add_song(s2)
    code_songs.add_song(s3)
    code_songs.add_song(gn1)
    code_songs.add_song(gn2)
   # code_songs.print_songs()
    print(code_songs.total_length())
    #code_songs.artists()

    #code_songs.pprint_playlist()
    #code_songs.save()

    # my_playlist=code_songs.load('Rock-and-metal-playlist.json')
    # print(my_playlist.name=='Rock and metal playlist')

    #SHUFFLE
    # print('next song',code_songs.next_song(),'There are',code_songs.count_songs_left,'songs')
    # for el in code_songs.temp_songs:
    #     print(el)
    # print('===============')
    # print('next song',code_songs.next_song(),'There are',code_songs.count_songs_left,'songs')
    # for el in code_songs.temp_songs:
    #     print(el)
    # print('===============')
    # print('next song',code_songs.next_song(),'There are',code_songs.count_songs_left,'songs')
    # for el in code_songs.temp_songs:
    #     print(el)
    # print('===============')
    # print('next song',code_songs.next_song(),'There are',code_songs.count_songs_left,'songs')
    # for el in code_songs.temp_songs:
    #     print(el)
    # print('===============')
    # print('next song',code_songs.next_song(),'There are',code_songs.count_songs_left,'songs')
    # for el in code_songs.temp_songs:
    #     print(el)
    # print('===============')
    # print('next song',code_songs.next_song(),'There are',code_songs.count_songs_left,'songs')
    # for el in code_songs.temp_songs:
    #     print(el)
    # print('===============')
    # print('next song',code_songs.next_song(),'There are',code_songs.count_songs_left,'songs')
    # for el in code_songs.temp_songs:
    #     print(el)
    # print('===============')
    # print('next song',code_songs.next_song(),'There are',code_songs.count_songs_left,'songs')
    # for el in code_songs.temp_songs:
    #     print(el)
    # print('===============')

    #REPAT
    # print(code_songs.next_song())
    # print(code_songs.index_of_song)
    # print(code_songs.next_song())
    # print(code_songs.index_of_song)
    # print(code_songs.next_song())
    # print(code_songs.index_of_song)
    # print(code_songs.next_song())
    # print(code_songs.index_of_song)
    # print(code_songs.next_song())
    # print(code_songs.index_of_song)
    # print(code_songs.next_song())
    # print(code_songs.index_of_song)
    # print(code_songs.next_song())
    # print(code_songs.index_of_song)
    # print(code_songs.next_song())
    # print(code_songs.index_of_song)

if __name__=='__main__':
    main()