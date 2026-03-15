Produkte = []
Mahlzeiten = []

while True:
    print("\n1) Produkt hinzufügen")
    print("2) Mahlzeit hinzufügen")
    print("3) Produktliste anzeigen")
    print("4) Mahlzeitenliste anzeigen")
    print("5) Tageswerte anzeigen")
    print("6) Beenden")

    auswahl = input("Bitte wähle eine Option (1-6): ").strip()

    if auswahl == "1":
        Name = input("Produkt Name: ")

        while True:
            try:
                Kalorien = float(input("Kalorien auf 100g: ").replace(",", "."))
                break
            except ValueError:
                print("Bitte eine gültige Zahl eingeben.")

        while True:
            try:
                Eiweiß = float(input("Eiweiß auf 100g: ").replace(",", "."))
                break
            except ValueError:
                print("Bitte eine gültige Zahl eingeben.")

        while True:
            try:
                Fett = float(input("Fett auf 100g: ").replace(",", "."))
                break
            except ValueError:
                print("Bitte eine gültige Zahl eingeben.")

        while True:
            try:
                Kohlenhydrate = float(input("Kohlenhydrate auf 100g: ").replace(",", "."))
                break
            except ValueError:
                print("Bitte eine gültige Zahl eingeben.")

        Produkt = {
            "Name": Name,
            "Kalorien": Kalorien,
            "Eiweiß": Eiweiß,
            "Fett": Fett,
            "Kohlenhydrate": Kohlenhydrate
        }

        Produkte.append(Produkt)
        print("Produkt gespeichert.")

    if auswahl == "2":

        Meal_type = ""

        while True:
            print("\n1) Frühstück")
            print("2) Mittagessen")
            print("3) Abendessen")
            print("4) Zurück")

            Meal = input("Bitte wählen eine Option (1-4): ").strip()

            if Meal == "1":
                Meal_type = "Frühstück"
                break

            elif Meal == "2":
                Meal_type = "Mittagessen"
                break

            elif Meal == "3":
                Meal_type = "Abendessen"
                break

            elif Meal == "4":
                break

            else:
                print("Bitte eine gültige Zahl eingeben.")

        if Meal_type != "":

            Food_type = []

            while True:
                print("\n1) Produkt Auswählen")
                print("2) Zurück")

                Food = input("Bitte wähle eine Option (1-2): ").strip()

                if Food == "1":
                    user_input_name = input("Produkt Name: ").strip()

                    Produkt_gefunden = False
                    gespeichert_Produkt = None

                    for product in Produkte:
                        if product["Name"] == user_input_name:
                            Produkt_gefunden = True
                            gespeichert_Produkt = product
                            break

                    if Produkt_gefunden:
                        while True:
                            try:
                                Gramm = float(input("Gramm: ").replace(",", "."))
                                break
                            except ValueError:
                                print("Bitte eine gültige Zahl eingeben.")

                        Mahlzeit_produkt = {
                            "Name": gespeichert_Produkt["Name"],
                            "Gramm": Gramm
                        }

                        Food_type.append(Mahlzeit_produkt)
                        print("Gramm zu Mahlzeit gespeichert.")

                    else:
                        print("Produkt existiert nicht. Bitte zuerst anlegen.")

                elif Food == "2":
                    break

                else:
                    print("Bitte eine gültige Zahl eingeben.")

            if Food_type:
                Mahlzeit = {
                    "Typ": Meal_type,
                    "Produkte": Food_type
                }
                Mahlzeiten.append(Mahlzeit)
                print("Mahlzeit zu Mahlzeiten gespeichert.")

    elif auswahl == "3":
        if not Produkte:
            print("Keine Produkte gespeichert.")
        else:
            print("\nProduktliste:")
            for Produkt in Produkte:
                print("Name:", Produkt["Name"],
                      "| Kalorien:", Produkt["Kalorien"],
                      "| Eiweiß:", Produkt["Eiweiß"],
                      "| Fett:", Produkt["Fett"],
                      "| Kohlenhydrate:", Produkt["Kohlenhydrate"])

    elif auswahl == "4":
        if not Mahlzeiten:
            print("Keine Mahlzeiten gespeichert.")
        else:
            print("\nMahlzeitenliste:")
            for mahlzeit in Mahlzeiten:
                print(mahlzeit["Typ"])
                for product in mahlzeit["Produkte"]:
                    print("  Produkt:", product["Name"],
                          "| Gramm:", product["Gramm"])

    elif auswahl == "5":
        Gesamt_Kalorien = 0
        Gesamt_Eiweiß = 0
        Gesamt_Fett = 0
        Gesamt_Kohlenhydrate = 0

        for mahlzeit in Mahlzeiten:
            for product in mahlzeit["Produkte"]:
                for gespeichertes_produkt in Produkte:
                    if gespeichertes_produkt["Name"] == product["Name"]:
                        faktor = product["Gramm"] / 100
                        Gesamt_Kalorien += gespeichertes_produkt["Kalorien"] * faktor
                        Gesamt_Eiweiß += gespeichertes_produkt["Eiweiß"] * faktor
                        Gesamt_Fett += gespeichertes_produkt["Fett"] * faktor
                        Gesamt_Kohlenhydrate += gespeichertes_produkt["Kohlenhydrate"] * faktor

        tageswerte = {
            "Kalorien": Gesamt_Kalorien,
            "Eiweiß": Gesamt_Eiweiß,
            "Fett": Gesamt_Fett,
            "Kohlenhydrate": Gesamt_Kohlenhydrate
        }

        print("\nTageswerte:")
        for name, wert in tageswerte.items():
            print(f"{name}: {wert:.2f}")

    elif auswahl == "6":
        print("Programm beendet.")
        break

    else:
        print("Bitte eine gültige Option wählen.")