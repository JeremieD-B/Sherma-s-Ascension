import random
# Import du module random qui permet de générer des nombres aléatoires

from time import sleep
# Autorisé exceptionnellement par le professeur 
# La fonction sleep du module time permet de mettre un temps d'arrêt dans le programme
# Elle permet donc de faire attendre le joueur à certain moment pour leur donner plus de crédibilité

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
 
R = input("Souhaitez-vous partir à gauche ou à droite ?\n"
        "    1. Gauche\n"
        "    2. Droite\n"
        "Votre réponse : ")
print()
while R not in ("1","2","Q","q"):
    R =input("Souhaitez-vous partir à gauche ou à droite ?\n"
        "    1. Gauche\n"
        "    2. Droite\n"
        "Votre réponse : ")
    print()
if R in ("q","Q"):
        quit()
### Branche 1 : Jérémie
elif R == "1": 
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
    while R not in ("1","2","Q","q"):
        R = input("Pour continuer vous n'avez d'autre choix que de faire bouger cette invité indésirable,\n" 
                "  1. Lancer une pierre dessus en espérant la faire fuir \n"
                "  2. Essayer de la pousser doucement pour passer à coté \n"
                "Votre réponse :")
    if R in ("q","Q"):
        quit()
    #Branche 1.1.1
    elif R == "1" :
          print("Vous décidez de ramasser une pierre de la taille de votre main et la lancez sur l'étrange insecte qui vous bloque \n"
            "Après avoir sursauté en recevant la pierre sur son dos, l'insecte se mets à trembler\n"
            "Après quelque seconde d'étranges pics aussi longs qu'un bras sortent tout d'un coup de tout son corps \n"
            "Vous avez bien fait de ne pas vous approcher\n"
            "Vous pouvez donc continuer votre avancée en contournant cet ennemis\n")
    #Branche 1.1.2
    elif R == "2":
        PV -= 1
        print("Lorsque que vous vous approchez de cet étrange insecte, \n"
            "Vous le voyez pousser un faible cri aigu avant de se mettre à trembler \n"
            "Lorsque d'un coup de nombreux pics aussi long qu'un bras et ascérées comme des couteaux sortent de son corps \n"
            "N'ayant pas le temps de réagir vous ne pouvez que vous protéger avec votre bras \n"
            ">>> Vous perdez 1 PV\n")
    
    ##Branche 1.2
    print("-----\n"
        "Continuant votre avancée, vous arrivez face à une pente que vous devrez escalader,\n"
        "Vous regardez de plus près les différentes prises qui vous seront disponibles.\n"
        "Elles sont petites et ne semblent pas stables, l'escalade sera difficile.\n")
    R = input("Ils vous faut choisir :\n"
        "    1. Essayer d'escalader rapidement espérant que les pierres tiennent le coup\n"
        "    2. Prendre son temps avec le maximum de précautions\n"
        "Votre réponse : ")
    while R not in ("1","2","Q","q"):
        R = input("Ils vous faut choisir :\n"
        "    1. Essayer d'escalader rapidement espérant que les pierres tiennent le coup\n"
        "    2. Prendre son temps avec le maximum de précautions\n"
        "Votre réponse : ")
    if R in ("q","Q"):
        quit()
    #Branche 1.2.1
    elif R == "1" :
        print("Vous vous mettez à courir le plus rapidement possible\n"
            "Sous chacun de vos pas, la prise que vous utilisez se brise,\n"
            "Sans votre élan vous n'arriveriez jamais à grimper.\n"
            "Il est certain qu'avoir couru était l'unique solution\n")
    #Branche 1.2.2
    elif R == "2" :
        print("\nVous escaladez tout doucement, sauf qu'en posant le pied sur la première prises, \n"
            "Vous vous rendez compte qu'elle n'est pas stable, \n"
            "En essayant de changer d'appui, vous glissez et retombez en bas de cette pente.\n")
        PV -= 1
        print(">>> Vous perdez 1 PV\n")
        R = input("Vous n'avez d'autre choix que de réessayer de monter.\n"
            "  1. Commencer à courir espérant avoir assez de force pour atteindre le haut sans tomber. \n"
            "  2. Attraper les prises doucement une par une.\n"
            "Votre réponse : ")
        print("")
        while R not in ("1","2","Q","q"):
            R = input("Vous n'avez d'autre choix que de réessayer de monter.\n"
                "  1. Commencer à courir espérant avoir assez de force pour atteindre le haut sans tomber. \n"
                "  2. Attraper les prises doucement une par une.\n"
                "Votre réponse : ")    
        if R in ("q","Q"):
            quit()
        #Branche 1.2.2.1
        elif R == "1" : 
            print("Vous vous mettez à courir le plus rapidement possible\n"
                "Dans votre élan vous réussissez à atteindre la haut de la peinte\n"
                "Fière de vos efforts vous avancez désormais vers une nouvelle pièce\n")
        #Branche 1.2.2.2
        elif R == "2":
            print("Malgré toutes les précautions que vous avez su prendre, \n"
                "Les prises ne tiennent pas sous votre poids pendant plus d'une seconde. \n"
                "C'est durant votre dernière chute que vous réalisiez que cette fois ci, \n"
                "La précipitation était le bon choix\n")
            input(">>> Vous êtes mort.")
            quit()
    ##Branche 1.3 
    print("-----\n"
        "Vous faites maintenant face à une grande allée dégagée,\n"
        "Les rayons de lumières qui percent a travers la végétation toujours denses\n"
        "Donnent une atmosphère particulière à la pièces\n")
    R = input("Vous remarquez un petit couloir à votre droite \n"
        "  1. Vous allez explorer ce couloir sombre.\n"
        "  2. Vous préfèrez continuer dans cette grande allée.\n"
        "Votre réponse :")
    print()
    while R not in ("1","2","Q","q"):
        R = input("Vous remarquez un petit couloir à votre droite \n"
        "  1. Vous allez explorer ce couloir sombre.\n"
        "  2. Vous préfèrez continuer dans cette grande allée.\n"
        "Votre réponse :")
        print()
    if R in ("q","Q"):
        quit()
    #Branche 1.3.1
    elif R == "1" :
        print("En entrant dans ce couloir, la visibilitée est très faible. \n"
            "Vous voyez des gouttes perler du plafonds, la pièce est très humide \n"
            "Alors que vous continuiez votre avancée, vouss entendez l'entrée de ce couloir s'effondrer \n"
            "Il va être difficile de ressortir.\n"
            "Au moins vous avez trouver un chapelet contenant 30 perles.\n")
        print(">>> Vous gagnez 30 perles\n")
        #A finir !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        R = input("Pour ressortir d'ici il va falloir choisir a quoi se consacrer.\n"
            "  1. Chercher une autre sortie\n"
            "  2. Ecarter les pierres qui se sont effondrer pour revenir en arrière\n"
            "Votre réponse :")
        print("")
        while R not in ("1","2","Q","q"):
            R = input("Pour ressortir d'ici il va falloir choisir a quoi se consacrer.\n"
            "  1. Chercher une autre sortie\n"
            "  2. Ecarter les pierres qui se sont effondrer pour revenir en arrière\n"
            "Votre réponse :")
            print()
        if R in ("q","Q"):
            quit()
        #Branche 1.3.1.1
        elif R == "1" :
            print("Après des heures d'errances vous n'avez trouvez aucune sortie.\n"
                "Malgré tous vos effort les heures passes, le temps passe et aucune sortie n'est décelable.\n"
                "Vos recherches font du bruit, des vers géant qui vivent dans les murs de cette cavernes viennent vous rendre visites.\n")
            input(">>> Vous êtes mort.\n")
            quit()
        #Branche 1.3.1.2 
        elif R == "2":
            print("Vous creusez de toutes vos forces pour paser cet amas de pierre\n"
                "Malgré la difficulté manifeste de cette action vous réussisez a vous en sortir.\n")
            PV -= 1 
            if PV <= 0:
                input(">>> Vous êtes mort.")
    elif R == "2" :
        #Branche 1.3.2
        print("Vous traversez cette grande allée et observez autour de vous \n"
            "La végétation de ces cavernes est extrêmement développée.\n"
            "Vous ne connaissiez aucune de ces espèces avant de venir ici \n"
            "Les différentes plantes et arbres autour de vous vous parraissent très jolis \n"
            "Cet arbre là par exemple, ses branches sont toutes courbées, pas une seule partie de l'arbre n'est rectili...\n"
            "BRRAOUUUUUMMMMMM\n"
            "Vous venez d'entendre le couloir que vous aviez vu précédemment s'effondrer.\n"
            "Cette caverne n'est définitivement pas accueillante. \n")
    #Branche 1.4
    print("Après avoir avancer dans cette grande allée, vous faites à un nouvel ennemis.\n"
        "Physiquement il ressemble fortement à la chenille croisée auparavant, mais celle-ci vole !\n")
    R = input("Pour atteindre le bout de cette allée il va falloir passer. \n"
        "  1. Lancer une pierre sur l'insecte volant dans l'espoir de le faire fuir.\n"
        "  2. Courir de toutes vos forces en dessous pour atteindre la porte avant qu'il ne réagisse\n"
        "Votre réponse : ")
    print()
    while R not in ("1","2","Q","q"):
        R = input("Pour atteindre le bout de cette allée il va falloir passer. \n"
        "  1. Lancer une pierre sur l'insecte volant dans l'espoir de le faire fuir.\n"
        "  2. Courir de toutes vos forces en dessous pour atteindre la porte avant qu'il ne réagisse\n"
        "Votre réponse : ")
        print()
    if R in ("q","Q"):
        quit()
    #Branche 1.4.1 
    elif R == "1" :
        print("Tir cool")
        print(">>> Vous gagnez 1 Fragment de carapace")
        Inv["Carapaces"] += 1
    #Branche 1.4.2
    elif R == "2" :
        print("En courant vers la porte, vous trébuchez et vous faites remarquer par l'ennemis, \n"
            "En trébuchant vous vous blessez a la jambe\n")
        print(">>> Vous perdez 1 PV\n")
        PV -= 1 
        if PV <= 0:
            input(">>> Vous êtes mort.")
        R = input("Pour atteindre le bout de cette allée est nécessaire de s'échapper de cette situation. \n"
            "  1. Courir de plus belle vers la sortie.\n"
            "  2. Foncer vers l'ennemi afin de le faire tomber et de l'abattre.\n"
            "Votre réponse : ")
        print()
        while R not in ("1","2","Q","q"):
            R = input("Pour atteindre le bout de cette allée est nécessaire de s'échapper de cette situation. \n"
            "  1. Courir de plus belle vers la sortie.\n"
            "  2. Foncer vers l'ennemi afin de le faire tomber et de l'abattre.\n"
            "Votre réponse : ")
            print("")
        if R in ("q","Q"):
            quit()
        #Branche 1.4.2.1
        elif R == "1" :
            print("Vous avez trébuché de nouveau, vous ne sentez même plus votre jambe blessée, cet insecte approche vers vous.\n")
            input(">>> Vous êtes mort.")
            quit()
        #Branche 1.4.2.2 
        elif R == "2" :
            print("En fonçant vers cet insecte il descend a vive allure vers vous son dard diriger vers votre tête. \n")
            input(">>> Vous êtes mort.")
            quit()
    ##Branche 1.5
    print("Vous arrivez finalement vers une grande porte entrouverte un léger filet de lumière la traverse.\n")
    R = input("Vous apercevez un petit recoin dans lequel vous pourriez vous faufiler pour explorer\n"
            "  1. Traverser cette énorme porte et avancer vers la Citadelle\n"
            "  2. Commencer par explorer ce petit recoin.\n"
            "Votre réponse : ")
    print()
    while R not in ("1","2","Q","q"):
        R = input("Vous apercevez un petit recoin dans lequel vous pourriez vous faufiler pour explorer\n"
            "  1. Traverser cette énorme porte et avancer vers la Citadelle\n"
            "  2. Commencer par explorer ce petit recoin.\n"
            "Votre réponse : ")
        print()
    if R in ("q","Q"):
        quit()
    #Branche 1.5.1
    elif R == "1" :
        print("Vous traversez la grande porte, vous ne saurez jamais ce qu'il y avait dans ce recoin.")
    #Branche 1.5.2
    elif R == "2" :
        print("En entrant dans ce recoin vous trouver une pierre ayant la forme d'un banc\n"
            "Vous profitez de ce moment de calme pour vous asseoir un moment\n")
        print(">>> Vous regagnez 1 PV")
        if PV < 5 :
            PV += 1
