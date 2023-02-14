##Création d'une grille 3x3 "vide"
grille = [["_", "_", "_"],
          ["_", "_", "_"],
          ["_", "_", "_"]]

##Fonction encoreCaseVide, qui prend en paramètre une grille et vérifie que celle ci possède encore une ou plusieurs cases vides
def encoreCaseVide(grille):
    caseVide = False
    if "_" in grille[0] or "_" in grille[1] or "_" in grille[2]:
        caseVide = True
    return caseVide

##Fonction etatFinal, permet de vérifier si la grille est dans un état final ou non et calcule le score de cet état.
##Etats finaux: la grille est remplie ou un joueur a réussi à aligner 3 symboles
def etatFinal(grille):
    etatFinal = False
    scoreFinal = 0
    ##Vérification de l'état final: grille remplie
    if encoreCaseVide(grille) == False:
        etatFinal = True
    ##Vérification de l'état final: 3 symboles sont alignés
    ##1.Vérification lignes par lignes
    for ligne in grille:
        if ligne == ["X","X","X"] or ligne == ["O","O","O"]:
            if ligne == ["X","X","X"]:
                scoreFinal = 1
            elif ligne == ["O","O","O"]:
                scoreFinal = -1
            etatFinal = True
    ##2.Vérifications colonnes par colonnes
    for i in range(3):
        if grille[0][i] == "X" and grille[1][i] == "X" and grille[2][i] == "X":
            etatFinal = True
            scoreFinal = 1
            break
        if grille[0][i] == "O" and grille[1][i] == "O" and grille[2][i] == "O":
            etatFinal = True
            scoreFinal = -1
            break
    ##Vérification des diagonales
    if grille[0][0] == "X" and grille[1][1] == "X" and grille[2][2] == "X":
        etatFinal = True
        scoreFinal = 1
    if grille[0][2] == "X" and grille[1][1] == "X" and grille[2][0] == "X":
        etatFinal = True
        scoreFinal = 1
    if grille[0][0] == "O" and grille[1][1] == "O" and grille[2][2] == "O":
        etatFinal = True
        scoreFinal = -1
    if grille[0][2] == "O" and grille[1][1] == "O" and grille[2][0] == "O":
        etatFinal = True
        scoreFinal = -1
    print(etatFinal)
    print(scoreFinal)
        
##Manque ça
def minimax(grille, joueur):
    print("plouf")

##Fonction qui permet d'afficher la grille de morpion créée précédement
def affichage(grille):
    for ligne in grille:
        print(" | ".join(ligne))

##Manque ça aussi
def trouverAction(grille, joueur):
    print("plouf")

affichage(grille)