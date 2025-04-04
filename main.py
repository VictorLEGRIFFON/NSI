import pickle

contacts = []
   
#---------------------------------Fonction pour Ajouter un contact---------------------------------

def enregistrer_contact():
    nom_fichier = "repertoire"
    nom = str(input("Donner un nom : "))
    nom = nom.capitalize()
    numero = input("Donner un Numéro : ")
    questAnnniv = input("Voulez-vous ajouter un anniversaire (Y/N) : ")
    if questAnnniv == "Y" or questAnnniv == "y":
        jour = input("Jour : ")
        mois = input("Mois : ")
        année = input("Année : ")
        anniv = (jour+"/"+mois+"/"+année)
        print(anniv)
    else:
        anniv = ''
    questMail = input("Voulez-vous ajouter un mail (Y/N) : ")
    if questMail == "Y" or questMail == "y":
        mail = input("Adresse Mail : ")
    else:
        mail = ''
    annivText = "Anniversaire : " + anniv
    mailText = "Mail : " + mail
    contacts.append(["Nom : ", nom, "Numéro : ", numero, annivText if anniv else "", mailText if mail else ""])
    with open(nom_fichier, "wb") as fichier:
        pickle.dump(contacts, fichier)
    

#---------------------------------Fonction pour lire les contacts---------------------------------

def lire_contacts():
    nom_fichier = "repertoire"
    try:
        with open(nom_fichier, "rb") as fichier:
            contenu = pickle.load(fichier)
            print(contenu)
    except:
        print("Aucun contact")
    

#---------------------------------Fonction pour Rechercher les contacts---------------------------------



#---------------------------------Fonction pour Supprimer les contacts---------------------------------

def supprimer_contact():
    nom_fichier = "repertoire"
    nomChercher = str(input("Nom du contact à supprimer : "))
    print(contacts)
    for elm in contacts:
        for nom in elm:
            if nomChercher == str(nom):
                with open(nom_fichier, "wb") as nom_fichier:
                    contacts.remove(elm)
                    print("Le contact ", nom ,"a été supprimé")
                    break   
            elif nomChercher == "Nom : ":
                pass
            
            else:
                print("Contact non trouvé")

#---------------------------------Fonctiion pour créer le menu-------------------------------------

while True:
    def menu():
        print("-"*30)
        print("  Gestionnaire de contacts")
        print("1. Ajouter un contact")
        print("2. Lire les contacts")
        print("3. Rechercher un contact")
        print("4. Supprimer un contact")
        choix = input("Votre choix: ")
        if choix == "1":
            enregistrer_contact()
        elif choix == "2":
            print("-"*30)
            print("Répertoire des contacts :")
            print("")
            lire_contacts()
        elif choix == "3":
            lire_contacts()
        elif choix == "4":
            supprimer_contact()
    menu()



