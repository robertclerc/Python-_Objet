#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 16:28:56 2021

@author: fitec
"""

#declaration des variables globales

liste_plafond_frais = {1:1000,2:1500,3:2000,4:2500,5:3000}

#Declaration des classes

class Personnel :
    
    def __init__(self):
        
        self.id = 1
        self.nom = "Clerc"
        self.prenom = "Robert"
        self.numero_rue = 45
        self.nom_rue = "avenue jean martin"
        self.code_postal = 75000
        self.ville = "Paris"
        self.salaire_mensuel_brut = 2800
        
        
    def afficher_coordonnes_personnel(self):
        
        print("Ci - joint les coordonnees de l'employé : \n")
        print(self.nom, self.prenom)
        print(self.numero_rue, self.nom_rue)
        print(self.code_postal,self.ville)
        
               
    def augmenter_selaire(self,augmentation):
        
        self.salaire_mensuel_brut += augmentation
        
        
    def changer_adresse(self,numero_rue,nom_rue,code_postal,ville):

        self.numero_rue = numero_rue
        self.nom_rue = nom_rue
        self.code_postal = code_postal
        self.ville = ville
        
  
class Salarie(Personnel):
     
    def __init__(self):
        #comment gerer les attributs qui ont le meme nom dans l'heritage de classe ?
        Personnel.__init__(self)
        
        self.fonction = "Data Analyst"
        self.chiffre_affaire = 0
        self.frais = 0
        self.commission = 0
        self.numero_plafond = 3
    
    
    def afficher_coordonnes_salarie(self):
        
        print("Ci - joint les coordonnees de l'employé : \n")
        print(self.nom, self.prenom)
        print(self.numero_rue, self.nom_rue)
        print(self.code_postal,self.ville)
        
        
    def changer_fonction(self,nouvelle_fonction):
        
        self.fonction = nouvelle_fonction
        
        
    def affiche_salaire(self):
        
        print(self.salaire_mensuel_brut)
        
        
    def augmenter_chiffre_affaire(self,nouveau_chiffre_affaire):
        
        self.chiffre_affaire += nouveau_chiffre_affaire
        
  
    def augmenter_chiffre_frais(self,nouveau_frais):
        
        self.frais += nouveau_frais
        
        
    def remise_zero_CA_et_frais(self):
        
        self.chiffre_affaire = 0
        self.frais = 0
        
        
    def calcul_salaire(self):
     
         if self.chiffre_affaire < 100000:
         
             self.commission = self.chiffre_affaire * 0.02
         
         elif self.chiffre_affaire < 200000:

             self.commission = 2000 + ( self.chiffre_affaire - 100000 ) * 0.04
         
         else:
         
             self.commission = 6000 + ( self.chiffre_affaire-  200000 ) * 0.06
             
             
    def calcul_plafond_frais(self):
        
   
        plafond_employe = liste_plafond_frais[self.numero_plafond]
  
        if self.frais > plafond_employe : 
            
            return plafond_employe
        
        else:
            
            return self.frais
        

        
    def afficher_salaire(self):
        
        
        if self.fonction=="REPRESENTANT" : 
            
            self.calcul_salaire()
            
            salaire = self.salaire_mensuel_brut + self.commission + self.calcul_plafond_frais()
            
            print("N° : ",self.id)
            print("Nom du salarié : ",self.nom)
            print("Adresse : ",self.numero_rue,self.nom_rue)
            print("Ville : ",self.ville)
            print("Fonction : ",self.fonction)
            print("Salaire Fixe : ",self.salaire_mensuel_brut)
            print("Commission : ",self.commission)
            print("CA : ",self.chiffre_affaire)
            print("Remboursement des notes de frais: :",self.frais)
            print("Total à payer : ",salaire)
        
        
        else :

            print("N° : ",self.id)
            print("Nom du salarié : ",self.nom)
            print("Adresse : ",self.numero_rue,self.nom_rue)
            print("Ville : ",self.ville)
            print("Fonction : ",self.fonction)
            print("Salaire  à payer : ",self.salaire_mensuel_brut)
            
            
   
   
   

employee_1 = Salarie()
   
        
employee_1.id = 1
employee_1.nom = "Mickael"
employee_1.prenom = "Laffrata"
employee_1.numero_rue = 3
employee_1.nom_rue = "Rue pasteur"
employee_1.code_postal = 75000
employee_1.ville = "Maubeuge"
employee_1.salaire_mensuel_brut = 7500



employee_1.fonction = "REPRESENTANT"
employee_1.chiffre_affaire = 186000
employee_1.frais = 750
employee_1.commission = 5440
employee_1.numero_plafond = 1   


employee_1.afficher_salaire()      


print("\n")


employee_2 = Salarie()
   
        
employee_2.id = 9
employee_2.nom = "Marc"
employee_2.prenom = "Anthony"
employee_2.numero_rue = 87
employee_2.nom_rue = "Rue de la liberté"
employee_2.code_postal = 75000
employee_2.ville = "Bordeaux"
employee_2.salaire_mensuel_brut = 8690



employee_2.fonction = "Magasinier"
 


employee_2.afficher_salaire()  
   
employee_2.numero_rue = 52
employee_2.nom_rue = "Rue de grèce"
employee_2.code_postal = 75000
employee_2.ville = "Bordeaux"

employee_2.salaire_mensuel_brut = employee_2.salaire_mensuel_brut = 8690 * 1.05






employee_1.augmenter_chiffre_affaire(100000)
employee_1.augmenter_chiffre_frais(700)


print("\n")
employee_1.afficher_salaire()  
print("\n")
employee_2.afficher_salaire()  


