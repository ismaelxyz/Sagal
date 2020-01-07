#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Consola (Interfaz de Consola para Sagal in Spanish).

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

        Control del sistema de interfaz de consola de Sagal, el punto
    central de apollo para la interfaz de consola de ya sabes.
    
        Madre de Main (metaforicamente).
"""

#from Padres.Utilidades.Constantes import *
from Padres.Utilidades.Micrapps import salida, msj_i, msj_e
from Padres.Utilidades.Datma import *
from time import sleep
from tkinter import *


ayuda_comandos = None
salida_m = ""

def verInfo(elemento):
    if elemento == "Nombre":
        print(nom_programa)
    
    elif elemento == "NombreV":
        print(nom_clave)
    
    elif elemento == "Versión":
        print(n_version)
    
    elif elemento == "Copyright":
        print(Copyright)
    
    elif elemento == "NomLicencia":
        print(nom_licencia)
    
    elif elemento == "Licencia":
        for y in range(0, len(licencia) - 1):
            if licencia[y] == "\n":
                print(licencia[y])

            else:
                print(licencia[y].replace("\n", "\r"))
            if y > 0 and y % 19 == 0 and len(licencia) - 1 != y:
                input("--Más--")
        
    elif elemento == "Autor...":
        print(in_autor)
    
    elif elemento == "Autor":
        print(autor)
    
    elif elemento == "InfoP":
        print("\n" + info_pro)
    
    else:
        print("Sagal: Error: Argumento no reconocido: %s." % elemento)
    
    print()


def comaEn(m_ayuda, clase=False, entrada=""):
    """ Comandos de entrada """
    print(mensaje_licensia)

    while True:

        if not entrada:   
            entrada = input(">")
                
        if entrada and not entrada.isspace():
            if entrada in ("-a", "--ayuda"):
                m_ayuda()
                print()
                    
            elif entrada in ("-s", "--salir"):
                salida(0)
                break
                   
            elif len(entrada.split(" ")) in (2, 3):
                entrada = entrada.split(" ")
                        
                if len(entrada) == 3 and entrada[0].isspace():
                    del entrada[0]
                        
                if entrada[0] in ("-v", "--ver"):
                    verInfo(entrada[1])
                        
                elif entrada[0] in ("-m", "--modo") and clase:
                    principal = clase(entrada[1])

                    if principal.retorno:
                        break
                
                elif entrada[0] in ("-m", "--modo") and not clase:
                    print(msj_i % entrada[0])
                        
                else:
                    print(msj_e % entrada[0])
                    
            else:
                print(msj_e % entrada)

        entrada = ""

class Consola:
     
    def __init__(self, mensaj_ay):
        self.mensaj_ay = mensaj_ay
        self.iniciarC()

    def iniciarC(self):
        self.datos_usuario = None #  [random.randint(1, 2)]
        self.menus_app = ["Inicio", "Sujetos", "Notas", "Notificasiones", "Sobre las Especialidades", 
                          "Usuarios", "Detalles Sistema", "Configuración", "Cerrar Sesión", "Salir"]
    
    
    def enviarDatosUsuarioC(self, mensaje_l=True):  # iniciarSeciónConsola

        print("*" * 50 + "\n", " " * 20 + "Bienvenido")
        usuario = clave = ""

        while not usuario:
            usuario = input("\nUsuario: ")
            print()
        
        while not clave:
            clave = input("\nClave: ")
            print()

        return [usuario, clave]
    
    def imprimeMenu(self, menu_m):
    
        print(" " * 23 + "Menu\n\n")
        for y, x in enumerate(menu_m):
      
            if y < 4:
                print(f"{y+1}) " + x[0] + ", ", end=" ")
                
            elif 6 > y >=4:
      
                if y == 4:
                    print()
                print(f"{y+1}) " + x[0] + ", ", end=" ")
      
                if y == 5:
                    print()
                
            elif y == 7:
                print(f"{y+1}) " + x[0] + ".")

            else:
                print(f"{y+1}) " + x[0] + ", ", end=" ")
    
    def modoConsola(self):
        def motrarMenusC():
            for indice, meni in enumerate(self.menus_app):

                if 0 < indice and indice % 4 == 0:
                    print("\n" + str(indice + 1) + ") " + meni, end=" ")
                
                else:
                    print(str(indice + 1) + ") " + meni, end=" ")
        
            print()

        if self.datos_usuario[0] == 1:

            print("*" * 50 + "\n" + " " * 20 + "Bienvenido")
        
        else:
            print("    Si no tiene conocimiento de que es o como\n" +
                  "funciona esta aplicación y este dispocitivo le\n" +
                  "pertenece se le recomienda descintalarla,\n" +
                  "si este dispocitivo no le pertenece se le \n" +
                  "recomienda cerrarla.")
        
            sleep(3)

        print()
        motrarMenusC()

        while True:
            comando = input("\n>")
            if comando.isdecimal() and 1 <= int(comando) <= len(self.menus_app):
                comando = self.menus_app[int(comando) - 1]

            if comando in self.menus_app and comando not in ("Salir", "Cerrar Sesión") :
                self.sub_menus(comando)
            
            elif comando == "Menus":
                motrarMenusC()
            
            elif comando == "Cerrar Sesión":
                print("Reiniciando Sesión")
                return "Reiniciar"
            
            elif comando == "Salir":
                salida(0)
                break
    
    def sub_menus(self, lugar):
        print(lugar)
    
    def mensajesFalloC(self, fallo):
        if fallo == "Dfinal":
            print("Sagal: Error: Demaciados fallos.")
