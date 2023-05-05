import subprocess as sp
import tkinter
from tkinter import *
def execut():
    meter=input("how many to count: ")
    script=open("meter.py","w")
    script.write(f"""i=0
for i in range({meter}):
    print(i)
""")
    script.close()
def runWINDOWNSMODE():
    sp.run("dir", shell=True)
    sp.run("meter.py", shell=True)
def runmacosbash():
    sp.run("dir", shell=True)
    sp.run("meter.py", shell=True)

window=tkinter.Tk()
label=Label(text="PyTest").pack()
button=Button(text="make meter",command=execut).pack()
button2=Button(text="run (WINDOWS mode)",command=runWINDOWNSMODE).pack()
button2=Button(text="run (MACOS OR BASH mode mode)",command=runmacosbash).pack()
window.mainloop()
