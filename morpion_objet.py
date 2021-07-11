# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import tkinter as tk
import random


class Joueur:
    
    
    def __init__(self,score,name,symbole):
        
        self.__score = 0
        self.premier_joueur = 0
        self.name=name
        self.symbol=symbole
        
    def get_score(self):
        
        return self.__score
        
    def augmenter_score(self):
        
        self.__score = self.__score + 1
        
    def score_zero(self):
        
        self.__score = 0
        
    def get_premier_joueur(self,pj):
        
        self.premier_joueur = pj
        
    def set_premier_joueur(self):
        
        return self.premier_joueur

    
class Case(): 
    
    #attribut de classe,accessibkles entre eux n'ont pas acces aux attributs d'instance
    # les changer permet de les modifier pour toutes les futures instanciations
    #a eviter sauf poru faire une variable globale a toutes les instances de la classe
    # loc_x_t = 0
    # loc_y_t = 0
    # statut = "Vide"
    
    def __init__(self,X,Y,fenetre):
        
        #attribut d'instance, a privilieger pour garder les attributs propres a l'instanciation
        self.loc_x = X
        self.loc_y = Y
        self.statut = "Vide"
        self.bouton = tk.Button(fenetre, text ='',width=10, height=5,command=self.bouton_clique)
        
        self.bouton.place(x=(X+1)*75,y=(Y+1)*75)


    def bouton_clique(self):

        j1=Joueur_1.set_premier_joueur()
        j2=Joueur_2.set_premier_joueur()
        

        if self.bouton['text']=='':
        
            if(j1):
                
                self.bouton['text']=Joueur_1.symbol

                Joueur_2.get_premier_joueur(1)
                Joueur_1.get_premier_joueur(0)
                la_grille.verifier_grille(self.bouton['text'],Joueur_1.name)
                
                
                
            elif(j2):
                
                self.bouton['text']=Joueur_2.symbol

                Joueur_1.get_premier_joueur(1)
                Joueur_2.get_premier_joueur(0)
                la_grille.verifier_grille(self.bouton['text'],Joueur_2.name)
                

    # @classmethod
    # def methode_classe(cls):

    
