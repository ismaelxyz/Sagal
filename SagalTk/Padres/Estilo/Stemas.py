#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import Label, Button, Frame, Entry


class Estilos(dict):
    
    def __init__(self):
        self.asige = self.asignarEstilo
        self.introducir = self.update
        self.eliminar = self.__delitem__
    
        #def __delitem__(self, elemnto):
        
    
    def update(self, dic_lis):
        def revisar(lista, nombre):
            
            if len(lista[nombre]) in (16, 12, 5, 3, 13):
                super(Estilos, self).update(lista)
        
        if isinstance(dic_lis, dict):
            revisar(dic_lis, list(dic_lis.keys())[0])
            
        elif isinstance(dic_lis, list):
            for dic in dic_lis:
                if isinstance(dic, dict):
                    revisar(dic, list(dic.keys())[0])
    
    def asignarEstilo(self, nombre, estilo, superior, 
                      extra=[None for i in range(4)]):
        
        stl = self[estilo]
        while len(extra) != 4 and nombre not in ("Ve", "Lt"):
            extra.append(None)
            
        #            Posiciones
        #               stl
        
        #  Ventana:[color=0, relieve=1, bd=2]
        
        #  Linea_de_texto:[color=0, color_sobre=1, color_foco=2, 
        #  color_letra=3, color_letra_sobre=4, color_letra_foco=5, relieve=6,
        #  relieve_sobre=7, relieve_foco=8, fuente=9, color_puntero=10, 
        #  sobra=11, letra_sombra=12, tamaño_borde=13, 
        #  tamaño_borde_sobre=14, tamaño_borde_foco=15]
        
        #  Botón:BoE[color=0, color_sobre=1, color_precionado=2, color_foco=3
        #  color_letra=4, color_letra_sobre=5, color_letra_precionado=6,
        #  color_letra_foco=7, relieve=8, relieve_sobre=9, relieve_foco=10, relieve_foco_precionado=11 
        #  fuente=12]
        
        # Botón-Etiqueta (Cuando los botones no alludan) 
        
        #  Etiqueta:[color=0, color-fuente=1, fuente=2, relieve=3, 
        #            tamaño-borde=4]
        
        #  Cuadro:[color=0, relieve=1, tamaño-borde=2]
        #
        #               extra 
        #  Botón:[texto=0, comando=1, height=2, width=3]
        #  Cuadro:[height=0, width=1]
        #  Etiqueta:[texto=0, height=1, width=2]
        # Liberation Serif
        if nombre == "Ve":
            superior["bg"] = stl[0]
            superior["relief"] = stl[1]
            superior["bd"] = stl[2]
        
        elif nombre == "Lt":
            #"""
            e = Entry(superior, width=extra[0], justify=extra[1], bg=stl[0], 
                      fg=stl[3], relief=stl[6], font=stl[9], 
                      insertbackground=stl[10], selectbackground=stl[11],
                      selectforeground=stl[12])
            #"""
            e.bind("<Enter>", lambda x: (e.__setitem__("bg", stl[1]), 
                                         e.__setitem__("fg", stl[4]),
                                         e.__setitem__("relief", stl[7]),
                                         e.__setitem__("bd", stl[14])))
            
            e.bind("<FocusIn>", lambda x: (e.__setitem__("bg", stl[2]),
                                           e.__setitem__("fg", stl[5]),
                                           e.__setitem__("relief", stl[8]),
                                           e.__setitem__("bd", stl[15])))
            
            for _x in ["<Leave>", "<FocusOut>"]:
                e.bind(_x, lambda x: (e.__setitem__("bg", stl[0]),
                                      e.__setitem__("fg", stl[3]),
                                      e.__setitem__("relief", stl[6]),
                                      e.__setitem__("bd", stl[13])))
            #"""
            #print(stl)
       
            return e
        
        elif nombre == "Bo":
            
            b = Button(superior, text=extra[0], command=extra[1], height=extra[2], 
                  width=extra[3], bg=stl[0], activebackground=stl[2], fg=stl[4],
                  activeforeground=stl[6], overrelief=stl[9],
                  relief=stl[8], font=stl[12], )

            
            
            b.bind("<Enter>", lambda x: (b.__setitem__("bg", stl[1]), 
                                         b.__setitem__("fg", stl[5]),
                                         b.__setitem__("relief", stl[10])))
            
            b.bind("<FocusIn>", lambda x: (b.__setitem__("bg", stl[3]),
                                           b.__setitem__("fg", stl[7])))

            for _x in ["<Leave>", "<FocusOut>"]:
                    b.bind(_x, lambda x: (b.__setitem__("bg", stl[0]),
                                          b.__setitem__("fg", stl[4]),
                                          b.__setitem__("relief", stl[8])))
       
            return b

        elif nombre in ("BoE", "BoE2"):
            
            b = Label(superior, text=extra[0], height=extra[2], 
                  width=extra[3], bg=stl[0], fg=stl[4],
                  relief=stl[8], font=stl[12])

            
            
            b.bind("<Enter>", lambda x: (b.__setitem__("bg", stl[1]), 
                                         b.__setitem__("fg", stl[5]),
                                         b.__setitem__("relief", stl[10])))
            
            b.bind("<FocusIn>", lambda x: (b.__setitem__("bg", stl[3]),
                                           b.__setitem__("fg", stl[7])))
            
            b.bind("<Button-1>", lambda x: (b.__setitem__("bg", stl[2]),
                                                 b.__setitem__("fg", stl[6]),
                                                 b.__setitem__("relief", stl[11]),
                                                 extra[1]()))
                
            if nombre == "BoE2":
                for _x in ["<Leave>", "<FocusOut>"]:
                    b.bind(_x, lambda x: (b.__setitem__("bg", stl[0]),
                                          b.__setitem__("fg", stl[4]),
                                          b.__setitem__("relief", stl[8])))
       
            return b
        
        elif nombre == "Et":
             return Label(superior, text=extra[0], height=extra[1], 
                          width=extra[2], bg=stl[0], fg=stl[1], font=stl[2], 
                          relief=stl[3], bd=stl[4])
        
        elif nombre == "Cu":
             return Frame(superior, height=extra[0], width=extra[1],
                          bg=stl[0], relief=stl[1], bd=stl[2])
