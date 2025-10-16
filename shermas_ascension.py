import random

### Stats de base

PV = 5
Inv = {"Arme": "Baguette de métal, 
      "Mélodies" : [],
      "Carapaces" : 0
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
    continue
  else: 
    print("Vous observez le paysage, il est beau")
  print("Vous arrivez devant un ennemi")
  R = input("Combattre cet ennemi ?
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
  # Branche Jérémie
