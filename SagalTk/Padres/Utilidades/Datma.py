#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Datma (Datos del programa Sagal in Spanish).

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

        Centro de la información de Sagal como programa.
"""
"""
if __name__ == "__main__":
    from os import chdir, getcwd
    from os.path import basename
    
    if basename(getcwd()) != "SagalTk":
        chdir(getcwd()[:-18])
"""

nom_programa = "Sagal"
nom_clave = "Nombre de la Versión Neo Genesis"
n_version = "Version 1.0"
Copyright = "Copyright © 2019 Ismael Belisario"
nom_licencia = "Licensia GPL 3"

licencia = [open("Asuntos Legales/COPYING.txt", "r")]
licencia.append(licencia[0].readlines())
licencia[0].close()
licencia = licencia[1]

autor = "Autor Ismael Belisario"
in_autor = "Ismael Belisario\n" +\
        "Contactame a: ismaelbeli.com@gmail.com"
uso_s = "Uso: Sagal argumento opción."

mensaje_licensia = f"""
                    Sagal

   Copyright © 2019 Ismael Belisario

   Este programa viene ABSOLUTAMENTE SIN 
GARANTÍA; para detalles escriba '-v Licencia'.
Este es un software gratuito y puede 
redistribuirlo bajo ciertas condiciones; escriba
'-v Licencia' para más detalles.

   {uso_s}
   Escriba -a (para mostrar la ayuda)
"""

info_pro = " " * 20 + nom_programa + "\n" +\
           " " * 18 + n_version + "\n" +\
           " " * 9 + nom_clave + "\n" +\
           " " * 9 + Copyright + "\n" +\
           " " * 18 + nom_licencia + "\n" +\
           " " * 14 + autor + "\n"

"""
 u0 = datetime(2016, 11, 6, 4, tzinfo=timezone.utc)
 for i in range(4):
     u = u0 + i*HOUR
     t = u.astimezone(Eastern)
     print(u.time(), 'UTC =', t.time(), t.tzname(), t.fold)

"""
"""
Para resolver errores class Error(Exception) -> class Mierror(Error) 
"""