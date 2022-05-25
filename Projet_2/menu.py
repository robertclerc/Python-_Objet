#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 15:17:17 2021

@author: maël
"""

def displayMenu():
    
    print ('Bienvenue dans le menu. Merci de saisir le numéro correspondant à \
           la destination voulue.')

    print('1 : Ajouter des classes')
    print('2 : Ajouter des élève')
    print('3 : Ajouter des matières')
    print('4 : Supprimer un élève')
    print('5 : Supprimer une matière')
    print('6 : Supprimer une classe')
    print('7 : Modifier élève')
    print('8 : Modifier matière')
    print('9 : Afficher liste élèves par classe')
    print('10 : Saisir les notes des élèves pour une matière donnée')
    print('11 : Calculer et afficher les moyennes générales des élèves selon \
          leurs rangs')
    print('12 : Quitter le programme')
    print('13 : Effectuer une sauvegarde des données dans un fichier texte')
    print('14 : Consulter le fichier de sauvegarde')
    print('15 : Affiche liste matières')
    print('16 : Afficher note par matière')
    print('17 To MySQL DataBase')






def userChoice():
    user_input = 'Mauvaise réponse' # on intialise sur une mauvaise réponse qui 
        # invitera donc le user à saisir un élément du menu affiché
    
    while user_input not in list(range(1,18)):
        displayMenu()
        user_input = int(input('Merci de saisir le numéro correspondant \
                               à la destination voulue : '))
        
        # établir une liste pour détailler l'action du numéro séléctionné
        selected = ['Ajouter des classes', 'Ajouter des élèves', 
                    'Ajouter des matières', 'Supprimer un élève',
                    'Supprimer une matière', 'Supprimer une classe', 
                    'Modifier élève','Modifier matière',
                    'Afficher liste élèves par classe',
                    'Saisir les notes des élèves pour une matière donnée', 
                    'Calculer et afficher les moyennes générales des élèves selon leurs rangs', 
                    'Quitter le programme',
                    'Effectuer une sauvegarde des données dans un fichier texte', 
                    'Consulter le fichier de sauvegarde']
        
        print(f'Vous vaez choisi {user_input}, redirection vers \
              {selected[user_input]}')
        
        # gestion du 12 => quitter le programme
        if user_input == 12:
            print('___À bientôt! Fermeture du programme.___')
        else: 
            return user_input
        
userChoice()