import sys 

LISTE = []

MENU = """Choisissez parmi les 5 options suivantes : 
1: Ajouter un élément à la liste
2: Retirer un élément de la liste
3: Afficher la liste
4: Vider la liste
5: Quitter
--> Votre Choix:  """

MENU_CHOICES = ["1", "2", "3", "4", "5"]


while True:
    user_choice = ""
    while user_choice not in MENU_CHOICES:
        user_choice = input(MENU)
        if user_choice not in MENU_CHOICES:
            print("Veuillez saisir une option valide")

    if user_choice == "1": # Ajouter un élément 
        item = input("Entrez nom d'un élément à ajouter à la liste de course: ")
        LISTE.append(item)
        print(f"l'élément {item} a bien été ajouté à la liste.")
    elif user_choice == "2": # Retirer un élément
        item = input("Entrez le nom d'un élément à retirer dans la liste de courses: ")
        if item in LISTE:
            LISTE.remove(item)
            print(f"l'élément {item} a bien été retiré de la liste")
        else:
            print(f"L'élément {item} n'est pas dans la liste")
    elif user_choice == "3": # Afficher la liste
        if LISTE: # Ici LISTE renvoie True s'il contient au moins un élément et False s'il ne contient aucun élément
            print("Voici le contenu de votre liste: ") 
            for i, item in enumerate(LISTE, 1): # Ici la fonction enumerate récupère l'indice et l'élément, le nombre 1 permet de spécifier à quel indice on souhaite commencer)
                print(f"{i}. {item}")
        else: 
            print("Votre liste est vide")
    elif user_choice == "4":  # Vider la liste
        LISTE.clear()
        print("La liste a été vidée de son contenu")
    elif user_choice == "5": #Quitter le script
        print("A bientôt")
        sys.exit()


print("-" * 75) # Permet de séparer entre deux instances de script.
