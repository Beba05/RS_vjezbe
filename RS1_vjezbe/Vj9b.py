# koristi skup za provjeru ponavljanja, ali zadržava originalni redoslijed elemenata

def ukloni_duplikate(lista):
    novi = []
    vidjeni = set()
    for x in lista:
        if x not in vidjeni:
            novi.append(x)
            vidjeni.add(x)
    return novi


# Primjer upotrebe:
lista = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print(ukloni_duplikate(lista))  # [1, 2, 3, 4, 5]