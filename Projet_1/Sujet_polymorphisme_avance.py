#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 16:28:56 2021

@author: fitec
"""

import inspect

#declaration des variables globales

liste_plafond_frais = {1:1000,2:1500,3:2000,4:2500,5:3000}

#Declaration des classes

class Personnel:
    
    def __init__(self,id_employe,nom):
        
        self.__id_employe = id_employe
        self.__nom = nom
        self.__prenom = "Vide"
        self.numero_rue = 45
        self.nom_rue = "avenue jean martin"
        self.code_postal = 75000
        self.ville = "Paris"
        self.salaire_mensuel_brut = 2800
        
        
    def changer_prenom(self,prenom):
        
        self.__modifier_prenom(prenom)
        
        
    #declaration d'une methode privee
    def __modifier_prenom(self,prenom):
        
        self.__prenom = prenom
        
    
    def get_prenom(self):
        
        return self.__prenom
        
        
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
     
    def __init__(self,id_employe,nom,fonction,chffre_affaire):
        #si on cree salarie, comment passer des variables a personnel ?
        #comment gerer les attributs qui ont le meme nom dans l'heritage de classe ?
        Personnel.__init__(self,id_employe,nom)
        
        self.__fonction = "Data Analyst"
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
            
            
            
"""

Exemple d'utilisation de la classe Personnel

"""
   
personnel_1 = Personnel(1,"Clerc")   

#genere une erreur car l'attribut est prive
#print(personnel_1.prenom)

#genere une erreur car la methode est prive
#personnel_1.__modifier_prenom("Robert")

personnel_1.changer_prenom("Robert")

print(personnel_1.get_prenom())



"""

Exemple d'utilisation de la classe Salarie

"""

employee_1 = Salarie(2,"Jean","Consultant",10000)

#genere une erreur car l'attribut est prive
#print(employee_1.prenom)

#genere une erreur car la methode est prive
#employee_1.__modifier_prenom("Robert")

employee_1.changer_prenom("Jean")

print(employee_1.get_prenom())
   
        
# employee_1.id = 1
# employee_1.nom = "ABIDI"
# employee_1.prenom = "Besma"
# employee_1.numero_rue = 3
# employee_1.nom_rue = "Rue el Hayet"
# employee_1.code_postal = 75000
# employee_1.ville = "JENDOUBA"
# employee_1.salaire_mensuel_brut = 7500



# employee_1.fonction = "REPRESENTANT"
# employee_1.chiffre_affaire = 186000
# employee_1.frais = 750
# employee_1.commission = 5440
# employee_1.numero_plafond = 1   


# employee_1.afficher_salaire()      


# print("\n")


# employee_2 = Salarie()
   
        
# employee_2.id = 9
# employee_2.nom = "AYADI"
# employee_2.prenom = "Salah"
# employee_2.numero_rue = 87
# employee_2.nom_rue = "Rue de la liberté"
# employee_2.code_postal = 75000
# employee_2.ville = "TUNIS"
# employee_2.salaire_mensuel_brut = 8690



# employee_2.fonction = "Magasinier"
 


# employee_2.afficher_salaire()  
   
# employee_2.numero_rue = 52
# employee_2.nom_rue = "Rue de grèce"
# employee_2.code_postal = 75000
# employee_2.ville = "Soliman"

# employee_2.salaire_mensuel_brut = employee_2.salaire_mensuel_brut = 8690 * 1.05






# employee_1.augmenter_chiffre_affaire(100000)
# employee_1.augmenter_chiffre_frais(700)


# print("\n")
# employee_1.afficher_salaire()  
# print("\n")
# employee_2.afficher_salaire()  



class P1:
    
    nb = 0
    
    nb_static = 10
    
    def __init__(self,id_employe,nom):
        
        self.__id_employe = id_employe
        self.__nom = nom
        self.__prenom = "Vide"
        self.numero_rue = 45
        self.nom_rue = "avenue jean martin"
        self.code_postal = 75000
        self.ville = "Paris"
        self.salaire_mensuel_brut = 2800
        
    def get_id_employe(self):

        return self.__id_employe

    def __get_id_nom(self):

        return self.__nom
    
    def get_id_prenom(self):

        return self.__prenom
    
    
    @classmethod
    def get_nb(cls):
        
        cls.nb+=1
        return P1.nb
    
    
    @staticmethod
    def get_nb_static(nb_static):  

        return nb_static+P1.nb
    
    
    
    @classmethod
    def __get_nb_private(cls):
        
        cls.nb+=1
        return P1.nb
    
class P2(P1):
    
    def __init__(self,id_employe,nom):
        
        P1.__init__(self,id_employe,nom)
        
        self.__id_employe = 1
        self.nom = "michel"
        self.prenom = "Prenom"
        
    def get_id_employe(self):

        return self.__id_employe
    
    def get_id_nom(self):

        return self.nom

    def get_id_Prenom(self):

        return self.prenom

print("test = ", P1.get_nb())
print("test = ", P1.get_nb())

print("test = ", P1.get_nb_static(2))
print("test = ", P1.get_nb_static(5))

test = P1(1,"test")


test2 = P2(2,"test2")


#print(dir(test2))
print(inspect.getmembers(test2))

print(test2.get_id_employe())
print(test2.get_id_nom())
print(test2.get_id_Prenom())



