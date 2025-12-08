##### Imports

from random import randint # Génère des nombres aléatoires (dans une portée donnée)
from time import sleep, time # Fait une pause du programme pendant un temps donné

#### Constantes de jeu 

vitesse_texte = 0 # 0.025 vitesse normale
vitesse_pause = 0.1 # 0.35 vitesse normale

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
- Pour utiliser un objet de votre inventaire au moment d'une question, indiquez le nom de l'objet à utiliser
- Vous pouvez a tout moment afficher votre inventaire en écrivant Inv et voir vos stats en écrivant Stats
Bon jeu !
"""

TEntreeDesc = """
    Le silence est dense. Une brume dorée se dissipe lentement autour de vous. Devant, se dresse une porte scellée, haute et fine, faite d’un métal chantant.
Chaque souffle de vent fait vibrer sa surface, produisant un écho lointain — comme un souvenir d’hymne oublié.
Derrière vous, les profondeurs. Devant, la Citadelle Mélodieuse, si haute que ses sommets se perdent dans les nuées. Vous savez qu’il faut atteindre son sommet — mais la voie reste voilée.
À votre gauche, un sentier s’enfonce dans les forêts sombres où se cache derrière un mont juxtaposé à la Citadelle.
À votre droite, un escalier de pierre descend vers des cavernes où l’eau résonne comme une harpe. Une lumière turquoise y palpite, irrégulière.
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

TFIN = """
La porte se ferme brutalement, il vous est impossible de revenir en arrière.
Vous pensez être sur le bon chemin, une 1ère étape vient d'être franchi et venez de comprendre les bases."""


### Stats de base
Armes = {
    "Baguette de métal" : 4,
    "Épée d'argent cristallisée" : 8

}

Inv = {"Arme": "Baguette de métal", 
        "Mélodies" : [],
        "Carapaces" : 0,
        "Objets" : [],
        "Perles" : 2000}

Stats = {
"TailleInv": 5,
"PV": 5,
"Cle_consultee" : 0,
"Pv_Max" : 5,
"Atk": 1,
"Agi" : 0,
"mort": 0
}

Sherma = {
"Inv" : Inv, 
"Stats" : Stats,
"Emplacement" : "Tutoriel",
"lacets_faits" : True,
"a_finit": False,
"Checkpoint" : "Tutoriel",
"salle_visitee" : []
}

Salles = {
    "Tutoriel" : {"NomAffichee" : "Tutoriel","Desc" : TEntreeDesc},
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
}

###### FONCTIONS GÉNÉRALE:

def question(text : str,rep : tuple) -> str:
    """
    Pose la question "text"
    Si les réponse est q ou Q : quitte le programme
    R est la Réponse que l'on attend
    """
    R = None
    tour = 0
    while R not in rep and R not in ("Q","q"):
        if R == "Suicide":
            perdre_pv(Sherma["Stats"]["PV"], Sherma["Stats"]["PV"])
        elif R == "Inv" :
            afficher_inv()
            R = None
        elif R == "Stats" :
            afficher_stats()
            R = None
        elif R in Sherma["Inv"]["Objets"]:
            utiliser_objet(R)
        if tour == 0 :
            ecrire(text)
        else : 
            ecrire(text, 0.005,0.01)
        R = input()
        tour +=1
    if R in ("q","Q") :
        quit()
    return R

