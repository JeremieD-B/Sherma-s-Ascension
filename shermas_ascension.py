##### Imports

from random import randint # Génère des nombres aléatoires (dans une portée donnée)
from time import sleep, time # Fait une pause du programme pendant un temps donné

#### Constantes de jeu 

vitesse_texte = 0.01 # 0.025 vitesse normale
vitesse_pause = 0.05 # 0.35 vitesse normale

### Constantes de description de salles

# QEvent = Question event
# QEventRep = Réponse autorisé du Question event 
# TEvent = Texte event

TIntro = """
Bienvenue.
    Vous êtes une jeune aventurière du nom de Sherma, la musique est votre vie, et ainsi vous souhaitez atteindre la Citadelle Mélodieuse pour apprendre les plus grands secrets.
Avant tout, une petite explication sur vos capacités : 
- Vous êtes capable faire des choix au fur et à mesure de votre avancée et de prendre les meilleurs décisions tout au long de votre aventure.
- Vous pouvez quitter à tout moment l'aventure en appuyant sur 'q' ou 'Q'.
Bon jeu !
"""

TReunirCarapaces = """

>>> Vous avez 4 fragments de Carapaces
Vous réunnissez vos fragments de carapaces et formez une caparaces !
Avec cette nouvelle carapace vous améliorez la vôtre et gagner en Point de vie maximum !
>>> Vos PV Max ont augmenté d'une unité"""

TEntreeDesc = """
    Le silence est dense. Une brume dorée se dissipe lentement autour de vous. Devant, se dresse une porte scellée, haute et fine, faite d’un métal chantant.
Chaque souffle de vent fait vibrer sa surface, produisant un écho lointain — comme un souvenir d’hymne oublié.
Derrière vous, les profondeurs. Devant, la Citadelle Mélodieuse, si haute que ses sommets se perdent dans les nuées. Vous savez qu’il faut atteindre son sommet — mais la voie reste voilée.
À votre droite, un sentier s’enfonce dans les forêts sombres où se cache derrière un mont juxtaposé à la Citadelle.
À votre gauche, un escalier de pierre descend vers des cavernes où l’eau résonne comme une harpe. Une lumière turquoise y palpite, irrégulière.
"""
TGrandeAlleeDesc = """
"""

TSentierDesc = """
-----

    Vous tournez à droite. Le sentier se fait étroit, bordé d’arbres aux troncs torsadés, dont les branches s’élancent comme des doigts vers le ciel.
La lumière s’amenuise à mesure que vous avancez."""

TCaverneDesc = """
-----
    Vous avancez dans une caverne, et arrivez dans une nouvelle zone sombre. Cette zone est plus humide, la pierre est donc très friable.
Afin de monter plus haut, vous devez monter sur les pierres. En revanche, vous apercevez une lueur blanchâtre dans un coin similaire à celui d'une lanterne."""

TPierresDesc = """
À chaque geste, un son différent s’élève — grave, aigu, bref ou prolongé.
En vous élevant, vous comprenez que l’éboulis tout entier est un instrument, un assemblage naturel et ancien, accordé au souffle du vent.
------

Vous sentez la fatigue dans vos membres, la poussière dans vos poumons, mais aussi un appel : la montagne semble vous éprouver, jauger votre détermination.

>>> Vous gagnez 1 point d'Agilité."""

TExterieurDesc = """
-----
    Vous vous approchez prudemment de cette mystérieuse lumière.
Vous constatez que cette lumière provient du Soleil entre les pierres, ce n'est pas ce que vous recherchiez.
Cependant, votre curiosité vous force à creuser les murs et ainsi sortir de la grotte."""


TEntreeDeplacement = """
Souhaitez-vous partir à gauche ou à droite ?
    1. Gauche    
    2. Droite
Votre réponse : """
TEntreeDeplacementRep = ("1","2")

TGrotteHumideQEvent1 = """
Pour continuer vous n'avez d'autre choix que de faire bouger cette invité indésirable,
    1. Lancer une pierre dessus en espérant la faire fuir
    2. Essayer de la pousser doucement pour passer à coté 
Votre réponse :"""
TGrotteHumideQEvent1Rep = ("1","2")

TGrotteHumideTEvent1_1 = """
    Vous décidez de ramasser une pierre de la taille de votre main et la lancez sur l'étrange insecte qui vous bloque
Après avoir sursauté en recevant la pierre sur son dos, l'insecte se mets à trembler
Après quelque seconde d'étranges pics aussi longs qu'un bras sortent tout d'un coup de tout son corps
Vous avez bien fait de ne pas vous approcher
Vous pouvez donc continuer votre avancée en contournant cet ennemis
"""
TGrotteHumideTEvent1_2 = """
    Lorsque que vous vous approchez de cet étrange insecte,
Vous le voyez pousser un faible cri aigu avant de se mettre à trembler
Lorsque d'un coup de nombreux pics aussi long qu'un bras et ascérées comme des couteaux sortent de son corps
N'ayant pas le temps de réagir vous ne pouvez que vous protéger avec votre bras
"""
TGrotteHumideTEvent2 = """
-----
    Continuant votre avancée, vous arrivez face à une pente que vous devrez escalader,
Vous regardez de plus près les différentes prises qui vous seront disponibles.
Elles sont petites et ne semblent pas stables, l'escalade sera difficile.
"""
TGrotteHumideQEvent2 = """
Ils vous faut choisir :
    1. Essayer d'escalader rapidement espérant que les pierres tiennent le coup
    2. Prendre son temps avec le maximum de précautions
Votre réponse : """
TGrotteHumideQEvent2Rep =("1","2") 
TGrotteHumideTEvent2_1 = """
    Vous vous mettez à courir le plus rapidement possible
Sous chacun de vos pas, la prise que vous utilisez se brise,
Sans votre élan vous n'arriveriez jamais à grimper.
Il est certain qu'avoir couru était l'unique solution.

>>> Vous gagnez 1 d'Agilité.
"""
TGrotteHumideTEvent2_2 = """
    Vous escaladez tout doucement, sauf qu'en posant le pied sur la première prises, 
Vous vous rendez compte qu'elle n'est pas stable, 
En essayant de changer d'appui, vous glissez et retombez en bas de cette pente.
""" 
TGrotteHumideQEvent2_1 = """
Vous n'avez d'autre choix que de réessayer de monter.
    1. Commencer à courir espérant avoir assez de force pour atteindre le haut sans tomber. 
    2. Attraper les prises doucement une par une.
Votre réponse : """
TGrotteHumideQEvent2_1Rep = ("1","2")
TGrotteHumideTEvent2_1_1 = """
    Vous vous mettez à courir le plus rapidement possible
Dans votre élan vous réussissez à atteindre la haut de la peinte
Fière de vos efforts vous avancez désormais vers une nouvelle pièce

>>> Vous gagnez 1 d'Agilité.
"""
TGrotteHumideTEvent2_1_2 = """
    Malgré toutes les précautions que vous avez su prendre, 
Les prises ne tiennent pas sous votre poids pendant plus d'une seconde. 
C'est durant votre dernière chute que vous réalisiez que cette fois ci, 
La précipitation était le bon choix
"""

TGrotteHumideDesc = """
-----
    Vous arrivez dans une pièce sombre, seuls quelques rayon de lumière percent au travers de la dense végétation qui vous entoure
L'atmosphère est pesante, des bruits inquiétant d'insecte percent au travers du silence qui vous entoure
Après avoir marcher quelques minutes, determiné à avancer vers la Citadelle Mélodieuse, vous faites face à un étrange insecte
Cet insecte ressemble à une énorme chenille, elle vous arrive au genoux et est couverte de poils vert formant une fourure
"""

TGrandeAlleeT1 = """-----
    Vous faites maintenant face à une grande allée dégagée,
Les rayons de lumières qui percent à travers la végétation toujours denses
Donnent une atmosphère particulière à la pièce
"""

TGrandeAlleeQEvent1 ="""
Vous remarquez un petit couloir à votre droite 
    1. Vous allez explorer ce couloir sombre.
    2. Vous préfèrez continuer dans cette grande allée.
Votre réponse :"""
TGrandeAlleeQEvent1Rep = ("1","2")

TGrandeAlleeTEvent1_1 = """
-----
    En entrant dans ce couloir, la visibilitée est très faible. 
Vous voyez des gouttes perler du plafonds, la pièce est très humide 
Alors que vous continuiez votre avancée, vouss entendez l'entrée de ce couloir s'effondrer 
Il va être difficile de ressortir.
Au moins vous avez trouver un chapelet contenant 30 perles.)
""" 

TGrandeAlleeQEvent1_1 = """
Pour ressortir d'ici il va falloir choisir à quoi se consacrer.
    1. Chercher une autre sortie
    2. Ecarter les pierres qui se sont effondrer pour revenir en arrière
Votre réponse :"""
TGrandeAlleeQEvent1_1Rep = ("1","2")

TGrandeAlleeTEvent1_1_1 = """
    Après des heures d'errances vous n'avez trouvez aucune sortie.
Malgré tous vos effort les heures passes, le temps passe et aucune sortie n'est décelable.
Vos recherches font du bruit, des vers géant qui vivent dans les murs de cette cavernes viennent vous rendre visites.
"""

TGrandeAlleeQEvent1_1_2 = """
    Vous creusez de toutes vos forces pour passer cet amas de pierre
Malgré la difficulté manifeste de cette action vous réussisez a vous en sortir.
"""

TGrandeAlleeTEvent1_2 = """
    Vous traversez cette grande allée et observez autour de vous 
La végétation de ces cavernes est extrêmement développée.
Vous ne connaissiez aucune de ces espèces avant de venir ici 
Les différentes plantes et arbres autour de vous vous parraissent très jolis 
Cet arbre là par exemple, ses branches sont toutes courbées, pas une seule partie de l'arbre n'est rectili...
        BRRAOUUUUUMMMMMM
Vous venez d'entendre le couloir que vous aviez vu précédemment s'effondrer.
Cette caverne n'est définitivement pas accueillante.
"""

TGrandeAlleeT2 = """
    Après avoir avancer dans cette grande allée, vous faites à un nouvel ennemis.
Physiquement il ressemble fortement à la chenille croisée auparavant, mais celle-ci vole !
"""

