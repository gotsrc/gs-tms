################################################
# Tournament Management Software               #
# version:    0.01-dev                         #
# author:     Paul "Ninj4" Chater aka PC Hater #
################################################

import tkinter as tk
from tkinter import ttk

LARGE_FONT = ("Arial", 12)

class gsTMS(tk.Tk):
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		
		tk.Tk.iconbitmap(self,default=None)
		tk.Tk.wm_title(self, "Tournament Management Software")
		
		container = tk.Frame(self)
		
		container.pack(side="top", fill="both", expand = True)
		
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)
		
		self.frames = {}
		
		for F in (Welcome, User, TMS):
			frame = F(container, self)
			self.frames[F] = frame
			frame.grid(row=0, column=0, sticky="nsew")
			
		self.show_frame(Welcome)
		
	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()
		
def qf(quickPrint):
	print(quickPrint)
	
class Welcome(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		lblWelcome = ttk.Label(self, text="Welcome to TMS", font=LARGE_FONT)
		lblWelcome.pack(pady=10, padx=10)
		
		btnLogin = ttk.Button(self, text="Login",
			command=lambda: controller.show_frame(User))
		btnLogin.pack(pady=5, padx=5)
		
class User(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		lblLogin = ttk.Label(self, text="Login to TMS", font=LARGE_FONT)
		lblLogin.pack(pady=10, padx=10)
		
		btnLogin = ttk.Button(self, text="Verify Credentials",
			command=lambda: controller.show_frame(TMS))
		btnLogin.pack(pady=5, padx=5)

class TMS(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		
		lblTMS = ttk.Label(self, text="Hello there, {user}", font=LARGE_FONT)
		lblTMS.pack(pady=10, padx=10)

		lblLogout = ttk.Label(self, text="Wanna Logout?")
		lblLogout.pack(pady=10, padx=10)
		
		btnLogout = ttk.Button(self, text="Log Out",
			command=lambda: controller.show_frame(Welcome))
		btnLogout.pack(pady=5, padx=5)
		
app = gsTMS()
app.mainloop()
