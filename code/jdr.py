# problème avec potion, retire une potion a chaque tour que le joueur en utilise ou attaque. manque de temps pour finir.

# lorsque vous utilisez une potion vous passer le prochain tour

import random
use = False
jeu_en_cours = True
potion_dispo=True
# code non conservé
# def actu_valeurs():
#     dgt_j1 = random.randint(5, 10)
#     dgt_en = random.randint(5, 15)
#     soin_recu = random.randint(15, 50)
# dgt_j1 = 0
# dgt_en = 0
# votre attaque inflige a l'ennemi un nb aléatoire de points de vie entre 5 et 10 pv
# dgt_j1 = random.randint(5, 10)
# l'attaque de l'ennemi vous inflige un nb aléatoire de points de vie entre 5 et 15 pv
# dgt_en = random.randint(5, 15)
# chaque potion permet de récuperer un nb aleatoire de pv entre 15 et 50 pv
# soin_recu = random.randint(15, 50)
# 2 joueurs, commence avec 50 hp,notre personnage a 3 potions, l'ennemi aucun

class Personnage:
    def __init__(self,nom,pv,p_attaque,potions):
       self.nom = nom
       self.pv = pv
       self.p_attaque = p_attaque
       self.potions = potions
Joueur_1 = Personnage("J1",50,0,3)
Ennemi = Personnage("Ennemi",50,0,0)

# code non fonctionnel
# def potion_utilisable(Joueur_1):
#     global potion_dispo
#     if (Joueur_1.potions >0) and (Joueur_1.potions <=3):
#         potion_dispo = True
#     else:
#         potion_dispo = False

# problème sur potion
# def utilise_potion(self):
#     while 3<=self.potions>0:
#         self.pv = soin_recu + self.pv
#         self.potions -= 1
#     print(f"{self.nom} a utilisé une potion, il a récuperé {soin_recu} il lui reste maintenant {self.pv} et {self.potions} Potions. \n le joueur passe le prochain tour")

# attaque et génère les valeurs de dégats
def attaque(self, cible):
    global dgt_j1
    global dgt_en
    Joueur_1.p_attaque=dgt_j1 = random.randint(5, 10)
    Ennemi.p_attaque=dgt_en = random.randint(5, 15)
    global jeu_en_cours
    cible.pv -= self.p_attaque
    print(f"{self.nom} a infligé {self.p_attaque} dégats a {cible.nom}, il reste donc {cible.pv} PV a {cible.nom} .")

# verifie les pv du joueur et de l'ennemi si plus de pv afficher victoire du joueur

def verif_victoire(self, cible):
    global jeu_en_cours
    if self.pv <=0 :
        jeu_en_cours=False
        print(f"{cible.nom} a gagné !")
    elif  cible.pv <= 0:
        jeu_en_cours=False
        print(f"{self.nom} a gagné !")

# problème sur potion et sa boucle
# def utilise_potion(Joueur_1):
#     while potion_utilisable == True:               
#             Joueur_1.pv = soin_recu + Joueur_1.pv
#             Joueur_1.potions = Joueur_1.potions -1
#     print(f"{Joueur_1.nom} a utilisé une potion, il a récuperé {soin_recu} il lui reste maintenant {Joueur_1.pv} et {Joueur_1.potions} Potions. \n le joueur passe le prochain tour")
#     # else:print(f"{Joueur_1.nom} n'a plus de potions.", entree_du_joueur(self))    
                
# boucle joueur 
def entree_du_joueur(self):
    global use
    choix = int(input(" \n Souhaiter vous attaquer(1) ou utiliser une potion(2) ? "))
    if choix ==1:
        attaque(Joueur_1,Ennemi)
        use = False
    if choix == 2 :
        utilise_potion(Joueur_1) and compte_potion(Joueur_1)
        use = True

# version corrigée des potions
def utilise_potion(Joueur_1):
    soin_recu = random.randint(15, 50)
    if Joueur_1.potions>0:
        Joueur_1.pv = soin_recu + Joueur_1.pv
        print(f"{Joueur_1.nom} a utilisé une potion, il a récuperé {soin_recu} PV il lui reste maintenant {Joueur_1.pv} PV et {Joueur_1.potions-1} Potions. \n le joueur passe le prochain tour")
        attaque(Ennemi,Joueur_1)
    elif Joueur_1.potions<=0:
# quand le joueur prend une potion il passe le prochain tour.
        print("le Joueur n'as plus de potions.")
        entree_du_joueur(Joueur_1)

    # else:print(f"{Joueur_1.nom} n'a plus de potions.", entree_du_joueur(self)) 

def compte_potion(Joueur_1):
    if use == True:
        Joueur_1.potions = Joueur_1.potions -1
        
# def actu_valeurs():
#     global soin_recu, dgt_j1,dgt_en
#     dgt_j1 = random.randint(5, 10)
#     dgt_en = random.randint(5, 15)
#     soin_recu = random.randint(15, 50)
    
print("Bonjour et bienvenu dans ce rpg ou jdr en français textuel \n dans ce jeu tu utiliseras les touches 1 et 2 pour choisir d'attaquer ou de te soigner pour venir a bout de l'ennemi, il faudra faire preuve de logique.")

# fonction qui vérifie le tour 
while jeu_en_cours:
    
    entree_du_joueur(Joueur_1)
    verif_victoire(Joueur_1, Ennemi)
    attaque(Ennemi,Joueur_1) 
    verif_victoire(Joueur_1, Ennemi)
    compte_potion(Joueur_1)
    # actu_valeurs()
# ?  Si l'utilisateur choisit la première option (1), vous infligez des points de dégâts à l'ennemi.


# boucle jeu en cour

# si plus de potion lui proposer a nouveau le choix     
# fonction qui verifie les pv de l'ennemi 
# si <=0 le jeu se termine et vous avez perdu la partie
# afficher les pv du joueur et de l'ennemi en fin de tour


