import pickle



listeMois = ["janvier", "fevrier", "mars", "avril", "mai", "juin" , "juillet", "aout", "septembre", "octobre", "novembre", "decembre"]
listeChiffre = ["O","1","2","3","4","5","6","7","8","9"]
listeCaractereMail = ["@","gmail","."]


listeNom = []
lsiteNumero = []
listeMail = []
listeAnniv = []



while True:

    print("VOS CONTACT")
    print("")
    print("1. Ajouter un contact")
    print("2. Modifier un contact")
    print("3. Supprimer un contact")
    print("4. Voir mes contacts")
    print("5. Chercher un contact")
    
    action = int(input("Que voulez_vous faire : "))
    if action == 1:
        nom = input("Nom : ")
        numero = int(input("Numéro : "))
        questAnniv = input("Voulez-vous ajouter un anniversaire ? ")
        if questAnniv == "Y":
            anniv = input("Date d'anniversaire : ")
        else:
            pass
        questMail = input("Voulez-vous ajouter un mail ?")
        if questMail == "Y":
            mail = input("Mail : ")
        else:
            pass
        if questAnniv == "Y" and questMail == "Y":
            print(nom,numero,anniv,mail)
            listeNom.append(nom)
            lsiteNumero.append(numero)
            listeAnniv.append(anniv)
            listeMail.append(mail)
        elif questAnniv == "Y" and questMail != "Y":
            print(nom,numero,anniv)
            listeNom.append(nom)
            lsiteNumero.append(numero)
            listeAnniv.append(anniv)
            listeMail.append(None)
        elif questAnniv != "Y" and questMail == "Y":
            print(nom,numero,mail)
            listeNom.append(nom)
            lsiteNumero.append(numero)
            listeAnniv.append(None)
            listeMail.append(mail)
        else:
            print(nom,numero)
            listeNom.append(nom)
            lsiteNumero.append(numero)
            listeAnniv.append(None)
            listeMail.append(None)
            
        """validation = input("Valider l'enregistrement : ")
        if validation == "Y":
            pickle.dump()"""
            
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