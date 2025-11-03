def validiraj_broj_telefona(broj: str):
    """
    Validacija i parsiranje hrvatskih telefonskih brojeva.
    """

    #  Tablica pozivnih brojeva RH 
    pozivni_brojevi = {
        # FIKSNE MREŽE
        "01": ("Grad Zagreb i Zagrebačka županija", "fiksna mreža", None),
        "020": ("Dubrovačko-neretvanska županija", "fiksna mreža", None),
        "021": ("Splitsko-dalmatinska županija", "fiksna mreža", None),
        "022": ("Šibensko-kninska županija", "fiksna mreža", None),
        "023": ("Zadarska županija", "fiksna mreža", None),
        "031": ("Osječko-baranjska županija", "fiksna mreža", None),
        "032": ("Vukovarsko-srijemska županija", "fiksna mreža", None),
        "033": ("Virovitičko-podravska županija", "fiksna mreža", None),
        "034": ("Požeško-slavonska županija", "fiksna mreža", None),
        "035": ("Brodsko-posavska županija", "fiksna mreža", None),
        "040": ("Međimurska županija", "fiksna mreža", None),
        "042": ("Varaždinska županija", "fiksna mreža", None),
        "043": ("Bjelovarsko-bilogorska županija", "fiksna mreža", None),
        "044": ("Sisačko-moslavačka županija", "fiksna mreža", None),
        "047": ("Karlovačka županija", "fiksna mreža", None),
        "048": ("Koprivničko-križevačka županija", "fiksna mreža", None),
        "049": ("Krapinsko-zagorska županija", "fiksna mreža", None),
        "051": ("Primorsko-goranska županija", "fiksna mreža", None),
        "052": ("Istarska županija", "fiksna mreža", None),
        "053": ("Ličko-senjska županija", "fiksna mreža", None),

        # MOBILNE MREŽE
        "091": (None, "mobilna mreža", "A1 Hrvatska"),
        "092": (None, "mobilna mreža", "Tomato"),
        "095": (None, "mobilna mreža", "Telemach"),
        "097": (None, "mobilna mreža", "bonbon"),
        "098": (None, "mobilna mreža", "Hrvatski Telekom"),
        "099": (None, "mobilna mreža", "Hrvatski Telekom"),

        # POSEBNE USLUGE
        "0800": (None, "posebne usluge", None),
        "060": (None, "posebne usluge", None),
        "061": (None, "posebne usluge", None),
        "064": (None, "posebne usluge", None),
        "065": (None, "posebne usluge", None),
        "069": (None, "posebne usluge", None),
        "072": (None, "posebne usluge", None)
    }

    #  Čišćenje ulaza 
    def ocisti_broj(b):
        for znak in [' ', '-', '(', ')']:
            b = b.replace(znak, '')
        return b.strip()

    broj = ocisti_broj(broj)

    #  Normalizacija međunarodnog formata u oblik s nulom 
    if broj.startswith('+385'):
        broj = '0' + broj[4:]
    elif broj.startswith('00385'):
        broj = '0' + broj[5:]
    elif broj.startswith('385'):
        broj = '0' + broj[3:]

    #  Sada broj uvijek treba počinjati s 0 
    if not broj.startswith('0'):
        broj = '0' + broj  # osiguraj nulu ako fali

    #  Identifikacija pozivnog broja 
    pozivni_broj = None
    for duljina in [4, 3, 2]:
        prefiks = broj[:duljina]
        if prefiks in pozivni_brojevi:
            pozivni_broj = prefiks
            break

    rezultat = {
        "pozivni_broj": pozivni_broj,
        "broj_ostatak": broj[len(pozivni_broj):] if pozivni_broj else broj,
        "vrsta": None,
        "mjesto": None,
        "operater": None,
        "validan": False
    }

    if not pozivni_broj:
        return rezultat

    mjesto, vrsta, operater = pozivni_brojevi[pozivni_broj]
    rezultat["vrsta"] = vrsta
    rezultat["mjesto"] = mjesto
    rezultat["operater"] = operater

    ostatak = rezultat["broj_ostatak"]
    if not ostatak.isdigit():
        return rezultat

    duljina = len(ostatak)
    valjan = False

    if vrsta == "fiksna mreža" and duljina in [6, 7]:
        valjan = True
    elif vrsta == "mobilna mreža" and duljina in [6, 7]:
        valjan = True
    elif vrsta == "posebne usluge" and duljina == 6:
        valjan = True

    rezultat["validan"] = valjan
    return rezultat


print(validiraj_broj_telefona("+385 91 721 7633"))
print(validiraj_broj_telefona("00385(1)2345678"))
print(validiraj_broj_telefona("095-123-4567"))
print(validiraj_broj_telefona("0800123456"))
print(validiraj_broj_telefona("072654321"))

