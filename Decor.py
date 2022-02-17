class Decor:
    def __init__(self, laby):
        """
        Argument:
            laby = Fichier csv du labyrinthe
        """
        self.grille = self.toList(laby) # Transforme le csv en liste de liste
        
        self.longueurCase = height / len(self.grille[0]) + .3 # Variable qui contiendra la longueur d'une case (Pour qu'on puisse y acceder dans les autres fichiers)

        
    def toList(self, csv):
        """
        Transforme le csv du labyrinthe en liste de liste et la retourne
        Argument:
            csv = Fichier csv a transformer en liste de liste
        """
        liste = []
        for row in csv:
            liste.append([int(elements) for elements in row])
        
        return liste # Retourne la liste contenant tous les elements du labyrinthe
    
    
    def reset(self):
        """
        Reinitialise les pacgums
        Fonction appelee lors d'un gameover
        """
        for rangee in range(len(self.grille)):
            for case in range(len(self.grille[rangee])):
                if self.grille[rangee][case] > 10: # Si la case a ete remplace par un nombre > 10, cela veut dire que pacman est passe et a mange la pacgum
                    self.grille[rangee][case] = self.grille[rangee][case] - 10
    
    
    def dessine(self):
        """
        Dessine le labyrinthe sur l'interface utilisateur
        """
        rectMode(CENTER)
        
        # On creer une variable pour self.grille
        liste = self.grille
        
        
        for x in range(len(liste)):
            for y in range(len(liste[0])):
                case = liste[x][y]
                
                # Coordonnees x et y
                _x, _y = x + 0.5, y + 0.5
                
                # Afficher la case sur l'ecran du joueur
                longueurCase = self.longueurCase
                
                # Change les couleurs a afficher pour representer le labyrinthe
                # J'ai dessine un fond noir sur les pastilles et super pastilles pour ne pas afficher le joueur a chaque fois
                if case == 10: 
                    # La case est un mur
                    fill(color(0, 51, 255))
                elif case == 1:
                    # La case est une pastille
                    fill(color(0, 0, 0))
                    rect(_x * longueurCase, _y * longueurCase, longueurCase, longueurCase)
                    fill(color(255, 213, 0))
                elif case == 5: 
                    # La case est une super pastille
                    fill(color(0, 0, 0))
                    rect(_x * longueurCase, _y * longueurCase, longueurCase, longueurCase)
                    fill(color(255, 68, 0))
                else:
                    # La case est vide
                    fill(color(0, 0, 0))
                    
                # Dessine un cube ou une ellipse en fonction de si c'est une case ou une pastille
                if case in [1, 5]:
                    taillePacGum = 8
                    ellipse(_x * longueurCase, _y * longueurCase, taillePacGum, taillePacGum)
                else:
                    rect(_x * longueurCase, _y * longueurCase, longueurCase, longueurCase)
            
                            
    def afficheScore(self, score):
        """
        Affiche le score dans la fenetre
        Argument:
            score = Entier qui contient le score du joueur
        """
        fill(color(255, 206, 92))
        text("SCORE: " + str(score), 500, 40) # Ecrit le score sur l'ecran
