# Program koji traži unos dva broja i operatora

# unos brojeva
broj1 = float(input("Unesi prvi broj: "))
broj2 = float(input("Unesi drugi broj: "))

# unos operatora
operator = input("Unesi operator (+, -, *, /): ")

# računanje prema operatoru
if operator == "+":
    rezultat = broj1 + broj2
    print(f"Rezultat operacije {broj1} + {broj2} je {rezultat}")
elif operator == "-":
    rezultat = broj1 - broj2
    print(f"Rezultat operacije {broj1} - {broj2} je {rezultat}")
elif operator == "*":
    rezultat = broj1 * broj2
    print(f"Rezultat operacije {broj1} * {broj2} je {rezultat}")
elif operator == "/":
    if broj2 == 0:
        print("Dijeljenje s nulom nije dozvoljeno!")
    else:
        rezultat = broj1 / broj2
        print(f"Rezultat operacije {broj1} / {broj2} je {rezultat}")
else:
    print("Nepodržani operator!")