TGrandeAlleeQEvent2 ="""
Pour atteindre le bout de cette allée il va falloir passer. 
    1. Lancer une pierre sur l'insecte volant dans l'espoir de le faire fuir.
    2. Courir de toutes vos forces en dessous pour atteindre la porte avant qu'il ne réagisse
Votre réponse : """
TGrandeAlleeQEvent2Rep = ("1","2")

TGrandeAlleeTEvent2_1 = """
    Vous lancez une pierre vers l'insecte, il perd l'équilibre de son vol et s'écrase au sol
"""

TGrandeAlleeTEvent2_2 = """
    En courant vers la porte, vous trébuchez et vous faites remarquer par l'ennemis,
En trébuchant vous vous blessez a la jambe
"""

TGrandeAlleeQEvent2_1 = """
Pour atteindre le bout de cette allée est nécessaire de s'échapper de cette situation.
  1. Courir de plus belle vers la sortie.
  2. Foncer vers l'ennemi afin de le faire tomber et de l'abattre.
Votre réponse : """
TGrandeAlleeQEvent2_1Rep = ("1","2")

TGrandeAlleeTEvent2_1_1 = """
    Vous avez trébuché de nouveau, vous ne sentez même plus votre jambe blessée, cet insecte approche vers vous.
"""

TGrandeAlleeTEvent2_1_2 = """
    En fonçant vers cet insecte il descend a vive allure vers vous son dard diriger vers votre tête.
"""

TGrandeAlleeT3= """
    Vous arrivez finalement vers une grande porte entrouverte un léger filet de lumière la traverse.
"""

TGrandeAlleeQEvent3 = """
Vous apercevez un petit recoin dans lequel vous pourriez vous faufiler pour explorer
    1. Traverser cette énorme porte et avancer vers la Citadelle
    2. Commencer par explorer ce petit recoin.
Votre réponse : """
TGrandeAlleeQEvent3Rep = ("1","2")

TGrandeAlleeTEvent3_1 = """
    Vous traversez la grande porte, vous ne saurez jamais ce qu'il y avait dans ce recoin.
"""
TGrandeAlleeTEvent3_2 = """

    En entrant dans ce recoin vous trouver une pierre ayant la forme d'un banc
Vous profitez de ce moment de calme pour vous asseoir un moment
"""

TSentierQEvent1 = """
Observez autour de vous ?
    1. Oui
    2. Non
Votre réponse : """
TSentierQEvent1Rep = ("1", "2")

TSentierQEvent1_1 = """
    L’air est saturé d’humidité et d’un parfum âcre de mousse et de sève. Sous vos pas, le sol chante à peine — un bruissement discret, presque un murmure.
Au loin, au-delà de la canopée, se dresse un mont gigantesque, une masse sombre collée contre la Citadelle Mélodieuse. Ses pentes abruptes semblent fusionner avec les fondations mêmes de la tour. 
À sa base, les arbres se tordent, comme attirés ou repoussés par la musique silencieuse qui émane de la Citadelle.
Par moments, un son traverse la forêt — une note isolée, pure, qui résonne dans l’air avant de se dissoudre dans le vent. Était-ce un instrument, un oiseau, ou la montagne elle-même qui soupire ?
\nVous sentez que cette voie mène à quelque chose d’enfoui, peut-être une entrée dissimulée. Les branches s’entrelacent au-dessus de vous, formant une voûte presque organique. 
L’obscurité devient tangible, épaisse, comme une étoffe que l’on pourrait écarter d’un geste."""

TSentierQEvent2 = """
Puis soudain, un ennemi apparait d'entre les branches, celui-ci est laid et n'aurait peur de rien. Pris de panique, il décide de vous attaquer.
Combattre cet ennemi ?
    1. Combattre
    2. Esquive
Votre réponse : """

TSentierQEvent2Rep = ("1", "2")

TSentierQEvent2_1 = """
Vous décidez de combattre l'ennemi
"""

TSentierQEvent2_2 = """
Vous décidez de contourner l'ennemi, celui-ci est finalement très lent il ne vous rattrape pas.

Vous continuez votre périple."""

TSentierQEvent3 = """

    Votre lacet s'est dénoué sur votre chaussure gauche, vous avez du mal à refaire vos lacets mais finissez toujours par y arriver.
Souhaitez-vous le refaire (Cela prendra un cours instant) ?
    1. Continuer sur le chemin
    2. Refaire les lacets avec difficulté
Votre Réponse : """
TSentierQEvent3Rep = ("1", "2")

TSentierQEvent3_1 = """
Vous refaites vos lacets
"""

TCaverneQEvent1 = """
Qu'allez-vous faire ?
    1. Monter sur les pierres
    2. Se diriger vers la lumière
Votre réponse : """
TCaverneQEvent1Rep = ("1", "2")

TCaverneQEvent1_1 = """
    Vous commencez à grimper. Les pierres sont glissantes, couvertes d’un lichen argenté.
Sous vos doigts, certaines vibrent faiblement, comme si elles gardaient en elles la trace d’un ancien chant.

>>> Vous gagnez 1 d'Agilité.

Puis vient un grondement.

Une note fausse, un craquement, et la montagne semble s’éveiller. Des pierres roulent en contrebas. Le sol se dérobe un instant sous vos pieds.
Votre chaussure est prise dans ces pierres."""

TCaverneEvent2_1 = """
Par chance, vous avez refaits vos lacets au préalable et votre chaussure reste intacte. Vous continuez donc votre ascension."""

TCaverneEvent2_2 = """
Votre chaussure n'étant pas bien attaché, celle-ci s'enlève et tombe tout en bas."""

TCaverneQEvent3 = """
Aller chercher votre chaussure ?
    1. Continuer
    2. Descendre
    3. Descendre rapidement
Votre réponse : """
TCaverneQEvent3Rep = ("1", "2", "3")

TCaverneQEvent3_1 = """
Vous décidez de continuer votre ascension vertigineuse qui ne semble plus en finir.

>>> Vous perdez 1 PV."""

TCaverneQEvent3_2 = """
Vous êtes en bas, vous remettez votre chaussure. La lumière entre aperçu plus tôt a disparu.
Etait-ce un mirage ? Une illusion ?"""

TCaverneQEvent3_3 = """
Vous ne voulez pas perdre de temps et choisissez de dégringoler cette pente.
Cependant, vous glissez sur une pierre et tomber la tête la première par terre.
Cette chaussure ne valait peut être pas d'être récupérée ...\n
"""

TCaverneQEvent4 = """
Que faire maintenant ?
    1. Reprendre l'ascension
    2. Aller vers le sentier
Votre réponse : """
TCaverneQEvent4Rep = ("1", "2")

TCaverneQEvent4_1 = """
    Votre ascension reprend de plus belle, vous pressez le pas au risque de vous faire repérer.
Cependant, vous apercevez à travers des pierres une petite lumière.
En vous posant correctement et en creusant, vous apercevez une sorte de vieux papier contenant des inscriptions musicales très éffacées.
                           
>>> Vous récupérer le parchemin : Entre pierres et cordes."""

TCaverneQEvent4_2 = """
La famille de l'ennemi du sentier ont vu votre présence et suive désormais vos pas.
Vous vous dirigez vers eux sans le savoir. Vous entendez un bruit et stopper le pas."""

TCaverneQEvent5 = """
Vous paniquez, que choisissez-vous de faire ?
    1. Se cacher
    2. Aller combattre
    3. Reprendre l'ascension
Votre réponse : """
TCaverneQEvent5Rep = ("1", "2", "3")

TCaverneQEvent5_1 = """
Vous vous cachez, pendant un très long moment. Personne ne vous remarque.
>>> Vous perdez 1 point d'agilité.

Vous décidez de reprendre l'ascension."""

TCaverneQEvent5_2 = """
Vous brandissez votre Baguette de métal et combattez les ennemis. Ceux-ci prennent peur sauf un.
Vous le combattez et êtes légèrement blessé. Vous repreennez voter ascension finalement.
"""

TPierresQEvent1 = """
Devant vous, deux passages se dessinent dans la paroi :
    1. À gauche, une fissure étroite d’où s’échappe une lueur rougeâtre et un grondement profond.
    2. À droite, un passage peu éclairé d'un ton blanc pâle.
Votre réponse : """
TPierresQEvent1Rep = ("1", "2")

TPierresQEvent1_1 = """
Vous arrivez dans une chambre magmatique, la roche glisse et tombez dans de la lave.
"""

TPierresQEvent1_2 = """
Vous continuez votre chemin, vous apercevez une porte. Vous décidez donc de la franchir."""

TExterieurQEvent1 = """
Enfin dehors, un monstre vous aperçoit et souhaite prévenir les autres de votre présence : 
    1. Le combattre pour ne pas qu'il informe les autres
    2. Se cacher
Votre réponse : """
TExterieurQEvent1Rep = ("1", "2")

TExterieurQEvent1_1 = """
Vous descendez des pierres et attaquez le monstre, finalement vous voyez qu'il y en a une cinquantaine autour de lui.
Tous les monstres vous chassent.
"""

TExterieurQEvent1_2 = """
Vous attendez longuement afin de ne pas vous faire repérer, le monstre a prévenu ses acolytes et sont à votre recherche."""

TExterieurQEvent2 = """
Vous décidez d'agir : 
    1. Combattre tous les monstres
    2. Rester cacher
Votre réponse : """
TExterieurQEvent2Rep = ("1", "2")

TExterieurQEvent2_1 = """"
Vous êtes sur de vous et attaquez les monstres.
>>> Vous perdez 1 point de vie."""

TExterieurQEvent2_2 = """
Vous vous fatiguez et tombez le long des pierres qui vous tenait jusque là en position.

>>> Vous perdez 1 point de vie."""

TExterieurQEvent3 = """
Vous vous faites remarquer et les monstres vous attaque tous ensemble.
    1. Combattre
    2. Fuir
Votre réponse : """
TExterieurQEvent3Rep = ("1", "2")

TExterieurQEvent3_1 = """
Les monstres sont trop nombreux, vous êtes surpassé.
"""

TExterieurQEvent3_2 = """
Vous fuyez mais glissez sur une pierre, les monstres vous rattrape.
"""

