from csv import *
from Decor import Decor
from Pac_Man import PacMan
from Fantome import Fantome

class Jeu:
    def __init__(self, fichier):
        """
        Info: Cette fonction est appelee une seule fois dans le setup
        Argument:
            fichier = Fichier csv contenant le labyrinthe
        """
        file = open(fichier)
        self.laby = reader(file)
        
        # --- MAIN --- #
        self.status = "menu" # Status du jeu, soit menu, soit jeu, soit gameover
        
        self.decor = Decor(self.laby) # Creer un nouveau decor depuis le fichier csv
        self.pacMan = PacMan(self.decor.longueurCase) # Creer le joueur
        self.points = 0 # Creer une variable qui va contenir le nombre de points
        self.timer = 0 # Le temps durant le quel pacman est invincible
        
        # --- IMAGES --- #
        self.logoImage = loadImage("logo.png") # Image du logo
        self.gameOverImage = loadImage("gameOver.png") # Image du game over
        self.playButton = loadImage("play.png") # Image du bouton jouer
        
        self.backgroundImage = loadImage("bg.jpg") # Charge l'image de fond
        self.backgroundImage.resize(666, 630) # Et la redimensionne pour qu'elle soit de la meme taille que la fenetre
        
        # --- PAC GUMS --- #
        self.totalPacGums = 0 # Le nombre de pacGums au total
        for rangee in self.decor.grille:
            self.totalPacGums += rangee.count(1) + rangee.count(5)   
            
        # -- FANTOMES --- #
        fantomesCouleur = ["red", "cyan", "orange", "pink", "purple"]
        
        self.classFantomes = [] # Tableau qui contiendra les fantomes
        for couleur in fantomesCouleur: # Creation des fantomes
            self.classFantomes.append(Fantome(self.decor.longueurCase, couleur))
            

    def menuPrincipal(self):
        """
        Cette fonction affiche le menu principal
        """
        background(self.backgroundImage) # Change le fond
        image(self.logoImage, (width * 0.5) - self.logoImage.width // 2, 15) # Affiche le logo
        image(self.playButton, (width * 0.5) - self.playButton.width // 2, self.logoImage.height * 1.2) # Affiche le bouton jouer
        
        # Regarde les coordonnees du bouton jour afin de regarder si il pose sa souris dedans
        xBoutonMin, xBoutonMax = (width * 0.5) - self.playButton.width // 2, (width * 0.5) + self.playButton.width // 2
        yBoutonMin, yBoutonMax = self.logoImage.height * 1.2, self.logoImage.height * 1.2 + self.playButton.height
        
        if xBoutonMin < mouseX < xBoutonMax and yBoutonMin < mouseY < yBoutonMax: # Le joueur a mit sa souris sur le bouton
            if mousePressed: # Si l'utilisateur clique sur le bouton 
                self.status = "jeu" # Change le status en jeu
  
    
    def reinitialise(self):
        """
        Cette fonction reinitialise le jeu
        """
        self.points = 0
        self.timer = 0
        self.decor.reset()
        self.pacMan.reset()
        
        for fantome in self.classFantomes: # Reinitialise les fantomes
            fantome.reset()
            
    
    def gameOver(self):
        """
        Cette fonction affiche le game over
        """
        background(self.backgroundImage) # Change le fond
        
        # Affiche le logo gameOver
        image(self.gameOverImage, (width * 0.5) - self.gameOverImage.width // 2, 15)
        
        # Affiche le score
        textAlign(CENTER)
        fill(color(255, 213, 0))
        text("Tu as fait un score de " + str(self.points) + " points!",  width * 0.5, self.gameOverImage.height)
        textAlign(LEFT) # Le remet a LEFT, sa valeur par defaut
        
        # S'occupe du bouton jouer
        image(self.playButton, (width * 0.5) - self.playButton.width // 2, self.gameOverImage.height * 1.2)
        
        # Regarde les coordonnees du bouton jour afin de regarder si il pose sa souris dedans
        xBoutonMin, xBoutonMax = (width * 0.5) - self.playButton.width // 2, (width * 0.5) + self.playButton.width // 2
        yBoutonMin, yBoutonMax = self.gameOverImage.height * 1.2, self.gameOverImage.height * 1.2 + self.playButton.height
        
        if xBoutonMin < mouseX < xBoutonMax and yBoutonMin < mouseY < yBoutonMax: # Le joueur a mit sa souris sur le bouton
            if mousePressed: # Si l'utilisateur clique sur le bouton 
                # Reinitialise
                self.reinitialise()                
                self.status = "jeu" # Change le status en jeu
        
         
    def jouer(self):
        """
        Cette fonction permet d'executer tous les elements du jeu
        """        
        background(0, 0, 0) # Change le fond
        
        # --- DECOR --- #
        self.decor.dessine() # Dessine le decor
        self.decor.afficheScore(self.points) # Affiche le score
        
        # --- PACMAN --- #
        self.pacMan.dessine() # Dessine le joueur
        self.pacMan.deplacement(self.decor.grille) # Permet au joueur de deplacer pac man (Passe la grille en argument pour analyser les cases aux alentours de pacman)
        
        # --- FANTOMES --- #
        for fantome in self.classFantomes: # Affiche et deplace les fantomes
            fantome.dessine()
            fantome.deplacement(self.decor.grille, self.pacMan)
            
            # Si la distance entre les fantomes et pacman sont trop proches et que pacman n'a pas de super pacgum, on affiche le gameover
            d = sqrt( (fantome.x - self.pacMan.x)**2 + (fantome.y - self.pacMan.y)**2 )
            if d <= fantome.r and not fantome.panic: 
                self.status = "gameover"
            
            # Si la distance entre les fantomes et pacman sont trop proches et que pacman a une super pacgum, on reset le fantome et ajoute 10 points
            elif d <= fantome.r and fantome.panic:
                fantome.reset()
                self.points += 10
        
        # --- PAC GUMS + SUPER PACGUMS --- #
        verification = self.pacMan.verifiePacGums(self.decor.grille) # Verifie si pacman se trouve sur une pacgum, si oui incremente le score et mange la pacgum (La fonction retourne un tuple, c'est pourquoi [0])
        if verification[0]: 
            X, Y = verification[1], verification[2]
            
            if self.decor.grille[X][Y] == 5: # Pacman mange une super pacgum, on met tous les fantomes en panique
                self.timer = 10
                for fantome in self.classFantomes:
                    fantome.panic = True

            self.points += self.decor.grille[X][Y]
            self.decor.grille[X][Y] += 10 # Va permettre de savoir ou remettre toutes les pacgums/super pacgums
            self.totalPacGums -= 1 # On enleve une pacgum car une a ete supprimee
            
        # --- TIMER --- #
        if self.timer > 0:
            self.timer -= 0.02
        else: # Fin du timer, tous les fantomes redeviennent normaux
            for fantome in self.classFantomes:
                fantome.panic = False
            
        # --- GAME OVER --- #
        # Compte le nombre de pacgums restants dans la grille, si il en reste 0, le joueur a gagne et on bascule sur l'ecran de fin
        if self.totalPacGums == 0:
            self.status = "gameover"
            
        # Permet de terminer le jeu rapidement pour les tests (afin de ne pas avoir a rejouer tout le temps pour regarder l'ecran de fin)
        if keyPressed:
            if key in ["e", "E"]:
                self.totalPacGums = 0
        
