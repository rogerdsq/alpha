#!/usr/bin/env python

import Tkinter

root = Tkinter.Tk()
s = Tkinter.Scrollbar(root)
T = Tkinter.Text(root)

T.focus_set()
s.pack(side=Tkinter.RIGHT, fill=Tkinter.Y)
T.pack(side=Tkinter.LEFT, fill=Tkinter.Y)
s.config(command=T.yview)
T.config(yscrollcommand=s.set)

for i in range(40): 
   T.insert(Tkinter.END, "This is line %d\n" % i)

Tkinter.mainloop()

