notes = [12, 4, 14, 11, 18, 13, 7, 10, 5, 9, 15, 8, 14, 16]
moyenne = sum(notes) / len(notes)

notes_sup_moyenne = [note for note in notes if note > moyenne]

print("Moyenne :", moyenne)
print("Notes superieures a la moyenne :", notes_sup_moyenne)
