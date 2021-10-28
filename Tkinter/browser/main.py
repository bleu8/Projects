import webbrowser
from tkinter import *
root=Tk()

root.title("webBrowser")

root.geometry("300x200")

def google():
    webbrowser.open("www.google.com")

mygoog=Button(root,text="open google",command=google).pack(pady=20)

root.mainloop()