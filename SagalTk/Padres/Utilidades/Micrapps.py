#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Micrapps (Micro Aplicasiones para Sagal in spanish).

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

    
       Conjunto de micro aplicaciones con el fin de servir
    de soporte a los padres de Sagal (Consola y Grafico.
    Por extención tambien sirven de ayuda a sagal).
"""

#import shutil
from time import strftime
import os
#from py_compile import compile
#import random
#import sys

msj_e = "Sagal: Error: No se reconoce el comando: %s.\n"
msj_i = "Sagal: Información: Comando no disponible: %s.\n"


class BasesDeDatos:
    """
    Nombre
            BasesDeDatos (Gestor de Base de Datos para Sagal)
    
    Descripción
            Servil de soporte a Sagal como su gestor
        (Controlador si es posible) de bases de
        datos.
    """
    def __init__(self, base_n, ruta, info_t=None, tabla=None):
        import sqlite3


        self.base_n = base_n
        self.ruta = ruta
        self.nombre_archivo = os.path.basename(self.ruta)
        self.info_t = info_t #  Información de la tabla

        if tabla:
            self.tabla = self.tabla
        
        else:
            self.tabla = self.nombre_archivo.replace(".db", "")
        
        crearElemento("c", os.path.dirname(self.ruta))

        if not os.path.isfile(self.ruta):
            self.base = sqlite3.connect(self.ruta)
            self.cursor = self.base.cursor()
            self.crearBase()

        self.base = sqlite3.connect(self.ruta)
        self.cursor = self.base.cursor()

    def crearBase(self):
        if self.base_n == "Usuarios":
            self.cursor.execute(f"""CREATE TABLE IF NOT EXISTS {self.tabla}(
                                    Id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                    Nombre TEXT NOT NULL UNIQUE, 
                                    Clave TEXT NOT NULL,
                                    Puerta INTEGER NOT NULL, Nota TEXT)""")
            
        elif self.base_n == "Sujetos":
            self.cursor.execute(f"""CREATE TABLE IF NOT EXISTS {self.tabla}(
                                    Nombre1 TEXT NOT NULL UNIQUE, 
                                    Nombre2 TEXT NOT NULL UNIQUE,
                                    Apellidos TEXT NOT NULL, 
                                    Alias TEXT NOT NULL UNIQUE, 
                                    Aplicación TEXT NOT NULL,
                                    Nacimiento TEXT NOT NULL,
                                    Estado TEXT NOT NULL,
                                    Nivel TEXT NOT NULL, 
                                    Tiempo_trabajo INTEGER NOT NULL,
                                    Pruebas_ejecutadas INTEGER NOT NULL, 
                                    Pruebas_exitosas INTEGER NOT NULL, 
                                    Pruebas_erroneas INTEGER NOT NULL, 
                                    Ponderación INTEGER NOT NULL, 
                                    Especializaciones TEXT, 
                                    Notas TEXT)""")
            
        elif self.base_n == "Respaldo":
            self.cursor.execute(f"""CREATE TABLE IF NOT EXISTS {self.tabla}(Id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                                            Nombre TEXT NOT NULL UNIQUE,
                                                                            Datos TEXT NOT NULL UNIQUE)""")
            pass

        self.cerrarBase()

    
    def escribir(self, tupla):
        
        if self.base_n == "Usuarios":
          
            self.cursor.execute(f'insert into {self.tabla}(Nombre, Clave,' +\
                                 'Puerta, Nota) values(?, ?, ?, ?)', tupla)

        elif self.base_n == "Sujetos":
            
            self.cursor.execute(f'insert into {self.tabla}('+
                                 'Nombre1, Nombre2, Apellidos, Alias,' +
                                 'Aplicación, Nacimiento, Estado, Nivel,'+
                                 'Tiempo_trabajo, Pruebas_ejecutadas,' +
                                 'Pruebas_exitosas, Pruebas_erroneas,'+
                                 'Ponderación, Especializaciones, Notas)' +
                                f'values({"?, " * 14 + "?"})', tupla)
        
        elif self.base_n == "Respaldo":
            self.cursor.execute(f'insert into {self.tabla}(Nombre, Datos) values(?, ?)', tupla)
        
    def leer(self, columna="", odjeto="", selecionados=""):
        # XXX Recuerda enviar la tupla entre parentesis y "'xxxx'"

        if selecionados and selecionados != "*":
            self.cursor.execute(f'SELECT {selecionados} FROM {self.tabla} WHERE {columna}="{odjeto}"')
        
        elif selecionados == "*":
            self.cursor.execute(f'SELECT {selecionados} FROM {self.tabla}')
            fila = self.cursor.fetchall()
            
            dicci = {}

            if fila:
                for x in fila:
                    dicci.update({x[1]: x[2]})

                return dicci

        else:
            self.cursor.execute(f'SELECT * FROM {self.tabla} where {columna}="{odjeto}"')
        
        fila = self.cursor.fetchall()

        if fila:
            return list(fila[0])
    
    def actualizar(self, columna_ac, objeto_ac, columna, objeto):
        # XXX Recuerda que Where existe set se actualizara
        self.cursor.execute(f'UPDATE {self.tabla} SET {columna_ac}="{objeto_ac}" where {columna}="{objeto}"')
    
    def eliminar(self, columna, objeto):
        self.cursor.execute(f"DELETE FROM {self.tabla} WHERE {columna}='{objeto}'")

    def cerrarBase(self):
        self.base.commit()
        self.cursor.close()
        self.base.close()


class Codígo:
    """
    Nombre
            Codígo (Servicio de Codificación y
        decodificasion para Sagal)
    
    Descipción
            Codifica y decodifica los datos de Sagal.
    """

    def __init__(self, numero, codigo_a_trabajar):

        self.codigo = codigo_a_trabajar 
        self.numero = numero

        self.letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "m", "n", "ñ", 
                       "o", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
        self.numeros = ["0BA", "0AB", "0BB", "0AA", "0BC", "0AC", "0CA", "0CB", "0CC", "0DA"]

    def codificar(self):
        codigo_final = ""

        for a in self.codigo:

            if a.lower() in self.letras:

                indice = self.letras.index(a.lower())
                
                for b in range(0, self.numero + 1):

                    if indice == len(self.letras) - 1:
                        indice = 0
                    
                    else:
                        indice += 1
                
                codigo_final += self.retornarLetra(a, indice)
            
            elif a.isdecimal():
                codigo_final += self.numeros[int(a)]
            
            else:
                codigo_final += a

        
        return codigo_final

    def decodificar(self):
        codigo_final = ""
        _continuar = -1

        for x, a in enumerate(self.codigo):

            if a.lower() in self.letras and _continuar == -1:

                indice = self.letras.index(a.lower())
                
                for b in range(0, self.numero + 1):

                    if indice == 0:
                        indice = len(self.letras) - 1
                    
                    else:
                        indice -= 1

                codigo_final += self.retornarLetra(a, indice)
            
            elif a == "0":
                codigo_final += str(self.numeros.index(self.codigo[x:x+3]))
                _continuar += 1
                
            
            elif 1 > _continuar > -1:
                _continuar += 1
            
            elif _continuar == 1:
                _continuar -= 2
            
            else:
                codigo_final += a

        
        return codigo_final      

    def retornarLetra(self, letra, indice):

        if letra.isupper():
            return self.letras[indice].lower()

        else:
            return self.letras[indice].upper()

def fecha():
    
    día = strftime("%A")
    mes = strftime("%B")

    días = {"Monday":"Lunes", "Tuesday":"Martes", "Wednesday":"Miércoles",
            "Thursday":"Jueves", "Friday":"Viernes", "Saturday":"Sábado", 
            "Sunday":"Domingo"}
    
    meses = {"January":"Enero", "February":"Febrero", "March":"Marzo", 
             "April":"Abril", "May":"Mayo", "June":"Junio", "July":"Julio",
             "August":"Agosto", "September":"Septiembre", "October":"Octubre",
             "November":"Noviembre", "December":"Diciembre"}

    return "%s %s de %s del %s hora: %s" %\
           (días[día], strftime("%d"), meses[mes], strftime("%Y"), strftime("%X"))

def traducirTipo(tipo):
    
    if isinstance(tipo, str):
        tipo = "un texto"
    
    elif isinstance(tipo, int):
        tipo = "un entero"
    
    elif isinstance(tipo, dict):
        tipo = "un diccíonario"
    
    elif isinstance(tipo, bool):
        tipo = "un booleano"
    
    elif isinstance(tipo, float):
        tipo = "un flotante"
    
    elif isinstance(tipo, type):
        tipo = "una clase"

    return tipo

def creArPy(archivo):
    """
       Crea archivos tipo py con las carapteristicas que
    Sagal necesita.
    """
    bas = BasesDeDatos("Respaldo", archivo)

    info = bas.leer(selecionados="*")
    archivo_e = open(archivo, "w", encoding="utf-8")
    archivo_e.write(info[archivo])
    archivo_e.close()

    bas.cerrarBase()
    
def crearElemento(tipo, odjeto, modo="w"):

    def crearCarpeta(carpeta):
        if not os.path.isdir(carpeta):
            os.makedirs(carpeta)
    
    if tipo == "c": #  c = carpeta
        crearCarpeta(odjeto)

    elif tipo == "a": # a = archivo
        if "/" in odjeto:
            crearCarpeta(os.path.dirname(odjeto))
        
        if not os.path.isfile(odjeto):
            if odjeto[-3:] != ".py":
                archivo = open(odjeto, "w", encoding="utf-8")
                archivo.close()
            
            else:
                creArPy(odjeto)
        
        elif modo != "w":
            archivo = open(odjeto, modo, encoding="utf-8")
            if odjeto[-5:] == ".json" and modo == "r":
                from json import loads
                from json.decoder import JSONDecodeError
                lectura = archivo.read()
                archivo.close()
                return loads(lectura)
                try:
                    pass
                except JSONDecodeError:
                    print("Error: Archivo basio")
                    return ""
                    
            return archivo

def editarSj(sujeto, variable, nuevo_v):
    # XXX Cuidado con el str '"Ejemplo"'
    archivo = open("Padres/Sujetos/Cuerpos.py", "r")
    leer = archivo.readlines()
    archivo.close()

    indices = {"Nombre":4, "Apellidos":5, "Alias":6, "Aplicación":7, 
               "Nacimiento":8, "Estado":9, "Nivel":10, "Tiempo_trabajo":11, 
               "Pruebas_ejecutadas":12, "Pruebas_exitosas":13, 
               "Pruebas_erroneas":14, "Ponderación":15, "Especializaciones":16, 
               "Notas":17}

    indice1 = leer.index(f"class {sujeto}:\n") + indices[variable]
    indice2 = leer[indice1][:leer[indice1].index("=") + 2]

    if nuevo_v.isdecimal():
        leer[indice1] = indice2 + nuevo_v + "\n"

    else:
        leer[indice1] = indice2 + f'"{nuevo_v}"' + "\n"
    
    archivo = open("Padres/Sujetos/Cuerpos.py", "w")
    archivo.writelines(leer)
    archivo.close()


class Scargar:
    """ Carga configuración de Sagal"""
    def __init__(self):
        from Padres.Utilidades.Micrapps import crearElemento
        #  c = carpeta
        #  a = archivo
        self.a_confi = "Padres/Conf.json"
        self.c_temas = "Padres/Estilo/Temas/"
        self.cre_ele = crearElemento
        self.tema_actual = None
        self.nombre_tema = None
        self.conf_actual = None
        self.modo_actual = None
        self.nivelt_actual = None  # Nivel de trabajo
        self.loc_tema = None  # Localizacion tema
    
    def config(self, devolver=True):
        confi = self.cre_ele("a", "Padres/Conf.json", "r")
        if confi:
            self.loc_tema = self.c_temas + confi["Tema"] + "/"
            self.nombre_tema = confi["Tema"]
            self.modo_actual = confi["Modo"]
            self.nivelt_actual = confi["Nivel"]
            self.conf_actual = True
        
        else:
            print("Recuerda recrear archivo")
    
    def tema(self, ver=False):
        if self.conf_actual:
            
            confi = self.cre_ele("a", self.loc_tema + "Activar.json", "r")
            carga = []
            for i in confi:
                i = self.loc_tema + i
                carga += self.cre_ele("a", i, "r")

            self.tema_actual = carga
            
            if ver:
                return carga
        else:
            print("sin_conf")


def salida(numero):
    
    if numero == 1:
        exit("\nAdíos")
    
    else:
        print("\nAdíos")
    
    return True

if __name__ == "__main__":
    if os.path.basename(os.getcwd()) != "SagalTk":
        os.chdir(os.getcwd()[:-18])
    
    #bvc = BasesDeDatos(base_n="Respaldo", ruta="Padres/Utilidades/Respaldo.db")
    #bvc.escribir(("gty", "hyt",  "Resurection aa", "qjuy", "Nose", 0, 2, "Nunca", 0, 0, 0, "BajaM", "g2", 4, "", ""))
    
    #archivo = open("Padres/Sujetos/Cuerpos.py", "r")
    #leer = archivo.read()
    #bvc.escribir(("Padres/Sujetos/Cuerpos.py", leer))
    
    #codi = Codígo(109, "123Z<a")
    #bvc.escribir(("Ismael", codi.codificar(), 109, ""))
    #codi1 = Codígo(219, "1234a")
    #bvc.escribir(("Prueba", codi1.codificar(), 219, ""))
    #codi2 = Codígo(139, "a1234")
    #bvc.escribir(("Soin", codi2.codificar(), 139, ""))

    #print(bvc.leer(selecionados="*")["Padres/Sujetos/Cuerpos.py"])

    #print(bvc.leer("Nombre", 'Prueba'))
    #print(bvc.leer("Nombre", 'Soin'))
    #print(bvc.leer("Nombre", "Ismael"))

    #print(bvc.leer("Nombre", "Ismael"))
    """bvc.actualizar("Nota", "", "Nombre", "Ismael")
    bvc.actualizar("Nota", "", "Nombre", "Prueba")
    bvc.actualizar("Nota", "", "Nombre", "Soin")
    """
    #bvc.cerrarBase()
