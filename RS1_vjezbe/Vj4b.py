# Program koji koristi for petlju i prekida unos ako se unese 0

zbroj = 0
max_pokusaja = 10  # korisnik može unijeti najviše 10 brojeva

print(f"Unesi najviše {max_pokusaja} cijelih brojeva (0 za prekid):")

for i in range(max_pokusaja):
    try:
        broj = int(input(f"Unesi broj {i+1}: "))
    except ValueError:
        print("Molim te, unesi cijeli broj!")
        continue  # preskače ovaj unos ako nije broj

    if broj == 0:
        print("Unesena je nula — prekid unosa.")
        break  # izlazak iz for petlje prije kraja

    zbroj += broj

print(f"Zbroj svih unesenih brojeva je: {zbroj}")