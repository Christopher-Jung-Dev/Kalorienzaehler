import tkinter as tk


# Liste für alle eingegebenen Produkte
produkte = []


# Fügt ein Produkt hinzu und aktualisiert die Anzeige
def klick():
    name = eingabe.get().strip()
    kalorien = kalorien_eingabe.get().strip()
    eiweiss = eiweiss_eingabe.get().strip()
    fett = fett_eingabe.get().strip()
    kohlenhydrate = kohlenhydrate_eingabe.get().strip()

    # Prüfen, ob alle Felder ausgefüllt sind
    if name == "" or kalorien == "" or eiweiss == "" or fett == "" or kohlenhydrate == "":
        ausgabe_label.config(text="Bitte alle Felder ausfüllen!")
        return

    # Prüfen, ob die Nährwerte ganze Zahlen sind
    if not kalorien.isdigit() or not eiweiss.isdigit() or not fett.isdigit() or not kohlenhydrate.isdigit():
        ausgabe_label.config(text="Kalorien, Eiweiss, Fett und Kohlenhydrate muessen Zahlen sein!")
        return

    # Produkt als Dictionary speichern
    eintrag = {
        "name": name,
        "kalorien": int(kalorien),
        "eiweiss": int(eiweiss),
        "fett": int(fett),
        "kohlenhydrate": int(kohlenhydrate)
    }

    produkte.append(eintrag)

    # Gesamtwerte berechnen
    text = ""
    gesamt_kalorien = 0
    gesamt_eiweiss = 0
    gesamt_fett = 0
    gesamt_kohlenhydrate = 0

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

        gesamt_kalorien += p["kalorien"]
        gesamt_eiweiss += p["eiweiss"]
        gesamt_fett += p["fett"]
        gesamt_kohlenhydrate += p["kohlenhydrate"]

    text += (
        "\nGesamt: "
        + str(gesamt_kalorien) + " kcal"
        + " | "
        + str(gesamt_eiweiss) + " g Eiweiss"
        + " | "
        + str(gesamt_fett) + " g Fett"
        + " | "
        + str(gesamt_kohlenhydrate) + " g Kohlenhydrate"
    )

    # Ausgabe aktualisieren
    ausgabe_label.config(text=text)

    # Eingabefelder leeren
    eingabe.delete(0, tk.END)
    kalorien_eingabe.delete(0, tk.END)
    eiweiss_eingabe.delete(0, tk.END)
    fett_eingabe.delete(0, tk.END)
    kohlenhydrate_eingabe.delete(0, tk.END)


# Enter-Taste löst ebenfalls das Hinzufügen aus
def klick_enter(event):
    klick()


# Fenster erstellen
root = tk.Tk()
root.title("Kalorien Tracker")
root.geometry("500x500")


# Überschrift
label = tk.Label(root, text="Produkt hinzufügen")
label.pack()


# Eingabefeld: Produktname
name_label = tk.Label(root, text="Produktname")
name_label.pack()
eingabe = tk.Entry(root)
eingabe.pack()


# Eingabefeld: Kalorien
kalorien_label = tk.Label(root, text="Kalorien")
kalorien_label.pack()
kalorien_eingabe = tk.Entry(root)
kalorien_eingabe.pack()


# Eingabefeld: Eiweiß
eiweiss_label = tk.Label(root, text="Eiweiss")
eiweiss_label.pack()
eiweiss_eingabe = tk.Entry(root)
eiweiss_eingabe.pack()


# Eingabefeld: Fett
fett_label = tk.Label(root, text="Fett")
fett_label.pack()
fett_eingabe = tk.Entry(root)
fett_eingabe.pack()


# Eingabefeld: Kohlenhydrate
kohlenhydrate_label = tk.Label(root, text="Kohlenhydrate")
kohlenhydrate_label.pack()
kohlenhydrate_eingabe = tk.Entry(root)
kohlenhydrate_eingabe.pack()


# Enter-Taste in allen Eingabefeldern aktivieren
eingabe.bind("<Return>", klick_enter)
kalorien_eingabe.bind("<Return>", klick_enter)
eiweiss_eingabe.bind("<Return>", klick_enter)
fett_eingabe.bind("<Return>", klick_enter)
kohlenhydrate_eingabe.bind("<Return>", klick_enter)


# Button zum Hinzufügen
button = tk.Button(root, text="Produkt hinzufügen", command=klick)
button.pack()


# Ausgabefeld
ausgabe_label = tk.Label(root, text="", justify="left", wraplength=450)
ausgabe_label.pack()


# Programm starten
root.mainloop()