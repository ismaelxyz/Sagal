#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Grafico (Interfaz Grafica de Sagal in Spanish).

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

       Control del sistema de interfaz grafica de Sagal, el punto
    central de apollo para las interfazes graficas de ya sabes.

       Padre de Main (tanto metaforica como realmente).
"""

#from Padres.Utilidades.Micrapps import *
#from Padres.Utilidades.Constantes import *
#from Padres.Utilidades.Datma import *
from Padres.Estilo.General import Sesión, messagebox
from Padres.Estilo.Teclado import Eventec


class Ventana(Sesión):

    def __init__(self, confg, tema):
        super().__init__(Eventec, tema)
        
        self.protocol("WM_DELETE_WINDOW", self.salir)
        self.datos_usuario = None
        self.fallo_usuario = 0

    def enviarDatosUsuarioG(self):
        usu_clave = super().enviarDatosUsuarioG()

        if not usu_clave[0] or not usu_clave[1]:
            self.mensajesFalloG("cfaltate")

        else:
            self.validarUsuario(usu_clave)
    
    def validarUsuario(self, usu_clave):
        pass

    def usuarioValidadoG(self):
        self.limpieza()
        self.geometry("700x500+200+100")
        self.resizable(True, True)
        self.asignabos()
        self.segundaEtapa()

    def sesion(self, inicio=False):
        # Reiniciamos o Iniciamos  # XXX Hacerlo tambien en Consola
        self.datos_usuario = None


    def asignabos(self):
        # XXX asignaraccionBotones
        pass
    
    def commutarPanel(self):
        pass
    
    def salir(self):
        super().salir(self.datos_usuario, "¿Quieres salir de Sagal ahora?")
    
    def mensajesFalloG(self, fallo, cerra=False):
        if self.fallo_usuario == 5:
            fallo = "Dfinal"

        if fallo == "Dfinal":
                messagebox.showerror("Error del Usuario", 
                                     "Sagal se cerrara, debido a demaciados" +\
                                     " fallos.")
                self.destroy()

        elif fallo == "cfaltate":
            self.fallo_usuario += 1
            messagebox.showerror("Error del Usuario", "Rellene el campo " +\
                                 "faltante.")
            
            
"""

if __name__ == "__main__":
    # Eval
    print(os.getcwd())
    " ""
    os.chdir("Padres")
    Ventana()
 """