from tkinter import Frame, Label, Button, Tk, Entry, StringVar
#from re import *
from tkinter.colorchooser import askcolor
from tkinter import TclError

ven = Tk(className=" Buscar un Color")
FILESAVE = "SaveColors.json"

def viewFileJsom(fl=FILESAVE):
    import os
    is_file = os.path.isfile(fl)
   
    if not is_file:
        with open(fl, "w") as fil:
            fil.close()

        return None
    
    elif is_file:
        from json import load
        with open(fl, "r") as fil:
            #read_fil = fil.read()
            #fil.close()
            return [load(fil), fil.close()][0]
    
def searchColor(lbel1, entry):
    my_color = askcolor()

    if my_color is not None:
        lbel1["bg"] = my_color[1]
        entry.set("Hex: %s" % my_color[1])
        listColors(my_color[1])
        print(listColors())

def changeColor(lbel1, entry):
    valor = entry.get()
    
    if "Hex: " in valor:
        valor = valor[5:]

    while valor[0].isspace():
        valor = valor[1:]
    
    if not valor.isalpha():
        print("entr")
        vl = ""
        for x in valor:
            if x.isdigit():
                vl += x
                
        if vl.isdigit():
            valor = vl

            if not "#" in valor and len(valor) >= 6:
                valor = "#" + valor[:6]

    print(valor, "z")
    try:
        if valor is not None:
            lbel1["bg"] = valor
            entry.set("Hex: %s" % valor)
            listColors2(valor)
            print(listColors2())
   
    except TclError:
        lbel1["bg"] = "white"
        entry.set("Color desconocido se cambia: white")

def modelarExtructura(master, text, command, textvar):
    fr = Frame(master)
    fr.pack()

    fr1 = Frame(fr)
    fr1.pack()

    fr2 = Frame(fr)
    fr2.pack(ipadx=150)

    Button(fr1, text=text, 
        command=command).pack(pady=3, side="right")
    Entry(fr1, width=50, font=("Arial", 9, "italic"),
          textvariable=textvar).pack(pady=5, padx=4, side="right")

    Button(fr2, text="Siguiente").pack(side="left")
    Button(fr2, text="Anterior").pack(side="left", padx=8)

    return fr

def modelerWindow():  # Modelar ventana
    color = StringVar()
    color1 = StringVar()

    modelarExtructura(ven, "Buscar Color", lambda:
                      searchColor(lab1, color),color).\
                      pack_configure(pady=15, ipadx=8)

    modelarExtructura(ven, "Cambiar Color", lambda:
                      changeColor(lab2, color1), color1).\
                      pack_configure(pady=10, ipadx=4)

    fr = Frame(ven)
    Label(fr, text="Tipos de Colores\nHex\t\t\t\tRGB o Hex", font=("Arial", 12, "italic")).pack()

    lab1 = Label(fr, bg="white", width=40, height=15)
    lab2 = Label(fr, bg="white", width=40, height=15)

    lab1.pack(padx=2, side="left")
    lab2.pack(padx=2, side="left")
    fr.pack(pady=4, padx=10)

def saveFile():
    from json import dump
    with open(FILESAVE, "w") as fil:
        
        dump({"search":listColors(),
              "choce":listColors2()}, fil)
        fil.close()

def listColors(new_var=None, var=[]):
    if new_var is not None:
        var.append(new_var)
    
    else:
        return var

def listColors2(new_var=None, var=[]):
    if new_var is not None:
        var.append(new_var)
    
    else:
        return var

def main():
    ven.protocol("WM_DELETE_WINDOW", lambda: (saveFile, ven.destroy()))
    modelerWindow()

    global_color = viewFileJsom()
    
    if global_color is not None:
        print(type(global_color))
    
        for xy in global_color["search"]:
            listColors(xy)

        for xy in global_color["choce"]:
            listColors2(xy)

if __name__ == "__main__":
    main()
    ven.mainloop()