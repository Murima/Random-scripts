#writen by Murima
"""
File: pycon.py
Author: Murima
Github: https://github.com/murima
Description: downloads pycon videos that are not in my directory
and are short versions of pycon videos

"""

from __future__ import unicode_literals
import os.path
from youtube_dl import YoutubeDL

def get_names(d):
    """
    get the names of the videos already in my directory and the size of the vids
    """
    file_attributes = []
    for name in os.listdir(d):
        if os.path.isfile(os.path.join(d,name)):
            file_attributes.append((name, os.path.getsize(d+name)))

    return file_attributes


def get_average_size(d, names):
    """
    get the average size of the files that are considered
    short
    """
    size = 0
    name=0
    length = len(names)

    for name, size in names:
        size+=size

    return (size/1000000)/length



def download(link, files_present, avg):
    '''gets the playlist and Downloads the videos that i dont have'''

    #url = 'https://www.youtube.com/watch?v=MCs5OvhV9S4'
    url = 'https://www.youtube.com/playlist?list=PLwyG5wA5gIzjhW36BxGBoQwUZHnPDFux3'
    ydl=YoutubeDL()
    ydl.add_default_info_extractors()
    playlist = ydl.extract_info(url, download=False)
    for video in playlist['entries']:
        import ipdb; ipdb.set_trace()
        if video['title'] in files_present:
            print ("Video #{} {} is present and will be ignored").format(video['playlist_index'], video['title'])
        else:
            print   ("currently downloading: {}").format(video['title'])
            ydl.download(video['webpage_url'])


def save_vids():
    """
    save the videos to the right directory
    """
    return




if __name__ =='__main__':
    link = ''
    d = '/home/killer/games/Gilu/pycon/PyCon/Short/'
    files = get_names(d)
    average = get_average_size(d, files)
    download(link, files, average)
    save_vids()
