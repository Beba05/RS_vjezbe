# Napravimo rječnik rezultat s dva ključa:
# 'parni' → lista parnih brojeva
# 'neparni' → lista neparnih brojeva

# Petljom prolazimo kroz svaki broj:
# ako je broj djeljiv s 2 (broj % 2 == 0), dodajemo ga u listu 'parni'
# inače ide u 'neparni'

def grupiraj_po_paritetu(lista):
    rezultat = {'parni': [], 'neparni': []}

    for broj in lista:
        if broj % 2 == 0:
            rezultat['parni'].append(broj)
        else:
            rezultat['neparni'].append(broj)

    return rezultat


# Primjer upotrebe:
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(grupiraj_po_paritetu(lista))
