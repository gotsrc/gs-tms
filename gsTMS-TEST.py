# Tournament Operations Manager
# FOR TESTING USE ONLY
# Built in Python by Paul "Ninj4" Chater
# FOR Coventry Pokemon League

# Initiate Libraries
from tkinter import Tk, Label, Button, Frame, Canvas, Entry, Menu, messagebox, PhotoImage

import time
## Create the Splash Page (Not that it's needed anyway)
class Splash(object):
    def __init__(self, root, file, wait):
        self.__root = root
        self.__file = file
        self.__splash = None
        self.__wait = wait + time.clock()

    def __enter__(self):

        self.__root.withdraw()

        window = Toplevel(self.__root)
        canvas = Canvas(window)
        splash = PhotoImage(root=window, file=self.__file)

        scrW = window.winfo_screenwidth()
        scrH = window.winfo_screenheight()

        imgW = splash.width()
        imgH = splash.height()

        Xpos = (scrW - imgW) // 2
        Ypos = (scrH - imgH) // 2

        window.overrideredirect(True)
        window.geometry('+{}+{}'.format(Xpos, Ypos))

        canvas.configure(width=imgW, height=imgH, highlightthickness=0)
        canvas.grid()

        cnavas.create_image(imgW // 2, imgH //2, image=splash)
        window.update()

        self.__window = window
        self.__canvas = canvas
        self.__splash = splash

    def __exit__(self, exc_type, exc_val, exc_tb):
        now = time.clock()
        if now < self.__wait:
            time.sleep(self.__wait - now)
        del self.__splash
        self.__canvas.destroy()
        self.__window.destroy()

        self.__root.update_idletasks()
        self.__root.deiconify()
        
# Create the Login Form.
class Login:
    def __init__(self, master):
        self.master = master
        master.title("Login to Tournament Manager")
        w = 300
        h = 150

        ws = master.winfo_screenwidth()
        hs = master.winfo_screenheight()

        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        master.geometry('%dx%d+%d+%d' % (w, h, x, y))
        
        self.label = Label(master, text="Welcome to CPL's Tournament Manager!")
        self.label.pack()

        self.username_label = Label(master, text="Username: ")
        self.username_label.pack()

        self.username_input = Entry(master)
        self.username_input.pack()

        self.password_label = Label(master, text="Password: ")
        self.password_label.pack()

        self.password_input = Entry(master)
        self.password_input.pack()

        self.login_button = Button(master, text="Login", command=self.greet)
        self.login_button.pack()

    def greet():
        TOM(root)

class TOM:
    def __init__(self, master):
        self.master = master
        version = "0.0.1"
        company = "gotSrc Development"
        master.title("Tournament Manager v" + version + " by " + company)
        w = 1000
        h = 725

        ws = master.winfo_screenwidth()
        hs = master.winfo_screenheight()

        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        master.geometry('%dx%d+%d+%d' % (w, h, x, y))


        # Generate the Menu Bar
        menubar = Menu(master)

        # File Menu
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New Tournament", command=self.nocmd)
        filemenu.add_command(label="Open Tournament", command=self.nocmd)
        filemenu.add_command(label="Edit Tournament", command=self.nocmd)
        filemenu.add_separator()
        filemenu.add_command(label="Save", command=self.nocmd)
        filemenu.add_command(label="Save As...", command=self.nocmd)
        filemenu.add_command(label="Save All", command=self.nocmd)
        filemenu.add_command(label="Close", command=self.nocmd)
        filemenu.add_separator()
        filemenu.add_command(label="Export", command=self.nocmd)
        filemenu.add_command(label="Edit Profile", command=self.nocmd)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        # Player Menu
        playermenu = Menu(menubar, tearoff=0)
        playermenu.add_command(label="Add Player", command=self.nocmd)
        playermenu.add_command(label="Standings", command=self.nocmd)
        playermenu.add_command(label="List / Search", command=self.nocmd)
        playermenu.add_separator()
        playermenu.add_command(label="Edit", command=self.nocmd)
        playermenu.add_command(label="History", command=self.nocmd)
        playermenu.add_command(label="Drop", command=self.nocmd)
        playermenu.add_command(label="Disqualify", command=self.nocmd)
        playermenu.add_separator()
        playermenu.add_command(label="Speed Slip Match Entry", command=self.nocmd)
        menubar.add_cascade(label="Player", menu=playermenu)

        # Reports Menu
        reportmenu = Menu(menubar, tearoff=0)
        reportlist = Menu(reportmenu, tearoff=0)
        reportlist.add_command(label="Draft Pods", command=self.nocmd)
        reportlist.add_command(label="All Pairings", command=self.nocmd)
        reportlist.add_command(label="Re-Paired Pairings", command=self.nocmd)
        reportlist.add_command(label="Player History", command=self.nocmd)
        reportlist.add_command(label="Match Records", command=self.nocmd)
        reportlist.add_command(label="Standings", command=self.nocmd)
        reportlist.add_command(label="Roster", command=self.nocmd)
        reportlist.add_command(label="Tournament Details", command=self.nocmd)
        reportmenu.add_cascade(label="Reports", menu=reportlist, underline=0)
        menubar.add_cascade(label="Reports", menu=reportmenu)

        # Help Menu
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Contents", command=self.nocmd)
        helpmenu.add_command(label="Help", command=self.nocmd)
        helpmenu.add_separator()
        helpmenu.add_command(label="About", command=self.nocmd)
        menubar.add_cascade(label="Help", menu=helpmenu)
        root.config(menu=menubar)
        
    def nocmd(self):
        messagebox.showinfo('Tournament Manager', "This feature has not yet been implemented.")
        
    def quit(self):
        self.master.destroy()

root = Tk()

TOM = TOM(root)

root.mainloop()
