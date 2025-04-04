from action1 import *
from action2 import *
from action3 import *
from action4 import *
from action5 import *
import pickle



listeMois = ["janvier", "fevrier", "mars", "avril", "mai", "juin" , "juillet", "aout", "septembre", "octobre", "novembre", "decembre","/"]
listeChiffre = ["0","1","2","3","4","5","6","7","8","9"]
listeCaractereMail = ["@","gmail",".","com","fr","net","org","/","_","-"]


elementActif = []





while True:

    print("        CONTACT")
    print("")
    print("1. Ajouter un contact")
    print("2. Modifier un contact")
    print("3. Supprimer un contact")
    print("4. Voir mes contacts")
    print("5. Chercher un contact")
    
    action = int(input("Que voulez_vous faire : "))
    if action == 1:
        nom = input("Nom : ")
        numero = input("Numéro : ")
        elementActif.append(nom)
        elementActif.append(numero)
        questAnniv = input("Voulez-vous ajouter un anniversaire ? ")
        if questAnniv == "Y" or questAnniv == "y":
            anniv = input("Date d'anniversaire : ")
            elementActif.append(anniv)
        else:
            pass
        questMail = input("Voulez-vous ajouter un mail ?")
        if questMail == "Y" or questMail == "y":
            mail = input("Mail : ")
            elementActif.append(mail)
        else:
            pass
        

        

        
            
    
        validation = input("Valider l'enregistrement : ")
        if validation == "Y" or validation == "y":
            for elm in elementActif:
                print(elm, end=" ")
                for k in listeMois:
                    if k in elm:
                        print("mois")
                        break
                for k in listeChiffre:
                    if k in elm:
                        print("chiffre")
                        break
                for k in listeCaractereMail:
                    if k in elm:
                        print("mail")
                        break
            fichierActif = open("contact.txt", "wb")
            pickle.dump(elementActif, fichierActif)
            fichierActif.close()
            print("Contact enregistré")
        else:
            print("Contact non enregistré")
            elementActif.clear()
            
    elif action == 2:
        print("Modifier Un Contact")
        
        print("Chercher:")
        print("1. Nom")
        print("2. Numero")
        print("3. Anniv")
        print("4. Mail")
        elementChercher = input("/")
        if elementChercher == "4":
            pass
        elif elementChercher == "3":
            pass
        elif elementChercher == "2":
            pass
        elif elementChercher == "1":
            pass
            
    elif action == 3:
        pass
    elif action == 4:
        pass
    elif action == 5:
        pass
