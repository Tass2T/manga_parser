import tkinter as tk
import os
from mangaGetter import scrapManga

# this is the place where documents will be set
path = os.path.expanduser("~/desktop")

interface = tk.Tk()
# we change the title here
interface.title("Pandaru Manga")

# we change the min and max resolution and keep it from changing
interface.minsize(640,480)
interface.maxsize(1240,720)
interface.resizable(width=False, height=False)
# default size and positioning in the middle of the screen
# below, we get the height and width of the window's screen
screen_x = interface.winfo_screenwidth()
screen_y = interface.winfo_screenheight()
# then the app width and height
window_x = 800
window_y = 600
# posX and posY are screen split in two minus halft width and height of app
posX = (screen_x // 2) - (window_x // 2)
posY = (screen_y // 2) - (window_y // 2)
geo = "{}x{}+{}+{}".format(window_x,window_y, posX, posY)
# change app gemometry based on previous variables
interface.geometry(geo)
# first label creation then how to display it
# pack display in block
welcome_text = tk.Label(interface, text="Welcome to the Pandaru Manga Scrapper!")
welcome_text.pack()
# here we get the manga chosen by the user
userInput = tk.Entry(interface)
userInput.pack()

def getManga () :
    formattedName = tk.Entry.get(userInput).replace(' ', '-')
    scrapManga(formattedName, path)

myFirstButton = tk.Button(interface, text="change the label", command=getManga)
myFirstButton.pack()

# will create an infinite loop to keep the windows open
interface.mainloop()