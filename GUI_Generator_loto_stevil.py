# -*- coding: utf-8 -*-


import Tkinter as Tk
import tkMessageBox
import random



pozdrav = "Pozdravljeni v generatorju Loto števil!"
poziv = "Prosimo, vnesite število željenih naključnih števil (med 1 in 30): "

main_window = Tk.Tk()

def main():

    def generacija_stevil():
        seznam_stevil = []
        izbira_stevil = int(wish.get())
        for it in range(0, izbira_stevil):
            while True:
                random_stevilo = random.randint(1, 30)
                if random_stevilo not in seznam_stevil:
                    break
            seznam_stevil.append(random_stevilo)
        print seznam_stevil
        tkMessageBox.showinfo("Seznam števil:", seznam_stevil)
        wish.delete(0, Tk.END)

    greeting = Tk.Label(main_window, text=pozdrav)
    greeting.pack()

    request = Tk.Label(main_window, text=poziv)
    request.pack()

    wish = Tk.Entry(main_window)
    wish.pack()

    button = Tk.Button(main_window, text="Potrdi", command=generacija_stevil)
    button.pack()




if __name__ == "__main__":  # this means that if somebody ran this Python file, execute only the code below
    main()






main_window.mainloop()