# Fragt eine Zahl vom Nutzer ab (mit Komma oder Punkt möglich)
# und wiederholt die Eingabe, bis eine gültige Zahl eingegeben wurde.
def zahl_eingeben(text):
    while True:
        try:
            return float(input(text).replace(",", "."))
        except ValueError:
            print("Bitte eine gültige Zahl eingeben.")




# Liest ein neues Produkt ein und speichert es in der Produktliste.
def produkt_hinzufuegen():
    name = input("Produkt Name: ").strip()

    kalorien = zahl_eingeben("Kalorien auf 100g: ")

    eiweiss = zahl_eingeben("Eiweiß auf 100g: ")

    fett = zahl_eingeben("Fett auf 100g: ")

    kohlenhydrate = zahl_eingeben("Kohlenhydrate auf 100g: ")


    produkt = {
        "Name": name,
        "Kalorien": kalorien,
        "Eiweiß": eiweiss,
        "Fett": fett,
        "Kohlenhydrate": kohlenhydrate
    }

    produkte.append(produkt)
    print("Produkt gespeichert.")

# Sucht ein Produkt anhand des Namens in der Produktliste
# und gibt das Produkt zurück, falls es gefunden wird, sonst None.
def produkt_finden(name):
    for produkt in produkte:
        if produkt["Name"] == name:
            return produkt
    return None

# Mahlzeit wird eingegeben, gespeichert und zur Liste mahlzeiten hinzugefückt.
def mahlzeit_hinzufuegen():
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
            break
        else:
            print("Bitte eine gültige Zahl eingeben.")

    if mahlzeit_typ != "":
        produkte_der_mahlzeit = []

        while True:
            print("\n1) Produkt auswählen")
            print("2) Zurück")

            auswahl_produkt = input("Bitte wähle eine Option (1-2): ").strip()

            if auswahl_produkt == "1":
                user_input_name = input("Produkt Name: ").strip()

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
                "Typ": mahlzeit_typ,
                "Produkte": produkte_der_mahlzeit
            }
            mahlzeiten.append(mahlzeit)
            print("Mahlzeit gespeichert.")

# zeigt alle gespeicherten Produkte mit Nährwerten.
def produktliste_anzeigen():
    if not produkte:
        print("Keine Produkte gespeichert.")
    else:
        print("\nProduktliste:")
        for produkt in produkte:
            print(
                "Name:", produkt["Name"],
                "| Kalorien:", produkt["Kalorien"],
                "| Eiweiß:", produkt["Eiweiß"],
                "| Fett:", produkt["Fett"],
                "| Kohlenhydrate:", produkt["Kohlenhydrate"]
            )

# Zeigt alle gespeicherten Mahlzeiten mit den enthaltenen Produkten und Grammangaben.
def mahlzeitenliste_anzeigen():
    if not mahlzeiten:
        print("Keine Mahlzeiten gespeichert.")
    else:
        print("\nMahlzeitenliste:")
        for mahlzeit in mahlzeiten:
            print(mahlzeit["Typ"])
            for produkt in mahlzeit["Produkte"]:
                print(
                    "  Produkt:", produkt["Name"],
                    "| Gramm:", produkt["Gramm"]
                )

# berechnet Tageswerte aus allen gespeicherten Mahlzeiten
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

    tageswerte = {
        "Kalorien": gesamt_kalorien,
        "Eiweiß": gesamt_eiweiss,
        "Fett": gesamt_fett,
        "Kohlenhydrate": gesamt_kohlenhydrate
    }

    print("\nTageswerte:")
    for name, wert in tageswerte.items():
        print(f"{name}: {wert:.2f}")

# zeigt die verschiedenen Auswahlmöglichkeiten an.
def menue_anzeigen():
    print("\n1) Produkt hinzufügen")
    print("2) Mahlzeit hinzufügen")
    print("3) Produktliste anzeigen")
    print("4) Mahlzeitenliste anzeigen")
    print("5) Tageswerte anzeigen")
    print("6) Beenden")

# Speichert alle angelegten Produkte
produkte = []

# Speichert alle eingegebenen Mahlzeiten
mahlzeiten = []

while True:
    menue_anzeigen()

    auswahl = input("Bitte wähle eine Option (1-6): ").strip()

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
        print("Programm beendet.")
        break

    else:
        print("Bitte eine gültige Option wählen.")