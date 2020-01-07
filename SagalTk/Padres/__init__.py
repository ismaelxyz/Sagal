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

""" Script encargado de revisar los posibles errores del programa. """

import os
import shutil


carpetas = {"Esto": "carpeta",
            "Nivel 1": ["Asuntos Legales", "Padres", "Padres/Estilos", "Padre/Foresjum"], 
            "Nivel 2": ["Padres/Utilidades", "Padres/Imágenes", "Caos"]}


archivos = {"Esto": "archivo",
            "Nivel 1": ["Mainso.cli", "Sagal.py", "Padres/Consola.py", "Padres/Grafica.py", "Padres/Utilidades/Constantes.py"],
            "Nivel 2": ["Padres/Utilidades/Micrapps.py", "mentira.fi"]}

fallos = []

def guardar(lugar, objecto, clasifi):
    lugar_n = "No"

    for nn in range(len(lugar)):
        if clasifi in lugar[nn]:
            lugar_n = nn

    if str(lugar_n).isdecimal():
        lugar[lugar_n][clasifi].append(objecto)
    
    else:
        lugar.append({clasifi:[objecto]})

for x in (carpetas, archivos):
    fallar = []

    for nivel in ["Nivel 1", "Nivel 2"]:
        
        for objecto in x[nivel]:

            if x["Esto"] == "carpeta" and not os.path.isdir(objecto):
                guardar(fallar, objecto, nivel)

            elif x["Esto"] == "archivo" and not os.path.isfile(objecto):
                guardar(fallar, objecto, nivel)
    
    if fallar:
        fallar.insert(0, x["Esto"])
        fallos.append(fallar)


class AsisFals:
    def __init__(self, no_existe=False):
        """AsisFals -> Asistente de fallos"""
        
        self.no_existe = no_existe

        print("_" * 50 + "\n\n" + " " * 20 + "Bienvenido\n"+ " " * 24 + "al\n" + " " * 16 + "Asistente de Fallos")
        print("\n\n     Si te encuentras aquí es debido a que hay\nuna falla en esta aplicación.\n")
        
        input("    Descuida existen 2 niveles para clasificar\nuna falla:\n>")

        print(" " * 10 + "1) No arreglable.\n" + " " * 10 + "2) Arreglable por desarrolladores.")

        input('\n    En un "instante" se mostrara el\n'+'diacnostico de el o los problemas\n>')
        self.NoEncontrados()
    
    def soluciónManual(self, archivo):
        pass
    
    def NoEncontrados(self):
        for elemento in self.no_existe:
            objeto = elemento[0]
            objeto_n1, objeto_n2 = [], []
            
            for i in elemento[1:]: #  i = Diccionario

                for nivel in i[list(i.keys())[0]]:
                    
                    if list(i.keys())[0] == "Nivel 1":
                        objeto_n1.append(nivel)
                    
                    elif list(i.keys())[0] == "Nivel 2":
                        objeto_n2.append(nivel)

            for numero, lista in enumerate([objeto_n1, objeto_n2]):
                print(self.frases(objeto, len(lista), "encontrar", numero + 1))
                
                for nombre in lista:
                    print(f"    {nombre}")
            
                if lista:
                    self.recomendar(numero + 1, objeto)
                
    def frases(self, palabra, conteo, comando, nivel):
        if comando == "encontrar":
            
            frase = "%s siguiente%s de nivel %s no fue%s allad%s:"

            if conteo == 1 and palabra == "carpeta":
                return frase % ("    La", " " + palabra, nivel, "", "a")
            
            elif conteo > 1 and palabra == "carpeta":
                return frase % ("    Las", "s " + palabra + "s", nivel, "ron", "as")
            
            elif conteo == 1 and palabra == "archivo":
                return frase % ("    El", " " + palabra, nivel, "", "o")
            
            elif conteo > 1 and palabra == "archivo":
                return frase % ("    Los", "s " + palabra + "s", nivel, "ron", "os")
        
            else:
                return ""
    
    def recomendar(self, nivel, elemento):
        print(" " * 18 + "Recomendaciones\n")
        los_las = "Los"

        def decisiones(a_decidir):
            a_decidir_texto = ""

            for x in a_decidir:
                a_decidir_texto += x + ", "
            
            a_decidir_texto = a_decidir_texto[:-2]

            while True:
                decision = input(f"¿Deseo, {a_decidir_texto}, Continuar o Salir?\n>")
                
                if decision == "Salir":
                    salida(1)
                
                elif decision == "Continuar":
                    break

                elif decision == "Desintalar" in a_decidir:
                    print("Desintalación en proceso.\n")

                    try:
                        rmtree(os.path.dirname(os.path.split(__file__)[0]))
                        
                    except:
                        print("    La desintalación no fue satisfactoria,")
                        print("elimine manuealmente la carpeta:\n")
                        print(os.path.dirname(os.path.split(__file__)[0]))

                    else:
                        print("Desintalación Satisfactoria.")
                    salida(1)
                
                elif decision == "Solucionar" in a_decidir:
                    self.soluciónManual(elemento)
        
        if nivel == 1:
            if elemento == "carpeta":
                los_las = "Las"

            print(f"    {los_las} {elemento}s de nivel 1 no tienen\n" +
                   "reparación y son vitales para el programa.\n" +
                   "Deverias desintalar el programa.\n")
           
            decisiones(["Desintalar"])
        
        elif nivel == 2 and elemento != "carpeta":
            print(f"    {los_las} {elemento}s de nivel 2 tienen reparación,\n" +
                   "preferiblemente debe ser llevada a cabo por un\n" +
                   "esperto. El programa no funcionara correctamen, el\n" +
                   "problema debe ser solucionado.\n")
            
            decisiones(["Desintalar", "Solucionar"])


if fallos:
    if __name__ == "__main__":
        AsisFals(fallos)