rijeci = [
    "jabuka", "pas", "knjiga", "zvijezda", "prijatelj",
    "zvuk", "čokolada", "ples", "pjesma", "otorinolaringolog"
]

duljine_sa_slovom_a = [len(r) for r in rijeci if "a" in r]
# for r in rijeci prolazi kroz svaku riječ.
#if "a" in r zadržava samo riječi koje sadrže slovo 'a'.
# len(r) računa duljinu te riječi

print(duljine_sa_slovom_a)
# [6, 3, 6, 8, 9, 8, 6, 17]
