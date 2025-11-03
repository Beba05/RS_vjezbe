def ukloni_duplikate(lista):
    # Pretvaranje liste u skup uklanja duplikate
    skup = set(lista)  # stvara skup koji ne može sadržavati duplikate
    # Vraćamo natrag listu 
    return list(skup) # vraća rezultat natrag kao listu

# Redoslijed elemenata se može promijeniti jer skup ne pamti redoslijed

# Primjer upotrebe:
lista = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print(ukloni_duplikate(lista))  # [1, 2, 3, 4, 5]