if R == "2": 
# Branche Sacha
    print("-----\n" # Branche 1
    "Vous changez d'atmosphère\n")
    R = input("Observez autour de vous ?\n"
    "    1. Oui\n"
    "    2. Non\n"
    "Votre réponse : ")
    if R == "2": 
        pass
    else: 
        print("Vous observez le paysage, il est beau")
    print("\nVous arrivez devant un ennemi")
    R = input("Combattre cet ennemi ?\n"
    "    1. Combattre\n"
    "    2. Esquive\n"
    "Votre réponse : ")
    if R == "2":
        print("Vous décidez de contourner l'ennemi, il ne vous a pas aperçu.")
    else:
        print("Vous décidez de combattre l'ennemi\n"
        ">>> Vous perdez 1 PV\n"
        ">>> Vous gagnez 1 fragment de carapace")
        PV -= 1
        Inv["Carapaces"] += 1
        print("Vous continuez votre périple")
    R = input("Votre lacet s'est dénoué sur votre chaussure gauche, vous avez du mal à refaire vos lacets mais finissez toujours par y arriver.\n"
    "Souhaitez-vous le refaire (Cela prendra un cours instant) ?\n"
    "    1. Continuer sur le chemin\n"
    "    2. Refaire les lacets avec difficulté\n"
    "Votre Réponse : ")
    if R == "2":
        print("Vous refaites vos lacets")
        while i < 100:
            sleep(1)
            i += randint(10, 30)
            if i >= 100:
                print(".....  100%")
                lacets_faits = True
                break
            else: 
                    print(f"..... {i}")
    else: 
        lacets_faits = False
    # Branche 1 (suite)
    print("-----\n"
    "Vous arrivez dans une nouvelle zone sombre. Cette zone est pu humide, la pierre est donc très friable.\n"
    "Afin de monter plus haut dans la caverne, vous devez monter sur les pierres. En revanche, vous apercevez une lumière dans un coin.")
    R = input("Qu'allez-vous faire ?\n"
    "    1. Monter sur les pierres\n"
    "    2. Se diriger vers la lumière\n"
    "Votre réponse : ")
    if R == "2":
        # Branche 1.2
        print("Vous vous approchez prudemment de cette mystérieuse lumière\n")
        "Vous constatez que cette lumière provient du Soleil entre les pierres, ce n'est pas ce que vous recherchiez.\n"
        "Cependant, votre curiosité vous force à creuser les murs et ainsi sortir de la grotte."
        R = input("Enfin dehors, on monstre vous aperçoit et souhaite prévenir les aitres de votre présence\n"
             "    1. Le combattre pour ne pas qu'il informe les autres\n"
             "    2. Se cacher\n"
              "Votre réponse : ")
        if R == "2": 
            # Branche 1.2.2
            print("Vous attendez longuement afin de ne pas vous faire repérer, le monstre a prévenu ses acolytes et sont à votre recherche./n")
            R = input("Vous décidez d'agir : \n"
                 "    1. Combattre tous les monstres\n"
                 "    2. Rester cacher\n"
                  "Votre réponse : ")
            if R == "2": 
                # Branche 1.2.2.2
                print("Vous vous fatiguez et tombez le long des pierres qui vous tenait jusque là en position\n"
                     ">>> Vous perdez 1 point de vie")
                PV -= 1
                R = input("Vous vous faites remarquer et les monstres vous attaque tous ensemble\n"
                     "    1. Combattre\n"
                     "    2. Fuir\n"
                        "Votre réponse : ")
                if R == 1: 
                    print("Les monstres sont trop nombreux, vous êtes surpassé\n>>> Vous êtes mort.")
                else: 
                    print("Vous fuyez mais glissez sur une pierre, les monstres vous rattrape\n>>> Vous êtes mort.")
                input()
                quit()
            else: 
                #Branche 1.2.2.1
                print("Vous êtes sur de vous et attaquez les monstres\n"
                      ">>> Vous perdez 1 point de vie")
                PV -= 1
                while PV > 0: 
                     print("Vous êtes persévérant et continuez à combattre\n"
                          ">>> Vous perdez 1 point de vie")
                     PV -= 1
                print("Vous n'avez plus de vie\n"
                      ">>> Vous êtes mort.")
                input()
                quit()
        else: 
            # Branche 1.2.1
            print("Vous descendez des pierres et attaquez le monstre, finalement vous voyez qu'il y en a une cinquantaine autour de lui\n"
                  "Tous les monstres vous chassent\n"
                  ">>> Vous êtes mort")
    else: 
        # Branche 1.1 
        print("Vous escaladez les pierres, vous avez beaucoup de difficulté à avancer mais parvenez à vous frayez un chemin.\n"
        ">>> Vous gagnez 1 d'Agilité.")
        Agi += 1
        print("Presque en haut, une pierre casse et tombe sur votre chaussure")
        if (lacets_faits):
            # Branche 1.1.2
            print("Par chance, vous avez refaits vos lacets au préalable. Vous continuez donc votre ascension.")
        else: 
                # Branche 1.1.1
            print("Votre chaussure n'étant pas bien attaché, celle-ci s'enlève et tombe tout en bas")
            R = input("Allez chercher votre chaussure ?\n"
                "    1. Continuer\n"
                "    2. Descendre\n"
                "    3. Descendre rapidement\n"
            "Votre réponse : ")
            if R == "2":
                # Branche 1.1.1.2
                print("Vous descendez prudemment jusqu'à atteindre votre chaussure.")
                while i < 100:
                        sleep(1)
                        i += randint(10, 30)
                        if i >= 100:
                            print(f".....  100%")
                            break
                        else: 
                            print(f"..... {i}")
                print("Vous êtes en bas, vous remettez votre chaussure. La lumière entre aperçu plus tôt a disparu.\n"
                            "Etait-ce un mirage ? Une illusion ?")
                R = input("Que souhaitez-vous faire ?\n"
                    "    1. Reprendre l'ascension vertigineuse\n"
                    "    2. Revenir en arrière\n"
                    "Votre réponse : ")
                if R == "2":
                    # Branche 1.1.1.2.2
                    print("La famille de l'ennemi de tout à l'heure ont vu votre présence et suive désormais vos pas\n"
                    "Vous vous dirigez vers eux sans le savoir. Vous entendez un bruit")
                    R = input("Vous paniquez, que choisissez-vous de faire ?\n"
                    "    1. Se cacher\n"
                    "    2. Aller combattre\n"
                    "    3. Reprendre l'ascension\n")
                    # Safe : famille
                if R == "3":
                # Branche 1.1.1.3
                    print("Vous ne voulez pas perdre de temps et choisissez de dégringoler cette pente.\n"
                "Cependant, vous glissez sur une pierre et tomber la tête la première par terre.\n"
                "Cette chaussure ne valait peut être pas d'être récupérée ...\n"
                ">>> Vous êtes mort.")
                input()
                quit() 
            else:
                # Branche 1.1.1.1 
                print("Vous arrivez finalement en haut ...\n"
                ">>> Vous gagnez 1 point d'Agilité.")
                Agi += 1
                R = input("Vous arrivez à une intersection 2 choix s'offre à vous\n"
                    "    1. Aller à gauche\n"
                    "    2. Aller à droite\n")
                if R == 2: 
                    # Branche 1.1.1.1.2 (pas safe)
                    pass
                else : 
                    # Branche 1.1.1.1.1 (pas safe)
                    pass

#Branche 2.
input("FIN.")
quit()
