#Cree Par Constant Dassonville pour le projet ISN : Pac-Man
from tkinter import *
from random import *
#Creation des fonctions
"""Cette fonction va tout d'abords verifier l'emplacement du joueur, ensuite elle verifie
donc la case situe au dessus d'elle (d'ou le -24 car dans la liste ce sera celle d'une
ligne au dessus et une ligne = 24 cases), une fois qu'elle a verifie cette condition
on fait avancer le joueur donc vers le haut a l'aide d'un can.coords, en meme temps que cela on
applique la condition si la case vers laquelle on se deplace est une piece, cette condition nous
permet d'augmenter le score et d'effacer la piece ainsi que de modifier la map pour inserer le
score 0 a cette position"""
def haut(event):
    global x_joueur ,y_joueur ,pas_x_joueur ,pas_y_joueur,score
    pas_y_joueur = -32

    verif = position(x_joueur,y_joueur)
    if carte[verif-24] == 2:
        print('Collision !')
    else:
        y_joueur = y_joueur + pas_y_joueur
        can.coords(id_img_pacman, x_joueur, y_joueur)

    verif_piece=position(x_joueur,y_joueur)        #On vÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©rifie si le joueur
    if carte[verif_piece] == 1:   #se trouve sur une piÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¨ce.
        carte[verif_piece] = 0    #Si c'est le cas, la piece disparait de la liste map[]
        score = score+25
        can.delete(dico_terrain['zone'+str(verif_piece)])  #on efface le piÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¨ce affichÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©e de la carte
                                                  # en s'aidant du dictionnaire dico_terrain{}
"""Cette fonction va tout d'abords verifier l'emplacement du joueur, ensuite elle verifie
donc la case situe en dessous d'elle (d'ou le +24 car dans la liste ce sera celle d'une
ligne en dessous, et une ligne = 24 cases), une fois qu'elle a verifie cette condition
on fait avancer le joueur vers le bas a l'aide d'un can.coords, en meme temps que cela on
applique la condition si la case vers laquelle on se deplace est une piece, cette condition nous
permet d'augmenter le score et d'effacer la piece ainsi que de modifier la map pour inserer le
score 0 a cette position"""
def bas(evenement):
    global x_joueur ,y_joueur ,pas_x_joueur ,pas_y_joueur,score
    pas_y_joueur = 32

    verif = position(x_joueur,y_joueur)        # On appelle la fonction position(), cette fonction donne ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â  quelle endroit
    if carte[verif+24] == 2:  # on se situe selon la liste carte[] , si la case en-dessous (donc +24 car
        print('Collision !')  # c'est une liste) est un 2 alors on fait rien, sinon on peut se dÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©placer
    else:                     # en-dessous
        y_joueur = y_joueur + pas_y_joueur
        can.coords(id_img_pacman, x_joueur, y_joueur)

    verif_piece=position(x_joueur,y_joueur)        #On vÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©rifie si le joueur
    if carte[verif_piece] == 1:   #se trouve sur une piÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¨ce.
        carte[verif_piece] = 0    #Si c'est le cas, la piece disparait de la liste map[]
        score = score+25
        can.delete(dico_terrain['zone'+str(verif_piece)]) #on efface le piÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¨ce affichÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©e de la carte
                                                      # en s'aidant du dictionnaire dico_terrain{}

"""Cette fonction va tout d'abords verifier l'emplacement du joueur, ensuite elle verifie
donc la case situe a gauche d'elle (d'ou le -1 car dans la liste ce sera celle a gauche) une fois
qu'elle a verifie cette condition on fait avancer le joueur donc vers la gauche a l'aide d'un
can.coords, en meme temps que cela on applique la condition si la case vers laquelle on se
deplace est une piece, cette condition nous permet d'augmenter le score et d'effacer la piece
ainsi que de modifier la map pour inserer le score 0 a cette position"""
def gauche(evenement):
    global x_joueur ,y_joueur ,pas_x_joueur ,pas_y_joueur,score
    pas_x_joueur= -32

    verif = position(x_joueur,y_joueur)        # On appelle la fonction position(), cette fonction donne ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â  quelle endroit
    if carte[verif-1] == 2:  # on se situe selon la liste carte[] , si la case ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â  gauche (donc -1 dans la liste)
        print('Collision !')  #) est un 2 alors on fait rien, sinon on peut se dÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©placer ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â  gauche
    else:                     #
        x_joueur = x_joueur + pas_x_joueur
        can.coords(id_img_pacman, x_joueur, y_joueur)

    verif_piece=position(x_joueur,y_joueur)        #On vÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©rifie si le joueur
    if carte[verif_piece] == 1:   #se trouve sur une piÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¨ce.
        carte[verif_piece] = 0    #Si c'est le cas, la piece disparait de la liste map[]
        can.delete(dico_terrain['zone'+str(verif_piece)]) #on efface le piÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¨ce affichÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©e de la carte
        score = score+25                                          # en s'aidant du dictionnaire dico_terrain{}

