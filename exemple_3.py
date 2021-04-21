
def addition1():
    result = 5 + 5
    return result


def addition(n = 35):
    result = 5 + n
    return result


def multiply():
    return 5 * 5


def get_message():
    return "le résulat du calcul est"


print(get_message(), multiply())
print("le résulat du calcul est", addition1())
print("le résulat du calcul est", addition())
print("le résulat du calcul est", addition(4))
print("le résulat du calcul est", addition(5))
print("le résulat du calcul est", addition(9))
