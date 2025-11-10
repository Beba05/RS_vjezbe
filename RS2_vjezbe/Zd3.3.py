kubovi = [{x: x**3 if x % 2 != 0 else x} for x in range(1, 11)]
# range(1, 11) daje brojeve od 1 do 10.
# x % 2 != 0 provjerava je li broj neparan.
# Ako je neparan → x**3, inače → x.
# Svaki rezultat se pohranjuje u obliku rječnika {x: vrijednost}

print(kubovi)
# [{1: 1}, {2: 2}, {3: 27}, {4: 4}, {5: 125}, {6: 6}, {7: 343}, {8: 8}, {9: 729}, {10: 10}]
