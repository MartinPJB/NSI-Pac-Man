from random import randint

class Fantome:
    def __init__(self, longueurCase, couleur):
        """
        Argument:
            longueurCase = La longueur d'une case
        """
        self.longueurCase = longueurCase
        
        self.r = 20 # Rayon du fantome
        
        self.origineX = (10 + 0.5) * longueurCase # Coordonnees de creation du fantome (original, permettra de les reset)
        self.origineY = (10 + 0.5) * longueurCase
        
        self.x = (10 + 0.5) * longueurCase # Coordonnees de creation du fantome
        self.y = (10 + 0.5) * longueurCase
    
        self.directionAttente = ""
        self.direction = "" # Stocke la direction en cours afin de faire bouger le fantome
        
        self.panic = False # Passe en true quand pacman a une super pacgum
        
        self.img = loadImage("ghost-"+ couleur +".png") # Charge l'image du fantome
        self.imgPanic = loadImage("ghost-panic.png")
        
        # On resize les images pour eviter que les fantomes soient trop gros
        self.img.resize(0, int(self.longueurCase))
        self.imgPanic.resize(0, int(self.longueurCase))
        
    
    def reset(self):
        """
        Cette fonction reset le fantome lors du demarrage d'une partie
        Fonction appelee lors d'un gameover ou lorsque pacman mange un fantome
        """
        self.x = self.origineX
        self.y = self.origineY
        
        self.panic = False
        self.directionAttente = ""
        self.direction = ""
            
        
    def dessine(self):
        """
        Cette fonction permet de dessiner le fantome sur la grille
        """
        rectMode(CENTER)
        
        if self.panic: # Si les fantomes sont paniques, on change couleur
            image(self.imgPanic, self.x - self.longueurCase / 3, self.y - self.longueurCase / 2)
        else:
            image(self.img, self.x - self.longueurCase / 3, self.y - self.longueurCase / 2)
        
    
    def est_au_centre(self):
        """
        Cette fonction permet de verifier si le fantome est centre de la case dans la quelle il se situe
        """
        coo = [int(self.x // self.longueurCase), int(self.y // self.longueurCase)] # Les coordonnees du fantome pour regarder les cases aux alentours
        X, Y = coo[0], coo[1]
        
        milieuX = round(X * self.longueurCase + self.longueurCase / 2, 2)
        milieuY = round(Y * self.longueurCase + self.longueurCase / 2, 2)
        
        return milieuX == round(self.x, 2) and milieuY == round(self.y, 2)
    
    
    def deplacement_valide(self, grille):
        """
        Cette fonction va verifier si le deplacement du fantome est valide (Si il y a un mur ou non)
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
        
        
    def avancer(self, vitesse):
        """
        Cette fonction permet de faire avancer le fantome dans une direction avec une vitesse definie
        Argument:
            vitesse = La vitesse du fantome
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
        
        
    def deplacement(self, grille, pacman):
        """
        Cette fonction permet de controler le fantome
        Argument:
            grille = La grille de jeu (Les cases) pour analyser l'environnement (Detecter murs etc..)
            pacman = Instance du joueur pour recuperer les coordonnees
        """        
        # Verifie si le fantome est au centre, si oui le deplace
        if self.est_au_centre():
            directions = ["up", "down", "left", "right"]
            t = randint(0, 100)
                
            if t <= 50: # Changement de direction
                self.directionAttente = directions[t % 4]
               
            
            if self.deplacement_valide(grille):
                self.direction = self.directionAttente                
                self.avancer(.1)
            else:
                self.directionAttente = self.direction         
        else:
            self.avancer(.1)