class Grille:
    

    def __init__(self,X,Y,alignement_victoire,premier_joueur):
        #methode d'instance

        if alignement_victoire < X or alignement_victoire < Y :
            
            print("erreur")
            #gerer l'erreur
            
        # encapsulation 
        # self.__x = x
            
        self.nb_colonnes = X
        self.nb_lignes = Y
        self.score_final = 0
        self.nom_vainqueur = ""
        self.i = 0
        self.j = 0
        self.score_a_faire=alignement_victoire

        
            
        #fenetre d'affichage    
        self.fenetre = tk.Tk()
        self.fenetre.minsize(width=370, height=400)

        # itinialise la grille
        self.matrix = [[j for j in range(Y)] for i in range(X)]    

        for i in range(0,X):
            
            for  j in range(0,Y):

                self.matrix[i][j] = Case(i,j,self.fenetre)
                
        
        self.condition_victoire = alignement_victoire
        
        self.title = tk.Label( self.fenetre, text="Morpion")
        self.title.place(x = 150, y = 10)
        
        self.score_joueur_1 = tk.Label( self.fenetre, text="Score joueur 1 : "+str(Joueur_1.get_score()))
        self.score_joueur_1.place(x = 70, y = 30)
        
        self.score_joueur_2 = tk.Label( self.fenetre, text="Score joueur 2 : "+str(Joueur_2.get_score()))
        self.score_joueur_2.place(x = 190, y = 30)
        
        self.vainqueur = tk.Label( self.fenetre, text="")
        self.vainqueur.place(x = 130, y = 50)
        
        
        self.reinit = tk.Button(self.fenetre, text ='Réinitaliser la partie',width=20, height=1,command=self.reinitialisation) 
        self.reinit.place(x = 110, y = 330)
        
        self.reinit_score = tk.Button(self.fenetre, text ='Réinitaliser les scores',width=20, height=1,command=self.reinit_score) 
        self.reinit_score.place(x = 110, y = 370)
     
    def display_windows(self):
        
        self.fenetre.mainloop()   
             
    def verifier_grille(self,symbole_joueur,name_joueur):
        

        self.verifer_colonnes(symbole_joueur,name_joueur)
        self.verifer_lignes(symbole_joueur,name_joueur)
        self.verifer_diagonales_1(symbole_joueur,name_joueur)
        self.verifer_diagonales_2(symbole_joueur,name_joueur)
        
        
        if  self.nom_vainqueur!="":

            #on bloque tout les boutons
            self.bloquer_bouton()
            
            if self.nom_vainqueur==Joueur_1.name:
            
                Joueur_1.augmenter_score()
                la_grille.vainqueur["text"]="Joueur 1 a gagné"
                self.score_joueur_1 = tk.Label( self.fenetre, text="Score joueur 1 : "+str(Joueur_1.get_score()))
                self.score_joueur_1.place(x = 70, y = 30)
                
            elif self.nom_vainqueur==Joueur_2.name:
                
                Joueur_2.augmenter_score()
                la_grille.vainqueur["text"]="Joueur 2 a gagné"
                self.score_joueur_2 = tk.Label( self.fenetre, text="Score joueur 2 : "+str(Joueur_2.get_score()))
                self.score_joueur_2.place(x = 190, y = 30)
                

                
    def verifer_colonnes(self,symbole_joueur,name_joueur):
        
        while self.i<self.nb_colonnes:

            while self.j<self.nb_lignes:
                
                valeur = self.matrix[self.i][self.j].bouton['text']
                
                if valeur==symbole_joueur:
                    
                    self.score_final+=1
                    
                else:
                    
                    self.score_final=0
                    
                
                if self.score_final == self.score_a_faire:
                    
                    self.nom_vainqueur=name_joueur

                
                self.j+=1
                
            self.j = 0
            self.i+=1
        
        
        self.i = 0
        self.j = 0
        self.score_final=0
    def verifer_lignes(self,symbole_joueur,name_joueur):
        
        
        while self.i<self.nb_lignes:

            while self.j<self.nb_colonnes:

                valeur = self.matrix[self.j][self.i].bouton['text']
                
                if valeur==symbole_joueur:
                    
                    self.score_final+=1
                    
                else:
                    
                    self.score_final=0

                if self.score_final == self.score_a_faire:
                    
                     self.nom_vainqueur=name_joueur

                self.j+=1
                
            self.j = 0
            self.i+=1
        
        
        self.i = 0
        self.j = 0
        self.score_final=0
    def verifer_diagonales_1(self,symbole_joueur,name_joueur):
        
                
        while self.i<self.nb_colonnes:

            while self.j<self.nb_lignes:
                valeur = self.matrix[self.i][self.j].bouton['text']
                
                if valeur==symbole_joueur:
                    
                    self.score_final+=1
                    
                else:
                    
                    self.score_final=0
                    
                if self.score_final == self.score_a_faire:

                     self.nom_vainqueur=name_joueur
                
                self.j+=1
                self.i+=1
        
        
        self.i = 0
        self.j = 0
        self.score_final=0
    def verifer_diagonales_2(self,symbole_joueur,name_joueur):

        self.i = 0
        self.j = self.nb_lignes - 1

        while self.i<self.nb_colonnes:
            
            while self.j>=0:

                valeur = self.matrix[self.i][self.j].bouton['text']
                
                if valeur==symbole_joueur:
                    
                    self.score_final+=1
                    
                else:
                    
                    self.score_final=0
                    
                if self.score_final == self.score_a_faire:

                     self.nom_vainqueur=name_joueur
                
                self.j =  self.j - 1
                self.i+=1
        
        self.i = 0
        self.j = 0
        self.score_final=0

    def bloquer_bouton(self):

        for i in range(0,self.nb_colonnes):
            
            for  j in range(0,self.nb_lignes):

                self.matrix[i][j].bouton['state'] = "disabled"

    def reinitialisation(self):
        
        self.vainqueur["text"]=""
        self.nom_vainqueur=""
        
        for i in range(0,self.nb_colonnes):
            
            for  j in range(0,self.nb_lignes):

                self.matrix[i][j].bouton['state'] = "normal"
                self.matrix[i][j].bouton['text'] = ""
                

    def reinit_score(self):
    
        Joueur_1.score_zero()
        Joueur_2.score_zero()
        
        self.score_joueur_1['text'] = "Score joueur 1 : "+str(Joueur_1.get_score())
        self.score_joueur_2['text'] = "Score joueur 2 : "+str(Joueur_2.get_score())


def choisir_premier_joueur(J1,J2):
          
    jpp = random.random()

    if jpp < 0.5 :

         jp = J1

    else:

         jp = J2

    return jp
                
        
#heritage de grille en choisissant la couleur de la case a faire



Joueur_1=Joueur(0,"Joueur 1","O")
Joueur_2=Joueur(0,"Joueur 2","X")


premier_joueur = choisir_premier_joueur(Joueur_1.name,Joueur_2.name)


if premier_joueur=="Joueur_1":

    Joueur_1.get_premier_joueur(1)

else:
    
    Joueur_2.get_premier_joueur(1)



la_grille = Grille(3,3,3,premier_joueur)

#

la_grille.display_windows()






































    
