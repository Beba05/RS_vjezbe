def filtriraj_parne(lista):
    parni = []
    for broj in lista:  # petljom prolazimo kroz svaki broj u listi
        if broj % 2 == 0:   # provjeravamo uvjet broj % 2 == 0 — ako je točno, broj je paran
            parni.append(broj)  # takve brojeve spremamo u novu listu 'parni'
    return parni  # funkcija vraća novu listu s parnim brojevima


# Primjer upotrebe:
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(filtriraj_parne(lista))  # [2, 4, 6, 8, 10]