def utiliser_objet(objet):
    if objet == "Parfum":
        rand = randint(1, 10)
        if rand == 1: ecrire(
"""Vous vous mettez du parfum ... Celui-ci arrive dans votre nez et vous pique le nez. Il Faudra faire attention la prochaine fois.""")
        else: ecrire(
"""Vous vous mettez du parfum sur vous ... Il sent bon ... Vous prennez le temps de respirer un bon coup ...""")
        return
    if objet == "Parchemin : Entre pierres et cordes":
        ecrire(
"""Vous lisez le parchemin, il vous indique comme un message, une inscription mystère ... Après moulte analyse, vous trouver : #§!lmp^¨$au5
S'agirait-il d'un mot de passe secret ? ... Cependant, vous vous rappelez d'un cours à l'Université des Reliques Lyriques (ou URL).
Dans celui-ci vous aviez joué pour la première fois avec votre instrument favori et compris la signification des symboles derrière ...
En vous rappelant de toutes ses informations, vous vous souvenez d'un endroit caché, vous vous rappelez alors du chemin pour y parvenir

>>> Chemin : https://creations.mtdv.me/articles/parchemin-entre-pierre-et-cordes""")
    if objet == "Clé de déchiffrement":
        ecrire(
"""1. La croissance et n'est que l'unique fruit inéluctable de l'évolution.
2. La vie n'est que retournement de situation.
3. Vous n'avez que décroissance de votre âge à travers les âges.
4. Les [êtres dont on ne doit pas prononcer le nom] écrivaient le mot 'jour' avec 'f' mais il n'y en avait tout autant que les grégoriens dans une année.
5. « Plus ça change, plus c’est la même chose. » — Jean-Baptiste Alphonse Karr

6. L'égalité doit encadrer l'infomation, quelle soit vraie ou fausse.
""")
    if objet == "Orbe de vie":
        ecrire("""
Vous utilisez une Orbe de vie, celle-ci à 3 chance sur 4 de vous soignez et 1 chance sur 100 de vous faire perdre 2 PV""")
        rand = randint(1, 100)
        if rand == 1: 
            perdre_pv(Sherma["Stats"]["PV"], 2)
        elif 1 < rand <= 25:
            ecrire("""
>>> L'orbe n'a pas eu d'effet sur vous;""")
        else:
            gagner_pv(Sherma["Stats"]["PV"], 1)
    ecrire(f"""
>>> Vous venez de consommer {objet}.""")
    Sherma["Inv"]["Objets"].remove(objet)
        
def question_temp(text : str,rep : tuple) -> tuple:
    TempsAvantRep = time()
    R = question(text,rep)
    TempsDeReponse = time() - TempsAvantRep
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
PV : {Sherma["Stats"]["PV"]}/{Sherma["Stats"]["Pv_Max"]}
Atk : {Sherma["Stats"]["Atk"]}
Agi : {Sherma["Stats"]["Agi"]}
---------
"""
    ecrire(TInv)

def afficher_inv():
    TStats = f"""
----------
Votre arme est {Sherma["Inv"]["Arme"]}
Vous avez {Sherma["Stats"]["PV"]}/{Sherma["Stats"]["Pv_Max"]} PV.
Vous possédez {Sherma["Inv"]["Carapaces"]} Fragments de Carapaces.
Vous possédez {Sherma["Inv"]["Perles"]} Perles.
Objets : {Sherma["Inv"]["Objets"]}
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
        ecrire("""

>>> Vous avez 4 fragments de Carapaces
Vous réunnissez vos fragments de carapaces et formez une caparaces !
Avec cette nouvelle carapace vous améliorez la vôtre et gagner en Point de vie maximum !
>>> Vos PV Max ont augmenté d'une unité""")
        Sherma["Stats"]["Pv_Max"] +=1 
        remplir_pv()

def calcul_degat():
    dgt = Armes[Sherma["Inv"]["Arme"]]
    dgt += Sherma["Stats"]["Atk"]*3
    return dgt


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
    Sherma["Stats"]["PV"] = Sherma["Stats"]["Pv_Max"]
    ecrire(f"\n>>> Vos PV se remplissent ! Vous avez désormais {Sherma['Stats']['Pv_Max']}/{Sherma['Stats']['Pv_Max']} PV\n")

