from tkinter import *
from idlelib.pyshell import *

ven = Tk(className="Sagal")
gtexto = Text(ven)
PyShell(gtexto)
gtexto.pack()
ven.mainloop()
