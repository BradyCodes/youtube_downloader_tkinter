import time
import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import messagebox,filedialog


def widgets():
    tk.Label(root,
                    text="Youtube downloader",
                    # bg="#202020",
                    fg="#000000",
                    font=("Arial", 20),
                    ).place(x=200,y=10)
    tk.Label(root,
                    text="Youtube Video URL: ",
                    font=("Arial", 14),
                    # bg="#FFBF00",
                    fg="#484848",
                    ).place(x=30, y=60)

    root.linkText = tk.Entry(root,
                             font=("Arial", 13),
                             width=43,
                             textvariable=link)
    root.linkText.place(x=230, y=60)

    tk.Label(root,
                    text="Path :",
                    font=("Arial,", 14),
                    # bg = "#FFBF00",
                    fg = "#484848",
                    ).place(x=30,y=120)

    root.pathText = tk.Entry(root,
                             font=("Arial", 13),
                             width=35,
                             textvariable=path)
    root.pathText.place(x=230, y=126)

    button1 = tk.Button(root,
                        text=" Browse",
                        fg="#000000",
                        highlightbackground="#00397c",
                        font=(" Gills Sans", 12),
                        height= 1,
                        width=5,
                        command=browse,
                    )
    button1.place(x=540, y=127.5)

    button2 = tk.Button(root,
                        text=" DOWNLOAD ",
                        fg="#ffffff",
                        highlightbackground="#000000",
                        font=("Gills Sans", 28),
                        height=2,
                        width=10,
                        command=download,
                        )
    button2.place(x=200, y=200)

def browse():
    d_path = filedialog.askdirectory(initialdir=" ")   # initial dir =" " --> where are you rn
    path.set(d_path)

def download():

    link_g = link.get()
    path_g = path.get()

    yo = YouTube(link_g)   # youtube() object

    # select the highest reso stream of the video
    ys = yo.streams.get_highest_resolution()
    tk.messagebox.showinfo(title="Congrats !", message= f'{yo.title} will start downloading shortly')
    # try:
    ys.download(path_g)
    tk.messagebox.showinfo(title="Yipeee!", message= f" Your video{yo.title} has downloaded at \n{path_g}")
    # except:
    #     tk.messagebox.showerror(title="FAILED", message= "Wrong values")
    #     time.sleep(3)
    #     root.destroy()

root = tk.Tk()
root.title("Yotube Downloader")
#root.resizable(False, False)
root.geometry('600x300')
root.config(bg="#ffffff")

link = tk.StringVar()
path = tk.StringVar()
widgets()

root.mainloop()
