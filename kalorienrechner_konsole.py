import json


# Listen für gespeicherte Produkte und Mahlzeiten
produkte = []
mahlzeiten = []


# Speichert die Produktliste dauerhaft in einer JSON-Datei
def produkte_speichern():
    with open("produkte.json", "w", encoding="utf-8") as datei:
        json.dump(produkte, datei, ensure_ascii=False, indent=4)


# Lädt die Produktliste aus der JSON-Datei
def produkte_laden():
    global produkte
    try:
        with open("produkte.json", "r", encoding="utf-8") as datei:
            produkte = json.load(datei)
    except FileNotFoundError:
        produkte = []


# Speichert die Mahlzeitenliste dauerhaft in einer JSON-Datei
def mahlzeiten_speichern():
    with open("mahlzeiten.json", "w", encoding="utf-8") as datei:
        json.dump(mahlzeiten, datei, ensure_ascii=False, indent=4)


# Lädt die Mahlzeitenliste aus der JSON-Datei
def mahlzeiten_laden():
    global mahlzeiten
    try:
        with open("mahlzeiten.json", "r", encoding="utf-8") as datei:
            mahlzeiten = json.load(datei)
    except FileNotFoundError:
        mahlzeiten = []


# Fragt eine Zahl ab und akzeptiert Komma oder Punkt
def zahl_eingeben(text):
    while True:
        try:
            return float(input(text).replace(",", "."))
        except ValueError:
            print("Bitte eine gültige Zahl eingeben.")


# Fügt ein neues Produkt zur Produktliste hinzu
def produkt_hinzufuegen():
    name = input("Produktname: ").strip()

    kalorien = zahl_eingeben("Kalorien auf 100 g: ")
    eiweiss = zahl_eingeben("Eiweiß auf 100 g: ")
    fett = zahl_eingeben("Fett auf 100 g: ")
    kohlenhydrate = zahl_eingeben("Kohlenhydrate auf 100 g: ")

    produkt = {
        "Name": name,
        "Kalorien": kalorien,
        "Eiweiß": eiweiss,
        "Fett": fett,
        "Kohlenhydrate": kohlenhydrate
    }

    produkte.append(produkt)
    produkte_speichern()
    print("Produkt gespeichert.")


# Sucht ein Produkt anhand des Namens
def produkt_finden(name):
    for produkt in produkte:
        if produkt["Name"].lower().strip() == name.lower().strip():
            return produkt
    return None


# Zeigt alle gespeicherten Produkte an
def produktliste_anzeigen():
    if not produkte:
        print("Keine Produkte gespeichert.")
        return

    print("\nProduktliste:")
    for produkt in produkte:
        print(
            f'Name: {produkt["Name"]} | '
            f'Kalorien: {produkt["Kalorien"]} | '
            f'Eiweiß: {produkt["Eiweiß"]} | '
            f'Fett: {produkt["Fett"]} | '
            f'Kohlenhydrate: {produkt["Kohlenhydrate"]}'
        )


# Fügt eine neue Mahlzeit hinzu
def mahlzeit_hinzufuegen():
    datum = input("Datum (TT.MM.JJJJ): ").strip()
    mahlzeit_typ = ""

    while True:
        print("\n1) Frühstück")
        print("2) Mittagessen")
        print("3) Abendessen")
        print("4) Zurück")

        auswahl_mahlzeit = input("Bitte wähle eine Option (1-4): ").strip()

        if auswahl_mahlzeit == "1":
            mahlzeit_typ = "Frühstück"
            break
        elif auswahl_mahlzeit == "2":
            mahlzeit_typ = "Mittagessen"
            break
        elif auswahl_mahlzeit == "3":
            mahlzeit_typ = "Abendessen"
            break
        elif auswahl_mahlzeit == "4":
            return
        else:
            print("Bitte eine gültige Zahl eingeben.")

    produkte_der_mahlzeit = []

    while True:
        print("\n1) Produkt auswählen")
        print("2) Zurück")

        auswahl_produkt = input("Bitte wähle eine Option (1-2): ").strip()

        if auswahl_produkt == "1":
            user_input_name = input("Produktname: ").strip()
            gespeichertes_produkt = produkt_finden(user_input_name)

            if gespeichertes_produkt:
                gramm = zahl_eingeben("Gramm: ")

                mahlzeit_produkt = {
                    "Name": gespeichertes_produkt["Name"],
                    "Gramm": gramm
                }

                produkte_der_mahlzeit.append(mahlzeit_produkt)
                print("Produkt zur Mahlzeit hinzugefügt.")
            else:
                print("Produkt existiert nicht. Bitte zuerst anlegen.")

        elif auswahl_produkt == "2":
            break
        else:
            print("Bitte eine gültige Zahl eingeben.")

    if produkte_der_mahlzeit:
        mahlzeit = {
            "Datum": datum,
            "Typ": mahlzeit_typ,
            "Produkte": produkte_der_mahlzeit
        }

        mahlzeiten.append(mahlzeit)
        mahlzeiten_speichern()
        print("Mahlzeit gespeichert.")


