import random

recommencer = True

#boucle qui permet a l'utilisateur de recommencer le jeu
while(recommencer == True):


    #mettre une limite (range) au nombre random maximal
    limite = int(input('quel est votre nombre maximal: \n'))

    num_random = random.randint(1, limite)

    reponse = False


    #boucle qui permet a l'utilisateur de refaire un essai
    while reponse == False:
        num = int(input("quel nombre veux-tu choisir? \n"))

        if num < num_random :
                print("trop petit")

        if num > num_random :
                print("trop grand")

        if num == num_random :
                print("bonne reponse")
                reponse = True

    choix_rejouer = str(input('veux-tu rejouer? \n'))
    if choix_rejouer == 'oui':
        recommencer = True
    else:
        recommencer = False