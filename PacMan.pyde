# Dependances
from Jeu import Jeu

# Variables globales
jeu = None

def setup():
    rectMode(CENTER)
    
    global jeu
    size(666, 630)
    background(0, 0, 0)
    
    f = createFont("Arial", 25)
    textFont(f, 25)   
    
    frameRate(60)
    jeu = Jeu("Maze.csv") # Creer un nouveau jeu
    
    
def draw():
    if jeu.status == "menu":
        jeu.menuPrincipal()
        
    elif jeu.status == "jeu":
        jeu.jouer()
        
    elif jeu.status == "gameover":
        jeu.gameOver()
            
        # Reset le nombre de pacgums
        for rangee in jeu.decor.grille:
            jeu.totalPacGums += rangee.count(1) + rangee.count(5)
