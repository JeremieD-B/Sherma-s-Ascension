from random import randint
# Import du module random qui permet de générer des nombres aléatoires

from time import sleep
# Autorisé exceptionnellement par le professeur 
# La fonction sleep du module time permet de mettre un temps d'arrêt dans le programme
# Elle permet donc de faire attendre le joueur à certain moment pour leur donner plus de crédibilité


##### Constantes
#### Tout les textes
T_intro = """
Bienvenue.
    Vous êtes une jeune aventurière du nom de Sherma, la musique est votre vie, et ainsi vous souhaitez atteindre la Citadelle Mélodieuse pour apprendre les plus grands secrets.
Avant tout, une petite explication sur vos capacités : 
- Vous êtes capable faire des choix au fur et à mesure de votre avancée et de prendre les meilleurs décisions tout au long de votre aventure.
- Vous pouvez quitter à tout moment l'aventure en appuyant sur 'q' ou 'Q'.
- Bon jeu !
"""
T_entree_desc = """
    Le silence est dense. Une brume dorée se dissipe lentement autour de vous. Devant, se dresse une porte scellée, haute et fine, faite d’un métal chantant.
Chaque souffle de vent fait vibrer sa surface, produisant un écho lointain — comme un souvenir d’hymne oublié.
Derrière vous, les profondeurs. Devant, la Citadelle Mélodieuse, si haute que ses sommets se perdent dans les nuées. Vous savez qu’il faut atteindre son sommet — mais la voie reste voilée.
À votre gauche, un sentier s’enfonce dans les forêts sombres où se cache derrière un mont juxtaposé à la Citadelle.
À votre droite, un escalier de pierre descend vers des cavernes où l’eau résonne comme une harpe. Une lumière turquoise y palpite, irrégulière.
"""

#### Autres constantes 

PV_MAX = 5
vitesse_texte = 0.025 # 0.025 vitesse normale
vitesse_pause = 0.35 # 0.35 vitesse normale

### Stats de base

Inv = {"Arme": "Baguette de métal", 
        "Mélodies" : [],
        "Carapaces" : 0,
        "Objets" : []}
Sherma = {
"PV": 5,
"Inv" : Inv, 
"Atk": 0,
"Def" : 0,
"Agi" : 0,
"Emplacement" : "Entree"
}
Salles = {
    "Entree" : {"NomAffichee" : "Entrée","Desc" : TEntreeDesc, "EventPast" : False, "Successeurs": ["GrotteHumide","Caverne"]},
    "GrotteHumide" : {"NomAffichee" : "Grotte humide","Desc" : TGrotteHumideDesc, "EventPast" : False, "Successeurs": ["GrandeAllee","PetitCouloir"]},
    "GrandeAllee" : {"NomAffichee" : "Grande Allée","Desc" : TGrandeAlleeDesc, "EventPast" : False, "Successeurs": ["GouffreDOs"]},
    "PetitCouloir" : {"NomAffichee" : "Petit Couloir","Desc" : TPetitCouloirDesc, "EventPast" : False, "Successeurs": []},
    "Caverne" : {"NomAffichee" : "Caverne","Desc" : None, "EventPast" : False, "Successeurs": [None]}, #A finir 
    "GouffreDOs" : {"NomAffichee" : "Gouffre d'Os","Desc" : TGouffreDOsDesc, "EventPast" : False, "Successeurs": ["GrandeAllee"]}
}
Fin = False
##### FONCTIONS :

def question(text : str,rep : tuple) -> str:
    """
    Pose la question "text"
    Si les réponse est q ou Q : quitte le programme
    R est la Réponse que l'on attend
    """
    R = None
    tour = 0
    while R not in rep and R not in ("Q","q"):
        if tour == 0 :
            ecrire(text)
        else : 
            ecrire(text, 0.005,0.01)
        R = input()
        tour +=1
    if R in ("q","Q") :
        quit()
    return R

def ecrire(text: str, vitesse = vitesse_texte, vitesse_pause = vitesse_pause) -> None:
    """
    Permet d'écrire a l'écran un texte de manière progressive
    """
    for lettre in text:
        sleep(vitesse)
        print(lettre,end="", flush=True)
        if lettre in (",",".",">"):
            sleep(vitesse_pause)
        # end="" permet de ne pas passer de ligne ; flush= True permet d'écrire le texte progressivement

