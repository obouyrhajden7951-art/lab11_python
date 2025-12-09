# Lab11 - Vectorisation
# Préparation de l'environnement

import numpy as np   # import de la bibliothèque NumPy
# Création des tableaux A et B

A = np.array([5, 10, 15, 20])
B = np.array([1, 2, 3, 4])

print("A :", A)
print("B :", B)
# Étape 2 - Opérations vectorisées

# Addition élément par élément
addition = A + B

# Multiplication élément par élément (Hadamard)
multiplication = A * B

# Exposant : carré de chaque valeur du tableau A
puissances = A ** 2

# Affichage des résultats
print("A + B =", addition)
print("A * B =", multiplication)
print("A ** 2 =", puissances)
# Étape 3 - Fonctions universelles (ufunc)

# Création d'un tableau d'angles entre 0 et π, en 5 valeurs
angles = np.linspace(0, np.pi, 5)

# Application des ufunc
sinus = np.sin(angles)
logarithmes = np.log(angles[1:])  # éviter log(0) -> erreur

# Affichage
print("Angles :", angles)
print("sin(angles) :", sinus)
print("log(angles[1:]) :", logarithmes)
# Étape 4 - Masques booléens et filtrage

# Création d'un masque booléen
masque = A > 10
print("Masque A > 10 :", masque)

# Filtrage grâce au masque
valeurs_filtrées = A[masque]
print("Valeurs de A > 10 :", valeurs_filtrées)
# Étape 5 - Broadcasting

# Broadcasting d'un scalaire sur un tableau
addition_scalaire = A + 5
print("A + 5 =", addition_scalaire)
# Matrice 3x3
M = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

# Vecteur ligne
vecteur_ligne = np.array([10, 20, 30])

# Broadcasting ligne → ajouté à chaque ligne de M
resultat = M + vecteur_ligne
print("M + vecteur_ligne :\n", resultat)
vecteur_colonne = np.array([[10],
                            [20],
                            [30]])

resultat_colonne = M + vecteur_colonne
print("M + vecteur_colonne :\n", resultat_colonne)
# Étape 6 - Applications et vérifications

# Opération composite sur A
C = (A * 2) + np.sin(A) - np.mean(A)
print("Opération composite sur A :", C)
log_A = np.log(A)

masque_log = log_A > 2   # masque booléen
print("log(A) > 2 :", log_A[masque_log])
print("Shape de A :", A.shape)
print("Shape de C :", C.shape)
print("Shape de M :", M.shape)
print("Shape de resultat (M + vecteur_ligne) :", resultat.shape)
print("Shape de resultat_colonne :", resultat_colonne.shape)
