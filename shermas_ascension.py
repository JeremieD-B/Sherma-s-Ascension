import random

### Stats de base

PV = 5
Inv = {"Arme": "Baguette de métal", 
      "Mélodies" : [],
      "Carapaces" : 0,
      "Objets" : []}
Atk = 0
Def = 0
Agi = 0

# Arriver à la porte
print("Vous arrivez à la porte, vous décidez de la franchir")
 
R = input("Souhaitez-vous partir à gauche ou à droite ?"
      "\n    1. Gauche"
      "\n    2. Droite"
      "\nVotre réponse : ")
if R == "2": 
  # Branche Sacha
  print("blabla")
  R = input("Observez autour de vous ?"
           "\n    1. Oui"
           "\n    2. Non"
           "Votre réponse : ")
  if R == "2": 
    pass
  else: 
    print("Vous observez le paysage, il est beau")
  print("Vous arrivez devant un ennemi")
  R = input("Combattre cet ennemi ?"
  "\n    1. Combattre"
  "\n    2. Esquive"
  "\nVotre réponse : ")
  if R == "2":
    print("Vous décidez de contourner l'ennemi, il ne vous a pas aperçu.")
  else:
    print("Vous décidez de combattre l'ennemi, celui-ci vous inflige 1 de dégât et vous donne 1 carapace")
    PV -= 1
    Inv["Carapaces"] += 1
  print("Vous continuez votre périple")
  
else: 
   print("Vous arrivez dans une pièce sombre, seuls quelques rayon de lumière percent au travers de la dense végétation qui vous entoure \n"
      "L'atmosphère est pesante, des bruits inquiétant d'insecte percent au travers du silence qui vous entoure\n"
      "Après avoir marcher quelques minutes, determiné à avancer vers la Citadelle Mélodieuse, vous faites face à un étrange insecte\n"
      "Cet insecte ressemble à une énorme chenille, elle vous arrive au genoux et est couverte de poils vert formant une fourure\n")
   R = input("Pour continuer vous n'avez d'autre choix que de faire bouger cette invité indésirable,\n" 
            "  1. Essayer de la pousser doucement pour passer à coté \n"
            "  2. Lancer une pierre dessus en espérant la faire fuir \n")
   if R == "2":
        print("Lorsque que vous vous approchez de cet étrange insecte,")
        PV -= 1

   else :
        print("cool")
   R = input("choix 2")
   quit()
