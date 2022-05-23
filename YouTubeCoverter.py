from pytube import YouTube
import os
import requests as re
import math

def onComplete(stream, file_path):
    print("Download Complete")

def onProgress(stream, chunk, bytes_remaining):
    # prints the percentage of the file that has been downloaded
    print(f"{math.floor(((stream.filesize-bytes_remaining)/stream.filesize)*100)}%")

# url = input("Please enter the url of the video: ")
url = "https://www.youtube.com/watch?v=nwRoHC83wx0"
# check if url is valid
try :
    videoObject = YouTube(url, 
    on_progress_callback=onProgress, 
    on_complete_callback=onComplete)

    # video information
    # print(videoObject.title)
    # print(f"{videoObject.length/60}min")
    # print(videoObject.views)

    # The different streams available
    # for stream in videoObject.streams:
    #     print(stream)

    # few of the streams available
    # print(videoObject.streams.get_highest_resolution())
    # print(videoObject.streams.get_lowest_resolution())
    # print(videoObject.streams.get_audio_only())


    # check if directory exists
    if os.path.exists(os.path.join('C:',os. environ["HOMEPATH"],r'Downloads\Trying')):
        # download the video's audio
        videoObject.streams.get_audio_only().download(os.path.join('C:',os. environ["HOMEPATH"],r'Downloads\Trying'))
    else:
        # print that the directory download/trying does not exist
        print(os.path.join('C:',os. environ['HOMEPATH'],r'Downloads\Trying'), "does not exist")
    
except:
    print("Error")
