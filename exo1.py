"""
Exercice :
Demandez à l’utilisateur de saisir son PRENOM, puis son NOM, et enfin,
son année de naissance
Afficher « Bonjour PRENOM NOM, vous avez XX ans. »
"""

nom = input('Entrez votre Nom : ')
prenom = input('Entrez votre Prenom : ')
Age = int(input('Entrez votre Age : '))

Age = 2025 - Age

print(f"Bonjour {nom} {prenom}, vous êtes née en {Age}")
