from tkinter import *
from pytube import YouTube

root = Tk()

# window size
root.geometry('900x200')

# locked window size
root.resizable(0,0)

# window title
root.title("YouTube Downloader and Converter")

# download and convert labels
download_label = Label(root,text = 'Youtube Video Downloader', font='arial 20 bold').grid(row=0, column=0)
converter_label = Label(root,text = 'Mp4 to Mp3 Converter', font='arial 20 bold').grid(row=3, column=0)

# store URL from youtube
yt_url = StringVar()
yt_url_label = Label(root, text = 'Paste Link Here:', font='arial 15 bold').grid(row=1, column=0)
# textvariable responsible for getting value of text in yt_url
link_enter = Entry(root, width = 70 ,textvariable = yt_url).grid(row=1, column=1)



# Downloader
def downloader():
    video_url = YouTube(str(yt_url.get())) #get url through StringVar() and convert to string
    video = video_url.streams.first() #get first object of a list from a given link
    video.download() # start downloading
    Label(root, text='your file has been downloaded', font='arial 15').grid(row=4 ,column=0)

Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = downloader).grid(row=2 ,column=0)





# calling a program
root.mainloop()

