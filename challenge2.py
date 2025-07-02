Ch1 = "Le langage Python est très populaire"
Ch2 = "Python est un langage puissant"

set1 = set(Ch1.lower().split())
set2 = set(Ch2.lower().split())

communs = list(set1 & set2)
print("Mots communs :", communs)