## Textes Partie B (A partir du Gouffre d'Os)


TGouffreDOsDesc = """
Vous arrivez devant un gouffre où vous observez un petit village caché et oublié.
Vous décidez d'atteindre ce village. 
"""

TGouffreDOsQEvent1 = """
Vous arrivez dans le village, que voulez-vous faire ?
    1. Vous reposer sur le banc
    2. Aller voir le marchand
    3. Continuer votre chemin
Votre réponse : """

TGouffreDOsQEvent1Rep = ("1", "2", "3")

TGouffreDOsQEvent1_1 = """
Vous régénérez entièrement votre vie, vous sauvegardez votre progression."""

TGouffreDOsQEvent1_2 = """
Vous vous dirigez vers le marchand et commencez à converser avec lui. Vous avez du mal à le comprendre de part son dialecte.
Bnoujor et Benuienve j'ia pilen d'atlicres puor vous ! """

TGouffreDOsQEvent1_3 = """
Vous continuez vers une salle sombre"""

TGouffreDOsShopQEvent1 = """
Vous décidez de lire les étiquettes: 
    1. Fragment de carapaces [30 perles]
    2. Épée d'argent cristallisée [140 perles]
    3. Clé de déchiffrement [70 perles]
    4. Parfum [20 perles]
    5. Orbe de vie [30 perles]
    6. Partir 
Votre réponse : """

TGouffreDOsShopQEvent1Rep = ("1", "2", "3", "4", "5", "6")

TGouffreDOsShopQEvent1_PasAssezPerles = """
>>> Vous n'avez pas assez de perles."""

TGouffreDOsShopQEvent1_ADejaNouvelleArme = """
>>> Vous avez déjà cette arme !"""

TGouffreDOsShopQEvent1_NouvelleArme = """
>>> Vous obtenez l'Épée d'argent cristallisée."""

TGouffreDOsShopQEvent1_CleDechiffrement = """
>>> Vous obtenez une clé de déchiffrement."""

TGouffreDOsShopQEvent1_Parfum = """
>>> Vous obtenez un parfum, celui-ci à une très bonne odeur."""

TGouffreDOsShopQEvent1_OrbeDeVie = """
>>> Vous obtenez une orbe de vie, celle-ci vous confère la possibilité de vous régénérer quand vous le souhaitez."""
a = "aa"
TGouffreDOsShopQEvent1_Exit = """
Vous sortez de la boutique..."""

TGouffreDOsShopQEvent1_InventoryFull = """
>>> Votre inventaire est plein."""

# Block à utiliser dans l'énigme 2

PISTON_HAUT = "🠕"
PISTON_GAUCHE = "🠔"
PISTON_BAS = "🠗"        
PISTON_DROITE = "🠖"

PISTON_COLLANT_HAUT = "⇡"
PISTON_COLLANT_GAUCHE = "⇠"
PISTON_COLLANT_BAS = "⇣"
PISTON_COLLANT_DROITE = "⇢"

VIDE = "·"
ENERGIE = "🗲"
BLOCK = "◼"
POINT_ARRIVEE = "◎"

# Pistons étirés

PISTON_HAUT_ETIREE        = "ᐱ"
PISTON_GAUCHE_ETIREE      = "ᐸ"
PISTON_BAS_ETIREE         = "ᐯ"
PISTON_DROITE_ETIREE      = "ᐳ"

PISTON_COLLANT_HAUT_ETIREE = "▲"
PISTON_COLLANT_GAUCHE_ETIREE = "◀"
PISTON_COLLANT_BAS_ETIREE = "▼"
PISTON_COLLANT_DROITE_ETIREE = "▶"

PISTON_BLOCK_HORIZONTAL = "═"
PISTON_BLOCK_VERTICAL = "║"

TCaverneClocheDesc = """
Vous entrez dans une caverne qui pourrait être une symphonie silencieuse de métal. 
Des cloches de toutes formes et tailles ornent les murs, créant un labyrinthe obscur. 
La lumière filtre à travers les fissures, révélant des ombres dansantes et une atmosphère mystérieuse.
"""

TCaverneClocheApparition = """
Soudain, l'air vibre d'un silence pesant, interrompu par un léger tintement. 
Puis, les cloches s'animent, leur son s'amplifiant en un fracas assourdissant. 
Des profondeurs de la caverne de cloches entassées, la Bête émerge. 
Son corps massif déforme les cloches, créant un chemin destructeur. 
La lumière faiblissante révèle une silhouette imposante, prête à bondir, les cloches brisées résonnant à chaque pas.
"""
TCaverneClocheAtk1 = """
La bête se cabre, puis fonce droit sur vous en faisant résonner toutes les cloches de la grotte. 
L'impact projette et assourdit, rester face à la bête est très dangeureux.
"""
TCaverneClocheQAtk1 = """
Que faites-vous ? :
    1. Vous essayez de plonger sur le côté pour éviter l'attaque.
    2. Vous tentez de sauter par dessus la bête pour lui frapper le dos.
    3. Vous sautez en arrière pour l'attendre, prêt à contre-attaquer.
Votre réponse : """
TCaverneClocheAtk2 = """
La bête piètine le sol violemment et prend appui de toute ses forces.
Elle bondit en l'air et se dirige droit vers vous dans un fracas tonitruant.
"""
TCaverneClocheQAtk2 = """
Que faites-vous ? :
    1. Plonger sous la bête pour lui attaquer les pattes.
    2. Sauter en arrière pour prendre de la distance et ne pas se faire toucher.
    3. Essayer de grimper sur son dos pendant qu'elle est en l'air.
Votre réponse : """
TCaverneClocheAtk3 = """
La bête frappe le sol de ses pattes et commence a creuser entre les cloches.
Elle semble essayer de se cacher sous les cloches.
"""
TCaverneClocheQAtk3 = """
Que faites-vous ? :
    1. Attendre la bête en gardant ses distances pour l'attaquer quand elle ressortira.
    2. Se précipiter pour l'attaquer avant qu'elle ne puisse se cacher.
    3. Prendre de la hauteur pour observer d'où elle va ressortir.
Votre réponse : """
TCaverneClocheAtk4 = """
Enragée la bête des cloches frappe violemment le sol faisant trembler toute la caverne.
Les cloches qui recouvre le plafond vibrent et menace de tomber sur vous
Soudain la bête bondit en l'air, vous voyez les cloches autour d'elle tomber dans toutes les directions.
"""
TCaverneClocheQAtk4 = """
Que faites-vous ? :
    1. Plonger sur le coté pour éviter la bête de essayer d'éviter les cloches
    2. Sauter en arrière pour laisser la bête atterir devant vous
    3. Plonger sous la bête et lui attaquer les pattes pendant qu'elle est en l'air
Votre réponse : """
TCaverneClocheAtk5 = """
La bête des cloches est furieuse elle garde ses distances et frappe le sol pour déloger les cloches qui le constituent.
Elle se mets a frapper les cloches pour les envoyer en votre direction, certaines tombent du plafond.
Les cloches s'approchant dangeureusement de vous rebondissent de manière complétement imprévisible.
"""
TCaverneClocheQAtk5 = """
Que faites-vous ? :
    1. Frapper les cloches qui vous arrivent dessus pour les renvoyer à la bête
    2. Foncer vers la bête en évitant les cloches pour l'attaquer directement
    3. Maintenir ses distance et se concentrer pour éviter les cloches
Votre réponse : """
TCaverneClocheAtkRep = ("1","2","3")

TCaverneClocheRate = """
Vous essayez d'éviter l'attaque de la Bête des Cloches mais malheureusement elle avait prévue ce mouvement.
"""
TCaverneClocheEsquive = """ 
Vous réagissez rapidement et évitez l'attaque de la Bête des Cloches
Malheureusement voous ne trouvez pas le temps de lui infliger des dégâts
"""
TCaverneClocheDegat = """
Vous réussissez à devancer la vitesse de la Bête des Cloches
Vous la frappez de toutes vos forces ! 
"""
TCaverneClocheEnrage = """
La Bête des Cloches est blessée, elle devient folle de rage et attaque avec encore plus de férocité.
Ses attaques sont plus rapides et plus puissantes, il va falloir redoubler de réactivité.
"""
TCaverneClocheLent ="""
Vous ne réagissez pas assez vite, la Bête des Cloches vous percute de plein fouet.
"""
TCaverneClocheVictoire = """
Avec un dernier coup puissant, vous terrassez la Bête des Cloches.
Les cloches cessent de résonner, et un silence apaisant envahit la caverne.
Vous avez vaincu un ennemi redoutable et pouvez continuer votre ascension vers la Citadelle Mélodieuse.
"""
 
TFINPartieA = """
La porte se ferme brutalement, il vous est impossible de revenir en arrière.
Vous pensez être sur le bon chemin, une 1ère étape vient d'être franchi et venez de comprendre les bases."""

TFin = """
    Après être sortie de cette caverne au son discordant, vous avancez doucement, écoutant le son des cloches qui tintent sous vos pieds.
Les cloches qui constituaient le sol derrière vous laisse progressivement place aux pavées bien alignés.
Vous regardez autour de vous, vous êtes désormais sur un gigantesque pont, vous observez au loin bien en dessous de vous l'endroit d'où vous avez commencez votre ascension.
Autour de vous, sur le pont vous remarquez les jolis lampadaires qui vous éclaire d'une douce lumière blanche, à l'aspect pure.
Bien que ce pont paraisse très luxueux, digne de la grande Citadelle Mélodieuse que vous cherchez a atteindre, vous remarquez des défauts.
Le temps n'éparge rien ni personne, vous remarquez alors la rouilles sur les rembardes, la mousse entre les pavés et les fissures qui parsément les joints.
C'est alors seulement que vous levez les yeux.

La Citadelle Mélodieuse.
Gigantesque, Gracieuse, Impressionnante.
Elle dépasse tout ce que vous avez pus imaginer.
Elle est d'une auteur telle que vous n'arrivez même pas à en distinguer le sommet. 
Elle semble composée de long tubes métalique brillant d'un aspect cuivrée, semblant former un seul gigantesque instrument.
D'autre part vou remarquez de long fils tendues entres différents étages qui semblent former des harpes monumentales.
Vous trépignez d'impatience à l'idée de rentrer dans la Citadelle et de participer enfin à la chorale qui réunis tout les pélérins tel que vous.
Vous continuez votre avancée sur ce pont jusqu'à une porte qui serait capable de laisser passer un géant.

Alors que vous vous faufilez dans l'entrebaillement de la porte, vous admirez l'architecture de la Citadelle, rafinée, orginale, sans nuls comparaisons.
C'est seulement à ce moment que vous vous rendez compte du problème.
Depuis le début de votre ascencion. Vous n'avez rien vu provenant de la Citadelle. 
Pas un son, 
Pas un bruit,
Pas une seule mélodie.

Cette Citadelle est vide. 
Plus personne ne fait chanter tous ces instruments merveilleux.
Il ne vous reste plus rien à faire, votre but est atteint, mais il n'est en rien similaire à ce que vous cherchiez.

Vous n'avez qu'un seul choix, découvrir la source de la déchéance de cette si grande Citadalle.

Pour ce faire je n'ai qu'un seul conseil à te donner. 
La réponse à ces questions se trouve dans Hollow Knight Silksong.

>>> Merci d'avoir jouer.

Alesterm & Colddestructor
"""

