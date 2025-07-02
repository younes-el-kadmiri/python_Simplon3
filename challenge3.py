stock = ["Stylo", 25, "Classeur", 100, "Crayon", 12, "Surligneur", 40, "Feutre", 5]

print("Liste initiale :", stock)

chaines = []
nombres = []

for i in stock:
    if isinstance(i, str):
        chaines.append(i)
    elif isinstance(i, int):
        nombres.append(i)

chaines.sort()
nombres.sort(reverse=True)

print("Chaines triees :", chaines)
print("Nombres tries (decroissant) :", nombres)
