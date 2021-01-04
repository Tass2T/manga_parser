import tkinter as tk

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
# then the app geometry
window_x = 800
window_y = 600
# posX and posY are screen split in two minus halft width and height of app
posX = (screen_x // 2) - (window_x // 2)
posY = (screen_y // 2) - (window_y // 2)

geo = "{}x{}+{}+{}".format(window_x,window_y, posX, posY)
interface.geometry(geo)

# will create an infinite loop to keep the windows open
interface.mainloop()