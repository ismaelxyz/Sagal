#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Sagal (Soberania Global in spanish).

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

       La finalidad de Sagal es
    establecer un nuevo régimen de soberanía global, con la 
    instrumentalización de "Sujetos" creados por ella.

       La finalidad de los Sujetos es ayudar a las personas a nivel
    global en sus vida diaria y servir de instrumento a Sagal para 
    establecer la soberanía global (Sin embargo el creador de Sagal 
    reconoce que la soberanía de Sagal podría impartirse a nivel 
    Universal [Saunil]).
"""

from Padres.Grafico import Ventana
from Padres.Consola import Consola, comaEn, salida, uso_s
from Padres.Utilidades.Micrapps import (crearElemento, os, Scargar, Codígo,
                                        BasesDeDatos)
from Padres.Estilo.Stemas import Estilos
from Utilidades.Utilidades import Sagarmen
from json import dumps, loads

ver_activado = False
m_ayuda = None

class Main(Ventana, Consola):
    """
    Nombre 
           Main (Archivo Principal de Sagal)
        
    Descripsión
           Se encarga de gestionar todos los elementos de Sagal 
        haciendolos trabajar como uno solo.
    """

    def __init__(self, modo):
        from tkinter import PhotoImage        
        self.fallo_usuario = 0
        self.mensaj_ay = m_ayuda
        self.retorno = True
        self.confn = Scargar()  # confn = Configuración general
        self.confn.config()
        self.modo = modo

        if self.modo == "Grafico":
            self.confn.tema()
            ste = Estilos()
            ste.introducir(self.confn.tema_actual)
            super().__init__(self.confn, ste)
            
            self.mainloop()
        
        elif self.modo == "Consola":
            self.iniciarC()
            self.validarUsuario(self.enviarDatosUsuarioC())
        
        elif modo == "Modulo":
            pass

        else:
            print("Sagal: Error: El modo de interacción\n" +
                  "%s no a sido hallado.\n" % self.modo)
            self.retorno = False
        
    
    def validarUsuario(self, datos_u):
        """
            Gestiona el inicio de sesión.
        """

        base = BasesDeDatos("Usuarios", f"Usuarios/Lista.db")
       
        if base.leer("Nombre", datos_u[0]):

            codi = Codígo(base.leer("Nombre", datos_u[0], "Puerta")[0], base.leer("Nombre", datos_u[0], "Clave")[0])
            
            if datos_u[1] == codi.decodificar():
                
                self.datos_usuario = base.leer("Nombre", datos_u[0])

                if self.modo == "Grafico":
                    self.marco.destroy()
                    self.modoGrafico()
                
                elif self.modo == "Consola":
                    self.modoConsola()
                
        base.cerrarBase()

        if not self.datos_usuario:
            self.fallo_usuario += 1
        
        if self.fallo_usuario == 5:
            if self.modo == "Grafico":
                self.mensajesFalloG("Dfinal")

            elif self.modo == "Consola":
                self.mensajesFalloC("Dfinal")
        
        elif self.fallo_usuario < 5 and self.modo == "Consola":
            self.validarUsuario(self.enviarDatosUsuarioC())
    
    def modoConsola(self):
        """
            Inicia la sesión en modo Consola, ademas 
        de volver al inicio de sesión (si asi lo 
        requiere el usuario.
        """
        retorno = super().modoConsola()

        if retorno == "Reiniciar":
            self.iniciarC()
            self.validarUsuario(self.enviarDatosUsuarioC())

    def modoGrafico(self):
        """
            Inicia la sesión en modo Grafico.
        """
        self.usuarioValidadoG()
    
    def estadoSujetos(self, comando="None"):
        """
            Actualiza los estados de cada Sujeto ademas de retornarlos.
        """
        edos_local = {"Activados": [], "Desactivados": [],
                      "Inactivos": [], "Dañados": []}
        
        archivo = crearElemento("a", "Padres/Sujetos/EstadoSjs.json", "r")
        leer = archivo.read()

        pre_ss = loads(leer)
        archivo.close()

        for cuerpo in self.gestorSujetos("vcuerpos"):
            
            if isinstance(pre_ss, dict):
                if cuerpo in pre_ss["Desactivados"]:
                    edos_local["Desactivados"].append(cuerpo)

            if os.path.isdir("Padres/Sujetos/Fisico/" + cuerpo) and cuerpo not in edos_local["Desactivados"]:
        
                if os.path.isfile(f"Padres/Sujetos/{cuerpo}/{cuerpo}.db"):
                    edos_local["Activados"].append(cuerpo)

                else:
                    edos_local["Dañados"].append(cuerpo)
            
            if not os.path.isdir("Padres/Sujetos/Fisico/" + cuerpo) and cuerpo not in edos_local["Desactivados"]:
                edos_local["Inactivos"].append(cuerpo)
        
        if edos_local != leer:
            os.remove("Padres/Sujetos/EstadoSjs.json")
            archi = crearElemento("a", "Padres/Sujetos/EstadoSjs.json", "a")
            archi.write(dumps(edos_local))
            archi.close()

        return edos_local

    def gestorSujetos(self, comando):
        """
            Se encarga de as siguientes gestiones
        con respecto a los Sujetos:
            
            1) Lograr que exista el archivo madre de
               los Sujetos.

            2) Retornar una lista con los cuerpos de 
               los Sujetos.
        """

        crearElemento("a", "Padres/Sujetos/Cuerpos.py")
        sujetos = []

        if comando == "vcuerpos":
            archivo = open("Padres/Sujetos/Cuerpos.py", "r")
            leer = archivo.readlines()

            for bb in leer:
                if bb[:6] == "class " and bb[-2:] == ':\n':
                    sujetos.append(bb[6:-2])
            
            return sujetos
    
        """def __del__(self):
        if self.modo != "Grafico" and self.retorno:
            salida(0)"""


class Recoini:
    """
    Nombre 
           Recoini (Resector de comandos de inicio para Sagal)
    
    Descripción
           Recive los parametros (comandos) de inicio 
        para Sagal y los ejecuta. 
    """
    def __init__(self, comando=None):
        self.comando = comando
    
    def __call__(self, argumento=""):
        global ver_activado
        ver_activado = True

        if self.comando == "-v":
            comaEn(m_ayuda, Main, self.comando + " " + argumento)
        
        elif self.comando == "-m":
            Main(argumento)

    def forzarInicio(self):
        if not ver_activado:
            comaEn(m_ayuda, Main)


def iniciarArgumentos():
    global m_ayuda
    global ver_activado

    parser = Sagarmen("Sagal", usage=uso_s[5:], 
                                     description='Ayuda con el uso de comandos para Sagal')
    
    parser.add_argument('-s', "--salir", dest='salida', action='store_const',
                        const=salida, default=None,
                        help='Salir del Sagal.')
    
    parser.add_argument('-m', "--modo", metavar="modo", type=Recoini("-m"),
                        help='Iniciar Sagal en el modo elejido.')
    
    parser.add_argument('-v', "--ver", metavar="opción", type=Recoini("-v"),
                        help='Mostra la opcion elejida entre [Nombre, NombreV, '+
                        'Versión, Copyright, NomLicencia, Licencia, InfoP, Autor y Autor...].')
    
    
    m_ayuda = parser.print_help
    args = parser.parse_args()
    
    if not args.salida is None:
        ver_activado = args.salida(0)

if __name__ == "__main__":
    pass
    #self.text.tk.call('tk::GetSelection', self.text, 'CLIPBOARD')
    #iniciarArgumentos()
    Main("Grafico")
    #inicio = Recoini()
    #inicio.forzarInicio()
    #print(aa.sujetosDesactivos(), "asd")
    #print(aa.gestorSujetos("vcuerpos"))
    #from Padres.Utilidades import Micrapps
    #print(help(Micrapps))

#from tkinter import filedialog
#openfilename = filedialog.askopenfilename(filetypes=[("all files", "*")])
#saveasfilename = filedialog.asksaveasfilename()