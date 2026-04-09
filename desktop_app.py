import tkinter as tk

produkte = []

def klick():
    name = eingabe.get()
    kalorien = kalorien_eingabe.get()
    eiweiss = eiweiss_eingabe.get()
    fett = fett_eingabe.get()
    kohlenhydrate = kohlenhydrate_eingabe.get()

    if name == "" or kalorien == "" or eiweiss == "" or fett == "" or kohlenhydrate == "":
        ausgabe_label.config(text="Bitte alle Felder ausfüllen!")
        return
    
    if not kalorien.isdigit() or not eiweiss.isdigit() or not fett.isdigit() or not kohlenhydrate.isdigit():
        ausgabe_label.config(text="Kalorien, Eiweiss, Fett und Kohlenhydrate muessen Zahlen sein!")
        return

    eintrag = {
        "name": name,
        "kalorien": int(kalorien),
        "eiweiss": int(eiweiss),
        "fett": int(fett),
        "kohlenhydrate": int(kohlenhydrate)
    }
    
    produkte.append(eintrag)

    text = ""

    for p in produkte:
        text += (
            p["name"]
            + " - "
            + str(p["kalorien"]) + " kcal"
            + " - "
            + str(p["eiweiss"]) + " g Eiweiss"
            + " - "
            + str(p["fett"]) + " g Fett"
            + " - "
            + str(p["kohlenhydrate"]) + " g Kohlenhydrate\n"
        )

    ausgabe_label.config(text=text)

    eingabe.delete(0, tk.END)
    kalorien_eingabe.delete(0, tk.END)
    eiweiss_eingabe.delete(0, tk.END)
    fett_eingabe.delete(0, tk.END)
    kohlenhydrate_eingabe.delete(0, tk.END)

def klick_enter(event):
    klick()

root = tk.Tk()
root.title("Kalorien Tracker")
root.geometry("500x500")

label = tk.Label(root, text="Produkt hinzufügen")
label.pack()

name_label = tk.Label(root, text="Produktname")
name_label.pack()
eingabe = tk.Entry(root)
eingabe.pack()

kalorien_label = tk.Label(root, text="Kalorien")
kalorien_label.pack()
kalorien_eingabe = tk.Entry(root)
kalorien_eingabe.pack()

eiweiss_label = tk.Label(root, text="Eiweiss")
eiweiss_label.pack()
eiweiss_eingabe = tk.Entry(root)
eiweiss_eingabe.pack()

fett_label = tk.Label(root, text="Fett")
fett_label.pack()
fett_eingabe = tk.Entry(root)
fett_eingabe.pack()

kohlenhydrate_label = tk.Label(root, text="Kohlenhydrate")
kohlenhydrate_label.pack()
kohlenhydrate_eingabe = tk.Entry(root)
kohlenhydrate_eingabe.pack()

eingabe.bind("<Return>", klick_enter)

button = tk.Button(root, text="Produkt hinzufügen", command=klick)
button.pack()

ausgabe_label = tk.Label(root, text="")
ausgabe_label.pack()

root.mainloop()