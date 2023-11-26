import tkinter as tk
import pytube as pyt


url = str(input("Url do video: "))
yt = pyt.YouTube(url)
title = yt.title
thumb_url = yt.thumbnail_url
streams = yt.streams.filter(only_audio=True)
print(title)
# print(thumb_url)
print(streams)
select = streams.get_by_itag(139)
# select.download()


# window = tk.Tk()
# label = tk.Label(text="Hello, Tkinter")
# label.pack()
# window.mainloop()