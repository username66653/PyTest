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
def run():
    sp.run("ls", shell=True)
    sp.run("python3 meter.py", shell=True)

window=tkinter.Tk()
label=Label(text="PyTest").pack()
button=Button(text="make meter",command=execut).pack()
button2=Button(text="run",command=run).pack()
window.mainloop()
