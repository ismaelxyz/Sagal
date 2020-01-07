#!/usr/bin/env python
# -*- coding: utf-8 -*-


from tkinter import *

#ven = Tk(className="Sagal")
#Tk.__call__

#    idlelib_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#    print(idlelib_dir)
#print(os.path.abspath(__file__))
#from platform import system
# sys.__stderr__"""
# TODO FIXME XXX


#mbar.add_cascade(label=label, menu=menu, underline=underline)
#C:\Users\juan\AppData\Local\Programs\Python\Python38-32\Lib\idlelib\editor.py
"""
entry = Entry(ven, width=30)
entry.pack()

def ver(x):
    print(ven.call('tk::GetSelection', entry, 'CLIPBOARD'))
"""

#entry.bind("<Control-c>", ver)

#for veer in ven.children:
#    print(veer)
#ven.mainloop()
"""
#iniciar subclase
class PluginBase:
    subclasses = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.subclasses.append(cls)
        print(cls.subclasses)

class Plugin1(PluginBase):
    pass

class Plugin2(PluginBase):
    pass

obj = Plugin2()
"""

class IntField:
    def __get__(self, instance, owner):
        print("as", instance, owner)
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError(f'expecting integer in {self.name}')
        instance.__dict__[self.name] = value
        print("as2", instance, value)

    # this is the new initializer:
    def __set_name__(self, owner, name):
        self.name = name

class Model:
    int_field = IntField()
    int_field.__get__(str, "ismael")