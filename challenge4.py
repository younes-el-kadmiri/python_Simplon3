def rechercheElement(element, liste):
    for i in range(len(liste)):
        if liste[i] == element:
            return i
    return False

L = [5, 10, 15, 20]
print(rechercheElement(15, L)) 
print(rechercheElement(99, L)) 
