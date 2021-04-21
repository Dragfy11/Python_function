
def next_year():
    #pour inclure le year dans une function, on utilise global
    global year
    print("Fin de l'année", year)
    year += 1
    print("Début de l'année", year)


year = 2021
next_year()
next_year()