def perdre_pv(pv : int, pv_perdu :int):
    ecrire(f">>> Vous perdez {pv_perdu} PV. \n")
    pv -= pv_perdu
    if pv <= 0 :
        input("\n>>> Vous n'avez plus aucun PV. Vous êtes mort.")
        quit()
    return pv

def gagner_pv(pv : int, pv_gagne :int):
    if pv <= PV_MAX :
        pv += pv_gagne
        ecrire(f">>> Vous gagnez {pv_gagne} PV. \n")
    return pv

###### JEU


## TUTORIEL :
ecrire(T_intro)
sleep(1)
# Arriver à la porte
ecrire(Salles["Entree"]["Desc"])
R = question("""
Souhaitez-vous partir à gauche ou à droite ?
    1. Gauche    
    2. Droite
Votre réponse : """,("1","2"))

### Branche 1 : Jérémie
if R == "1": 
    #Branche 1.1
    ecrire("""
-----
    Vous arrivez dans une pièce sombre, seuls quelques rayon de lumière percent au travers de la dense végétation qui vous entoure
L'atmosphère est pesante, des bruits inquiétant d'insecte percent au travers du silence qui vous entoure
Après avoir marcher quelques minutes, determiné à avancer vers la Citadelle Mélodieuse, vous faites face à un étrange insecte
Cet insecte ressemble à une énorme chenille, elle vous arrive au genoux et est couverte de poils vert formant une fourure
""")
    R = question("""
Pour continuer vous n'avez d'autre choix que de faire bouger cette invité indésirable,
    1. Lancer une pierre dessus en espérant la faire fuir
    2. Essayer de la pousser doucement pour passer à coté 
Votre réponse :""",("1","2"))
    #Branche 1.1.1
    if R == "1" :
          ecrire("""
    Vous décidez de ramasser une pierre de la taille de votre main et la lancez sur l'étrange insecte qui vous bloque
Après avoir sursauté en recevant la pierre sur son dos, l'insecte se mets à trembler
Après quelque seconde d'étranges pics aussi longs qu'un bras sortent tout d'un coup de tout son corps
Vous avez bien fait de ne pas vous approcher
Vous pouvez donc continuer votre avancée en contournant cet ennemis
""")
    #Branche 1.1.2
    elif R == "2":
        ecrire("""
    Lorsque que vous vous approchez de cet étrange insecte,
Vous le voyez pousser un faible cri aigu avant de se mettre à trembler
Lorsque d'un coup de nombreux pics aussi long qu'un bras et ascérées comme des couteaux sortent de son corps
N'ayant pas le temps de réagir vous ne pouvez que vous protéger avec votre bras
""")
        PV = perdre_pv(PV,1)
    ##Branche 1.2
    ecrire("""-----
    Continuant votre avancée, vous arrivez face à une pente que vous devrez escalader,
Vous regardez de plus près les différentes prises qui vous seront disponibles.
Elles sont petites et ne semblent pas stables, l'escalade sera difficile.
""")
    R = question("""
Ils vous faut choisir :
    1. Essayer d'escalader rapidement espérant que les pierres tiennent le coup
    2. Prendre son temps avec le maximum de précautions
Votre réponse : """,("1","2"))
    #Branche 1.2.1
    if R == "1" :
        ecrire("""
    Vous vous mettez à courir le plus rapidement possible
Sous chacun de vos pas, la prise que vous utilisez se brise,
Sans votre élan vous n'arriveriez jamais à grimper.
Il est certain qu'avoir couru était l'unique solution""")
    #Branche 1.2.2
    elif R == "2" :
        ecrire("""
    Vous escaladez tout doucement, sauf qu'en posant le pied sur la première prises, 
Vous vous rendez compte qu'elle n'est pas stable, 
En essayant de changer d'appui, vous glissez et retombez en bas de cette pente.
""")
        PV = perdre_pv(PV,1)
        R = question("""
Vous n'avez d'autre choix que de réessayer de monter.
    1. Commencer à courir espérant avoir assez de force pour atteindre le haut sans tomber. 
    2. Attraper les prises doucement une par une.
Votre réponse : """,("1","2"))    
        #Branche 1.2.2.1
        if R == "1" : 
            ecrire("""
    Vous vous mettez à courir le plus rapidement possible
Dans votre élan vous réussissez à atteindre la haut de la peinte
Fière de vos efforts vous avancez désormais vers une nouvelle pièce
""")
        #Branche 1.2.2.2
        elif R == "2":
            ecrire("""
    Malgré toutes les précautions que vous avez su prendre, 
Les prises ne tiennent pas sous votre poids pendant plus d'une seconde. 
C'est durant votre dernière chute que vous réalisiez que cette fois ci, 
La précipitation était le bon choix
""")
            input(">>> Vous êtes mort.")
            quit()
    ##Branche 1.3 
    ecrire("""-----
    Vous faites maintenant face à une grande allée dégagée,
Les rayons de lumières qui percent a travers la végétation toujours denses
Donnent une atmosphère particulière à la pièces
""")
    R = question("""
Vous remarquez un petit couloir à votre droite 
    1. Vous allez explorer ce couloir sombre.
    2. Vous préfèrez continuer dans cette grande allée.
Votre réponse :""",("1","2"))
    #Branche 1.3.1
    if R == "1" :
        ecrire("""
-----
    En entrant dans ce couloir, la visibilitée est très faible. 
Vous voyez des gouttes perler du plafonds, la pièce est très humide 
Alors que vous continuiez votre avancée, vouss entendez l'entrée de ce couloir s'effondrer 
Il va être difficile de ressortir.
Au moins vous avez trouver un chapelet contenant 30 perles.)

>>> Vous gagnez 30 perles.
""")
        R = question("""
Pour ressortir d'ici il va falloir choisir à quoi se consacrer.
    1. Chercher une autre sortie
    2. Ecarter les pierres qui se sont effondrer pour revenir en arrière
Votre réponse :""",("1","2"))
        #Branche 1.3.1.1
        if R == "1" :
            ecrire("""
    Après des heures d'errances vous n'avez trouvez aucune sortie.
Malgré tous vos effort les heures passes, le temps passe et aucune sortie n'est décelable.
Vos recherches font du bruit, des vers géant qui vivent dans les murs de cette cavernes viennent vous rendre visites.
""")
            input(">>> Vous êtes mort.")
            quit()
        #Branche 1.3.1.2 
        elif R == "2":
            ecrire("""
    Vous creusez de toutes vos forces pour passer cet amas de pierre
Malgré la difficulté manifeste de cette action vous réussisez a vous en sortir.
""")
            PV = perdre_pv(PV,1)
    elif R == "2" :
        #Branche 1.3.2
        ecrire("""
    Vous traversez cette grande allée et observez autour de vous 
La végétation de ces cavernes est extrêmement développée.
Vous ne connaissiez aucune de ces espèces avant de venir ici 
Les différentes plantes et arbres autour de vous vous parraissent très jolis 
Cet arbre là par exemple, ses branches sont toutes courbées, pas une seule partie de l'arbre n'est rectili...
        BRRAOUUUUUMMMMMM
Vous venez d'entendre le couloir que vous aviez vu précédemment s'effondrer.
Cette caverne n'est définitivement pas accueillante.
""")
    #Branche 1.4
    ecrire("""
    Après avoir avancer dans cette grande allée, vous faites à un nouvel ennemis.
Physiquement il ressemble fortement à la chenille croisée auparavant, mais celle-ci vole !
""")
    R = question("""
Pour atteindre le bout de cette allée il va falloir passer. 
    1. Lancer une pierre sur l'insecte volant dans l'espoir de le faire fuir.
    2. Courir de toutes vos forces en dessous pour atteindre la porte avant qu'il ne réagisse
Votre réponse : """,("1","2"))
    #Branche 1.4.1 
    if R == "1" :
        ecrire("""
    Vous lancez une pierre vers l'insecte, il perd l'équilibre de son vol et s'écrase au sol

>>> Vous gagnez 1 Fragment de carapace
""")
        Inv["Carapaces"] += 1
    #Branche 1.4.2
    elif R == "2" :
        ecrire("""
    En courant vers la porte, vous trébuchez et vous faites remarquer par l'ennemis,
En trébuchant vous vous blessez a la jambe
""")
        PV = perdre_pv(PV,1)
        R = question("""
Pour atteindre le bout de cette allée est nécessaire de s'échapper de cette situation.
  1. Courir de plus belle vers la sortie.
  2. Foncer vers l'ennemi afin de le faire tomber et de l'abattre.
Votre réponse : """,("1","2"))
        #Branche 1.4.2.1
        if R == "1" :
            ecrire("""
    Vous avez trébuché de nouveau, vous ne sentez même plus votre jambe blessée, cet insecte approche vers vous.
""")
            input(">>> Vous êtes mort.")
            quit()
        #Branche 1.4.2.2 
        elif R == "2" :
            ecrire("""
    En fonçant vers cet insecte il descend a vive allure vers vous son dard diriger vers votre tête.
""")
            input(">>> Vous êtes mort.")
            quit()
    ##Branche 1.5
    ecrire("""
    Vous arrivez finalement vers une grande porte entrouverte un léger filet de lumière la traverse.
""")
    R = question("""
Vous apercevez un petit recoin dans lequel vous pourriez vous faufiler pour explorer
    1. Traverser cette énorme porte et avancer vers la Citadelle
    2. Commencer par explorer ce petit recoin.
Votre réponse : """,("1","2"))
    #Branche 1.5.1
    if R == "1" :
        ecrire("""
    Vous traversez la grande porte, vous ne saurez jamais ce qu'il y avait dans ce recoin.
""")
    #Branche 1.5.2
    elif R == "2" :
        ecrire("""
    En entrant dans ce recoin vous trouver une pierre ayant la forme d'un banc
Vous profitez de ce moment de calme pour vous asseoir un moment
""")
        PV = gagner_pv(PV,1)
            