### Stats de base

Inv = {"Arme": "Baguette de métal", 
        "Mélodies" : [],
        "Carapaces" : 0,
        "Objets" : [],
        "Perles" : 0}

Stats = {
"Pv_Max" : 5,
"Atk": 0,
"Agi" : 0,
"Dgt" : 10
}

Sherma = {
"PV": 5,
"Inv" : Inv, 
"Stats" : Stats,
"Emplacement" : "Tutoriel",
"lacets_faits" : True,
"mort": 0,
"a_finit": False,
"Checkpoint" : "Tutoriel"
}

Salles = {
    "Tutoriel" : {"NomAffichee" : "Entrée","Desc" : TEntreeDesc},
    "Entree" : {"NomAffichee" : "Entrée","Desc" : TEntreeDesc},
    "GrotteHumide" : {"NomAffichee" : "Grotte humide","Desc" : TGrotteHumideDesc},
    "GrandeAllee" : {"NomAffichee" : "Grande Allée","Desc" : TGrandeAlleeDesc},
    "Sentier": {"NomAffichee" : "Sentier","Desc" : TSentierDesc},
    "Caverne": {"NomAffichee" : "Caverne","Desc" : TCaverneDesc},
    "Pierres": {"NomAffichee" : "Pierres","Desc" : TPierresDesc},
    "Exterieur": {"NomAffichee" : "Extérieur","Desc" : TExterieurDesc},
    "GouffreDOs" : {"NomAffichee" : "Gouffre d'Os","Desc" : TGouffreDOsDesc},
    "Enigme1": {"NomAffichee" : "Salle d'Énigme 1","Desc" : None, "Past" : False},
    "Enigme2": {"NomAffichee" : "Salle d'Énigme 2","Desc" : None, "Past" : False},
    "Enigme3": {"NomAffichee" : "Salle d'Énigme 3","Desc" : None, "Past" : False},
    "CaverneCloches": {"NomAffichee" : "Caverne des Cloches","Desc" : TCaverneClocheDesc, "Past" : False},
    "Fin" : {"NomAffichee" : "Citadelle Mélodieuse", "Desc": TFin}
}

###### FONCTIONS GÉNÉRALE:

def input_time(timer : bool):
    TempsRep = None
    if timer :
        TempDepart = time()
        R = input()
        TempsRep = time() -TempDepart
    else :
        R = input()
    return (R,TempsRep)


def question(text : str,rep : tuple, timer = False) -> str:
    """
    Pose la question "text"
    Si les réponse est q ou Q : quitte le programme
    R est la Réponse que l'on attend
    """
    Renvoi = (None,None)
    tour = 0
    while Renvoi[0] not in rep and Renvoi[0] not in ("Q","q"):
        if Renvoi[0] == "Inv" :
            afficher_inv()
            Renvoi = (None,None)
        if Renvoi[0] == "Stats" :
            afficher_stats()
            Renvoi = (None,None)
        if tour == 0 :
            ecrire(text)
        else : 
            ecrire(text, 0.005,0.01)
        Renvoi = input_time(timer)
        """if timer == True :
            Tempsdepart = time()
            R = input()
            TempsReponse = time() - Tempsdepart
        else : 
            R = input()"""
        tour +=1
    if Renvoi[0] in ("q","Q") :
        quit()
    if timer == True :
        return Renvoi
    return Renvoi[0]

def question_temp(text : str,rep : tuple) -> tuple:
    TempsAvantRep = time()
    R = question(text,rep)
    TempsDeReponse = time() - TempsAvantRep
    print(TempsDeReponse)
    return R, TempsDeReponse

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

def afficher_stats():
    TInv = f"""
----------
Emplacement : {Salles[Sherma["Emplacement"]]["NomAffichee"]}
PV : {Sherma["PV"]}/{Sherma["Stats"]["Pv_Max"]}
Atk : {Sherma["Stats"]["Atk"]}
Agi : {Sherma["Stats"]["Agi"]}
Objet : {Sherma["Inv"]["Objets"]}
---------
"""
    ecrire(TInv)

def afficher_inv():
    TStats = f"""
----------
Vous avez {Sherma["PV"]}/{Sherma["Stats"]["Pv_Max"]} PV.

Vous possédez {Sherma["Inv"]["Carapaces"]} Fragments de Carapaces.

Vous possédez {Sherma["Inv"]["Perles"]} Perles.
---------
"""
    ecrire(TStats)

def modif_agi(modif : int):
    if Sherma["Stats"]["Agi"] + modif > 0 :
        Sherma["Stats"]["Agi"] += modif

def modif_perles(modif: int):
    Sherma["Inv"]["Perles"] += modif
    ecrire(f"\n>>> Vous gagnez {modif} perles.\n")

def gagner_carapaces():
    Sherma["Inv"]["Carapaces"] += 1
    ecrire("\n>>> Vous récupérez un fragment de Carapaces")
    if Sherma["Inv"]["Carapaces"] == 4 :
        Sherma["Inv"]["Carapaces"] = 0
        ecrire(TReunirCarapaces)
        Sherma["Stats"]["Pv_Max"] +=1 
        remplir_pv()

def perdre_pv(pv : int, pv_perdu :int):
    ecrire(f"\n>>> Vous perdez {pv_perdu} PV. \n")
    pv -= pv_perdu
    if pv <= 0 :
        mourir("\n>>> Vous n'avez plus aucun PV.")
    return pv

def gagner_pv(pv : int, pv_gagne :int):
    if pv <= Sherma["Stats"]["Pv_Max"] :
        pv += pv_gagne
        ecrire(f"\n>>> Vous gagnez {pv_gagne} PV. \n")
    return pv

def remplir_pv():
    Sherma["PV"] = Sherma["Stats"]["Pv_Max"]
    ecrire(f"\n>>> Vos PV se remplissent ! Vous avez désormais {Sherma['Stats']['Pv_Max']}/{Sherma['Stats']['Pv_Max']} PV\n")


def mourir(text_mort):
    ecrire(text_mort)
    ecrire("\n>>> Vous êtes mort.")
    Sherma["mort"] += 1
    if Sherma["mort"] < 10:
        R = question("""
Voulez-vous recommencer le jeu ?
    1. Oui
    2. Non
Votre réponse : """, ("1", "2"))
        if R == "1": 
            
            if Sherma["Checkpoint"] == "Tutoriel":
                Sherma["PV"] = 5
                Inv = {"Arme": "Baguette de métal", 
            "Mélodies" : [],
            "Carapaces" : 0,
            "Objets" : [],
            "Perles" : 0
                }

                Stats = Stats = {
                "Pv_Max" : 5,
                "Atk": 0,
                "Agi" : 0,
                "Dgt" : 10
                }
                Sherma["Stats"] = Stats
                Sherma["Inv"] = Inv
                Sherma["Emplacement"] = "Tutoriel"
            else :
                remplir_pv()
                Sherma["Emplacement"] = Sherma["Checkpoint"]
            jouer()
        elif R == "2": 
            quit() 
    else: 
        ecrire("\nVous êtes mort 10 fois, ainsi vous ne méritez plus vivre. Aurevoir.")
        quit()
       
###### FONCTION DE SALLE

def Tutoriel():
    ## TUTORIEL
    ecrire(TIntro)
    sleep(1)
    Sherma["Emplacement"] = "Entree"

def Entree(): 
    # Arriver à la porte
    ecrire(Salles["Entree"]["Desc"])
    R = question(TEntreeDeplacement,TEntreeDeplacementRep)
    if R == "1": 
        Sherma["Emplacement"] = "GrotteHumide"
    elif R == "2": 
        Sherma["Emplacement"] = "Sentier"

def GrotteHumide():
    #Branche 1.1 
    GrotteHumide1()
    GrotteHumide2()
    Sherma["Emplacement"] = "GrandeAllee"
def GrotteHumide1():
    #Branche 1.1
    ecrire(Salles["GrotteHumide"]["Desc"])
    R = question(TGrotteHumideQEvent1,TGrotteHumideQEvent1Rep)
    if R == "1" :
        #Branche 1.1.1
        ecrire(TGrotteHumideTEvent1_1)
    elif R == "2":
        #Branche 1.1.2
        ecrire(TGrotteHumideTEvent1_2)
        Sherma["PV"] = perdre_pv(Sherma["PV"], 1)
def GrotteHumide2():
    #Branche 1.2
    ecrire(TGrotteHumideTEvent2)
    R = question(TGrotteHumideQEvent2,TGrotteHumideQEvent2Rep)
    if R == "1" :
        #Branche 1.2.1
        ecrire(TGrotteHumideTEvent2_1)
        modif_agi(1)
    elif R == "2" :
        #Branche 1.2.2
        ecrire(TGrotteHumideTEvent2_2)
        Sherma["PV"] = perdre_pv(Sherma["PV"], 1)
        R = question(TGrotteHumideQEvent2_1,TGrotteHumideQEvent2_1Rep)    
        if R == "1" :
            #Branche 1.2.2.1 
            ecrire(TGrotteHumideTEvent2_1_1)
            modif_agi(1)
        elif R == "2":
            #Branche 1.2.2.2
            mourir(TGrotteHumideTEvent2_1_2)