"""Cette fonction va tout d'abords verifier l'emplacement du joueur, ensuite elle verifie
donc la case situe a droite d'elle (d'ou le +1 car dans la liste ce sera la prochaine) une fois
qu'elle a verifie cette condition on fait avancer le joueur donc vers la droite a l'aide d'un
can.coords, en meme temps que cela on applique la condition si la case vers laquelle on se
deplace est une piece, cette condition nous permet d'augmenter le score et d'effacer la piece
(C'est charles quis'est occupÃ© du can.delete et donc du dico) ainsi que de modifier la map pour
 inserer le score 0 a cette position(Charles s'est aussi occupÃ© de redefinir l'endroit de la
 carte en zone vide c'est a dire en 0)"""
def droite(evenement):
    global x_joueur ,y_joueur ,pas_x_joueur ,pas_y_joueur,score
    pas_x_joueur= 32

    verif = position(x_joueur,y_joueur)
    if carte[verif+1] == 2:
        print('Collision !')
    else:
        x_joueur = x_joueur + pas_x_joueur
        can.coords(id_img_pacman, x_joueur, y_joueur)

    verif_piece=position(x_joueur,y_joueur)        #On vÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©rifie si le joueur
    if carte[verif_piece] == 1:   #se trouve sur une piÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¨ce.
        carte[verif_piece] = 0    #Si c'est le cas, la piece disparait de la liste map[]
        score = score+25
        can.delete(dico_terrain['zone'+str(verif_piece)]) #on efface le piÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¨ce affichÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©e de la carte
                                                  # en s'aidant du dictionnaire dico_terrain{}
"""la fonction suivante permet elle de detecter l'emplacement par rapport a la liste
a l'aide d'une fonction qui permet de retrouver cette position grace aux coordonnees
(Charles)"""
def position(x,y):
    global x_joueur ,y_joueur ,pas_x_joueur ,pas_y_joueur, carte

    pos_x = (x-16)//32   # On divise la position actuel du joueur par 32 pour se reperer
    pos_y = (y-16)//32   # selon un repere de 32cases par 32cases (on -16 car on utilise
                                # les coordonnee images qui sont decale de 16px en x et y)


    pos_map = (pos_y)*24+pos_x  # Formule permettant de retrouver l'emplacement actuel dans la liste
                                # " carte[] "

    return pos_map

