#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Botones2.py
#  
#  Copyright 2020 fbarb <fbarb@LAPTOP-1D68D5IS>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

from tkinter import *



def sumar():
	r.set(float(n1.get()) + float(n2.get()))
	borrar()
def restar():
	r.set(float(n1.get()) - float(n2.get()))
	borrar()
def multiplicar():
	r.set(float(n1.get()) * float(n2.get()))
	borrar()
def dividir():
	r.set(float(n1.get()) / float(n2.get()))
	borrar()
	
def borrar():
	n1.set("")
	n2.set("")


root=Tk()

root.geometry("200x200")
root.title("Calculadora")
root.resizable(0,0)

n1=StringVar()
n2=StringVar()
r=StringVar()

Label(root, text="Numero 1").pack()
Entry(root, justify="center", textvariable=n1).pack()
Label(root, text="Numero 2").pack()
Entry(root, justify="center", textvariable=n2).pack()




Label(root, text="\nResultado").pack()
Entry(root, justify="center", textvariable=r,state="disabled").pack()

frame=Frame(root)
frame.pack()

Button(frame, text="+",command=sumar).pack(side="left")
Button(frame, text="-", command=restar).pack(side="left")
Button(frame, text="x", command=multiplicar).pack(side="left")
Button(frame, text="/", command=dividir).pack(side="left")






root.mainloop()

def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
