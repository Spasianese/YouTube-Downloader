from tkinter import *
from tkinter import filedialog
from pytube import YouTube
from pytube import Playlist
import os
import subprocess

import shutil

# Functions
def select_path():
    #Allows user to select path
    path = filedialog.askdirectory()
    address_label.config(text=path)

def download_file():
    #get user path
    get_link = link_field.get()
    #get selected path
    user_path = address_label.cget("text")
    screen.title('Downloading...')
    #Download video
    mp4_video = YouTube(get_link).streams.get_audio_only().download()
    # Convert mp4 file into m4a file
    CurrentFileName = mp4_video[mp4_video.rfind("\\")+1:]
    FinalFileName = mp4_video[mp4_video.rfind("\\")+1:mp4_video.rfind(".")] + '.m4a'
    subprocess.call(['ffmpeg', '-i', f'{CurrentFileName}', f'{FinalFileName}'])
    os.remove(CurrentFileName)
    ### move to selected dir
    shutil.move(FinalFileName, user_path)
    screen.title('Download Complete!')
    
def download_playlist():
    #playlist info
    p = Playlist(link_field.get())
    #get selected path
    user_path = address_label.cget("text")
    screen.title('Downloading...')
    #Download video
    for url in p.video_urls:
        get_link = url
        mp4_video = YouTube(get_link).streams.get_audio_only().download()
        CurrentFileName = mp4_video[mp4_video.rfind("\\")+1:]
        # Convert mp4 file into m4a file
        FinalFileName = mp4_video[mp4_video.rfind("\\")+1:mp4_video.rfind(".")] + '.m4a'
        subprocess.call(['ffmpeg', '-i', f'{CurrentFileName}', f'{FinalFileName}'])
        os.remove(CurrentFileName)
        shutil.move(FinalFileName, user_path)
    screen.title('Download Complete!')

screen = Tk()
title = screen.title('YouTube Downloader')
canvas = Canvas(screen, width=500,height=500)
canvas.pack()

#logo_img = PhotoImage(file='yt.png')
#logo_img = logo_img.subsample(2,2)
#canvas.create_image(250, 80, image=logo_img) x position, y pos

#Link Field
link_field = Entry(screen, width=50)
link_label = Label(screen, text="Enter Download Link: ", font=('Arial', 15))

#Select path for saving file
address_label = Label(screen, text="Select Path For Download", font=('Arial', 15))
selec_btn = Button(screen, text="Select", command=select_path)

# Add to window
canvas.create_window(250,280,window=address_label)
canvas.create_window(250,330,window=selec_btn)

#add widgets
canvas.create_window(250,170,window=link_label)
canvas.create_window(250,220,window=link_field)

# Download btns
download_btn = Button(screen, text="Download Video", command=download_file)
download_btn2 = Button(screen, text="Download Playlist", command=download_playlist)
#add to canvas
canvas.create_window(200,390,window=download_btn)
canvas.create_window(300,390,window=download_btn2)

screen.mainloop()