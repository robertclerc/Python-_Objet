#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 16:28:56 2021

@author: fitec
"""


from abc import ABC, abstractmethod

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

    def get_nom(self):
        
        return self.__nom    
    
    def get_prenom(self):
        
        return self.__prenom
        
    def get_id(self):
        
        return self.__id_employe

    def afficher_coordonnes_personnel(self):
        
        print("Ci - joint les coordonnees de l'employé : \n")
        print(self.nom, self.prenom)
        print(self.numero_rue, self.nom_rue)
        print(self.code_postal,self.ville)
        
               
    def augmenter_salaire(self,augmentation):
        
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
            
            print("N° : ",self.get_id())
            print("Nom du salarié : ",self.get_nom())
            print("Adresse : ",self.numero_rue,self.nom_rue)
            print("Ville : ",self.ville)
            print("Fonction : ",self.fonction)
            print("Salaire Fixe : ",self.salaire_mensuel_brut)
            print("Commission : ",self.commission)
            print("CA : ",self.chiffre_affaire)
            print("Remboursement des notes de frais: :",self.frais)
            print("Total à payer : ",salaire)
        
        
        else :

            print("N° : ",self.get_id())
            print("Nom du salarié : ",self.get_nom())
            print("Adresse : ",self.numero_rue,self.nom_rue)
            print("Ville : ",self.ville)
            print("Fonction : ",self.fonction)
            print("Salaire  à payer : ",self.salaire_mensuel_brut)
            
            
            
"""

Exemple d'utilisation de la classe Personnel

"""
   
# personnel_1 = Personnel(1,"Clerc")   

# #genere une erreur car l'attribut est prive
# #print(personnel_1.prenom)

# #genere une erreur car la methode est prive
# #personnel_1.__modifier_prenom("Robert")

# #Affiche vide
# print(personnel_1.get_prenom())

# personnel_1.changer_prenom("Robert")

# #Affiche Robert
# print(personnel_1.get_prenom())



# """

# Exemple d'utilisation de la classe Salarie

# """

# employee_1 = Salarie(2,"Jean","Consultant",10000)

# #genere une erreur car l'attribut est prive
# # print(employee_1.prenom)

# # genere une erreur car la methode est prive
# # donc uniquement accessible dans la classe
# # l'heritage de fonctionne pas pour les méthodes privées
# # employee_1.__modifier_prenom("Robert")

# # Changement d'attribut privé

# employee_1.changer_prenom("Jean")

# # Changement d'attributs public
          
# employee_1.numero_rue = 3
# employee_1.nom_rue = "Place Gambetta"
# employee_1.code_postal = 75000
# employee_1.ville = "Grenoble"
# employee_1.salaire_mensuel_brut = 7500
# employee_1.fonction = "REPRESENTANT"
# employee_1.frais = 750
# employee_1.commission = 5440
# employee_1.numero_plafond = 1   


# employee_1.afficher_salaire()      

# print("\n")


# """

# Declaration d'un deuxieme salarié

# """


# employee_2 = Salarie(3,"Marc","Magasinier",10000)
   

# employee_2.changer_prenom("Olivier")  
# employee_2.numero_rue = 87
# employee_2.nom_rue = "Rue de la liberté"
# employee_2.code_postal = 69000
# employee_2.ville = "Lyon"
# employee_2.salaire_mensuel_brut = 8690

   
# employee_2.numero_rue = 52
# employee_2.nom_rue = "Rue de grèce"
# employee_2.code_postal = 75000
# employee_2.ville = "Soliman"

# employee_2.salaire_mensuel_brut = employee_2.salaire_mensuel_brut = 8690 * 1.05


# employee_2.augmenter_chiffre_affaire(100000)
# employee_2.augmenter_chiffre_frais(700)


# print("\n")
# employee_2.afficher_salaire()  
# print("\n")


#######################
# Extention du projet #
#######################

class P1:
    """Documentation de la classe P1"""
    #Attributs de classe qui ne necessite pas d'instance pour etre utilisé
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
    
    # methode de classe qui ne necessite pas d'instanciation pour etre utilise
    
    #public
    @classmethod
    def get_nb(cls):
        
        cls.nb+=1
        return P1.nb

    #privee
    @classmethod
    def __get_nb_private(cls):
        
        cls.nb+=1
        return P1.nb
    
    # methode de classe qui n'utilise pas les objets et les attributs de sa classe
    # Cette methode peut etre utilise sans instancier de classe

    #public
    @staticmethod
    def get_nb_static(nb_static):  

        return nb_static+P1.nb

    #privee
    @staticmethod
    def __get_nb_static_private(nb_static):  

        return nb_static+P1.nb
    


#exemple d'utilisation de la methode de classe get_nb()

# print(P1.nb)
# P1.get_nb()
# print(P1.nb)

# print("\n")

#exemple d'utilisation de la methode statique get_nb_static()

# print(P1.get_nb_static(5))


# # exemple d'utilisation de la methode de classe __get_nb_private()
# # ne fonctionne pas car la méthode est privée

# print(P1.nb)
# P1.__get_nb_private()
# print(P1.nb)

# print("\n")

# # exemple d'utilisation de la methode statique __get_nb_static_private()
# ne fonctionne pas car la méthode est privée
# print(P1.__get_nb_static_private(5))


class P2(P1):
    """Documentation de la classe P2"""
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