def mourir(text_mort):
    ecrire(text_mort)
    ecrire("\n>>> Vous êtes mort.")
    Sherma["Stats"]["mort"] += 1
    if Sherma["Stats"]["mort"] < 10:
        R = question("""
Voulez-vous recommencer le jeu ?
    1. Oui
    2. Non
Votre réponse : """, ("1", "2"))
        if R == "1": 
            
            if Sherma["Checkpoint"] == "Tutoriel":
                Sherma["Stats"]["PV"] = 5
                Inv = {"Arme": "Baguette de métal", 
            "Mélodies" : [],
            "Carapaces" : 0,
            "Objets" : [],
            "Perles" : 0
                }

                Stats = {
                "Pv_Max" : 5,
                "Atk": 10,
                "Agi" : 0,
                }
                Sherma["Stats"] = Stats
                Sherma["Inv"] = Inv
                Sherma["Emplacement"] = "Tutoriel"
            else :
                remplir_pv()
                Sherma["Inv"]["Objets"] = [valeur for valeur in Sherma["Inv"]["Objets"] if valeur != "Parfum"]
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
        Sherma["Stats"]["PV"] = perdre_pv(Sherma["Stats"]["PV"], 1)
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
        Sherma["Stats"]["PV"] = perdre_pv(Sherma["Stats"]["PV"], 1)
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
            Sherma["Stats"]["PV"] = perdre_pv(Sherma["Stats"]["PV"], 1)
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
    Sherma["Stats"]["PV"] = perdre_pv(Sherma["Stats"]["PV"], 1)
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
        Sherma["Stats"]["PV"] = perdre_pv(Sherma["Stats"]["PV"], 1)

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
        Sherma["Stats"]["PV"] = perdre_pv(Sherma["Stats"]["PV"], 1)
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
        Sherma["Stats"]["PV"] = perdre_pv(Sherma["Stats"]["PV"], 1)
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
        Sherma["Inv"]["Objets"] += ["Parchemin : Entre pierres et cordes"]
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
            Sherma["Stats"]["PV"] = perdre_pv(Sherma["Stats"]["PV"], 1)
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
        Sherma["Stats"]["PV"] = perdre_pv(Sherma["Stats"]["PV"], 1)
        sleep(1)
        while Sherma["Stats"]["PV"] > 0: 
            ecrire("""
Vous êtes persévérant et continuez à combattre.
""")
            Sherma["Stats"]["PV"] = perdre_pv(Sherma["Stats"]["PV"], 1)
            sleep(2)
    elif R == "2": 
        # Branche 2.2.2.2
        ecrire(TExterieurQEvent2_2)
        Sherma["Stats"]["PV"] = perdre_pv(Sherma["Stats"]["PV"], 1)
        R = question(TExterieurQEvent3, TExterieurQEvent3Rep)
        if R == "1": 
            mourir(TExterieurQEvent3_1)
        elif R == "2": 
            mourir(TExterieurQEvent3_2)

def GouffreDOs(): 
    if "GouffreDOs" not in Sherma["salle_visitee"]:
        Sherma["salle_visitee"].append(Sherma["Emplacement"])
        ecrire("""
Les bancs vous permette de regagner entièrement votre vie et de sauvegarder votre progression.""")
        Sherma["Checkpoint"] = Sherma["Emplacement"]
        remplir_pv()
    R = question("""
Vous arrivez dans le village, que voulez-vous faire ?
    1. Vous reposer sur le banc
    2. Aller voir le marchand
    3. Continuer votre chemin
Votre réponse : """, ("1", "2", "3"))
    if R == "1":
        ecrire("""
Vous régénérez entièrement votre vie, vous sauvegardez votre progression.""")
        Sherma["Checkpoint"] = Sherma["Emplacement"]
        remplir_pv()
    if R == "2": 
        ecrire("""
Vous vous dirigez vers le marchand et commencez à converser avec lui. Vous avez du mal à le comprendre de part son dialecte.
Bnoujor et Benuienve j'ia pilen d'atlicres puor vous ! """)
        isQuittingShop = False
        while not(isQuittingShop):
            isQuittingShop = GouffreDOsShop()
    if R == "3":
        ecrire("""
Vous continuez vers une salle sombre""")
        Sherma["Emplacement"] = "Enigme1"
