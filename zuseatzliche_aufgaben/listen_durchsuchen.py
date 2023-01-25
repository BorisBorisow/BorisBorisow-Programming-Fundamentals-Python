farben = ["Rot", "Organe", "Gelb", "Grün", "Blau"]
farbeauswahl = ""
while str.upper(farbeauswahl) != "ENDE":
    farbeauswahl = input("Bitte geben Sie eine Farbe ein: ")
    if (farben.count(farbeauswahl) >= 1):
        print("Die Farbe ist in der Liste vorhanden!")
    elif(str.upper(farbeauswahl) != "ENDE"):
        print("Die Farbe kommt in der Liste nicht vor.")