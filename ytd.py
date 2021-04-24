from tkinter import *

root = Tk()

# window size
root.geometry('900x200')

# locked window size
root.resizable(0,0)

# window title
root.title("YouTube Downloader and Converter")

# download and convert labels
download_label = Label(root,text = 'Youtube Video Downloader', font='arial 20 bold').grid(row=0, column=0)
converter_label = Label(root,text = 'Mp4 to Mp3 Converter', font='arial 20 bold').grid(row=2, column=0)

# store URL from youtube
yt_url = StringVar()
yt_url_label = Label(root, text = 'Paste Link Here:', font='arial 15 bold').grid(row=1, column=0)
# textvariable responsible for getting value of text in yt_url
link_enter = Entry(root, width = 70 ,textvariable = yt_url).grid(row=1, column=1)




# calling a program
root.mainloop()