def GrandeAllee(): 
    #Branche 1.3
    GrandeAllee1()
    GrandeAllee2()
    GrandeAllee3()
    Sherma["Emplacement"] = "GouffreDOs"
def GrandeAllee1(): 
    ecrire(TGrandeAlleeT1)
    R = question(TGrandeAlleeQEvent1,TGrandeAlleeQEvent1Rep) 
    #Branche 1.3.1
    if R == "1" :
        ecrire(TGrandeAlleeTEvent1_1)
        modif_perles(30)
        R = question(TGrandeAlleeQEvent1_1,TGrandeAlleeQEvent1_1Rep)
        #Branche 1.3.1.1
        if R == "1" :
            mourir(TGrandeAlleeTEvent1_1_1)
        #Branche 1.3.1.2 
        elif R == "2":
            ecrire(TGrandeAlleeQEvent1_1_2)
            Sherma["PV"] = perdre_pv(Sherma["PV"], 1)
    elif R == "2" :
        #Branche 1.3.2
        ecrire(TGrandeAlleeTEvent1_2)
def GrandeAllee2(): 
    #Branche 1.4
    ecrire(TGrandeAlleeT2)
    R = question(TGrandeAlleeQEvent2,("1","2"))
    #Branche 1.4.1 
    if R == "1" :
        ecrire(TGrandeAlleeTEvent2_1)
        gagner_carapaces()
    #Branche 1.4.2
    elif R == "2" :
        GrandeAllee2_1()
def GrandeAllee2_1():
    ecrire(TGrandeAlleeTEvent2_2)
    Sherma["PV"] = perdre_pv(Sherma["PV"], 1)
    R = question(TGrandeAlleeQEvent2_1,TGrandeAlleeQEvent2_1Rep)
    #Branche 1.4.2.1
    if R == "1" :
        mourir(TGrandeAlleeTEvent2_1_1)
        #Branche 1.4.2.2 
    elif R == "2" :
        mourir(TGrandeAlleeTEvent2_1_2)     
def GrandeAllee3(): 
    ##Branche 1.5
    ecrire(TGrandeAlleeT3)
    R = question(TGrandeAlleeQEvent3,TGrandeAlleeQEvent3Rep)
    #Branche 1.5.1
    if R == "1" :
        ecrire(TGrandeAlleeTEvent3_1)
    #Branche 1.5.2
    elif R == "2" :
        ecrire(TGrandeAlleeTEvent3_2)
        Sherma["PV"] = perdre_pv(Sherma["PV"], 1)

#-------

def Sentier(): 
    # Branche 2
    ecrire(TSentierDesc)
    R = question(TSentierQEvent1, TSentierQEvent1Rep)
    if R == "1": 
        ecrire(TSentierQEvent1_1)
    R = question(TSentierQEvent2, TSentierQEvent2Rep)
    if R == "1":
        ecrire(TSentierQEvent2_1)
        Sherma["PV"] = perdre_pv(Sherma["PV"], 1)
        gagner_carapaces()
    elif R == "2":
        ecrire(TSentierQEvent2_2)
    R = question(TSentierQEvent3, TSentierQEvent3Rep)
    if R == "1": 
        Sherma["lacets_faits"] = False
    elif R == "2":
        Sentier1()
    Sherma["Emplacement"] = "Caverne"
def Sentier1():
    ecrire(TSentierQEvent3_1)
    i = 0
    while i < 100:
        sleep(1)
        i += randint(10, 30)
        if i >= 100:
            print("..... 100%")
            Sherma["lacets_faits"] = True
            break
        else: 
            print(f"..... {i}%")

def Caverne(): 
    # Branche 2
    ecrire(TCaverneDesc)
    R = question(TCaverneQEvent1, TCaverneQEvent1Rep)
    if R == "1": 
        # Branche 2.1 
        modif_agi(1) 
        ecrire(TCaverneQEvent1_1)
        if Sherma["lacets_faits"]:
            ## Branche 2.1.1
            Sherma["Emplacement"] = "Pierres"
        else: 
            # Branche 2.1.2
            ecrire(TCaverneEvent2_1)
            Caverne1()
    elif R == "2":
        # Branche 2.2
        Sherma["Emplacement"] = "Exterieur"
def Caverne1():
    # Branche 2.1.1
    ecrire(TCaverneEvent2_2)
    R = question(TCaverneQEvent3, TCaverneQEvent3Rep) 
    if R == "1":
        # Branche 2.1.1.1 
        ecrire(TCaverneQEvent3_1)
        Sherma["PV"] = perdre_pv(Sherma["PV"], 1)
        Sherma["Emplacement"] = "Pierres"
        
    elif R == "2":
        # Branche 2.1.1.2
        Caverne1_2()
def Caverne1_2():
    # Branche 2.1.1.2
    ecrire("""
Vous descendez prudemment jusqu'à atteindre votre chaussure.
""")
    i = 0
    while i < 100:
        sleep(1)
        i += randint(10, 30)
        if i >= 100:
            print(f"..... 100%")
            break
        else: 
            print(f"..... {i}%")
    ecrire(TCaverneQEvent3_2)
    R = question(TCaverneQEvent4, TCaverneQEvent4Rep)
    if R == "1": 
        ## Branche 2.1.1.2.1 = Branche 2.1.1
        ecrire(TCaverneQEvent4_1)
        Inv["Objets"] += ["Parchemin : Entre pierres et cordes"]
    elif R == "2":
        # Branche 2.1.1.2.2
        ecrire(TCaverneQEvent4_2)
        R = question(TCaverneQEvent5)
        if R == 1:
            ecrire(TCaverneQEvent5_1)
            modif_agi(-1)
            Sherma["Emplacement"] = "Pierres"
        elif R == 2:
            ecrire(TCaverneQEvent5_2)
            Sherma["PV"] = perdre_pv(Sherma["PV"], 1)
            Sherma["Emplacement"] = "Pierres"
        elif R == 3: 
            Sherma["Emplacement"] = "Pierres"
        ecrire("""
Vous décidez de reprendre l'ascension.""")
    elif R == "3":
        # Branche 2.1.1.2.3
        mourir(TCaverneQEvent3_3)

def Pierres(): 
    # Branche 2.1.1
    ecrire(TPierresDesc)
    modif_agi(1)
    R = question(TPierresQEvent1, TPierresQEvent1Rep)
    if R == "1":
        mourir(TPierresQEvent1_1)
    elif R == 2: 
        ecrire(TPierresQEvent1_2)
    Sherma["Emplacement"] = "GouffreDOs"

def Exterieur(): 
    ecrire(TExterieurDesc)
    R = question(TExterieurQEvent1, TExterieurQEvent1Rep)
    if R == "1": 
        # Branche 2.2.1
        mourir(TExterieurQEvent1_1)
    elif R == "2": 
        Exterieur1()
def Exterieur1():
    ecrire(TExterieurQEvent1_2)
    R = question(TExterieurQEvent2, TExterieurQEvent2Rep)
    if R == "1": 
        #Branche 2.2.2.1
        ecrire(TExterieurQEvent2_1)
        Sherma["PV"] = perdre_pv(Sherma["PV"], 1)
        sleep(1)
        while Sherma["PV"] > 0: 
            ecrire("""
Vous êtes persévérant et continuez à combattre.
""")
            Sherma["PV"] = perdre_pv(Sherma["PV"], 1)
            sleep(2)
    elif R == "2": 
        # Branche 2.2.2.2
        ecrire(TExterieurQEvent2_2)
        Sherma["PV"] = perdre_pv(Sherma["PV"], 1)
        R = question(TExterieurQEvent3, TExterieurQEvent3Rep)
        if R == "1": 
            mourir(TExterieurQEvent3_1)
        elif R == "2": 
            mourir(TExterieurQEvent3_2)

def GouffreDOs(): 
    ecrire(TGouffreDOsDesc)
    if "GouffreDOs" not in Sherma["salle_visitee"]:
        Sherma["salle_visitee"].append(Sherma["Emplacement"])
        ecrire(TGouffreDOsQEvent1_1)
        Sherma["Checkpoint"] = Sherma["Emplacement"]
        remplir_pv()
    R = question(TGouffreDOsQEvent1, TGouffreDOsQEvent1Rep)
    if R == "1":
        ecrire(TGouffreDOsQEvent1_1)
        Sherma["Checkpoint"] = Sherma["Emplacement"]
        remplir_pv()
    if R == "2": 
        ecrire(TGouffreDOsQEvent1_2)
        isQuittingShop = False
        while not(isQuittingShop):
            isQuittingShop = GouffreDOsShop()
    if R == "3":
        ecrire(TGouffreDOsQEvent1_3)
        Sherma["Emplacement"] = "Enigme1"
def GouffreDOsShop() -> bool:
    R = question(TGouffreDOsShopQEvent1, TGouffreDOsShopQEvent1Rep)
    if R == "1": 
        if Sherma["Inv"]["Perles"] >= 30:
            Sherma["Inv"]["Perles"] -= 30
            gagner_carapaces()
        else: 
            ecrire(TGouffreDOsShopQEvent1_PasAssezPerles)
    if R == "2":
        if Sherma["Inv"]["Arme"] == "Épée d'argent cristallisée": 
            ecrire(TGouffreDOsShopQEvent1_ADejaNouvelleArme)
        elif Sherma["Inv"]["Perles"] >= 140:
            Sherma["Inv"]["Perles"] -= 140
            Sherma["Inv"]["Arme"] = "Épée d'argent cristallisée"
            Sherma["Stats"]["Atk"] = 15
            ecrire(TGouffreDOsShopQEvent1_NouvelleArme)
        else: 
            ecrire(TGouffreDOsShopQEvent1_PasAssezPerles)
    if R == "3":
        if PerlesEtInventaireOK(70):
            Sherma["Inv"]["Perles"] -= 70
            Sherma["Inv"]["Objets"] += ["Clé de déchiffrement"]
            ecrire(TGouffreDOsShopQEvent1_CleDechiffrement)
    if R == "4":
        if PerlesEtInventaireOK(20):
            Sherma["Inv"]["Perles"] -= 20
            Sherma["Inv"]["Objets"] += ["Parfum"]
            ecrire(TGouffreDOsShopQEvent1_Parfum)
    if R == "5":
        if PerlesEtInventaireOK(30):
            Sherma["Inv"]["Perles"] -= 30
            Sherma["Inv"]["Objets"] += ["Orbe de vie"]
            ecrire(TGouffreDOsShopQEvent1_OrbeDeVie)
    if R == "6":
        ecrire(TGouffreDOsShopQEvent1_Exit)
        return True
    return False
