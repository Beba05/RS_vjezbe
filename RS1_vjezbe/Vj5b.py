for i in range(10, 1, 2):
    print(i)

# ne ispisuje ništa, jer raspon nema nijedan broj koji zadovoljava taj uvjet
# početna vrijednost 10 je veća od granične vrijednosti 1, a korak (2) je pozitivan — što znači da će Python pokušati rasti od 10 prema većim brojevima
# granica je manja (1), pa Python nikada neće ući u petlju, jer uvjet "idemo do 1" ne može biti ispunjen kad krećemo s 10 i rastemo prema gore