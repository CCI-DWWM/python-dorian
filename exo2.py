"""
Créez une liste contenant les carrés des nombres entre 1 et 10 (inclus).
"""

s = 0
n = 1

for l in range(1, 11) :
    s = n * n
    n = n +1
    print(f'- {s=}')

