"""
Écrivez un programme qui demande à l'utilisateur de saisir une phrase,
puis compte et affiche le nombre de voyelles (a, e, i, o, u, y) et consonnes dans la
phrase.
"""

p = input('Ecrit une phrase :').lower()
c = 0
v = 0
voyelles = ['a', 'e', 'i', 'o', 'u', 'y', 'à', 'â', 'ä', 'é', 'è', 'ê', 'ë', 'î', 'ï', 'ô', 'ö', 'ù', 'û', 'ü', 'ÿ']
consonnes = ['z', 'r']

for letter in p :
    if letter in voyelles :
        v = v +1
    if letter in consonnes :
        c = c +1

print (f'Il y a {v} voyelles et {c} consonnes')