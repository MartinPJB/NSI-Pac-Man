# NSI - Projet n°2 [Classe de terminale]
*Instructions du projet*

L'objectif de ce projet est de réaliser un jeu "Pac-Man" en langage Python sur processing.
Votre programme devra comporter
- Un écran d'accueil pour démarrer le jeu
- Le jeu
- Un écran de sortie à la fin du jeu

|Le jeu devra être réalisé en programmation orientée objet|
|--|

### 1 - La classe Decor
Le décor est défini par un tableau (une liste de listes) qui contient
- Des 10 pour les murs du labyrinthe
- Des 1 pour représenter les pastilles
- Des 5 pour représenter les super pastilles
- Des 0 pour représenter les cases vides

### 2 - La classe `Pac-Man`
- Se déplace à l'intérieur du labyrinthe à l'aide des flèches du clavier
- "Mange" les pastilles qui sont sur son chemin
- Se transforme quelques secondes en "super pac man" lorsqu'il mange une super pastille

### 3 - La classe `Fantome`
- Se déplacent aléatoirement dans le labyrinthe

### 4 - La classe `Jeu`
- Pac-Man gagne 1 point par pastille et 5 points par super pastille
- Le jeu comporte au moins 5 fantomes
- Les fantômes tuent pacman mais il peut les manger avec une super pastille et gagne alors 10 points
- Le score du joueur est affiché et mis à jour à chaque modification

## Critères
- Résultat final
- Implication en classe durant les séances de projet
- Respect des consignes
- Organisation et propreté du code informatique
- Présence de commentaires dans le code (*Avec #*)
- Spécifications des fonctions (`"""..."""`)
- Rapport clair avec un contenu significatif

## Remise du projet
Fichier zip contenant les programmes et le rapport **pour le 21/02/2022**.
