from tkinter import Frame, Tk, Toplevel

class BasePost(Toplevel):
    
    def __init__(self, padre, padre_sup, tema, estilo):
        super().__init__(padre_sup)
        self.tema = tema
        self.estilo = estilo
        self.wm_overrideredirect(1)
        self.cuadro = self.marco()  # Aqui insetas lo que desees
        self.withdraw() # La ventana desaparece
        self.geometry("+%d+%d" % (padre.winfo_rootx(), padre.winfo_rooty() + 20))
    
    def marco(self):
        cuadro = self.tema.asige("Cu", self.estilo, self)
        cuadro.pack()
        return cuadro

    def salir(self, evento=None):
        self.funcion()
        self.destroy()
    
    def mostrar(self):
        self.cuadro.bind("<Leave>", self.salir)
        self.deiconify()
        self.lift()
    
    def veredo(self):
        print("edo")
        return self.elimi
    
    def cargar(self, funcion):
        self.funcion = funcion


class Movimiento:

    def __init__(self, obj, obj_super):
        self.obj = obj
        self.obj_super = obj_super

        self.obj.bind("<ButtonPress-1>", self.iniciar)
        self.obj.bind("<B1-Motion>", self.mover)
        self.obj.bind("<ButtonRelease-1>", self.parar)
    
    def iniciar(self, event):
        print(event.x, "inicie")
        self.ini_x = event.x
        self.ini_y = event.y

    def mover(self, event):
        print(event.x, "movi")
        x = 0
        if event.x >= 0:
            x += 10
        else:
            x -= 10
        x = self.obj.winfo_rootx() + (event.x - self.ini_x)
        y = self.obj.winfo_rooty() + (event.y - self.ini_y)
        self.obj_super.geometry("+%d+%d" % (event.x_root, event.y_root))

    def parar(self, event):
        print(event.x, "pare")
        #self.obj_super.geometry("+%d+%d" % (x, y))
        self.ini_x = 0
        self.ini_y = 0


class Menu(Frame):

    def __init__(self, padre, tema, logo):
        self.padre = padre
        self.logo = logo
       
        self.tema = tema
        super().__init__(master=padre, bg=self.tema["Menu.SSC1"][0], relief=self.tema["Menu.SSC1"][1], 
                         bd=self.tema["Menu.SSC1"][2])
        #self = self.tema.asige("Cu", "Menu.SSC1", self.padre)
        asd = self.spack(self.tema.asige("Et", "Menu.SSE1", self), side="left")
        asd["image"] = self.logo#.put("{black green} {white yellow}", to=(4,6))
        self.bo1 = self.spack(self.tema.asige("BoE", "Menu.SSBoE1", self, ["Ir a", self.irA]), side="left")
        self.bo2 = self.spack(self.tema.asige("BoE", "Menu.SSBoE2", self, ["Ver", lambda: print("hola2")]), side="left")
        self.bo3 = self.spack(self.tema.asige("BoE", "Menu.SSBoE3", self, ["Ayuda", lambda: print("hola3")]), side="left")
        self.bo1
        self.title = self.spack(self.tema.asige("Et", "Menu.SSE2", self, ["Sagal"]), fill="x")#, expand=1
       
        
        #self.bo1.bind("<ButtonPress-1>", self.irA)
        #self.bo2.bind("<ButtonPress-1>", lambda y: self.asignarPost(self.bo2))
        #self.bo3.bind("<ButtonPress-1>", lambda y: self.asignarPost(self.bo3))
        
        #self.padre.wm_overrideredirect(1)
        self.pack(fill="x")
        self.title.bind("<Escape>", lambda x: self.padre.destroy())
        Movimiento(self.title, self.padre)
        self.lift()
        
    def llamada(self, obj):
        if obj == "bo1":
            if self.edos[0] is None:
                self.irA()
                
            return self.edos[0]
        return True
    
    def spack(self, objeto, cnf={}, **kw):
        "Una modificasión del pack de tekinter para Sagal"
        objeto.pack(**kw)

        return objeto
    
    def setTitle(self, new_title):
        self.title["text"] = new_title
    
    def cambio(self, estilo, objeto):
        objeto["bg"] = self.tema[estilo][0]
        objeto["fg"] = self.tema[estilo][4]
        objeto["relief"] = self.tema[estilo][8]
        print("llame")

    def irA(self, evento=None):
        me_nu = BasePost(self.bo1, self.padre, self.tema, "Menu.SSC2")
        nu = 1
        def crear(nu):
            ad = self.spack(self.tema.asige("Cu", f"Menu.SSC{nu + 2}", me_nu.cuadro), fill="x")

            self.tema.asige("BoE2", f"Menu.SSSBoE{nu}", ad, 
                            [i, lambda: print(f"hola{nu}")]).pack(side="left")

        for i in ["Inicio", "Sujetos", "Usuarios", "Notas",
                  "Deralles del sistema", "Configuración", 
                  "Cerrar Sesión", "Salir"]:
            
            crear(nu)
            nu += 1

        me_nu.cargar(lambda: self.cambio("Menu.SSSBoE1", self.bo1))
        me_nu.mostrar()
        #return regresar()
        
        
        # Inicio
        # Sujetos
        # Usuarios
        # Notas
        # Deralles del sistema
        # Configuración
        # Cerrar Sesión
        # Salir

    def ver(self):
        # Panel(Dependiente)
        # Notificasiones
        # Consola del sistema
        # Consola sapy
        pass

    def ayuda(self):
        # Autor
        # Esta versión
        # Aserca de Sagal
        pass

    def eliminarSubmenu(self, submenu):
        submenu.destroy()
    
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


#ven = Tk()
#m_nu = Menu(ven, "as")
#ven.mainloop()
"""
# where the corner of the canvas is relative to the screen:
        x_org = canvas.winfo_rootx()
        y_org = canvas.winfo_rooty()
        # where the pointer is relative to the canvas widget:
        x = event.x_root - x_org
        y = event.y_root - y_org
        # compensate for initial pointer offset
        return x - self.x_off, y - self.y_off

        dx, dy = x2-x1, y2-y1
"""