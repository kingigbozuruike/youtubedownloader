from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Progressbar
from pytube import YouTube
import requests

import ssl
ssl._create_default_https_context = ssl._create_unverified_context


root = Tk()
root.geometry('1000x600')
root.resizable(0, 0)
root.title('Youtube Downloader')
root.configure(bg='#202124')

Label(root, text='Download Youtube videos for free!', font='roboto 20 bold', fg='white', bg='#202124', pady=20).pack()

link = StringVar()

Label(root, text="Paste your link here", font='san-serif 15 bold', fg='white', bg='#202124').place(x=400, y=150)
link_enter = Entry(root, width=50, textvariable=link).place(x=300, y=200)

progress_bar = Progressbar(root, orient=HORIZONTAL, length=400, mode='determinate')
progress_bar.place(x=300, y=250)

def download():
    url = YouTube(str(link.get()))
    video = url.streams.filter(file_extension='mp4', resolution='720p').first()
    download_location = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[('MP4 files', '*.mp4')])

    response = requests.get(video.url, stream=True)
    total_size = int(response.headers.get('content-length'))

    with open(download_location, 'wb') as f:
        downloaded_bytes = 0
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                downloaded_bytes += len(chunk)
                progress = (downloaded_bytes / total_size) * 100
                progress_bar['value'] = progress
                root.update_idletasks()

    Label(root, text='Downloaded', font='arial 15', fg='white', bg='#202124').place(x=450, y=300)

Button(root, text='Download', font='san-serif 16 bold', bg='red', padx=2, command=download).place(x=450, y=300)

root.mainloop()
