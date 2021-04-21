# creer une function max() qui va renvoyer le réulatat le plus haut parmis 2 valeurs
def max(a,b):
    if a > b:
        return a
    else:
        return b

value_one = int(input("entrer la valeur de a (la premiere)"))
value_two = int(input("entre la valeur de b (la seconde)"))
value_max = max(value_one, value_two)
print("la valeur max est",max(value_one, value_two))