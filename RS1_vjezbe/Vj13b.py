def maks_i_min(lista):
    if not lista:
        return None  # ako postoji mogućnost da je lista prazna
    # inicijalno postavimo i maksimum i minimum na prvi element liste
    maksimum = minimum = lista[0]
    # petljom prolazimo kroz sve elemente
    for broj in lista:
        if broj > maksimum:  # ako je trenutni broj veći od maksimum, ažuriramo ga
            maksimum = broj
        elif broj < minimum: # ako je manji od minimum, ažuriramo i njega
            minimum = broj

    return (maksimum, minimum) # na kraju vraćamo n-torku (maksimum, minimum)

# Primjer upotrebe:
lista = [5, 10, 20, 50, 100, 11, 250, 50, 80]
print(maks_i_min(lista))  # (250, 5)
