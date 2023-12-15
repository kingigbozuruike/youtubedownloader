from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('1000x600')
root.resizable(0, 0)
root.title('Youtube Downloader')
root.configure(bg='#202124')


Label(root,text='Download Youtube videos for free!', font='roboto 20 bold', fg='white', bg='#202124', pady=20).pack()

link = StringVar()

Label(root, text="Paste your link here", font = 'san-serif 15 bold', fg='white', bg='#202124').place(x=400, y=150)
link_enter = Entry(root, width=70, textvariable=link).place(x=300, y=200)


def download():
    url = YouTube(str(link.get()))
    video = url.streams.filter(file_extension='mp4', resolution='720p').first()
    video.download()
    Label(root, text='Downloaded', font='arial 15', fg='white', bg='#202124').place(x=450, y=300)

Button(root, text='Download', font='san-serif 16 bold', bg='red', padx=2, command=download).place(x=450,y=250)

root.mainloop()