from tkinter import *
ven = Tk()

entr = Entry(ven, invcmd="der", bg="grey2", fg="whitesmoke", insertwidth=20,
             relief="groove", bd=40, selectborderwidth=5)
entr.pack(pady=5)

entr2 = Entry(ven, bg="#343535", fg="whitesmoke", relief="raised", bd=4,
              insertbackground="blue", selectbackground="red",
              selectforeground="orange", font=("Courier", 10))
entr2.pack(pady=5)

entr.bind("<Enter>", lambda x: (entr.__setitem__("bg", "whitesmoke"), 
                                entr.__setitem__("fg", "grey2")))
entr.bind("<Leave>", lambda x: (entr.__setitem__("bg", "grey2"), 
                                entr.__setitem__("fg", "whitesmoke")))


ven.mainloop()

# insertbackground = color del puntero
# selectbackground = color sobra seleccion
# flat, groove, raised, ridge, solid, or sunken

#
#  Linea_de_texto:[color=0, color_sobre=1, color_foco=2, color_letra=3,
#  color_letra_sobre=4, color_letra_foco=5, relieve=6, relieve_sobre=7, 
#  relieve_foco=8, fuente=9, color_puntero=10, sobra=11, letra_sombra=12]