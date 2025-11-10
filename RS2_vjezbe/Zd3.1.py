parni_kvadrati = [x**2 for x in range(20, 51) if x % 2 == 0]
# range(20, 51) daje sve brojeve od 20 do 50 uključivo.
# Uvjet if x % 2 == 0 zadržava samo parne brojeve.
# Svaki od tih brojeva se kvadrira pomoću x**2

print(parni_kvadrati)
# [400, 484, 576, 676, 784, 900, 1024, 1156, 1296, 1444, 1600, 1764, 1936, 2116, 2304, 2500]