"""cette fonction permet de definir la carte a l'aide d'une liste modifiable a notre guise
(Charles)"""
def map():
    global statut,carte,pas,dico_terrain, txt_vct, txt_vct2
    alea_carte=randrange(0,3,1)
    if alea_carte==0:
        carte=[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
               2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
               2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,
               2,2,1,2,1,2,2,1,2,2,2,2,2,2,2,2,1,2,2,1,2,1,2,2,
               2,2,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,2,2,
               2,2,1,2,1,2,2,2,2,1,2,2,1,2,1,2,2,2,2,1,2,1,2,2,
               2,2,1,2,1,2,1,1,1,1,2,1,1,2,1,1,1,1,2,1,2,1,2,2,
               2,2,1,2,1,2,1,2,2,2,2,1,2,2,2,2,2,1,2,1,2,1,2,2,
               2,2,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,2,2,
               2,2,1,2,2,2,1,2,1,2,2,1,1,2,2,1,2,1,2,2,2,1,2,2,
               1,1,1,2,1,1,1,2,1,2,2,2,2,2,2,1,2,1,1,1,2,1,1,1,
               2,2,1,2,1,2,1,2,1,1,2,0,0,2,1,1,2,1,2,1,2,1,2,2,
               2,2,1,2,1,2,1,2,1,1,2,0,0,2,1,1,2,1,2,1,2,1,2,2,
               1,1,1,2,1,1,1,2,1,2,2,2,2,2,2,1,2,1,1,1,2,1,1,1,
               2,2,1,2,2,2,1,2,1,2,2,1,1,2,2,1,2,1,2,2,2,1,2,2,
               2,2,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,2,2,
               2,2,1,2,1,2,1,2,2,2,2,1,2,2,2,2,2,1,2,1,2,1,2,2,
               2,2,1,2,1,2,1,1,1,1,2,1,1,2,1,1,1,1,2,1,2,1,2,2,
               2,2,1,2,1,2,2,2,2,1,2,2,1,2,1,2,2,2,2,1,2,1,2,2,
               2,2,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,2,2,
               2,2,1,2,1,2,2,1,2,2,2,2,2,2,2,2,1,2,2,1,2,1,2,2,
               2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,
               2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
               2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
    if alea_carte == 1:
        carte=[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
               2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
               2,2,1,1,1,1,1,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1,2,2,
               2,2,1,2,1,2,2,2,2,2,1,2,2,1,2,2,2,2,2,1,2,1,2,2,
               2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,
               2,2,1,2,1,2,2,2,2,2,1,2,2,1,2,2,2,2,2,1,2,1,2,2,
               2,2,1,2,1,2,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,2,
               2,2,1,2,1,2,1,2,1,2,1,2,2,1,2,1,2,1,2,1,2,1,2,2,
               2,2,1,2,1,2,1,1,1,2,1,2,2,1,2,1,1,1,2,1,2,1,2,2,
               2,2,1,2,1,2,1,2,2,2,1,2,2,1,2,2,2,1,2,1,2,1,2,2,
               2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,
               2,2,2,2,1,2,1,2,2,2,1,2,2,1,2,2,2,1,2,1,2,2,2,2,
               2,2,2,2,1,2,1,2,2,2,1,2,2,1,2,2,2,1,2,1,2,2,2,2,
               2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,
               2,2,1,2,1,2,1,2,2,2,1,2,2,1,2,2,2,1,2,1,2,1,2,2,
               2,2,1,2,1,2,1,1,1,2,1,2,2,1,2,1,1,1,2,1,2,1,2,2,
               2,2,1,2,1,2,1,2,1,2,1,2,2,1,2,1,2,1,2,1,2,1,2,2,
               2,2,1,2,1,2,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,2,
               2,2,1,2,1,2,2,2,2,2,1,2,2,1,2,2,2,2,2,1,2,1,2,2,
               2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,
               2,2,1,2,1,2,2,2,2,2,1,2,2,1,2,2,2,2,2,1,2,1,2,2,
               2,2,1,1,1,1,1,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1,2,2,
               2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
               2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,]
    """
    if alea_carte == 2:
        carte=[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
               2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
               2,2,1,1,1,1,1,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1,2,2,
               2,2,1,2,1,2,2,2,2,2,1,2,2,1,2,2,2,2,2,1,2,1,2,2,
               2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,
               2,2,1,2,1,2,2,2,2,2,1,2,2,1,2,2,2,2,2,1,2,1,2,2,
               2,2,1,2,1,2,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,2,
               2,2,1,2,1,2,1,2,1,2,1,2,2,1,2,1,2,1,2,1,2,1,2,2,
               2,2,1,2,1,2,1,1,1,2,1,2,2,1,2,1,1,1,2,1,2,1,2,2,
               2,2,1,2,1,2,1,2,2,2,1,2,2,1,2,2,2,1,2,1,2,1,2,2,
               2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,
               2,2,2,2,1,2,1,2,2,2,1,2,2,1,2,2,2,1,2,1,2,2,2,2,
               2,2,2,2,1,2,1,2,2,2,1,2,2,1,2,2,2,1,2,1,2,2,2,2,
               2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,
               2,2,1,2,1,2,1,2,2,2,1,2,2,1,2,2,2,1,2,1,2,1,2,2,
               2,2,1,2,1,2,1,1,1,2,1,2,2,1,2,1,1,1,2,1,2,1,2,2,
               2,2,1,2,1,2,1,2,1,2,1,2,2,1,2,1,2,1,2,1,2,1,2,2,
               2,2,1,2,1,2,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,2,
               2,2,1,2,1,2,2,2,2,2,1,2,2,1,2,2,2,2,2,1,2,1,2,2,
               2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,
               2,2,1,2,1,2,2,2,2,2,1,2,2,1,2,2,2,2,2,1,2,1,2,2,
               2,2,1,1,1,1,1,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1,2,2,
               2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
               2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,]
    """

    pas=0
    dico_terrain={}
    for rang_y in range(0,768,32):
        for rang_x in range(0,768,32):

           if carte[pas] == 0:

               dico_terrain['zone{0}'.format(pas)]=0

           if carte[pas] == 1:


               dico_terrain['zone{0}'.format(pas)]=can.create_oval(rang_x+12 ,rang_y+12,rang_x+20,rang_y+20, fill='yellow')

           if carte[pas] == 2:

               dico_terrain['zone{0}'.format(pas)]=can.create_image(rang_x+16 , rang_y+16 , image=img_mur)

           pas=pas+1


"""creation des ia"""
"""Les 2 premiers Ia fonctionnent de la maniere suivante : On detecte la position de l'Ia par rapport
au joueur, une fois que l'on connais cette position, selon une pourcentage redefinisable, l'Ia va se deplacer
dans la direction du joueur, le pourcentage represente d'une certaine maniere la dificultÃ©, pour arriver a ce resultat
il faut definir 2nombre aleatoire (un pour les x et un pour les y pour que ces 2 evenement soient independant
le deplacement donc est similaire a celui du joueur dans la maniere, on detecte la case ou l'ia compte aller et si toutes
les conditions (c'est a dire qu'il n'y ai pas de mur) sont respecte alor l'ia avance a l'aide du can.coords qui definie les
coordonnees. Enfin vu que cette fonction n'est pas appele par une touche on l'a fait fonctionner en continue a l'aide d'un fen.after
plus le temps de latence est elevee, moins les Ia vont vite donc plus le niveau est facile, on peut donc ajouter de la dificulte
avec cette maniere"""
def ia1():
    global x_ia1, y_ia1, pas_x_ia1, pas_y_ia1, x_joueur, y_joueur, pourcent
    alea_x=randrange(0,100,1)
    alea_y=randrange(0,100,1)
    if x_ia1-x_joueur > 0:
        if alea_x>= pourcent:
            pas_x_ia1 = 32
            verif = position(x_ia1,y_ia1)
            if carte[verif+1] == 2:
                print('Collision !')
            else:
                x_ia1 = x_ia1 + pas_x_ia1
                can.coords(id_img_fantome1, x_ia1, y_ia1)
        if alea_x< pourcent:
            pas_x_ia1 = -32
            verif = position(x_ia1,y_ia1)
            if carte[verif-1] == 2:
                print('Collision !')
            else:
                x_ia1 = x_ia1 + pas_x_ia1
                can.coords(id_img_fantome1, x_ia1, y_ia1)
    if x_ia1-x_joueur < 0:
        if alea_x>=pourcent:
            pas_x_ia1 = -32
            verif = position(x_ia1,y_ia1)
            if carte[verif-1] == 2:
                print('Collision !')
            else:
                x_ia1 = x_ia1 + pas_x_ia1
                can.coords(id_img_fantome1, x_ia1, y_ia1)
        if alea_x<pourcent:
            pas_x_ia1 = 32
            verif = position(x_ia1,y_ia1)
            if carte[verif+1] == 2:
                print('Collision !')
            else:
                x_ia1 = x_ia1 + pas_x_ia1
                can.coords(id_img_fantome1, x_ia1, y_ia1)
    if y_ia1-y_joueur > 0:
        if alea_y>=pourcent:
            pas_y_ia1 = 32
            verif = position(x_ia1,y_ia1)
            if carte[verif+24] == 2:
                print('Collision !')
            else:
                y_ia1 = y_ia1 + pas_y_ia1
                can.coords(id_img_fantome1, x_ia1, y_ia1)
        if alea_y<pourcent:
            pas_y_ia1 = -32
            verif = position(x_ia1,y_ia1)
            if carte[verif-24] == 2:
                print('Collision !')
            else:
                y_ia1 = y_ia1 + pas_y_ia1
                can.coords(id_img_fantome1, x_ia1, y_ia1)
    if y_ia1-y_joueur < 0:
        if alea_y>=pourcent:
            pas_y_ia1 = -32
            verif = position(x_ia1,y_ia1)
            if carte[verif-24] == 2:
                print('Collision !')
            else:
                y_ia1 = y_ia1 + pas_y_ia1
                can.coords(id_img_fantome1, x_ia1, y_ia1)
        if alea_y<pourcent:
            pas_y_ia1 = 32
            verif = position(x_ia1,y_ia1)
            if carte[verif+24] == 2:
                print('Collision !')
            else:
                y_ia1 = y_ia1 + pas_y_ia1
                can.coords(id_img_fantome1, x_ia1, y_ia1)
    fen.after(100, ia1)

def ia2():
    global x_ia2, y_ia2, pas_x_ia2, pas_y_ia2, x_joueur, y_joueur, pourcent
    alea_x=randrange(0,100,1)
    alea_y=randrange(0,100,1)
    if x_ia2-x_joueur > 0:
        if alea_x>=pourcent:
            pas_x_ia2 = 32
            verif = position(x_ia2,y_ia2)
            if carte[verif+1] == 2:
                print('Collision !')
            else:
                x_ia2 = x_ia2 + pas_x_ia2
                can.coords(id_img_fantome2, x_ia2, y_ia2)
        if alea_x<pourcent:
            pas_x_ia2 = -32
            verif = position(x_ia2,y_ia2)
            if carte[verif-1] == 2:
                print('Collision !')
            else:
                x_ia2 = x_ia2 + pas_x_ia2
                can.coords(id_img_fantome2, x_ia2, y_ia2)
    if x_ia2-x_joueur < 0:
        if alea_x>=pourcent:
            pas_x_ia2 = -32
            verif = position(x_ia2,y_ia2)
            if carte[verif-1] == 2:
                print('Collision !')
            else:
                x_ia2 = x_ia2 + pas_x_ia2
                can.coords(id_img_fantome2, x_ia2, y_ia2)
        if alea_x<pourcent:
            pas_x_ia2 = 32
            verif = position(x_ia2,y_ia2)
            if carte[verif+1] == 2:
                print('Collision !')
            else:
                x_ia2 = x_ia2 + pas_x_ia2
                can.coords(id_img_fantome2, x_ia2, y_ia2)
    if y_ia2-y_joueur > 0:
        if alea_y>=pourcent:
            pas_y_ia2 = 32
            verif = position(x_ia2,y_ia2)
            if carte[verif+24] == 2:
                print('Collision !')
            else:
                y_ia2 = y_ia2 + pas_y_ia2
                can.coords(id_img_fantome2, x_ia2, y_ia2)
        if alea_y<pourcent:
            pas_y_ia2 = -32
            verif = position(x_ia2,y_ia2)
            if carte[verif-24] == 2:
                print('Collision !')
            else:
                y_ia2 = y_ia2 + pas_y_ia2
                can.coords(id_img_fantome2, x_ia2, y_ia2)
    if y_ia2-y_joueur < 0:
        if alea_y>=pourcent:
            pas_y_ia2 = -32
            verif = position(x_ia2,y_ia2)
            if carte[verif-24] == 2:
                print('Collision !')
            else:
                y_ia2 = y_ia2 + pas_y_ia2
                can.coords(id_img_fantome2, x_ia2, y_ia2)
        if alea_y<pourcent:
            pas_y_ia2 = 32
            verif = position(x_ia2,y_ia2)
            if carte[verif+24] == 2:
                print('Collision !')
            else:
                y_ia2 = y_ia2 + pas_y_ia2
                can.coords(id_img_fantome2, x_ia2, y_ia2)
    fen.after(100, ia2)

"""Les 2 derniers Ia marche tres differement, le mouvement n'a aucune liaison avec la
position du joueur, le but ici est de creer un ia qui fonctionne de maniere assez logique
c'est a dire qu'il va allez en ligne droite pendant un certain temps lui aussi aleatoire
et biensur si il rencontre un mur il change de direction. Pour atteindre cette objectif
il faudra 2fonctions par ia, 2fonctoins pour pouvoir avoir un temps de latence different
ensuite donc avec les nombre aleatoire on associe une direction et donc tant que l'ia ne
rencontre pas de mur ou que le temps (un multiple de 750ms et au maximum 3s ( 750ms * 4)"""

def ia3_2():
    global alea_3, alea2_3
    alea_3 = randrange(0,4,1)
    alea2_3 = randrange (3,8,1)
    fen.after(1000*alea2_3, ia3_2)
def ia3():
    global x_ia3, y_ia3, pas_x_ia3, pas_y_ia3, x_joueur, y_joueur, carte, statut, pas, alea_3, alea2_3
    verif = position(x_ia3, y_ia3)
    if alea_3 == 0:
        pas_x_ia3 = 32
        pas_y_ia3 = 0
        x = 1
    if alea_3 == 1:
        pas_x_ia3 = -32
        pas_y_ia3 = 0
        x = -1
    if alea_3 == 2:
        pas_y_ia3 = 32
        pas_x_ia3 = 0
        x = 24
    if alea_3 == 3:
        pas_y_ia3 = -32
        pas_x_ia3 = 0
        x = -24
    if x_ia3 > 740:
        alea_3 = 1
    if x_ia3 < 40:
        alea_3 = 0
    if y_ia3 > 660:
        alea_3 = 3
    if y_ia3 < 120:
        alea_3 = 2
    if carte[verif+x] == 2:
        alea_3 = randrange(0,4,1)
        print('Collision !')
    else:
                x_ia3 = x_ia3 + pas_x_ia3
                y_ia3 = y_ia3 + pas_y_ia3
                can.coords(id_img_fantome3, x_ia3, y_ia3)
    fen.after(100, ia3)

def ia4_2():
    global alea_4, alea2_4
    alea_4 = randrange(0,4,1)
    alea2_4 = randrange (2,5,1)
    fen.after(1000*alea2_4, ia4_2)

def ia4():
    global x_ia4, y_ia4, pas_x_ia4, pas_y_ia4, x_joueur, y_joueur, carte, statut, pas, alea_4, alea2_4
    verif = position(x_ia4, y_ia4)
    if alea_4 == 0:
        pas_x_ia4 = 32
        pas_y_ia4 = 0
        x = 1
    if alea_4 == 1:
        pas_x_ia4 = -32
        pas_y_ia4 = 0
        x = -1
    if alea_4 == 2:
        pas_y_ia4 = 32
        pas_x_ia4 = 0
        x = 24
    if alea_4 == 3:
        pas_y_ia4 = -32
        pas_x_ia4 = 0
        x = -24
    if x_ia4 > 740:
        alea_4 = 1
    if x_ia4 < 40:
        alea_4 = 0
    if y_ia4 > 660:
        alea_4 = 3
    if y_ia4 < 120:
        alea_4 = 2
    if carte[verif+x] == 2:
        alea_4 = randrange(0,4,1)
        print('Collision !')
    else:
                x_ia4 = x_ia4 + pas_x_ia4
                y_ia4 = y_ia4 + pas_y_ia4
                can.coords(id_img_fantome4, x_ia4, y_ia4)
    fen.after(100, ia4)

"""La fonction defaite donc etabli les conditions de defaites (que les coordonnees d'un des 4Ias soient
les memes que le joueur, une fois cette condition respecter le joueur perd une vie (au maximum 3) et
les ia ainsi que le joueur reprenne les positions initiales, si la vie tombe a 0 un message de defaite s'affiche"""
def defaite():

    global id_img_pacman,id_img_fantome1,x_joueur,y_joueur,x_ia1,y_ia1,x_ia2,y_ia2,x_ia3,y_ia3,x_ia4,y_ia4,jeu,vie
    if x_joueur == x_ia1:
        if y_joueur == y_ia1:
            vie = vie-1
            x_joueur = 688
            y_joueur = 336
            x_ia1 = 304
            y_ia1 = 400
            x_ia2 = 400
            y_ia2 = 304
            x_ia3 = 400
            y_ia3 = 496
            x_ia4 = 496
            y_ia4 = 400
            can.coords(id_img_pacman, 688, 336)
            can.coords(id_img_fantome1, 304, 400)
            can.coords(id_img_fantome2, 400, 304)
            can.coords(id_img_fantome3, 400, 496)
            can.coords(id_img_fantome4, 496, 400)
        if vie == 0:
            can.create_rectangle(0,0,768,768,fill='black')
            can.create_text(384,384,text='Vous avez perdu',font="arial 50",fill='white')
    if x_joueur == x_ia2:
        if y_joueur == y_ia2:
            vie = vie-1
            x_joueur = 688
            y_joueur = 336
            x_ia1 = 304
            y_ia1 = 400
            x_ia2 = 400
            y_ia2 = 304
            x_ia3 = 400
            y_ia3 = 496
            x_ia4 = 496
            y_ia4 = 400
            can.coords(id_img_pacman, 688, 336)
            can.coords(id_img_fantome1, 304, 400)
            can.coords(id_img_fantome2, 400, 304)
            can.coords(id_img_fantome3, 400, 496)
            can.coords(id_img_fantome4, 496, 400)
        if vie == 0:
            can.create_rectangle(0,0,768,768,fill='black')
            can.create_text(384,384,text='Vous avez perdu',font="arial 50",fill='white')
    if x_joueur == x_ia3:
        if y_joueur == y_ia3:
            vie = vie-1
            x_joueur = 688
            y_joueur = 336
            x_ia1 = 304
            y_ia1 = 400
            x_ia2 = 400
            y_ia2 = 304
            x_ia3 = 400
            y_ia3 = 496
            x_ia4 = 496
            y_ia4 = 400
            can.coords(id_img_pacman, 688, 336)
            can.coords(id_img_fantome1, 304, 400)
            can.coords(id_img_fantome2, 400, 304)
            can.coords(id_img_fantome3, 400, 496)
            can.coords(id_img_fantome4, 496, 400)
        if vie == 0:
            can.create_rectangle(0,0,768,768,fill='black')
            can.create_text(384,384,text='Vous avez perdu',font="arial 50",fill='white')
    if x_joueur == x_ia4:
        if y_joueur == y_ia4:
            vie = vie-1
            x_joueur = 688
            y_joueur = 336
            x_ia1 = 304
            y_ia1 = 400
            x_ia2 = 400
            y_ia2 = 304
            x_ia3 = 400
            y_ia3 = 496
            x_ia4 = 496
            y_ia4 = 400
            can.coords(id_img_pacman, 688, 336)
            can.coords(id_img_fantome1, 304, 400)
            can.coords(id_img_fantome2, 400, 304)
            can.coords(id_img_fantome3, 400, 496)
            can.coords(id_img_fantome4, 496, 400)
        if vie == 0:
            can.create_rectangle(0,0,768,768,fill='black')
            can.create_text(384,384,text='Vous avez perdu',font="arial 50",fill='white')
            can.create_text(384,484, text='Appuyer sur "r"', font = 'Arial 50', fill = 'white')
    fen.after(10,defaite)

"""Le programme victoire est simple, il y a 244pieces dans le jeu rapportant chacune
25points, quand le joueur atteint 6100point il a eu toutes les pieces donc gagner
on affiche donc le message de victoire """

def victoire():
    global score, txt_vct; txt_vtc2
    if score == 6100:
        can.create_rectangle(0,0,768,768,fill="black")
        can.create_text(384,384,text='envoie sur discord !lien', font='Arial 30', fill='white')
        can.create_text(384,484, text='Appuyer sur "r" pour rejouer', font = 'Arial 30', fill = 'white')
        can.create_text(384,534, text='(uniquement pour le plaisir)', font = 'Arial 30', fill = 'white')
        can.create_text(384,584, text='Il y a plusieurs maps !!', font = 'Arial 30', fill = 'white')
        x_joueur = 368
        y_joueur = 368
        can.coords (id_img_pacman, x_joueur, y_joueur)
    fen.after(1000,victoire)

"""Le programme affichage permet d'afficher le score et la vie sans que celles ci se superposent
ceci est permi grace a l'insertion des textes dans des variables"""

def affichage():
    global score,vie,scj,viej
    can2.delete(scj)
    can2.delete(viej)
    scj=can2.create_text(250,130,text = score,font='arial 50',fill='white')
    viej=can2.create_text(200,50,text = vie,font='arial 50',fill='white')
    fen.after(100,affichage)
"""Le programme restart permet de pouvoir recommencer la partie a tout moment
pour cela il suffit de redéfinir toutes les variables et replacer les différentes images
a l'aide d'un can.coords"""
def restart(event):
    global score, vie, x_joueur,y_joueur, x_ia1, y_ia1, x_ia2, y_ia2, x_ia3, y_ia3, x_ia4, y_ia4, carte, txt_vtc2, txt_vct, id_img_fantome4, id_img_fantome1, id_img_fantome2, id_img_fantome3, id_img_pacman, img_fantome1, img_fantome2, img_fantome3, img_fantome4, img_pacman

    can.delete(ALL)
    map()

    alea_3 = 0
    alea2_3 = 0
    alea_4 = 0
    alea2_4 = 0

    y_joueur = 336
    x_joueur = 688
    pas_y_joueur = 0
    pas_x_joueur = 0

    pourcent = 60
    viej = 0
    scj=0
    vie = 3
    score = 0

    x_ia1 = 304
    y_ia1 = 368
    pas_x_ia1 = 0
    pas_y_ia1 = 0

    x_ia2 = 368
    y_ia2 = 304
    pas_x_ia2 = 0
    pas_y_ia2 = 0

    x_ia3 = 496
    y_ia3 = 432
    pas_x_ia3 = 0
    pas_y_ia3 = 0

    x_ia4 = 432
    y_ia4 = 496
    pas_x_ia4 = 0
    pas_y_ia4 = 0

    img_pacman = PhotoImage(file='pacman.png')
    id_img_pacman = can.create_image(x_joueur , y_joueur , image=img_pacman)

    img_fantome1 = PhotoImage(file='pacman 1.png')
    id_img_fantome1 = can.create_image(x_ia1 , y_ia1 , image=img_fantome1)

    img_fantome2 = PhotoImage(file='pacman 2.png')
    id_img_fantome2 = can.create_image(x_ia2 , y_ia2 , image=img_fantome2)

    img_fantome3 = PhotoImage(file='pacman 3.png')
    id_img_fantome3 = can.create_image(x_ia3 , y_ia3 , image=img_fantome3)

    img_fantome4 = PhotoImage(file='pacman 4.png')
    id_img_fantome4 = can.create_image(x_ia4 , y_ia4 , image=img_fantome4)

    can.coords(id_img_pacman, x_joueur, y_joueur)
    can.coords(id_img_fantome1, x_ia1, y_ia1)
    can.coords(id_img_fantome2, x_ia2, y_ia2)
    can.coords(id_img_fantome3, x_ia3, y_ia3)
    can.coords(id_img_fantome4, x_ia4, y_ia4)
"""ce programme permet d'augmenter le pourentage de chance que l'IA se déplace
vers le joueur"""
def dif_p(event):
    global pourcent
    if pourcent < 99:
        pourcent = pourcent+10
    else:
        print("erreur")
    restart()
    print(pourcent)

def dif_m(event):
    global pourcent
    if pourcent > 10:
        pourcent = pourcent-10
    else:
        print("erreur")
    restart()
    print(pourcent)

def triche(event):
    global vie
    vie = vie+3

""" Definition des variables"""
"""La plupart des variables sont donc les positions des joueurs qui sont positionner
de chaque cote du carre centrale """
alea_3 = 0
alea2_3 = 0
alea_4 = 0
alea2_4 = 0

y_joueur = 336
x_joueur = 688
pas_y_joueur = 0
pas_x_joueur = 0

pourcent = 60
viej = 0
scj=0
vie = 3
score = 0

x_ia1 = 304
y_ia1 = 368
pas_x_ia1 = 0
pas_y_ia1 = 0

x_ia2 = 368
y_ia2 = 304
pas_x_ia2 = 0
pas_y_ia2 = 0

x_ia3 = 496
y_ia3 = 432
pas_x_ia3 = 0
pas_y_ia3 = 0

x_ia4 = 432
y_ia4 = 496
pas_x_ia4 = 0
pas_y_ia4 = 0

txt_vct = 0
txt_vtc2 = 0

carte=[    2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
           2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
           2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,
           2,2,1,2,1,2,2,1,2,2,2,2,2,2,2,2,1,2,2,1,2,1,2,2,
           2,2,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,2,2,
           2,2,1,2,1,2,2,2,2,1,2,2,1,2,1,2,2,2,2,1,2,1,2,2,
           2,2,1,2,1,2,1,1,1,1,2,1,1,2,1,1,1,1,2,1,2,1,2,2,
           2,2,1,2,1,2,1,2,2,2,2,1,2,2,2,2,2,1,2,1,2,1,2,2,
           2,2,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,2,2,
           2,2,1,2,2,2,1,2,1,2,2,1,1,2,2,1,2,1,2,2,2,1,2,2,
           1,1,1,2,1,1,1,2,1,2,2,2,2,2,2,1,2,1,1,1,2,1,1,1,
           2,2,1,2,1,2,1,2,1,1,2,0,0,2,1,1,2,1,2,1,2,1,2,2,
           2,2,1,2,1,2,1,2,1,1,2,0,0,2,1,1,2,1,2,1,2,1,2,2,
           1,1,1,2,1,1,1,2,1,2,2,2,2,2,2,1,2,1,1,1,2,1,1,1,
           2,2,1,2,2,2,1,2,1,2,2,1,1,2,2,1,2,1,2,2,2,1,2,2,
           2,2,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,2,2,
           2,2,1,2,1,2,1,2,2,2,2,1,2,2,2,2,2,1,2,1,2,1,2,2,
           2,2,1,2,1,2,1,1,1,1,2,1,1,2,1,1,1,1,2,1,2,1,2,2,
           2,2,1,2,1,2,2,2,2,1,2,2,1,2,1,2,2,2,2,1,2,1,2,2,
           2,2,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,2,2,
           2,2,1,2,1,2,2,1,2,2,2,2,2,2,2,2,1,2,2,1,2,1,2,2,
           2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,
           2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
           2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]

"""---creation du widget principal ("maitre")---"""
fen=Tk()
fen.title("Pac-Man")

"""---creation des widgets "esclaves"---"""
#creation des Canvas

can1=Canvas(fen, bg='green', height=768, width=403)
can1.pack(side=LEFT, padx=5, pady=5)

can=Canvas(fen, bg='black', height=768, width=768)
can.pack(side=LEFT, padx=5, pady=5)
can.focus_set()

can2=Canvas(fen, bg='red', height=768, width=403)
can2.pack(side=LEFT, padx=5, pady=5)

#importation des images pacman
img_mur=PhotoImage(file='mur.png')
img_piece=PhotoImage(file='piece.png')

img_pacman = PhotoImage(file='pacman.png')
id_img_pacman = can.create_image(x_joueur , y_joueur , image=img_pacman)

img_fantome1 = PhotoImage(file='pacman 1.png')
id_img_fantome1 = can.create_image(x_ia1 , y_ia1 , image=img_fantome1)

img_fantome2 = PhotoImage(file='pacman 2.png')
id_img_fantome2 = can.create_image(x_ia2 , y_ia2 , image=img_fantome2)

img_fantome3 = PhotoImage(file='pacman 3.png')
id_img_fantome3 = can.create_image(x_ia3 , y_ia3 , image=img_fantome3)

img_fantome4 = PhotoImage(file='pacman 4.png')
id_img_fantome4 = can.create_image(x_ia4 , y_ia4 , image=img_fantome4)

img_bord_droit = PhotoImage(file='mur.png')
id_img_bord_droit = can2.create_image(201.5,383, image = img_bord_droit)

img_bord_gauche = PhotoImage(file='mur.png')
id_img_bord_gauche = can1.create_image(201.5,383, image = img_bord_gauche)

#details
can1.create_text(200,200, text='Pour deplacer votre Pac-Man utliser les fleches du clavier', font='Arial 10', fill='black')
can1.create_text(200,300, text='A tout moment vous pouvez recommencer', font='Arial 10', fill='black')
can1.create_text(200,330, text='en appuyant sur la touche "r"', font='Arial 10', fill ='black')
can1.create_text(200,600, text='Si vous etes nul, code de triche = o ', font='Arial 10', fill='black')
can1.create_text(200,700, text='Vous pouvez changer le niveau des IAs', font='Arial 10', fill='black')
can1.create_text(200,730, text='p augmente le niveau et m diminue le niveau', font='Arial 10', fill ='black')

can2.create_rectangle(175,20,225,80, fill='black')
can2.create_rectangle(175,100,325,160, fill='black')
can2.create_text(100,50,text='vie(s)=',font='Arial 35', fill='black')
can2.create_text(100,130,text='Score=',font='Arial 35', fill='black')

"""On appelle les commandes soit par des boutons, soit en continue"""

can.bind('<Up>',haut)
can.pack()

can.bind('<Down>',bas)
can.pack()

can.bind('<Left>',gauche)
can.pack()

can.bind('<Right>',droite)
can.pack()

can.bind('<r>',restart)
can.pack()

can.bind('<p>',dif_p)
can.pack()

can.bind('<m>',dif_m)
can.pack()

can.bind('<o>',triche)
can.pack()

ia1()
ia2()
ia3()
ia3_2()
ia4()
ia4_2()

victoire()
map()
defaite()
affichage()

fen.mainloop()