def PerlesEtInventaireOK(perles: int) -> bool:
    EspaceOK = len(Sherma["Inv"]["Objets"]) < Sherma["Stats"]["TailleInv"]
    if not(EspaceOK):
        ecrire(TGouffreDOsShopQEvent1_InventoryFull)
    PerlesOK = Sherma["Inv"]["Perles"] >= perles
    if not(PerlesOK):
        ecrire(TGouffreDOsShopQEvent1_PasAssezPerles)

    return EspaceOK and PerlesOK

def Enigme1():
    given_code =  "0165 - 6423 - 6564 - 3f56 - ./§ù"
    code =        "=0156 - 3246 - 6654 - 365f - ./§ù="
    ecrire(f"""
Vous arrivez face à une stèle sur laquelle est présente le code suivant {given_code}
Vous trouvez un parchemin au pied de cette stèle. Vous observez un encadré et supposé qu'il faut résoudre une énigme à partir de se fameux code. 
Ce code doit être uniquement connu des résidents du coin ou des personnes les plus braves.""")
    R = question("""
Souhaitez-vous répondre à l'énigme ?
    1. Non, revenir sur vos pas
    2. Oui
Votre réponse : """, ("1", "2"))
    if R == "1":
        ecrire("Vous décidez de revenir sur vos pas")
        Sherma["Emplacement"] = "GouffreDOs"
    elif R == "2":
        ecrire(
"""Vous posez une pointe sur la feuille et instantanément un message apparait juste au dessus : 
Donnez le code ou partez d'ici !""")
        R = question("""
Vos choix 
    1. Partir
    Ou Donner le code
Votre réponse : """, ("1", code))
        if R == "1":
            ecrire("Vous abandonnez pour le moment et revenez au Gouffre d'Os.")
            Sherma["Emplacement"] = "GouffreDOs"
        if R == code:
            ecrire("Une porte s'ouvre ! Vous n'avez pas beaucoup de temps pour la franchir ainsi, vous y aller directement.")
            Sherma["Emplacement"] = "Enigme2"

def get_Niveau_points_arrivee(Niveau):
    Niveau_points_arrivee = []
    for x in range(len(Niveau)):
        for y in range(len(Niveau[x])):
            if Niveau[x][y] == POINT_ARRIVEE:
                Niveau_points_arrivee += [(x, y)]
    return Niveau_points_arrivee

def update_niveau(Niveau, Niveau_points_arrivee):
    Pistons = {PISTON_HAUT,
        PISTON_GAUCHE,
        PISTON_BAS, 
        PISTON_DROITE,

        PISTON_COLLANT_HAUT,
        PISTON_COLLANT_GAUCHE,
        PISTON_COLLANT_BAS,
        PISTON_COLLANT_DROITE,

        PISTON_BLOCK_HORIZONTAL,
        PISTON_BLOCK_VERTICAL,
        }
    for x in range(len(Niveau)):
        ligne = Niveau[x]
        for y in range(len(ligne)):
            if (x, y) in Niveau_points_arrivee and Niveau[x][y] == VIDE:
                Niveau[x][y] = POINT_ARRIVEE
            if Niveau[x][y] == POINT_ARRIVEE and (x, y) not in Niveau_points_arrivee:
                Niveau[x][y] = VIDE
            Case = Niveau[x][y]
            if Case not in Pistons:
                continue
            isPowered = isPistonPowered(x, y, Niveau)
            if isPowered: 
                piston_expansion(Niveau, x, y)
            else: 
                piston_retraction(Niveau, x, y)

def getIsLevelEnded(Niveau, Niveau_points_arrivee):
    # Le niveau est terminé si toutes les cases autour du point d'arrivée sont des blocs
    for coords in Niveau_points_arrivee:
        if Niveau[coords[0]][coords[1]] != BLOCK:
            return False
    return True  

def piston_retraction(Niveau, x, y):
    Case = Niveau[x][y]
    if Case == PISTON_BLOCK_HORIZONTAL:
        if y >= 1 and Niveau[x][y - 1] in {PISTON_GAUCHE_ETIREE, PISTON_COLLANT_GAUCHE_ETIREE}:
            PISTON_GAUCHE_retraction(Niveau, x, y)
        if y <= len(Niveau) - 2 and Niveau[x][y + 1] in {PISTON_DROITE_ETIREE, PISTON_COLLANT_DROITE_ETIREE}:
            PISTON_DROITE_retraction(Niveau, x, y)
    elif Case == PISTON_BLOCK_VERTICAL:
        if x >= 1 and Niveau[x - 1][y] in {PISTON_HAUT_ETIREE, PISTON_COLLANT_HAUT_ETIREE}:
            PISTON_HAUT_retraction(Niveau, x, y)
        if x <= len(Niveau) - 2 and Niveau[x + 1][y] in {PISTON_BAS_ETIREE, PISTON_COLLANT_BAS_ETIREE}:
            PISTON_BAS_retraction(Niveau, x, y)

def PISTON_HAUT_retraction(Niveau, x, y):
    before = None
    before2 = None
    if Niveau[x - 1][y] == PISTON_COLLANT_HAUT_ETIREE:
        piston = PISTON_COLLANT_HAUT
        before2 = VIDE
        if x >= 2:
            if Niveau[x - 2][y] != POINT_ARRIVEE:
                before = Niveau[x - 2][y]
    else:
        piston = PISTON_HAUT
        before = VIDE
        if x >= 2:
            before2 = Niveau[x - 2][y]
    Niveau[x][y] = piston
    Niveau[x - 1][y] = before
    if x >= 2:
        Niveau[x - 2][y] = before2
def PISTON_BAS_retraction(Niveau, x, y):
    before = None
    before2 = None
    if Niveau[x + 1][y] == PISTON_COLLANT_BAS_ETIREE:
        piston = PISTON_COLLANT_BAS
        before2 = VIDE
        if x <= len(Niveau) - 3:
            if Niveau[x - 2][y] != POINT_ARRIVEE:
                before = Niveau[x + 2][y]
    else:
        piston = PISTON_BAS
        before = VIDE
        if x <= len(Niveau) - 3:
            before2 = Niveau[x + 2][y]
    Niveau[x][y] = piston
    Niveau[x + 1][y] = before
    if x <= len(Niveau) - 3:
        Niveau[x + 2][y] = before2
def PISTON_GAUCHE_retraction(Niveau, x, y):
    before = VIDE
    before2 = VIDE
    if Niveau[x][y - 1] == PISTON_COLLANT_GAUCHE_ETIREE:
        piston = PISTON_COLLANT_GAUCHE
        before2 = VIDE
        if y >= 2:
            if Niveau[x - 2][y] != POINT_ARRIVEE:
                before = Niveau[x][y - 2]
    else:
        piston = PISTON_GAUCHE
        before = VIDE
        if y >= 2:
            before2 = Niveau[x][y - 2]
    Niveau[x][y] = piston
    Niveau[x][y - 1] = before
    if y >= 2:
        Niveau[x][y - 2] = before2
def PISTON_DROITE_retraction(Niveau, x, y):
    before = VIDE
    before2 = VIDE
    if Niveau[x][y + 1] == PISTON_COLLANT_DROITE_ETIREE:
        piston = PISTON_COLLANT_DROITE
        before2 = VIDE
        print(y, len(Niveau) - 3)
        if y <= len(Niveau) - 3:
            print( Niveau[x][y + 2] )
            if Niveau[x][y + 2] != POINT_ARRIVEE:
                before = Niveau[x][y + 2]
    else:
        piston = PISTON_DROITE
        before = VIDE
        if y <= len(Niveau) - 3:
            before2 = Niveau[x][y + 2]
    Niveau[x][y] = piston
    Niveau[x][y + 1] = before
    if y <= len(Niveau) - 3:
        Niveau[x][y + 2] = before2

def piston_expansion(Niveau, x, y):
    Case = Niveau[x][y]
    if (Case == PISTON_HAUT or Case == PISTON_COLLANT_HAUT) and x >= 1:
        PISTON_HAUT_expansion(Niveau, x, y)
    elif (Case == PISTON_GAUCHE or Case == PISTON_COLLANT_GAUCHE) and y >= 1:
        PISTON_GAUCHE_expansion(Niveau, x, y)
    elif (Case == PISTON_BAS or Case == PISTON_COLLANT_BAS) and x <= len(Niveau) - 2:
        PISTON_BAS_expansion(Niveau, x, y)
    elif (Case == PISTON_DROITE or Case == PISTON_COLLANT_DROITE) and y <= len(Niveau) - 2:
        PISTON_DROITE_expansion(Niveau, x, y)

def PISTON_HAUT_expansion(Niveau, x, y):
    Case = Niveau[x][y]
    Niveau[x][y] = PISTON_BLOCK_VERTICAL
    save = []
    for i in range(0, len(Niveau)):
        save += [Niveau[i][y]]
    i = x - 1
    while save[i] != VIDE and i > 0:
        if save[i] != POINT_ARRIVEE:
            Niveau[i - 1][y] = save[i]
        else:
            break
        i -= 1 
    if Case == PISTON_COLLANT_HAUT:
        Niveau[x-1][y] = PISTON_COLLANT_HAUT_ETIREE
    else:
        Niveau[x-1][y] = PISTON_HAUT_ETIREE
def PISTON_BAS_expansion(Niveau, x, y):
    Case = Niveau[x][y]
    Niveau[x][y] = PISTON_BLOCK_VERTICAL
    save = []
    for i in range(0, len(Niveau)): 
        save += [Niveau[i][y]]
    i = x + 1 
    while save[i] != VIDE and i < len(Niveau) - 1:
        if save[i] != POINT_ARRIVEE:
            Niveau[i + 1][y] = save[i] 
        else:
            break
        i += 1 
    if Case == PISTON_COLLANT_BAS:
        Niveau[x + 1][y] = PISTON_COLLANT_BAS_ETIREE
    else:
        Niveau[x + 1][y] = PISTON_BAS_ETIREE
