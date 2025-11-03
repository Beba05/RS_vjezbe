# Program koji zbraja unesene brojeve dok korisnik ne unese 0

zbroj = 0  # početna vrijednost zbroja
broj = None  # početna vrijednost varijable broj (da uđe u petlju)

print("Unosi cijele brojeve (0 za kraj):")

# Petlja traje dok korisnik ne unese 0
while broj != 0:
    try:
        broj = int(input("Unesi broj: "))
    except ValueError:
        print("Molim te, unesi cijeli broj!")
        continue

    zbroj += broj  # dodaj broj na ukupni zbroj

# Nakon izlaska iz petlje (kad korisnik unese 0)
print(f"Zbroj svih unesenih brojeva je: {zbroj}")