# Objet P1
objet_P1 = P1(1,"personne_1")

# Objet P2 avec une classe herite de la classe P1
objet_P2 = P2(2,"personne_2")


# Declaration d'une classe abstraite

class P3_abstract(ABC):
    
    
    def __init__(self,number=0):
        
        self.number=number
    
    @abstractmethod
    def methode_abstraite(self):
        pass


    def motor(self):
        
        return 3


class P4_inherit(P3_abstract):
    
    
    def __init__(self,number=0):
        
        P3_abstract.__init__(self,number)
    
    
    def methode_abstraite(self):
        
        print("Number is",self.number)
        
        
    #Override de la méthode mère
    def motor(self):
        
        return 4
            
    # appel de la fonction mère motor grace à la fonction super()
    def motor_inherited(self):
        
        return super().motor()
        
 
class P5_inherit(P3_abstract):
    
    def __init__(self,number=0):
        
        P3_abstract.__init__(self,number)
    
    def methode_abstraite(self):
        
        print("Number is the",self.number)
    
    #Override de la méthode mère
    def motor(self):
        
        return 5
            
    # appel de la fonction mère motor grace à la fonction super()
    def motor_inherited(self):
        
        return super().motor()


    
#Declaration d'une classe abstraite
#from abc import ABC, abstractmethod
      
#Ne fonctionne pas car la methode est abstraite
#objet_P3 = P3_abstract()
        

objet_P4 = P4_inherit(2)
# objet_P4.methode_abstraite()


objet_P5 = P5_inherit(4)
# objet_P5.methode_abstraite()



#appel d'une fonction override

# print(objet_P4.motor())

# print(objet_P4.motor_inherited())





#Multiple heritage de classe

class Ecran :
    
    def __init__(self):
        
        self.longeur=40
        self.largeur=30
        self.diagonale=50
        self.constructeur="Sony"
        
        
    def allumer_ecran(self):
        
        return "ecran allumer"
    
    def eteindre_ecran(self):
        
        return "ecran eteint"   
      
    def afficher_menu(self):
        
        return "menu ecran afficher"
    
 
    
    
class Peripherique_sortie_ordinateur :
    
    def __init__(self) :
        
        self.constructeur = "Samsung"
        self.type_sortie = "Visuel"
        
        
    def afficher_menu(self):
        
        return "menu peripherique afficher"    


class Ecran_ordinateur(Ecran,Peripherique_sortie_ordinateur) :
    
    def __init__(self):
        
        Ecran.__init__(self)
        Peripherique_sortie_ordinateur.__init__(self)
        
    def allumer_ecran(self):
            
        return "ecran ordinateur allumer"
        
    
    
Premier_ecran_ordinateur = Ecran_ordinateur()

print(Premier_ecran_ordinateur.allumer_ecran())
print(Premier_ecran_ordinateur.eteindre_ecran())
print(Premier_ecran_ordinateur.afficher_menu())



# # retourne tous les attributs et toutes les methodes de l'objet
# print(dir(objet_P1))
# print(dir(objet_P2))

# # retourne la classe de l'objet
# print(objet_P1.__class__)
# print(objet_P2.__class__)

# # retourne la classe de l'objet
# print(objet_P1.__delattr__)

# # retourne l'ensemble des paires attributs/valeurs sous forme de dictionnaire
# print(objet_P1.__dict__)
# print(objet_P2.__dict__)

# # retourne la doc de classe
# print(objet_P1.__doc__)
# print(objet_P2.__doc__)

# # retourne un booleen resultant de la comparaison de deux objets
# peut etre modifie
# print(objet_P1.__eq__)
# print(objet_P1.__eq__(objet_P1))
# print(objet_P1.__eq__(objet_P2))

# a approfondir
#print(objet_P1.__format__)
#print(objet_P1.__format__("test"))

# aucune implementation par defaut, elle doit etre créer
#permet de comparer deux attributs avec >=
#print(objet_P1.__ge__)

# retourne la classe de l'objet
#print(objet_P1.__getattribute__)

# retourne la classe de l'objet
#print(objet_P1.__gt__)

# retourne la classe de l'objet
#print(objet_P1.__hash__)

# retourne la classe de l'objet
#print(objet_P1.__init_subclass__)

# retourne la classe de l'objet
#print(objet_P1.__le__)

# retourne la classe de l'objet
#print(objet_P1.__lt__)

# retourne la classe de l'objet
#print(objet_P1.__module__)

# retourne la classe de l'objet
#print(objet_P1.__ne__)

# retourne la classe de l'objet
#print(objet_P1.__new__)

# retourne la classe de l'objet
#print(objet_P1.__reduce__)

# retourne la classe de l'objet
#print(objet_P1.__reduce_ex__)

# retourne la classe de l'objet
#print(objet_P1.__repr__)

# retourne la classe de l'objet
#print(objet_P1.__setattr__)

# retourne la classe de l'objet
#print(objet_P1.__sizeof__)

# retourne la classe de l'objet
#print(objet_P1.__str__)

# retourne la classe de l'objet
#print(objet_P1.__subclasshook__)

# retourne la classe de l'objet
#print(objet_P1.__weakref__)


# print(inspect.getmembers(test2))

# print(test2.get_id_employe())
# print(test2.get_id_nom())
# print(test2.get_id_Prenom())