def PISTON_GAUCHE_expansion(Niveau, x, y):
    Case = Niveau[x][y]
    Niveau[x][y] = PISTON_BLOCK_HORIZONTAL
    save = []
    for j in range(0, len(Niveau[x])):
        save += [Niveau[x][j]]
    j = y - 1
    while save[j] != VIDE and j > 0:
        if save[j] != POINT_ARRIVEE:
            Niveau[x][j - 1] = save[j]
        else:
            break
        j -= 1 
    if Case == PISTON_COLLANT_GAUCHE:
        Niveau[x][y - 1] = PISTON_COLLANT_GAUCHE_ETIREE
    else:
        Niveau[x][y - 1] = PISTON_GAUCHE_ETIREE
def PISTON_DROITE_expansion(Niveau, x, y):
    Case = Niveau[x][y]
    Niveau[x][y] = PISTON_BLOCK_HORIZONTAL
    save = []
    for j in range(0, len(Niveau[x])): 
        save += [Niveau[x][j]]
    j = y + 1 
    while save[j] != VIDE and j < len(Niveau) - 1:
        if save[j] != POINT_ARRIVEE:    
            Niveau[x][j + 1] = save[j]
        else:
            break
        j += 1
    if Case == PISTON_COLLANT_DROITE:
        Niveau[x][y + 1] = PISTON_COLLANT_DROITE_ETIREE
    else:
        Niveau[x][y + 1] = PISTON_DROITE_ETIREE

def isPistonPowered(x, y, Niveau):
    isPowered = False
    if x >= 1:
        if Niveau[x-1][y] == ENERGIE:
            isPowered = True
    if y >= 1:
        if Niveau[x][y-1] == ENERGIE:
            isPowered = True
    # On veut x inférieur strictement à len(Niveau) - 1
    if x <= len(Niveau) - 2:  
        if Niveau[x+1][y] == ENERGIE:
            isPowered = True
    # Idem pour y
    if y <= len(Niveau) - 2:
        if Niveau[x][y+1] == ENERGIE:
            isPowered = True     
    return isPowered

def init_value_OK(Niveau):
    Lettre_OK = []; Num_OK = []
    for i in range(len(Niveau)):
        Lettre_OK += [chr(97 + i)] # chr(97) = "A"
        Lettre_OK += [chr(65 + i)] # chr(65) = "a"
        Num_OK += [str(i+1)]
    return Lettre_OK, Num_OK

def placer_energie(R, Niveau):
    XYvalues = getXYValue(R)
    x_value, y_value = XYvalues[0], XYvalues[1]
    Case = Niveau[x_value][y_value]
    if Case != VIDE and Case != ENERGIE:
        print("La case choisie n'est pas vide.")
        return
    clear_energie(Niveau)
    if Case != ENERGIE:
        Niveau[x_value][y_value] = ENERGIE
    else:
        Niveau[x_value][y_value] = VIDE

def clear_energie(Niveau):
    for x in range(len(Niveau)):
        for y in range(len(Niveau[x])):
            if Niveau[x][y] == ENERGIE:
                Niveau[x][y] = VIDE

def getXYValue(R: str):
    if ord(R[0]) - 97 < 0:
        y_value = int(ord(R[0]) - 65)
    else: 
        y_value = int(ord(R[0]) - 97)
    x_value = int(R[1]) - 1 # Premier index à 1 et pas 0
    return x_value, y_value

def value_OK(R: str, Lettre_OK: list, Num_OK: list):

    if len(R) == 2:
        if R[0] in Lettre_OK and R[1] in Num_OK:
            return True
    return False

def afficher_niveau(Niveau: list):
    ch = "   "
    if len(Niveau) >= 10:
        ch += " "
    for i in range(len(Niveau)):
        ch += f"{chr(97 + i)}  "
    print(ch)
    
    for i in range(len(Niveau)):
        if len(Niveau) >= 10 and i < 9:
            space = " "
        else: 
            space = ""
        ligne = Niveau[i]
        print(f"{i+1}{space}| ", end="")
        for ch in ligne[:-1]:
            print(ch, end="  ")
        print(ligne[-1])
    print("\n")

def quitOrRestart(R):
    if R in ("q", "Q"):
        print("Merci d'avoir joué ! À bientôt.")
        exit()
    elif R in ("r", "R"):
        print("Redémarrage du niveau...")
        return True

def copy_level(Niveau):
    new_Niveau = []
    for x in range(len(Niveau)):
        new_ligne = []
        for y in range(len(Niveau[x])):
            new_ligne += [Niveau[x][y]]
        new_Niveau += [new_ligne]
    return new_Niveau

def play_level(Niveau):
    init_Niveau = copy_level(Niveau)
    values_OK =  init_value_OK(Niveau)
    Lettre_OK, Num_OK = values_OK[0], values_OK[1]

    levelIsDone = False 
    Niveau_points_arrivee = get_Niveau_points_arrivee(Niveau)
    while not(levelIsDone):
        afficher_niveau(Niveau)
        R = input("Placez un cube d'énergie : ")
        if quitOrRestart(R): 
            play_level(init_Niveau)
            return
        if value_OK(R, Lettre_OK, Num_OK):
            placer_energie(R, Niveau)
            update_niveau(Niveau, Niveau_points_arrivee)
            levelIsDone = getIsLevelEnded(Niveau, Niveau_points_arrivee)
        else: 
            print("Valeur incorrecte !")
    afficher_niveau(Niveau)

def Enigme2():
    
    # Le niveau doit être un carré
    # Niveau 1
    Niveau1 = [
               [VIDE, VIDE, VIDE, VIDE, VIDE],
               [VIDE, PISTON_DROITE, BLOCK, POINT_ARRIVEE, VIDE],
               [VIDE, VIDE, VIDE, VIDE, VIDE],
               [VIDE, PISTON_DROITE, BLOCK, POINT_ARRIVEE, VIDE],
               [VIDE, VIDE, VIDE, VIDE, VIDE],
               ]
    ecrire("""
Vous entrez dans une pièce circulaire où se trouve une stèle au centre. En vous approchant, un hologramme apparaît devant vous.
Bienvenue dans l'énigme 2 ! Placez de l'énergie pour activer les pistons faites glisser les blocs jusqu'au(x) point(s) d'arrivée(s).
Piston = 🠖   Piston collant = ⇢   Energie = 🗲   Bloc = ◼
Bonne chance !
----------------------------------------------
NIVEAU 1 : Placer un cube d'énergie autour du piston
Vous ne pouvez placer qu'un seul cube d'énergie à la fois.

""")
    print("\nBienvenue dans l'énigme 2 ! Placez de l'énergie pour activer les pistons faites glisser les blocs jusqu'au(x) point(s) d'arrivée(s).")
    print("Piston = 🠖   Piston collant = ⇢   Energie = 🗲   Bloc = ◼ \nBonne chance !")
    print("----------------------------------------------")
    print("NIVEAU 1 : Placer un cube d'énergie autour du piston")
    print("Vous ne pouvez placer qu'un seul cube d'énergie à la fois.\n") 
    play_level(Niveau1)
    ecrire("""
Félicitations ! Vous avez terminé le niveau 1""")

    Niveau2 = [
               [VIDE, VIDE, VIDE, VIDE, VIDE],
               [VIDE, PISTON_COLLANT_DROITE, POINT_ARRIVEE, BLOCK, VIDE],
               [VIDE, VIDE, VIDE, VIDE, VIDE],
               [VIDE,  PISTON_COLLANT_DROITE, POINT_ARRIVEE, BLOCK, VIDE],
               [VIDE, VIDE, VIDE, VIDE, VIDE],
               ]

    ecrire("""
----------------------------------------------
NIVEAU 2 : Utiliser un piston collant pour déplacer un bloc""")
    play_level(Niveau2)
    ecrire("""
Félicitations ! Vous avez terminé le niveau 2
----------------------------------------------
    
NIVEAU 3 : Combiner pistons normaux et collants, vous pouvez déclencher plusieurs pistons en même temps en plaçant un cube d'énergie entre eux.

""")
    Niveau3 = [
               [VIDE, VIDE, VIDE, VIDE, VIDE, VIDE, VIDE],
               [VIDE, VIDE, POINT_ARRIVEE, VIDE, VIDE, VIDE, VIDE],
               [VIDE, VIDE, BLOCK, VIDE, VIDE, VIDE, VIDE],
               [VIDE, VIDE, PISTON_HAUT, VIDE, VIDE, VIDE, VIDE],
               [VIDE, VIDE, VIDE, PISTON_COLLANT_DROITE, POINT_ARRIVEE, BLOCK, VIDE],
               [VIDE, VIDE, VIDE, VIDE, VIDE, VIDE, VIDE],
               [VIDE, VIDE, VIDE, VIDE, VIDE, VIDE, VIDE],
               ]
    play_level(Niveau3)
    ecrire("""
Félicitations ! Vous avez terminé le niveau 3
-----------------------------------------------
           
Niveau 4 : Double piston extender
""")
    Niveau4 = [
               [VIDE, VIDE, VIDE, VIDE, VIDE, VIDE, VIDE],
               [VIDE, VIDE, VIDE, VIDE, VIDE, VIDE, VIDE],
               [VIDE, VIDE, VIDE, VIDE, VIDE, VIDE, VIDE],
               [VIDE,  PISTON_DROITE, PISTON_DROITE, BLOCK, VIDE, POINT_ARRIVEE, VIDE],
               [VIDE, VIDE, VIDE, VIDE, VIDE, VIDE, VIDE],
               [VIDE, VIDE, VIDE, VIDE, VIDE, VIDE, VIDE],
               [VIDE, VIDE, VIDE, VIDE, VIDE, VIDE, VIDE],
               ]
    play_level(Niveau4)
    ecrire("""
Félicitations ! Vous avez terminé le niveau 4
------------------------------------------------
Niveau 5 : Prendre l'habitude
""")
    Niveau5 = [
               [VIDE, VIDE, VIDE, VIDE, VIDE, VIDE, VIDE],
               [VIDE, VIDE, VIDE, VIDE, VIDE, VIDE, VIDE],
               [VIDE, VIDE, VIDE, PISTON_BAS, VIDE, VIDE, VIDE],
               [VIDE,  PISTON_DROITE, BLOCK, VIDE, VIDE, VIDE, VIDE],
               [VIDE, VIDE, VIDE, POINT_ARRIVEE, VIDE, VIDE, VIDE],
               [VIDE, VIDE, VIDE, VIDE, VIDE, VIDE, VIDE],
               [VIDE, VIDE, VIDE, VIDE, VIDE, VIDE, VIDE],
               ]
    play_level(Niveau5)
    ecrire("""
Félicitations ! Vous avez terminé le niveau 5
------------------------------------------------
Niveau 6 : Combinaison avancée de pistons normaux et collants
""")
    Niveau6 = [
               [VIDE, PISTON_BAS, VIDE, VIDE, VIDE, VIDE, VIDE],
               [VIDE, PISTON_DROITE, BLOCK, BLOCK, VIDE, VIDE, VIDE],
               [VIDE, VIDE, VIDE, VIDE, VIDE, VIDE, VIDE],
               [VIDE, VIDE, VIDE, VIDE, VIDE, VIDE, VIDE],
               [VIDE, VIDE, PISTON_COLLANT_HAUT, PISTON_COLLANT_HAUT, VIDE, VIDE, VIDE],
               [VIDE, PISTON_DROITE, PISTON_COLLANT_HAUT, VIDE, VIDE, VIDE, VIDE],
               [VIDE, VIDE, VIDE, VIDE, VIDE, VIDE, VIDE],
               ]
    Niveau6[2][4] = POINT_ARRIVEE
    play_level(Niveau6)
    ecrire("""
Félicitations ! Vous avez terminé le niveau 6
------------------------------------------------
Niveau Final : Bonne chance !
""")
    Niveau_Final = [
        [VIDE, VIDE, VIDE, VIDE, PISTON_BAS, VIDE, VIDE],
        [PISTON_HAUT, VIDE, PISTON_DROITE, BLOCK, VIDE, VIDE, VIDE],
        [VIDE, PISTON_COLLANT_BAS, VIDE, PISTON_COLLANT_DROITE, VIDE, PISTON_COLLANT_BAS, VIDE],
        [VIDE, POINT_ARRIVEE, VIDE, VIDE, VIDE, POINT_ARRIVEE, VIDE],
        [VIDE, BLOCK, PISTON_DROITE, PISTON_COLLANT_DROITE, VIDE, VIDE, POINT_ARRIVEE],
        [VIDE, VIDE, VIDE, VIDE, PISTON_COLLANT_HAUT, BLOCK, VIDE],
        [VIDE, VIDE, VIDE, VIDE, PISTON_COLLANT_HAUT, PISTON_HAUT, VIDE],
    ]
    play_level(Niveau_Final)
    ecrire("""
Félicitations ! Vous avez terminé l'énigme 2 !""")
    Sherma["Emplacement"] = "CaverneCloches"

