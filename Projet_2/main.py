#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 16:46:22 2021

@author: Robert
"""

# ajouter classe
# ajouter/supprimer eleve
# ajouter/supprimer matiere 
# afficher les eleves d'une classe
# saisir les note des eleve d'une pour une matiere
# calculer les moyennes generales et classer les eleves en fonctions de ces moyennes
# quitter le programme
# sauvegarder les données
# consulter les données de sauvegarde
# afficher la liste des matieres
# afficher les notes par matieres

import os

class Classe : 
    
    """ Une classe d'eleves """
    
    id_classe_compteur = 0
    path_enregistrement_classe_fichier = "/home/fitec/formation_fitec/python/projet/"
    
    def __init__(self,niveau,nom_de_classe) :
        
        self.__id_classe = 0
        self.nombre_eleves = 0
        self.niveau = niveau
        self.nom_de_classe = nom_de_classe
        self.liste_id_eleves = []
        
    # @staticmethod    
    # def enregistrement_classe_fichier(self):
        
    #     if os.path.isfile(self.path_enregistrement_classe_fichier) == False :
            
    #         self._creer_fichier(self.path_enregistrement_classe_fichier,self.nom_enregistrement_classe_fichier)
            
        
    @staticmethod    
    def _creer_fichier(path,nom_fichier,sep="/"):    
        
        """ creer le fichier de sauvegarde """
        
        open(path+sep+nom_fichier, 'w').close()
        
        
    # amelioration possible
    # def modifier_chemin_acces_fichier():
        
Classe._creer_fichier("/home/fitec/formation_fitec/python/projet/","classe.txt")

# Classe.enregistrement_classe_fichier()

premiere_classe = Classe(5,"5_A")


premiere_classe._creer_fichier("/home/fitec/formation_fitec/python/projet/","classe.txt")



class Eleve :   
    
    """ Un(e) eleve """
    
    id_eleve_compteur = 0
    path_enregistrement_eleve_fichier = ""
    
    def __init__(self,nom,prenom,date_de_naissance,nom_classe,niveau) :
        
        self.__id_eleve = 0
        self.nom = nom
        self.prenom = prenom
        self.date_de_naissance = date_de_naissance
        self.nom_classe = nom_classe
        self.niveau = niveau
        self.liste_id_notes = []
        
    @staticmethod      
    def _creer_fichier(path,nom_fichier,sep="/"): 
        
        """ creer le fichier de sauvegarde """
        
        open(path+sep+nom_fichier, 'w').close()


Eleve._creer_fichier("/home/fitec/formation_fitec/python/projet/","eleve.txt")

class Matiere:
    
    """ Une matiere"""
    
    id_matiere_compteur = 0
    path_enregistrement_matiere_fichier = ""
    
    def __init__(self,nom_matiere,niveau) :
        
        self.__id_matiere = 0
        self.nom_matiere = nom_matiere
        self.niveau = niveau
        # amelioration possible
        # self.volume_horaire_global = 0
        
        
    # def __creer_fichier(self,path,nom_fichier,sep="/"): 
        
    #     """ creer le fichier de sauvegarde """
        
    #     open(path+sep+nom_fichier, 'w').close()
        
        
# amelioration possible
# class Creneau_horaire :
    
#     def __init__(self) :
        
#         self.__id_creaneu_horaire = 0
#         self.id_matiere = 0
#         self.id_classe = 0
#         self.id_enseignant = 0
#         self.horaire_debut = 0
#         self.horaire_fin = 0
#         self.duree = 0
        # amelioration possible
        # self.id_salle_de_cours = 0
       
        

        
        
class Note :   
    
    """ Une note """
    
    id_note_compteur = 0
    path_enregistrement_note_fichier = ""
    
    def __init__(self,note,coefficient) :
        
        self.__id_note = 0
        self.note = note
        self.coefficient = coefficient
        self.id_eleve = 0
        self.id_matiere = 0
        #amelioration possible
        # self.id_enseignant = 0
        # self.trimestre = ""
        
        
    def __creer_fichier(self,path,nom_fichier,sep="/"): 
        
        """ creer le fichier de sauvegarde """
        
        open(path+sep+nom_fichier, 'w').close()
        

    
   
# amelioration possible
# class Enseignant :
    
#     def __init__(self) :
        
#         self.__id_enseignant = 0
#         self.nom = ""
#         self.prenom = ""
#         self.matiere = ""
#         self.liste_id_classe = []
        
        
        
# amelioration possible      
# class Emploi_du_temps : 
    
#     def __init(self) :
        
#         self.id_emploi_du_temps = 0
#         self.id_classe = 0
#         self.liste_id_creneau_horaire = []
        
        
        
        
# amelioration possible
# class Salle_de_cours :

#       def __init(self) :
          
#         self.id_salle_de_cours = 0
#         self.numero_salle = 0
#         self.liste_id_creneau_horaire = []
        