# Zeigt alle gespeicherten Mahlzeiten an
def mahlzeitenliste_anzeigen():
    if not mahlzeiten:
        print("Keine Mahlzeiten gespeichert.")
        return

    print("\nMahlzeitenliste:")

    nach_datum = {}

    for mahlzeit in mahlzeiten:
        datum = mahlzeit.get("Datum", "Kein Datum")

        if datum not in nach_datum:
            nach_datum[datum] = []

        nach_datum[datum].append(mahlzeit)

    for datum, mahlzeiten_liste in nach_datum.items():
        print(datum)

        for mahlzeit in mahlzeiten_liste:
            print(" ", mahlzeit["Typ"])

            for produkt in mahlzeit["Produkte"]:
                print(f'   Produkt: {produkt["Name"]} | Gramm: {produkt["Gramm"]}')

        print()


# Berechnet Tageswerte für ein bestimmtes Datum
def tageswerte_fuer_datum():
    datum = input("Datum eingeben (TT.MM.JJJJ): ").strip()

    gesamt_kalorien = 0
    gesamt_eiweiss = 0
    gesamt_fett = 0
    gesamt_kohlenhydrate = 0

    for mahlzeit in mahlzeiten:
        if mahlzeit.get("Datum", "Kein Datum") == datum:
            for produkt in mahlzeit["Produkte"]:
                for gespeichertes_produkt in produkte:
                    if gespeichertes_produkt["Name"] == produkt["Name"]:
                        faktor = produkt["Gramm"] / 100
                        gesamt_kalorien += gespeichertes_produkt["Kalorien"] * faktor
                        gesamt_eiweiss += gespeichertes_produkt["Eiweiß"] * faktor
                        gesamt_fett += gespeichertes_produkt["Fett"] * faktor
                        gesamt_kohlenhydrate += gespeichertes_produkt["Kohlenhydrate"] * faktor

    print(f"\nTageswerte für {datum}:")
    print(f"Kalorien: {gesamt_kalorien:.2f}")
    print(f"Eiweiß: {gesamt_eiweiss:.2f}")
    print(f"Fett: {gesamt_fett:.2f}")
    print(f"Kohlenhydrate: {gesamt_kohlenhydrate:.2f}")


# Berechnet die Gesamtwerte aus allen gespeicherten Mahlzeiten
def tageswerte_anzeigen():
    gesamt_kalorien = 0
    gesamt_eiweiss = 0
    gesamt_fett = 0
    gesamt_kohlenhydrate = 0

    for mahlzeit in mahlzeiten:
        for produkt in mahlzeit["Produkte"]:
            for gespeichertes_produkt in produkte:
                if gespeichertes_produkt["Name"] == produkt["Name"]:
                    faktor = produkt["Gramm"] / 100
                    gesamt_kalorien += gespeichertes_produkt["Kalorien"] * faktor
                    gesamt_eiweiss += gespeichertes_produkt["Eiweiß"] * faktor
                    gesamt_fett += gespeichertes_produkt["Fett"] * faktor
                    gesamt_kohlenhydrate += gespeichertes_produkt["Kohlenhydrate"] * faktor

    print("\nGesamtwerte aus allen gespeicherten Mahlzeiten:")
    print(f"Kalorien: {gesamt_kalorien:.2f}")
    print(f"Eiweiß: {gesamt_eiweiss:.2f}")
    print(f"Fett: {gesamt_fett:.2f}")
    print(f"Kohlenhydrate: {gesamt_kohlenhydrate:.2f}")


# Zeigt das Hauptmenü an
def menue_anzeigen():
    print("\n1) Produkt hinzufügen")
    print("2) Mahlzeit hinzufügen")
    print("3) Produktliste anzeigen")
    print("4) Mahlzeitenliste anzeigen")
    print("5) Gesamtwerte anzeigen")
    print("6) Tageswerte nach Datum anzeigen")
    print("7) Beenden")


# Start: Daten laden
produkte_laden()
mahlzeiten_laden()


# Hauptschleife des Programms
while True:
    menue_anzeigen()
    auswahl = input("Bitte wähle eine Option (1-7): ").strip()

    if auswahl == "1":
        produkt_hinzufuegen()
    elif auswahl == "2":
        mahlzeit_hinzufuegen()
    elif auswahl == "3":
        produktliste_anzeigen()
    elif auswahl == "4":
        mahlzeitenliste_anzeigen()
    elif auswahl == "5":
        tageswerte_anzeigen()
    elif auswahl == "6":
        tageswerte_fuer_datum()
    elif auswahl == "7":
        print("Programm beendet.")
        break
    else:
        print("Bitte eine gültige Option wählen.")