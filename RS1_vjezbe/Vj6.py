# --- Glavni izbornik programa ---

def zadatak1_for():
    suma = 0
    for i in range(2, 101, 2):
        suma += i
    print("Zbroj parnih brojeva od 1 do 100 je:", suma)

def zadatak1_while():
    suma = 0
    i = 2
    while i <= 100:
        suma += i
        i += 2
    print("Zbroj parnih brojeva od 1 do 100 je:", suma)


def zadatak2_for():
    neparni = [i for i in range(1, 20, 2)]
    print("Prvih 10 neparnih brojeva u obrnutom redoslijedu:")
    for broj in reversed(neparni):
        print(broj)

def zadatak2_while():
    neparni = []
    i = 1
    while len(neparni) < 10:
        neparni.append(i)
        i += 2

    print("Prvih 10 neparnih brojeva u obrnutom redoslijedu:")
    i = len(neparni) - 1
    while i >= 0:
        print(neparni[i])
        i -= 1


def zadatak3_for():
    a, b = 0, 1
    print("Fibonaccijev niz do 1000 (for petlja):")
    print(a)
    print(b)
    for _ in range(2, 100):
        c = a + b
        if c > 1000:
            break
        print(c)
        a, b = b, c

def zadatak3_while():
    a, b = 0, 1
    print("Fibonaccijev niz do 1000 (while petlja):")
    print(a)
    print(b)
    while True:
        c = a + b
        if c > 1000:
            break
        print(c)
        a, b = b, c


# --- Glavna logika programa ---

while True:
    print("\n=== IZBORNIK ===")
    print("1. Zbroj svih parnih brojeva od 1 do 100")
    print("2. Prvih 10 neparnih brojeva u obrnutom redoslijedu")
    print("3. Fibonaccijev niz do 1000")
    print("0. Izlaz")
    
    try:
        izbor = int(input("Odaberi zadatak (0–3): "))
    except ValueError:
        print("Molim te, unesi broj od 0 do 3!")
        continue

    if izbor == 0:
        print("Hvala na korištenju programa! 👋")
        break

    if izbor not in (1, 2, 3):
        print("Nevažeći izbor, pokušaj ponovo.")
        continue

    petlja = input("Želiš li verziju s 'for' ili 'while' petljom? ").strip().lower()

    if izbor == 1:
        if petlja == "for":
            zadatak1_for()
        else:
            zadatak1_while()
    elif izbor == 2:
        if petlja == "for":
            zadatak2_for()
        else:
            zadatak2_while()
    elif izbor == 3:
        if petlja == "for":
            zadatak3_for()
        else:
            zadatak3_while()
