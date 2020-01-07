#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Program Sagal (Soberania Global in Spanish).

    Copyright © 2019 Ismael Belisario

    This file is part of Sagal.

    Sagal is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Sagal is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Sagal.  If not, see <https://www.gnu.org/licenses/>.
"""

from tkinter import Tk, Menu, Entry, PhotoImage#, TclError
from tkinter import messagebox
from Padres.Utilidades.Smenu import Menu
# Los nombres de los estilos se representan con
# Nombre del area punto nombre del objeto ejemplo: Ini.SSV1


class Stk(Tk):
    """Stk (Tk para Sagal)
    
            Una forma de simplificar la creación y
        aplicar los cambios nesesarios para el Tk que lleva Sagal
        en su modo grafico
    """
    
    def __init__(self):
        super().__init__(className=" Sagal")
        self.logo = PhotoImage(file="Padres/Imágenes/Logol.png")
        self.call('wm', 'iconphoto', self, self.logo)
    
    
class Sesión(Stk):

    def __init__(self, fun_t, tema):
        super().__init__()
        # fun_t = funcion de teclado
        # confg = clase de configuración
        self.geometry("+100+20")
        Menu(self, tema, self.logo)
        """
        self.tema = tema
        self.resizable(False, False)
        self.geometry("550x340")
        #self.segundaEtapa()
        #" ""
        self.tema.asige("Ve", "Sesi.SSV1", self)
        self.marco = self.tema.asige("Cu", "Sesi.SSC1", self)
        #self.datos_usuario = None
        
        #self.labt1(self.marco, "Bienvenido", fuente=("Liberation Serif", 20)).pack()
        self.tema.asige("Et", "Sesi.SSE1", self, ["Bienvenido"]).pack()
        self.tema.asige("Et", "Sesi.SSE2", self).pack(pady=4)
        
        self.tema.asige("Et", "Sesi.SSE3", self.marco, ["Usuario"]).\
        pack()
        
        self.etra_usu = self.tema.asige("Lt", "Sesi.SSL1", self.marco, 
                                        [35, "center"])
        self.etra_usu.pack()
        

        self.tema.asige("Et", "Sesi.SSE4", self.marco).pack(pady=5, 
                                                       padx=200)


        self.tema.asige("Et", "Sesi.SSE5", self.marco, ["Clave"]).pack()      
        self.etra_cla = self.tema.asige("Lt", "Sesi.SSL1", self.marco, 
                                        [35, "center"])
        self.etra_cla["show"] = "*"
        self.etra_cla.pack()

        self.activarBotones()

        self.tema.asige("Et", "Sesi.SSE6", self.marco).pack(pady=5, 
                                                       padx=200)

        acep = self.tema.asige("Bo", "Sesi.SSB1", self.marco, 
                                       ["Aceptar", self.enviarDatosUsuarioG])
        sali = self.tema.asige("Bo", "Sesi.SSB2", self.marco, 
                                       ["Salir", self.salir])
        
        acep.pack(pady=2, ipadx=90, ipady=1)
        sali.pack(pady=2, ipadx=98, ipady=1)
        
        self.marco.pack(fill="both", ipady=10)
        
        self.fun_t = fun_t()
        self.btn_pan = self.fun_t.btn_pan
        self.btn_pan.append([acep, sali])  # Underline [[0], [1]]alt_lTecla
        """
        #self.bind("<Alt_L-A>", self.fun_t.alt_lPres)
        #self.bind("<Alt_L-a>", self.fun_t.alt_lPres)
        #eviarATeclado([[<"Alt_L-a">, ]])

        #self.bind("<KeyRelease-Alt_L>", self.fun_t.alt_lSol)
        #self.bind("<KeyPress-Alt_L>", self.fun_t.alt_lPres)
        #self.bind("<KeyRelease-Alt_L>", self.fun_t.alt_lSol)
    
    def segundaEtapa(self):
        self.tema.asige("Ve", "Ini.SSV1", self)
        self.VenPe = VentPe(self, self.salir, self.__init__, self.crearCas)

        self.marco_dos = self.tema.asige("Cu", "Ini.SSC1", self, [None, 100, 50])
        self.marco_dos.pack(pady=20, padx=15)#fill="both")
        self.einicio(True)
        
    def einicio(self, root=False):
        if root:
            self.tema.asige("Et", "Ini.SSE1", self.marco_dos,
                            ["Bienvenido I"]).pack()
        else:
            self.tema.asige("Et", "Ini.SSE2", self.marco_dos,
                            ["Acvertencia"]).pack()
            
    
    def activarBotones(self):
        for nombre in (self.etra_usu, self.etra_cla):
            for evento in ("<Button-2>", "<Button-3>", "<Key-App>"):
                nombre.bind(evento, lambda x: self.asignarPost(x))
    
    def enviarDatosUsuarioG(self):
        return (self.etra_usu.get(), self.etra_cla.get())
    
    def asignarPost(self, evento):

        mi_menu = Menu(master=self, background="#343535", tearoff=0, 
                       relief="flat", activebackground="#878b8b", 
                       activeforeground="#242424")
        
        self.crearCas([["Cortar", None, "Ctrl+X"], ["Copiar", None, "Ctrl+C"], 
                       ["Pegar", None, "Ctrl+P"], ["Limpiar", None, "Ctrl+D"], 
                       ["Seleccionar Todo", lambda: print("asd"), "Ctrl+A"]], 
                      mi_menu, True)

        self.crearCas([["Deshacer", None, "Ctrl+Z"], 
                       ["Rehacer", None, "Ctrl+Shift+Z"]], mi_menu, True)

        self.crearCas(["Acerca de...", None, "Ctrl+Shift+A"], mi_menu)

        mi_menu.tk_popup(evento.x_root, evento.y_root)
    
    def crearCas(self, lista, menu, separador=False):
        if isinstance(lista[0], list):
            for x in lista:
                menu.add_command(label=x[0], command=x[1], accelerator=x[2], 
                                 font=("Courier New", 9))
        
        else:
            menu.add_command(label=lista[0], command=lista[1], 
                             accelerator=lista[2], font=("Courier New", 9))
           
        if separador:
            
            menu.add_separator()
            
    def limpieza(self):
        for c in list(self.children.values()):
            c.destroy()
    
    def salir(self, var, mensaje):
        if var is not None:
            mensaje = messagebox.askyesno("Confirmación", mensaje)
            
            if mensaje:
                self.destroy()
        
        else:
            self.destroy()


class VentPe:
    """ encargado del menu"""

    def __init__(self, ventana, f_cierre, f_inicio, f_cre_m):
        self.padre = ventana
        self.salir = f_cierre
        self.inicio = f_inicio
        self.crearCas = f_cre_m
        self.menu = Menu(self.padre, background="#343535",
                         activebackground="#878b8b", 
                         activeforeground="#242424")

        self.direcion = Menu(self.menu, tearoff=0, background="#343535", 
                             relief="flat", activebackground="#878b8b", 
                             activeforeground="#242424")
        
        #Alt_R        Tk.bind
        self.crearCas(["@", None, "Ctrl+H"], self.menu)
        self.crearCas([["Inicio", None, "Ctrl+I"], ["Sujetos", None, "Ctrl+S"],
                       ["Notas", None, "Ctrl+N"], 
        ["Notificasiones", None, "Ctrl+O"], ["Sobre las Especialidades", None,
                                             "Ctrl+B"]], 
          self.direcion, True)

        self.crearCas([["Usuarios", None, "Ctrl+U"], ["Detalles Sistema", None,
                                                      "Ctrl+D"], 
                       ["Configuración", None, "Ctrl+C"]],
                       self.direcion, True)

        self.crearCas([["Cerrar Sesión", self.cerrarSesion, "Ctrl+E"], 
                       ["Salir", self.salir, "Ctrl+L"]], self.direcion)

        self.menu.add_cascade(label="Ir a", menu=self.direcion, 
                              accelerator="Ctrl+R")
        
        self.crearCas(["Notificasiones", None, "Control+T"], self.menu)

        self.padre.configure(menu=self.menu)
        self.menu.config(bg="yellow")
    
    def cerrarSesion(self):
        self.padre.destroy()
        self.inicio(self.modo)

"""
if __name__ == "__main__":
    from os import chdir, getcwd
    from os.path import basename
    
    if basename(getcwd()) != "SagalTk":
        chdir(getcwd()[:-14])
    
    est = Scargar()
    est.config()
    
    asd = Estilos()
    asd.introducir(est.tema_actual)
    print(asd)
    # print(os.getcwd()[:-18])
    print(getcwd(), basename(getcwd()))
"""