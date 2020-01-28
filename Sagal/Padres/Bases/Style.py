#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Style(dict):

    def __init__(self):
        self.add = self.update
        # self.clear clear dict whit style
    
    def update(self, teme):

        if isinstance(teme, list):
            for style in teme:
               super().update(style)
        else:
            raise ValueError


class CreatedWigets(Style):

    def __init__(self):
        from tkinter import Label, Frame, LabelFrame
        super().__init__(self)
    
    def frame(self, master, name, return_frame=False):
        __s = self[name]  # estilo del tema elegido.
        
        fra = Frame(master, height=__s["height"], width=__s["width"],
        relief=__s["relief"], bg=__s["bg"], bd=__s["bd"])
        
        if return_frame:
            return fra
        
        fra.pack()
    
    def label(self, text=None, return_label=False):
        __s = self[name]  # estilo del tema elegido.
        
        lab = Label(master, height=__s["height"], width=__s["width"],
        relief=__s["relief"], bg=__s["bg"], bd=__s["bd"], text=text)
        
        
        if __s["change"]:#change=None:
            lab.bind("<Enter>", lab.__setitem__("bg", __s["bg"]))
            lab.bind("<Leave>",)
        
        
        if return_label:
            return lab
        
        lab.pack()
    
    def labelButton(self):
        pass
     
    def labelFrame(self):
        pass
      
    def entry(self):
        pass
    
    def text(self):
        pass
    
    def menu(self):
        pass
    
    def buttonMenu(self):
        pass