def GouffreDOsShop() -> bool:
    R = question("""
Vous décidez de lire les étiquettes: 
    1. Fragment de carapaces [30 perles]
    2. Épée d'argent cristallisée [140 perles]
    3. Clé de déchiffrement [70 perles]
    4. Parfum [20 perles]
    5. Orbe de vie [30 perles]
    6. Partir 
Votre réponse : """, ("1", "2", "3", "4", "5", "6"))
    if R == "1": 
        if Sherma["Inv"]["Perles"] >= 30:
            Sherma["Inv"]["Perles"] -= 30
            gagner_carapaces()
        else: 
            ecrire("""
>>> Vous n'avez pas assez de perles.""")
    if R == "2":
        if Sherma["Inv"]["Arme"] == "Épée d'argent cristallisée": 
            ecrire("""
>>> Vous avez déjà cette arme !""")
        elif Sherma["Inv"]["Perles"] >= 140:
            Sherma["Inv"]["Perles"] -= 140
            Sherma["Inv"]["Arme"] = "Épée d'argent cristallisée"
            Sherma["Stats"]["Atk"] = 15
            ecrire("""
>>> Vous obtenez l'Épée d'argent cristallisée.""")
        else: 
            ecrire("""
>>> Vous n'avez pas assez de perles.""")
    if R == "3":
        if PerlesEtInventaireOK(70):
            Sherma["Inv"]["Perles"] -= 70
            Sherma["Inv"]["Objets"] += ["Clé de déchiffrement"]
            ecrire("""
>>> Vous obtenez une clé de déchiffrement.""")
    if R == "4":
        if PerlesEtInventaireOK(20):
            Sherma["Inv"]["Perles"] -= 20
            Sherma["Inv"]["Objets"] += ["Parfum"]
            ecrire("""
>>> Vous obtenez un parfum, celui-ci à une très bonne odeur.""")
    if R == "5":
        if PerlesEtInventaireOK(30):
            Sherma["Inv"]["Perles"] -= 30
            Sherma["Inv"]["Objets"] += ["Orbe de vie"]
            ecrire("""
>>> Vous obtenez une orbe de vie, celle-ci vous confère la possibilité de vous régénérer quand vous le souhaitez.""")
    if R == "6":
        ecrire("""
Vous sortez de la boutique...""")
        return True
    return False
def PerlesEtInventaireOK(perles: int) -> bool:
    EspaceOK = len(Sherma["Inv"]["Objets"]) < Sherma["Stats"]["TailleInv"]
    if not(EspaceOK):
        ecrire("""
>>> Votre inventaire est plein.""")
    PerlesOK = Sherma["Inv"]["Perles"] >= perles
    if not(PerlesOK):
        ecrire("""
>>> Vous n'avez pas assez de perles.""")

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

def CaverneCloches():
    BeteDesCloches = {
    "PV" : 120,
    "TpsAtk" : 16
    }
    ecrire(TCaverneClocheDesc)
    ecrire(TCaverneClocheApparition)
    while BeteDesCloches["PV"] > 40 :
        BeteDesCloches["PV"] -= BeteDesClochesAtkNormale(BeteDesCloches["TpsAtk"])
        print(BeteDesCloches["PV"])
    BeteDesCloches["TpsAtk"] = 8.5
    ecrire(TCaverneClocheEnrage)
    while BeteDesCloches["PV"] > 0:
        BeteDesCloches["PV"] -= BeteDesClochesAtkEnrage(BeteDesCloches["TpsAtk"])
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
    R, TempsDeReponse = question_temp(TCaverneClocheQAtk1,TCaverneClocheAtkRep)
    if TempsDeReponse > TpsAtk :
        ecrire(TCaverneClocheLent)
        Sherma["Stats"]["PV"] = perdre_pv(Sherma["Stats"]["PV"], 1)
    elif R == "1" :
        ecrire(TCaverneClocheEsquive)
    elif R == "2" :
        ecrire(TCaverneClocheDegat)
        return calcul_degat()
    elif R == "3" : 
        ecrire(TCaverneClocheRate)
        Sherma["Stats"]["PV"] = perdre_pv(Sherma["Stats"]["PV"], 1)
    return 0
