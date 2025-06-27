"""Créer une fonction est_premier(N) qui retourne True si le nombre passé est premier, False sinon."""

def premier():
    n = int(input("Entrez un nombre : "))

    if n<=1:
        print("pas premier")

    for i in range (2, n):
        if n % i == 0:
            print("pas premier, divisible par ", i)
    print("c'est un nombre premier")