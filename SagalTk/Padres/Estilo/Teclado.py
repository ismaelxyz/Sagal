#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Teclado (Teclado de Sagal in spanish).

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

       Gestor de eventos del teclado de Sagal.
"""

class Eventec:
    # Eventos del Teclado
    def __init__(self):
        self.btn_pan = []
        self.llamada_f = {}
    
    def iniciarTeclas(self, lista):
        pass
    
    def alt_boton(self, comando, boton):
        if comando == "boton":
            boton.invoke()

    def alt_lPres(self, evento):
            print(evento)
            for idice, l_btn in enumerate(self.btn_pan):
                for btn in l_btn:
                    btn.configure(underline=idice)

        
    def alt_lSol(self, evento):
            
        for l_btn in self.btn_pan:
            for btn in l_btn:
                btn.configure(underline=-1)