### Branche 2 : Sacha
elif R == "2": 
    ecrire("""
-----
Vous tournez à droite.

    Le sentier se fait étroit, bordé d’arbres aux troncs torsadés, dont les branches s’élancent comme des doigts vers le ciel.
La lumière s’amenuise à mesure que vous avancez.""")
    R = question("""
Observez autour de vous ?
    1. Oui
    2. Non
Votre réponse : """, ("1", "2"))
    if R == "1": 
        ecrire("""
    L’air est saturé d’humidité et d’un parfum âcre de mousse et de sève. Sous vos pas, le sol chante à peine — un bruissement discret, presque un murmure.
Au loin, au-delà de la canopée, se dresse un mont gigantesque, une masse sombre collée contre la Citadelle Mélodieuse. Ses pentes abruptes semblent fusionner avec les fondations mêmes de la tour. À sa base, les arbres se tordent, comme attirés ou repoussés par la musique silencieuse qui émane de la Citadelle.
Par moments, un son traverse la forêt — une note isolée, pure, qui résonne dans l’air avant de se dissoudre dans le vent. Était-ce un instrument, un oiseau, ou la montagne elle-même qui soupire ?
\nVous sentez que cette voie mène à quelque chose d’enfoui, peut-être une entrée dissimulée. Les branches s’entrelacent au-dessus de vous, formant une voûte presque organique. L’obscurité devient tangible, épaisse, comme une étoffe que l’on pourrait écarter d’un geste.""")
    ecrire("""
Puis soudain, un ennemi apparait d'entre les branches, celui-ci est laid et n'aurait peur de rien. Pris de panique, il décide de vous attaquer.""")
    R = question("""
Combattre cet ennemi ?
    1. Combattre
    2. Esquive
Votre réponse : """, ("1", "2"))
    if R == "1":
        ecrire("""
Vous décidez de combattre l'ennemi

>>> Vous perdez 1 PV
>>> Vous gagnez 1 fragment de carapace
""")
        perdre_pv(PV, 1)
        Inv["Carapaces"] += 1
    elif R == "2":
        ecrire("""
Vous décidez de contourner l'ennemi, celui-ci est finalement très lent il ne vous rattrape pas.""")
    ecrire("""

Vous continuez votre périple""")
    R = question("""

    Votre lacet s'est dénoué sur votre chaussure gauche, vous avez du mal à refaire vos lacets mais finissez toujours par y arriver.
Souhaitez-vous le refaire (Cela prendra un cours instant) ?
    1. Continuer sur le chemin
    2. Refaire les lacets avec difficulté
Votre Réponse : """, ("1", "2"))
    if R == "1": 
        lacets_faits = False
    elif R == "2":
        ecrire("""
Vous refaites vos lacets""")
        i = 0
        while i < 100:
            sleep(1)
            i += randint(10, 30)
            if i >= 100:
                print("..... 100%")
                lacets_faits = True
                break
            else: 
                print(f"..... {i}%")
    ## Branche 2
    ecrire("""
-----
    Vous avancez dans la montagne, et arrivez dans une nouvelle zone sombre. Cette zone est plus humide, la pierre est donc très friable.
Afin de monter plus haut dans la caverne, vous devez monter sur les pierres. En revanche, vous apercevez une lueur blanchâtre dans un coin similaire à celui d'une lanterne.""")
    R = question("""
Qu'allez-vous faire ?
    1. Monter sur les pierres
    2. Se diriger vers la lumière
Votre réponse : """, ("1", "2"))
    if R == "1": 
        # Branche 2.1 
        ecrire("""
    Vous commencez à grimper. Les pierres sont glissantes, couvertes d’un lichen argenté.
Sous vos doigts, certaines vibrent faiblement, comme si elles gardaient en elles la trace d’un ancien chant.\n

>>> Vous gagnez 1 d'Agilité.
""")
        Agi += 1
        ecrire("""

Puis vient un grondement.

Une note fausse, un craquement, et la montagne semble s’éveiller. Des pierres roulent en contrebas. Le sol se dérobe un instant sous vos pieds.
Votre chaussure est prise dans ces pierres.""")
        if lacets_faits:
            # Branche 2.1.2
            ecrire("""
Par chance, vous avez refaits vos lacets au préalable et votre chaussure reste intacte. Vous continuez donc votre ascension.""")
            chaussure_gauche = True
        else: 
            # Branche 2.1.1
            ecrire("""
Votre chaussure n'étant pas bien attaché, celle-ci s'enlève et tombe tout en bas.""")
            R = question("""
Aller chercher votre chaussure ?
    1. Continuer
    2. Descendre
    3. Descendre rapidement
Votre réponse : """, ("1", "2", "3"))
            if R == "1":
                # Branche 2.1.1.1 
                ecrire("""
Vous décidez de continuer votre ascension vertigineuse qui ne semble plus en finir.\n

>>> Vous perdez 1 PV.""")
                perdre_pv(PV, 1)
                chaussure_gauche = False
                
            elif R == "2":
                # Branche 2.1.1.2
                ecrire("""
Vous descendez prudemment jusqu'à atteindre votre chaussure.""")
                i = 0
                while i < 100:
                    sleep(1)
                    i += randint(10, 30)
                    if i >= 100:
                        print(f"..... 100%")
                        break
                    else: 
                        print(f"..... {i}%")
                ecrire("""
Vous êtes en bas, vous remettez votre chaussure. La lumière entre aperçu plus tôt a disparu.
Etait-ce un mirage ? Une illusion ?""")
                R = question("""
Aller chercher votre chaussure ?
    1. Continuer
    2. Descendre
    3. Descendre rapidement
Votre réponse : """, ("1", "2"))
                if R == "1": 
                    ecrire("""
    Votre ascension reprend de plus belle, vous pressez le pas au risque de vous faire repérer.
Cependant, vous apercevez à travers des pierres une petite lumière.
En vous posant correctement et en creusant, vous apercevez une sorte de vieux papier contenant des inscriptions musicales.
                           
>>> Vous récupérer le parchemin : Entre pierres et cordes.""")
                    Inv["Objets"] += ["Parchemin : Entre pierres et cordes"]
                    chaussure_gauche = True
                elif R == "2":
                    # Branche 2.1.1.2.2
                    ecrire("""
La famille de l'ennemi de tout à l'heure ont vu votre présence et suive désormais vos pas.
Vous vous dirigez vers eux sans le savoir. Vous entendez un bruit""")
                    R = question("""
Vous paniquez, que choisissez-vous de faire ?
    1. Se cacher
    2. Aller combattre
    3. Reprendre l'ascension
Votre réponse : """, ("1", "2", "3"))
                    if R == 1:
                        ecrire("""
Vous vous cachez, pendant un très long moment. Personne ne vous remarque.
>>> Vous perdez 1 point d'agilité.

Vous décidez de reprendre l'ascension.""")
                        Agi -= 1
                    elif R == 2:
                        ecrire(f"""
Vous brandissez votre {Inv['Arme']} et combattez les ennemis. Ceux-ci prennent peur sauf un.
Vous le combattez et êtes légèrement blessé.

>>> Vous perdez 1 PV""")
                        perdre_pv(PV, 1)
                    elif R == 3: 
                        pass # Reprend directment l'ascension
                    ecrire("""
Vous décidez de reprendre l'ascension.""")
            elif R == "3":
               # Branche 2.1.1.3
               ecrire("""
Vous ne voulez pas perdre de temps et choisissez de dégringoler cette pente.
Cependant, vous glissez sur une pierre et tomber la tête la première par terre.
Cette chaussure ne valait peut être pas d'être récupérée ...\n

>>> Vous êtes mort.""")
               input()
               quit() 
        ## Branche 2.1
        ecrire("""À chaque geste, un son différent s’élève — grave, aigu, bref ou prolongé.\n"
En vous élevant, vous comprenez que l’éboulis tout entier est un instrument, un assemblage naturel et ancien, accordé au souffle du vent.\n")
------

Vous sentez la fatigue dans vos membres, la poussière dans vos poumons, mais aussi un appel : la montagne semble vous éprouver, jauger votre détermination.\n")

>>> Vous gagnez 1 point d'Agilité.""")
        Agi += 1
        R = question("""
Devant vous, deux passages se dessinent dans la paroi :
    1. À gauche, une fissure étroite d’où s’échappe une lueur rougeâtre et un grondement profond.
    2. À droite, un passage peu éclairé d'un ton blanc pâle.
Votre réponse : """, ("1", "2"))
        if R == "1":
            ecrire("""
Vous arrivez dans une chambre magmatique, la roche glisse et tombez dans de la lave.
                   
>>> Vous êtes mort.""") 
            input()
            quit()
        elif R == 2: 
            ecrire("""
Vous continuez votre chemin, vous apercevez une porte. Vous décidez donc de la franchir.""")
    elif R == "2":
        # Branche 2.2
        ecrire("""
Vous vous approchez prudemment de cette mystérieuse lumière.
Vous constatez que cette lumière provient du Soleil entre les pierres, ce n'est pas ce que vous recherchiez.
Cependant, votre curiosité vous force à creuser les murs et ainsi sortir de la grotte.""")
        R = question("""
Enfin dehors, un monstre vous aperçoit et souhaite prévenir les autres de votre présence : 
    1. Le combattre pour ne pas qu'il informe les autres
    2. Se cacher
Votre réponse : """, ("1", "2"))
        if R == "1": 
            # Branche 2.2.1
            ecrire("""
Vous descendez des pierres et attaquez le monstre, finalement vous voyez qu'il y en a une cinquantaine autour de lui.
Tous les monstres vous chassent.

>>> Vous êtes mort.""")
            input()
            quit()
        elif R == "2": 
            # Branche 2.2.2
            ecrire("""
Vous attendez longuement afin de ne pas vous faire repérer, le monstre a prévenu ses acolytes et sont à votre recherche.""")
            R = question("""
Vous décidez d'agir : 
    1. Combattre tous les monstres
    2. Rester cacher
Votre réponse : """, ("1", "2"))
            if R == "1": 
                #Branche 2.2.2.1
                ecrire(""""
Vous êtes sur de vous et attaquez les monstres.
>>> Vous perdez 1 point de vie""")
                perdre_pv(1)
                sleep(1)
                while PV > 0: 
                    ecrire("""
Vous êtes persévérant et continuez à combattre.
>>> Vous perdez 1 point de vie.""")
                    perdre_pv(PV, 1)
                    sleep(2)
            elif R == "2": 
                # Branche 2.2.2.2
                ecrire("""
Vous vous fatiguez et tombez le long des pierres qui vous tenait jusque là en position.

>>> Vous perdez 1 point de vie""")
                perdre_pv(PV, 1)
                R = question("""
Vous vous faites remarquer et les monstres vous attaque tous ensemble.
    1. Combattre
    2. Fuir
Votre réponse : """, ("1", "2"))
                if R == "1": 
                    print("Les monstres sont trop nombreux, vous êtes surpassé.\n\n>>> Vous êtes mort.")
                elif R == "2": 
                    print("Vous fuyez mais glissez sur une pierre, les monstres vous rattrape.\n\n>>> Vous êtes mort.")
                input()
                quit()
#Branche B.
ecrire("""
Vous avez fini la 1ère étape dans votre quête de la Citadelle...
La Fin n'est jamais vraiment la fin mais juste un nouveau commencement.
  -  Sensei Wu""")
input()
quit()

