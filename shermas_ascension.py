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


### Branche 1 : Jérémie
else: 
   #Branche 1.1
   print("-----\n"
      "Vous arrivez dans une pièce sombre, seuls quelques rayon de lumière percent au travers de la dense végétation qui vous entoure \n"
      "L'atmosphère est pesante, des bruits inquiétant d'insecte percent au travers du silence qui vous entoure\n"
      "Après avoir marcher quelques minutes, determiné à avancer vers la Citadelle Mélodieuse, vous faites face à un étrange insecte\n"
      "Cet insecte ressemble à une énorme chenille, elle vous arrive au genoux et est couverte de poils vert formant une fourure\n")
   R = input("Pour continuer vous n'avez d'autre choix que de faire bouger cette invité indésirable,\n" 
            "  1. Lancer une pierre dessus en espérant la faire fuir \n"
            "  2. Essayer de la pousser doucement pour passer à coté \n"
            "Votre réponse :")
   #Branche 1.1.2
   if R == "2":
      PV -= 1
      print("Lorsque que vous vous approchez de cet étrange insecte, \n"
         "Vous le voyez pousser un faible cri aigu avant de se mettre à trembler \n"
         "Lorsque d'un coup de nombreux pics aussi long qu'un bras et ascérées comme des couteaux sortent de son corps \n"
         "N'ayant pas le temps de réagir vous ne pouvez que vous protéger avec votre bras \n"
         ">>> Vous perdez 1 PV\n")
   #Branche 1.1.1
   else :
        print("Vous décidez de ramasser une pierre de la taille de votre main et la lancez sur l'étrange insecte qui vous bloque \n"
         "Après avoir sursauté en recevant la pierre sur son dos, l'insecte se mets à trembler\n"
         "Après quelque seconde d'étranges pics aussi longs qu'un bras sortent tout d'un coup de tout son corps \n"
         "Vous avez bien fait de ne pas vous approcher\n"
         "Vous pouvez donc continuer votre avancée en contournant cet ennemis\n")
   #Branche 1.2
   print("-----\n"
      "Continuant votre avancée, vous arrivez face à une pente que vous devrez escalader,\n"
      "Vous regardez de plus près les différentes prises qui vous seront disponibles.\n"
      "Elles sont petites et ne semblent pas stables, l'escalade sera difficile.\n")
   R = input("Ils vous faut choisir :\n"
      "    1. Essayer d'escalader rapidement espérant que les pierres tiennent le coup\n"
      "    2. Prendre son temps avec le maximum de précautions\n"
      "Votre réponse : ")
   #Branche 1.2.2
   if R == "2" :
      print("\nVous escaladez tout doucement, sauf qu'en posant le pied sur la première prises, \n"
         "Vous vous rendez compte qu'elle n'est pas stable, \n"
         "En essayant de changer d'appui, vous glissez et retombez en bas de cette pente.\n")
      PV -= 1
      print(">>> Vous perdez 1 PV\n")
      R = input("Vous n'avez d'autre choix que de réessayer de monter.\n"
         "  1. Commencer à courir espérant avoir assez de force pour atteindre le haut sans tomber. \n"
         "  2. Attraper les prises doucement une par une.\n"
         "Votre réponse : ")
      #Branche 1.2.2.2
      if R == "2":
         print("\nMalgré toutes les précautions que vous avez su prendre, \n"
            "Les prises ne tiennent pas sous votre poids pendant plus d'une seconde. \n"
            "C'est durant votre dernière chute que vous réalisiez que cette fois ci, \n"
            "La précipitation était le bon choix\n")
         input(">>> Vous êtes mort.")
         quit()
      #Branche 1.2.2.1
      else : 
         print("Vous vous mettez à courir le plus rapidement possible\n"
            "Dans votre élan vous réussissez à atteindre la haut de la peinte\n"
            "Fière de vos efforts vous avancez désormais vers une nouvelle pièce\n")
   #Branche 1.2.1
   else :
      print("Vous vous mettez à courir le plus rapidement possible\n"
         "Sous chacun de vos pas, la prise que vous utilisez se brise,\n"
         "Sans votre élan vous n'arriveriez jamais à grimper.\n"
         "Il est certain qu'avoir couru était l'unique solution\n")
   #Branche 1.3 (suite)
   print("-----\n"
      "Vous faites maintenant face à une grande allée dégagée,\n"
      "Les rayons de lumières qui percent a travers la végétation toujours denses\n"
      "Donnent une atmosphère particulière à la pièces\n")
   R = input("Grande allée ou recoin ?")
   if R == "2" :
      #Branche 1.3.2
      print("Allée")
   else :
      #Branche 1.3.1
      print("Recoin into effondrement")
      # + Perles
      R = input("Chercher un chemin ou creuser")
      #Branche 1.3.2 
      if R == "2":
         print("Creuser, difficile")
         print(">>> Vous perdez 1 PV")
         PV -= 1
      #Branche 1.3.1
      else :
         print("Aucune sortie")
         input(">>> Vous êtes mort.")
         quit()
   #Branche 1.4
   print("ennemis volant")
   R = input("passer en dessous, ou tirer dessus")
   #Branche 1.4.2
   if R == "2" :
      print("courir")
      print(">>> Vous perdez 1 PV")
      R = input("faux choix")
      #Branche 1.4.2.2 
      if R == "2" :
         print("écrasé")
         input(">>> Vous êtes mort.")
         quit()
      #Branche 1.4.2.1
      else :
         print("mort nul trébuche")
         input(">>> Vous êtes mort.")
         quit()
   #Branche 1.4.1 
   else :
      print("Tir cool")
      print(">>> Vous gagnez 1 Fragment de carapace")
      Inv["Carapaces"] += 1
   #Branche 1.5
   print("Grande porte, recoin d'abord")
   R = input("grande porte ou ptit recoin")
   #Branche 1.5.2
   if R == "2" :
      print("recoin")
      print(">>> Vous gagnez 1 PV")
      if PV < 5 :
         PV += 1
   #Branche 1.5.1
   else :
      print("Grande porte vous ne saurez jamais ce qu'il y avait dans ce recoin.")

#Branche 2.
input("FIN.")
quit()
