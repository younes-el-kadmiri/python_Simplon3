L = [7, 23, 5, 23, 7, 19, 23, 12, 29]
a = 23

compteur = 0
for i in L:
    if i == a:
        compteur += 1

print(f"Nombre d'occurrences de {a} : {compteur}")
