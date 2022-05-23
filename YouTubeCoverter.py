from pytube import YouTube
import os
import requests as re

url = input("Please enter the url of the video: ")
# check if url is valid
try :
    videoObject = YouTube(url)

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
    if os.path.exists(os.path.join('C:',os. environ["HOMEPATH"],'Downloads\Trying')):
        # download the video's audio
        videoObject.streams.get_audio_only().download(os.path.join('C:',os. environ["HOMEPATH"],'Downloads\Trying'))
        print("Download Complete")
    else:
        # print that the directory download/trying does not exist
        print(os.path.join('C:',os. environ['HOMEPATH'],r'Downloads\Trying'), "does not exist")
    
except:
    print("Invalid url")