def CaverneCloches():
    BeteDesCloches = {
    "PV" : 120,
    "TpsAtk" : 12 + Sherma["Stats"]["Agi"]
    }
    ecrire(TCaverneClocheDesc)
    ecrire(TCaverneClocheApparition)
    while BeteDesCloches["PV"] > 40 :
        BeteDesCloches["PV"] += BeteDesClochesAtkNormale(BeteDesCloches["TpsAtk"])
    BeteDesCloches["TpsAtk"] = 6 + + Sherma["Stats"]["Agi"]
    ecrire(TCaverneClocheEnrage)
    while BeteDesCloches["PV"] > 0:
        BeteDesCloches["PV"] += BeteDesClochesAtkEnrage(BeteDesCloches["TpsAtk"])
    ecrire(TCaverneClocheVictoire)
    Sherma["a_finit"] = True
def BeteDesClochesAtkNormale(TpsAtk):
    Atk = randint(1,3)
    if Atk == 1 :
        return BeteDesClochesAtk1(TpsAtk)
    elif Atk == 2 :
        return BeteDesClochesAtk2(TpsAtk)
    else : 
        return BeteDesClochesAtk3(TpsAtk)
def BeteDesClochesAtkEnrage(TpsAtk):
    Atk = randint(1,5)
    if Atk == 1 :
        return BeteDesClochesAtk1(TpsAtk)
    elif Atk == 2 :
        return BeteDesClochesAtk2(TpsAtk)
    elif Atk == 3 : 
        return BeteDesClochesAtk3(TpsAtk)
    elif Atk == 4 :
        return BeteDesClochesAtk4(TpsAtk)
    else : 
        return BeteDesClochesAtk5(TpsAtk)
def BeteDesClochesAtk1(TpsAtk):
    ecrire(TCaverneClocheAtk1)
    R, TempsDeReponse = question(TCaverneClocheQAtk1,TCaverneClocheAtkRep,timer=True)
    if TempsDeReponse > TpsAtk :
        ecrire(TCaverneClocheLent)
        Sherma["PV"] = perdre_pv(Sherma["PV"], 1)
    elif R == "1" :
        ecrire(TCaverneClocheEsquive)
    elif R == "2" :
        ecrire(TCaverneClocheDegat)
        return -1*Sherma["Stats"]["Dgt"]
    elif R == "3" : 
        ecrire(TCaverneClocheRate)
        Sherma["PV"] = perdre_pv(Sherma["PV"], 1)
    return 0
def BeteDesClochesAtk2(TpsAtk):
    ecrire(TCaverneClocheAtk2)
    R, TempsDeReponse = question(TCaverneClocheQAtk2,TCaverneClocheAtkRep,timer=True)
    if TempsDeReponse > TpsAtk :
        ecrire(TCaverneClocheLent)
        Sherma["PV"] = perdre_pv(Sherma["PV"], 1)
    elif R == "1" :
        ecrire(TCaverneClocheDegat)
        return -1*Sherma["Stats"]["Dgt"]
    elif R == "2" :
        ecrire(TCaverneClocheEsquive)
    elif R == "3" : 
        ecrire(TCaverneClocheRate)
        Sherma["PV"] = perdre_pv(Sherma["PV"], 1)
    return 0
def BeteDesClochesAtk3(TpsAtk):
    ecrire(TCaverneClocheAtk3)
    R, TempsDeReponse = question(TCaverneClocheQAtk3,TCaverneClocheAtkRep,timer=True)
    if TempsDeReponse > TpsAtk :
        ecrire(TCaverneClocheLent)
        Sherma["PV"] = perdre_pv(Sherma["PV"], 1)
    elif R == "1" :
        ecrire(TCaverneClocheRate)
        Sherma["PV"] = perdre_pv(Sherma["PV"], 1)
    elif R == "2" :
        ecrire(TCaverneClocheDegat)
        return -1*Sherma["Stats"]["Dgt"]
    elif R == "3" : 
        ecrire(TCaverneClocheEsquive)
    return 0
def BeteDesClochesAtk4(TpsAtk):
    ecrire(TCaverneClocheAtk4)
    R, TempsDeReponse = question(TCaverneClocheQAtk4,TCaverneClocheAtkRep,timer=True)
    if TempsDeReponse > TpsAtk :
        ecrire(TCaverneClocheLent)
        Sherma["P2V"] = perdre_pv(Sherma["PV"], 2)
    elif R == "1" :
        ecrire(TCaverneClocheEsquive)
    elif R == "2" :
        Sherma["PV"] = perdre_pv(Sherma["PV"], 2)
        ecrire(TCaverneClocheRate)
    elif R == "3" : 
        ecrire(TCaverneClocheDegat)
        return -1*Sherma["Stats"]["Dgt"]
    return 0
def BeteDesClochesAtk5(TpsAtk):
    ecrire(TCaverneClocheAtk5)
    R, TempsDeReponse = question(TCaverneClocheQAtk5,TCaverneClocheAtkRep,timer=True)
    if TempsDeReponse > TpsAtk :
        ecrire(TCaverneClocheLent)
        Sherma["PV"] = perdre_pv(Sherma["PV"], 2)
    elif R == "1" :
        ecrire(TCaverneClocheDegat)
        return -1*Sherma["Stats"]["Dgt"]
    elif R == "2" :
        ecrire(TCaverneClocheRate)
        Sherma["PV"] = perdre_pv(Sherma["PV"], 2)
    elif R == "3" : 
        ecrire(TCaverneClocheEsquive) 
    return 0

def Fin():
    ecrire(TFin)
    input()
    quit()
##### FONCTIONS DE JEU

def script(salle: str):
    """
    Fonctionne mais on a pas le droit, rip ...
    for salle_iter in Salles.keys(): 
        if salle_iter == salle: 
            exec(salle + "()")
    """
    match salle:
        case "Tutoriel": Tutoriel()
        case "Entree": Entree()
        case "GrotteHumide" : GrotteHumide()
        case "GrandeAllee" : GrandeAllee()
        case "Sentier" : Sentier()
        case "Caverne" : Caverne()
        case "Pierres" : Pierres()
        case "Exterieur" : Exterieur()
        case "GouffreDOs" : GouffreDOs()
        case "Enigme1": Enigme1()
        case "Enigme2": Enigme2()
        case "Enigme3": pass
        # case "EnigmeTuringMachine: pass"
        case "CaverneCloches" : CaverneCloches()
        case "Fin" : Fin()
 
def triche():

    nbr_salle = []
    nom_salle = []
    i = 0
    question_triche = "Où souhaitez-vous aller ?\n"
    for salle in Salles:
        nbr_salle += [str(i)]
        nom_salle += [salle]
        question_triche += f"\t{i}. {Salles[salle]['NomAffichee']}\n"
        i += 1
    question_triche += "Votre réponse : "
    
    R = question(question_triche, nbr_salle)
    
    Sherma["Emplacement"] =  nom_salle[int(R)]


def jouer():
    Sherma["a_finit"] = False

    triche()

    while not(Sherma["a_finit"]):
        script(Sherma["Emplacement"])

    ecrire(TFINPartieA)
    input()
    quit()

###### JEU

jouer()
