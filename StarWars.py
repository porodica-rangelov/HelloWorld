# Baza podataka sa likovima i njihovim statistikama
likovi = {
    "Anakin Skywalker": {"snaga": 9, "brzina": 8, "sila": 9},
    "Obi-Wan Kenobi": {"snaga": 8, "brzina": 7, "sila": 9},
    "Darth Vader": {"snaga": 10, "brzina": 6, "sila": 10},
    "Yoda": {"snaga": 8, "brzina": 9, "sila": 10},
    "Darth Maul": {"snaga": 9, "brzina": 9, "sila": 7},
    "Luke Skywalker": {"snaga": 8, "brzina": 8, "sila": 9},
    "Count Dooku": {"snaga": 9, "brzina": 7, "sila": 9},
    "Kylo Ren": {"snaga": 8, "brzina": 7, "sila": 8},
    "Rey": {"snaga": 7, "brzina": 8, "sila": 8},
    "Mace Windu": {"snaga": 9, "brzina": 8, "sila": 9},
    "Emperor Palpatine": {"snaga": 8, "brzina": 6, "sila": 10},
    "Rick the Door Technician": {"snaga": 10, "brzina": 10, "sila": 10},
    "General Grievous": {"snaga": 9, "brzina": 8, "sila": 0},
    "Cal Kestis": {"snaga": 8, "brzina": 8, "sila": 8},
    "Captain Rex": {"snaga": 8, "brzina": 8, "sila": 0},
    "Commander Cody": {"snaga": 8, "brzina": 7, "sila": 0},
    "Ahsoka Tano": {"snaga": 8, "brzina": 9, "sila": 8},
    "Plo Koon": {"snaga": 8, "brzina": 7, "sila": 8},
    "Djordje Rangelov": {"snaga": 5, "brzina": 7, "sila": 6},
   "Darija Milcic": {"snaga": 4, "brzina": 7, "sila": 5} 
   }

# Unos dva lika od korisnika
prvi = input("Unesi ime prvog lika: ")
drugi = input("Unesi ime drugog lika: ")

# Provera da li oba lika postoje u bazi podataka
if prvi in likovi and drugi in likovi:
    # Racunanje ukupnog skora za oba lika
    prvi_skor = sum(likovi[prvi].values())
    drugi_skor = sum(likovi[drugi].values())
    
    # Ispis rezultata
    print(f"\n{prvi} ima skor {prvi_skor}")
    print(f"{drugi} ima skor {drugi_skor}")
    
    # Poredjenje i proglašenje pobednika
    if prvi_skor > drugi_skor:
        print(f"Pobednik je: {prvi}!")
    elif drugi_skor > prvi_skor:
        print(f"Pobednik je: {drugi}!")
    else:
        print("Nereseno je!")
else:
    print("Jedan ili oba lika nisu u bazi podataka.")

