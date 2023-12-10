from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('500x300')
root.resizable(0, 0)
root.title('youtube downloader')


Label(root,text='Download Youtube videos for free', font='san-serif 14 bold').pack()

link = StringVar()

Label(root, text="Paste your link here", font = 'san-serif 15 bold').place(x=150, y=55)
link_enter = Entry(root, width=70, textvariable=link).place(x=30, y=85)


def download():
    url = YouTube(str(link.get()))
    video = url.streams.filter(file_extension='mp4', resolution='720p').first()
    video.download()
    Label(root, text='Downloaded', font='arial 15').place(x=100, y=120)

Button(root, text='Download', font='san-serif 16 bold', bg='red', padx=2, command=download).place(x=100,y=150)

root.mainloop()
