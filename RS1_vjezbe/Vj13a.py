def prvi_i_zadnji(lista):
    return (lista[0], lista[-1]) if lista else None  # lista[0] — prvi element liste, lista[-1] — zadnji element liste
    # ( ... , ... ) — vraća n-torku s ta dva elementa
    # ako je lista prazna, funkcija će vratiti None umjesto da izbaci grešku
                                  
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(prvi_i_zadnji(lista))  # (1, 10);    