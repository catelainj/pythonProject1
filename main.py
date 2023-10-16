#TP2
import random

def jeu_dev():
    min = 0
    max = 1000
    nbr = random.randint(min, max)
    essaies = 0

    print("depart")
    print(f"choisi un nombre au hasard entre {min} et {max} .")
    print("devinne")

    while True:
        essaie = int(input("entre ton essaie : "))
        essaies += 1

        if essaie < nbr:
            print(f"pas bon, c'est plus grand que {essaie}")
        elif essaie > nbr:
            print(f"pas bon,c'est plus petit que {essaie}")
        else:
            print("bonne reponse")
            print(f"ta reussi en : {nbr} essai(s).")
            recomence = input("veut tu recomencer (o/n)? ")
            if recomence.lower() == "o":
                jeu_dev()
            else:
                print("a plus")
                break




