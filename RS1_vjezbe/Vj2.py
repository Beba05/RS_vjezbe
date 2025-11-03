# Program koji provjerava je li unesena godina prijestupna

godina = int(input("Unesi godinu: "))

# Godina je prijestupna ako je djeljiva s 4, ali ne i s 100,
# osim ako je djeljiva i s 400.
if (godina % 4 == 0 and godina % 100 != 0) or (godina % 400 == 0):
    print(f"Godina {godina}. je prijestupna.")
else:
    print(f"Godina {godina}. nije prijestupna.")