import tkinter as tk
import random as rn

def generer_tekst():
    navn = ["Kevin, ", "TC, ", "Jørgen, ", "Khyle, ", "Christian, ", "Are, ", "Maria, ", "Egil, "]
    del1 = ["du er ", "det fremstår som at du er ", "som elev er du ", "jeg er glad for at du er ", "i undervisningen er du "]
    del2 = ["meget ","mest sannsynlig ", "veldig ", "", "sinnsykt ", "ganske ", "flink i å være "]
    del3 = ["oppegående", "arbeidsom", "omsorgsfull", "forståelsesfull", "fornøyd", "inspirerende", "til stede", "kreaktiv", "kompetent", "god medelev", "smart", "tilgivende", "trygg", "empatisk", "klok", "unik", "empatisk"]
    del4 = ["!", "?", ".", "", "!?"]
    tekst.delete(0, "end")
    n = len(navn) - 1
    r = rn.randint(0, n)
    l1 = len(del1) - 1
    r1 = rn.randint(0, l1)
    l2 = len(del2) - 1
    r2 = rn.randint(0, l2)
    l3 = len(del3) - 1
    r3 = rn.randint(0, l3)
    l4 = len(del4) - 1
    r4 = rn.randint(0, l4)
    text = f"{navn[r]}{del1[r1]}{del2[r2]}{del3[r3]}{del4[r4]}"
    tekst.insert(0, text)
    #root.after(5000, generer_tekst)

root = tk.Tk()

tekst = tk.Entry(root, width=50, font = ("Arial", 30))
tekst.pack()

tk.Button(root, text="Trykk her!", font = ("Arial", 20), command=generer_tekst).pack()

root.mainloop()