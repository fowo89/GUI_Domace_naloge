# -*- coding: utf-8 -*-
import Tkinter as Tk
import tkMessageBox

pozdrav = "Pozdravljen, sem pretvornik razdalje iz kilometrov v milje in nazaj"
poziv = "Vnesi razdaljo, ki jo želiš pretvoriti:   "

main_window = Tk.Tk()

greeting = Tk.Label(main_window, text=pozdrav)
greeting.pack()

request = Tk.Label(main_window, text=poziv)
request.pack()

wish = Tk.Entry(main_window)
wish.pack()

pretvornik = 1.6

def km_v_mi():
    milje = float(wish.get())/pretvornik
    tkMessageBox.showinfo("Pretvorba iz kilometrov v milje:", str(wish.get()) + " " "km je enako " + str(milje) + " mi!")

def mi_v_km():
    kilometri = float(wish.get()) * pretvornik
    tkMessageBox.showinfo("Pretvorba iz milj v kilometre:", str(wish.get()) + " " "mi je enako " + str(kilometri) + " km!")

button_km = Tk.Button(main_window, text="Pretvorba iz kilometrov v milje", command=km_v_mi)
button_km.pack()

buttom_mi = Tk.Button(main_window, text="Pretvorba iz milj v kilometre", command=mi_v_km)
buttom_mi.pack()





main_window.mainloop()