#writen by Murima
"""
File: pycon.py
Author: Murima
Github: https://github.com/murima
Description: downloads pycon videos that are not in my directory
and are short versions of pycon videos

"""

import os.path
from pytube import YouTube
from subprocess import Popen, PIPE


def get_names(d):
    """
    get the names of the videos already in my directory and the size of the vids
    """
    names = [name for name in os.listdir(d) if os.path.isfile(os.path.join(d, name))]

    return names
def download(link, files, avg):
    '''gets the playlist and Downloads the videos that i dont have'''

    url = 'https://www.youtube.com/watch?v=MCs5OvhV9S4'
    command = 'youtube-dl --flat-playlist '+url
    playlist = Popen(command , stdout=PIPE, stderr=PIPE, shell=True)
    print(playlist.stdout)
    yt = YouTube()


    for v in playlist:
        vid = yt.download()
        if playlist.stdout not in files:
                save_vids(avg, vid)


def save_vids(avg, vid):
    """
    save the videos to the right directory
    """
    if vid < avg:
        os.system('mv ')

        return

        return
def get_average_size(d, names):
    """
    get the average size of the files that are considered
    short
    """
    size = []
    length = len(names)

    for results in  os.path.getsize(os.path.join(d, names)):
        size.append(results)
        avg = sum(size)/length





if __name__ =='__main__':
    link = ''
    d = '/home/killer/games/Gilu/pycon/PyCon/Short/'
    files = get_names(d)
    average = get_average_size(d, files)
    vids = download(link, files, average)
    save_vids(average, vids)
