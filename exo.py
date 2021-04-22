# tp: une function pour calculer le nombre de voyelles dans un mot
# definir une fonction get_vowels_numbers(mot)
# créer un compteur de voyelles
# pour chaque lettre du mot vous verifier s'il s'agit d'un voyelle
#si c'est le cas, on ajoute un au compteur
#à la fin de la fonction vous allez renvoyer le compteur

def nombre_voyelle(mot):
    # créer un compteur de voyelles
    nb_voy = 0

    # pour chaque lettre du mot vous verifiez s'il s'agit d'un voyelle
    for letter in mot:
        if letter in ['a', 'e', 'i', 'o', 'u', 'y']:
            # on ajoute un au compteur
            nb_voy += 1

    # à la fin de la fonction, vous allez renvoyer le compteur
    return nb_voy


mot = input("Entrer un mot: ")
voyelles_count = nombre_voyelle(mot)
print("Il y a", voyelles_count, "voyelles dans le mot", mot)