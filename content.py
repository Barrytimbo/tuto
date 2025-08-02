# Python Content - Les différents types de contenu

# 1. Variables simples
# Une variable est comme une boîte qui contient une valeur
nom = "Pierre"      # Texte (string)
age = 25           # Nombre entier (integer)
taille = 1.75      # Nombre décimal (float)
est_majeur = True  # Booléen (True/False)

# 2. Listes (collections ordonnées)
# Une liste peut contenir plusieurs éléments
fruits = ["pomme", "banane", "orange"]
print(f"Liste de fruits : {fruits}")

# Accès aux éléments
premier_fruit = fruits[0]  # Premier élément (index 0)
print(f"Premier fruit : {premier_fruit}")

# Modification
fruits[1] = "kiwi"  # Change le deuxième élément
print(f"Liste modifiée : {fruits}")

# Ajout d'éléments
fruits.append("fraise")  # Ajoute à la fin
print(f"Liste avec ajout : {fruits}")

# 3. Tuples (listes immuables)
# Un tuple ne peut pas être modifié après sa création
coordonnees = (10, 20)
print(f"Coordonnées : {coordonnees}")

# Déballage du tuple
x, y = coordonnees
print(f"x = {x}, y = {y}")

# 4. Dictionnaires (paires clé-valeur)
# Un dictionnaire associe des clés à des valeurs
personne = {
    "nom": "Pierre",
    "age": 25,
    "ville": "Paris"
}
print(f"Dictionnaire : {personne}")

# Accès aux valeurs
nom = personne["nom"]
print(f"Nom : {nom}")

# Modification
personne["age"] = 26
print(f"Âge modifié : {personne['age']}")

# Ajout
personne["pays"] = "France"
print(f"Dictionnaire avec ajout : {personne}")

# 5. Ensembles (collections uniques)
# Un ensemble ne contient pas de doublons
couleurs = {"rouge", "vert", "bleu", "rouge"}
print(f"Ensemble de couleurs : {couleurs}")  # Le rouge n'apparaît qu'une fois

# Ajout
couleurs.add("jaune")
print(f"Ensemble avec ajout : {couleurs}")

# 6. Chaînes de caractères (strings)
# Une chaîne est une séquence de caractères
texte = "Bonjour le monde"
print(f"Texte : {texte}")

# Longueur
longueur = len(texte)
print(f"Longueur du texte : {longueur}")

# Découpage
premiere_partie = texte[0:7]  # De l'index 0 à 7
print(f"Première partie : {premiere_partie}")

# 7. Nombres
# Entiers
nombre_entier = 42
print(f"Nombre entier : {nombre_entier}")

# Décimaux
nombre_decimal = 3.14
print(f"Nombre décimal : {nombre_decimal}")

# 8. Booléens
vrai = True
faux = False
print(f"Vrai : {vrai}, Faux : {faux}")

# 9. None (absence de valeur)
rien = None
print(f"None : {rien}")

# 10. Conversion entre types
# Texte vers nombre
texte_nombre = "123"
nombre = int(texte_nombre)
print(f"Conversion texte vers nombre : {nombre}")

# Nombre vers texte
nombre_texte = str(42)
print(f"Conversion nombre vers texte : {nombre_texte}") 