class PacMan:
    def __init__(self, longueurCase):
        """
        Argument:
            longueurCase = La longueur d'une case
        """
        self.longueurCase = longueurCase
        
        self.r = 20 # Rayon du personnage pacman
        self.x = 10.5 * longueurCase # Coordonnees de creation de pacman
        self.y = 15.5 * longueurCase
    
        self.directionAttente = ""
        self.direction = "" # Stocke la direction en cours afin de faire bouger pacman

    
    def reset(self):
        """
        Cette fonction reset pacman lors du demarrage d'une partie
        Fonction appelee lors d'un gameover
        """
        self.x = 10.5 * self.longueurCase
        self.y = 15.5 * self.longueurCase
        
        self.buffed = False
        self.directionAttente = ""
        self.direction = ""

    
    def dessine(self):
        """
        Cette fonction permet de dessiner pac man sur la grille
        """
        rectMode(CENTER)
        fill(color(255, 213, 0))
        ellipse(self.x, self.y, self.r, self.r)
    
            
    def est_au_centre(self):
        """
        Cette fonction permet de verifier si pacman est centre de la case dans la quelle il se situe
        """
        coo = [int(self.x // self.longueurCase), int(self.y // self.longueurCase)] # Les coordonnees de pacman pour regarder les cases aux alentours
        X, Y = coo[0], coo[1]
        
        milieuX = round(X * self.longueurCase + self.longueurCase / 2, 2)
        milieuY = round(Y * self.longueurCase + self.longueurCase / 2, 2)
        
        return milieuX == round(self.x, 2) and milieuY == round(self.y, 2)
    
            
    def deplacement_valide(self, grille):
        """
        Cette fonction va verifier si le deplacement de pacman est valide (Si il y a un mur ou non)
        Argument:
            grille = La grille de jeu (Les cases) pour analyser l'environnement (Detecter murs etc..)
        """
        coo = [int(self.x // self.longueurCase), int(self.y // self.longueurCase)] # Les coordonnees de pacman pour regarder les cases aux alentours
        X, Y = coo[0], coo[1]
        
        # Verification des murs dans chaque direction (Return not pour retourner True si l'emplacement suivant n'est pas un mur, False sinon)
        if self.directionAttente == "up":
            return not grille[X][Y - 1] == 10
        
        if self.directionAttente == "down":
            return not grille[X][Y + 1] == 10
        
        if self.directionAttente == "left":
            return not grille[X - 1][Y] == 10
    
        if self.directionAttente == "right":
            return not grille[X + 1][Y] == 10
      
      
    def verifiePacGums(self, grille):
        """
        Cette fonction va verifier si pacman se trouve sur une pacgum, si oui retourne un tuple (Booleen si il est sur une pacgum, la coordonnee X et Y)
        Argument:
            grille = La grille de jeu (Les cases) pour analyser l'environnement (Detecter murs etc..)
        """ 
        coo = [int(self.x // self.longueurCase), int(self.y // self.longueurCase)] # Les coordonnees de pacman pour regarder les cases aux alentours
        X, Y = coo[0], coo[1]
        
        if grille[X][Y] in [1, 5]: # Est une pacgum / super pacgum
            return (True, X, Y)
        return (False, X, Y)
        
          
    def avancer(self, vitesse):
        """
        Cette fonction permet de faire avancer pacman dans une direction avec une vitesse definie
        Argument:
            vitesse = La vitesse de pacman
        """
        vitesse = vitesse * self.longueurCase
        
        if self.direction == "up":
            self.y -= vitesse
        elif self.direction == "down":
            self.y += vitesse
        elif self.direction == "left":
            self.x -= vitesse
        elif self.direction == "right":
            self.x += vitesse
    
    
    def deplacement(self, grille):
        """
        Cette fonction permet de controler pac man
        Argument:
            grille = La grille de jeu (Les cases) pour analyser l'environnement (Detecter murs etc..)
        """        
        # Pour chaques conditions, on va changer le deplacement en cours (Quand les touches du clavier sont utilisees
        if keyPressed and key == CODED:
            if keyCode == UP:
                self.directionAttente = "up"
            elif keyCode == DOWN:
                self.directionAttente = "down"
            elif keyCode == LEFT:
                self.directionAttente = "left"
            elif keyCode == RIGHT:
                self.directionAttente = "right"
        
        
        
        # Verifie si pacman est au centre, si oui le deplace
        if self.est_au_centre():
            if self.deplacement_valide(grille):
                self.direction = self.directionAttente                
                self.avancer(.1)
            else:
                self.directionAttente = self.direction         
        else:
            self.avancer(.1)
