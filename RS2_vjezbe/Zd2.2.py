brojevi = [1, 21, 33, 45, 2, 2, 1, -32, 9, 10]

# filter() prima funkciju i kolekciju.
# lambda x: x > 5 vraća True samo za brojeve veće od 5.
# list(...) pretvara rezultat iz filter objekta u listu.
veci_od_5 = list(filter(lambda x: x > 5, brojevi))

print(veci_od_5)  # [21, 33, 45, 9, 10]
