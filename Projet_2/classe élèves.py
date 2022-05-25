class  eleve :
   
    def __init__(self, code, nom, prenom, naissance, classe):
        self.code = code
        self.nom = nom
        self.prenom = prenom
        self.naissance = 1/1/2000
        self.classe = classe
   
liste_eleves =[]      
def ajouter():
    eleve_suivant = ""   
    while eleve_suivant not in ["FIN", "fin"]:
        nbr_eleves = int(input("quel est le nombre d'élèves à rajouter ? "))
        
        for i in range(nbr_eleves) :
            code = int(input("Saisir le code "))
            nom = input("saisir le nom ")
            prenom = input("saisir le prénom ")
            naissance = input("saisir la date de naissance ")
            classe = input("saisir la classe ")
            liste_eleves.append(eleve(code, nom, prenom, naissance, classe))
            eleve_suivant = input("élève suivant ")

    with open("/home/fitec/Bureau/eduserv.txt","a") as file:
        for el in liste_eleves :   
            file.write("code : " + str(el.code) + " ; " +"Nom : " +  el.nom + " ; " + "Prénom : " + el.prenom + " ; " + "Naissance : " + str(el.naissance) + " ; " + "Classe : " + str(el.classe) + "\n")