def BeteDesClochesAtk2(TpsAtk):
    ecrire(TCaverneClocheAtk2)
    R, TempsDeReponse = question_temp(TCaverneClocheQAtk2,TCaverneClocheAtkRep)
    if TempsDeReponse > TpsAtk :
        ecrire(TCaverneClocheLent)
        Sherma["Stats"]["PV"] = perdre_pv(Sherma["Stats"]["PV"], 1)
    elif R == "1" :
        ecrire(TCaverneClocheDegat)
        return calcul_degat()
    elif R == "2" :
        ecrire(TCaverneClocheEsquive)
    elif R == "3" : 
        ecrire(TCaverneClocheRate)
        Sherma["Stats"]["PV"] = perdre_pv(Sherma["Stats"]["PV"], 1)
    return 0
def BeteDesClochesAtk3(TpsAtk):
    ecrire(TCaverneClocheAtk3)
    R, TempsDeReponse = question_temp(TCaverneClocheQAtk3,TCaverneClocheAtkRep)
    if TempsDeReponse > TpsAtk :
        ecrire(TCaverneClocheLent)
        Sherma["Stats"]["PV"] = perdre_pv(Sherma["Stats"]["PV"], 1)
    elif R == "1" :
        ecrire(TCaverneClocheRate)
        Sherma["Stats"]["PV"] = perdre_pv(Sherma["Stats"]["PV"], 1)
    elif R == "2" :
        ecrire(TCaverneClocheDegat)
        return calcul_degat()
    elif R == "3" : 
        ecrire(TCaverneClocheEsquive)
    return 0
def BeteDesClochesAtk4(TpsAtk):
    ecrire(TCaverneClocheAtk4)
    R, TempsDeReponse = question_temp(TCaverneClocheQAtk4,TCaverneClocheAtkRep)
    if TempsDeReponse > TpsAtk :
        ecrire(TCaverneClocheLent)
        Sherma["P2V"] = perdre_pv(Sherma["Stats"]["PV"], 2)
    elif R == "1" :
        ecrire(TCaverneClocheEsquive)
    elif R == "2" :
        Sherma["Stats"]["PV"] = perdre_pv(Sherma["Stats"]["PV"], 2)
        ecrire(TCaverneClocheRate)
    elif R == "3" : 
        ecrire(TCaverneClocheDegat)
        return calcul_degat()
    return 0
def BeteDesClochesAtk5(TpsAtk):
    ecrire(TCaverneClocheAtk5)
    R, TempsDeReponse = question_temp(TCaverneClocheQAtk5,TCaverneClocheAtkRep)
    if TempsDeReponse > TpsAtk :
        ecrire(TCaverneClocheLent)
        Sherma["Stats"]["PV"] = perdre_pv(Sherma["Stats"]["PV"], 2)
    elif R == "1" :
        ecrire(TCaverneClocheDegat)
        return calcul_degat()
    elif R == "2" :
        ecrire(TCaverneClocheRate)
        Sherma["Stats"]["PV"] = perdre_pv(Sherma["Stats"]["PV"], 2)
    elif R == "3" : 
        ecrire(TCaverneClocheEsquive) 
    return 0
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
        case "Enigme2": CaverneCloches() # TO DO
        case "Enigme3": CaverneCloches() # TO DO
        # case "EnigmeTuringMachine: pass"
        case "CaverneCloches" : CaverneCloches()
    
    if salle not in Sherma["salle_visitee"]: Sherma["salle_visitee"].append(Sherma["Emplacement"])

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
    print("\n"*1000)
    triche()

    while not(Sherma["a_finit"]):
        script(Sherma["Emplacement"])

    ecrire(TFIN)
    input()
    quit()

###### JEU

jouer()
