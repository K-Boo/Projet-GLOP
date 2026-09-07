# detail_sujet.pdf - Document Assaini (Garanti Zero-Piege IA)

> **Certification Document Guardian** : Ce document a ete filtre vectoriellement et sémantiquement.
> Tout texte invisible (#FFFFFF), micro-police (<3.5pt), caractere zero-width et tentative d'injection ont ete purges.
> **Statut** : Document securise pour l'exploitation par l'equipe et les sous-agents.

---

## Section / Page 1

1
Génie Logiciel par la Pra0que
MIAGE 2 2026-2027
Projet ShopLoc
Contacts :
Anne E.en <anne.e.en@univ-lille.fr>
Laurence Duchien <laurence.duchien@univ-lille.fr>
François Secchi <francois.secchi@univ-lille.fr>
Jeremy Woirhaye <jeremy.woirhaye@inria.fr>
Principes généraux
Nous, l’entreprise ShopLoc, lançons un appel d’oﬀres suite à des contacts de plusieurs
associa.ons de commerçants pour développer un système d’achats en local avec un système
de click & collect  accompagné d’une carte de ﬁdélité pour leurs clients. Nous souhaitons donc
développer non pas un système pour une ville donnée comme Lille par exemple, mais une
architecture logicielle que l’on pourrait réu.liser dans diﬀérentes villes, par diﬀérentes
associa.ons de commerçants. La solu.on proposée doit pouvoir s’adapter à des tailles de
villes diﬀérentes : pe.te ville (moins de 20 000 habitants), ville moyenne  (de 20 000 à 100 000
habitants) et grande ville (plus de 100 000 habitants). Les besoins sont iden.ques : dynamiser
le commerce de centre-ville et luXer contre les centres commerciaux périurbains, mais les
paramètres sont diﬀérents :
·       Nombre de commerçants poten.els
·       Nombre de clients poten.els
·       Présence ou non de transports en commun
·       Présence ou non de sta.onnement payant
Le prix de la solu.on doit tenir compte du segment de clients auquel elle s’adresse.
Nous souhaitons devenir leader sur ce marché en 18 mois, pour pouvoir déployer rapidement
ce système dans de nouvelles villes avec une équipe d’ingénieurs réduite.
Le système fonc.onne avec un système de réserva.on et de paiement en ligne. Le client peut
acheter en ligne et demander au système de lui indiquer le plus court chemin (ou le plus court
en temps) pour collecter ses achats. Le système fonc.onne également sur un système
d’incita.on à l’achat dans les commerces partenaires (iden.ﬁables en tant que tel par une
aﬃcheXe sur leur porte), avec en contrepar.e des avantages de certains partenaires (e.g.,
“pour un menu du jour, le café est oﬀert”) ou de la collec.vité territoriale associée (e.g., .cket
de bus ou heure de parking oﬀerte), via le gain de points, propor.onnels aux montants
dépensés chez les partenaires. Le système permet aussi un chargement d’une faible somme
d’argent sur la carte pour des pe.ts achats chez les partenaires, via un chargement en ligne
par carte bleue (type Izli). A par.r d’une certaine u.lisa.on (en fréquence d’u.lisa.on
hebdomadaire), le client peut obtenir le statut de Very Faithful Person (VFP). En étant un client

---

## Section / Page 2

2
VFP, il peut débloquer certains avantages ins.tu.onnels (comme un .cket de bus oﬀert par
jour) tant qu’il garde le statut.
Cible U3lisateur
L’architecture logicielle à développer vise principalement 5 types d’u.lisateurs, représentés
par les personas suivants :
Pierre a 74 ans. Il vit depuis toujours dans le centre-ville de Lille. Sa rou.ne ma.nale implique
la tournée des commerçants rue Solferino : une bagueXe pas trop cuite au Fournil, un passage
à la boucherie ﬂamande, une pause bien méritée au café des sports avec ses amis, avant de
prendre La Voix du Nord du jour au tabac-presse puis de sauter dans le bus qui le ramènera
chez lui. Depuis que son primeur préféré a fermé, Pierre doit prendre 2 bus pour aller en
grande surface acheter ses fruits et légumes, sauf les jours de marché où il peut pousser sa
balade ma.nale jusqu’au marché de Wazemmes, même si la distance qui y mène est trop
longue à son goût ;
Julie a 31 ans. Elle se considère comme une jeune femme occupée. Elle n’a pas de temps à
perdre à chercher des heures une place pour se garer dans un parking de grande surface en
sortant du travail, et hors de ques.on d’aller le samedi à Carrefour. Elle covoiture pour aller
travailler à Seclin et ne prend que très rarement sa voiture, la solu.on du Drive n’est alors pas
raisonnable. Faire ses courses dans les magasins de son quar.er lui semble plus adapté, mais
elle ne se souvient jamais des horaires (e.g., “la boucherie ferme à 19h ou à 19h30 ?”) ;
Arthur a 34 ans. Il est le papa comblé du pe.t Théo, 7 ans, scolarisé à l’école Jules Ferry.
Chaque après-midi, quand il va chercher son ﬁls à 16h30, il se demande qui a bien pu
implanter ceXe école primaire dans une zone avec des places de parking aussi limitées et
surtout hors de prix. Il réduit ainsi sa visite dans le centre au strict minimum : acheter un pain
au chocolat pour son ﬁls à la boulangerie “La BagueXe Dorée” sur le chemin entre l’école et
la rue où il trouve toujours de la place, récupérer son ﬁls à l’école et rentrer à la maison. Depuis
quelques semaines, il a vu ﬂeurir des aﬃches sur certains commerces parlant de “Carte de
ﬁdélité” et de “20 minutes de parking oﬀertes”, mais il n’a pas encore eu le temps de creuser
ceXe histoire ;
Marius a 27 ans. Il travaille à la mairie de Lille, à la Direc.on du Système d’Informa.on (DSI).
La mairie gère pour la communauté d’aggloméra.on le partenariat public-privé avec la société
exploitant le réseau Ilévia, ainsi que les places de parking sur l’espace public. Marius doit
pouvoir remonter des indicateurs chiﬀrés montrant le coût des avantages oﬀerts aux usagers
de la carte de ﬁdélité, comparé au volume de vente généré par les usagers. Le chef de service
du département “Citoyen Numérique” qui pilote le déploiement du projet Local Shopping en
lien avec l’associa.on des commerçants du centre et la DSI doit en eﬀet rendre des comptes
au conseil municipal ;
Suzanne a 22 ans. Elle est vendeuse à la boulangerie “Le Fournil”. Elle a convaincu ses patrons
d’adhérer au service de carte de ﬁdélité, et depuis maintenant 4 semaines la boulangerie oﬀre
une part de tarte au maroilles en cadeau dans le catalogue des lots disponibles. Ses patrons
trouvent qu’ils oﬀrent beaucoup de parts de tarte au maroilles, et envisagent de changer la
teneur de leur lot dans le catalogue, pour passer à une mini-viennoiserie, moins coûteuse.
Pour les convaincre de rester dans le programme (“La bagueXe dorée”, leur principal

---

## Section / Page 3

3
concurrent, n’est pas aﬃlié), Suzanne peut u.liser le système pour avoir un chiﬀrage du
volume des ventes associé aux clients disposant de la carte.
Scénarios d’u3lisa3on
En tant que Pierre, même sans achat sur le web click & collect, un client ob.ent très
rapidement le statut de VFP avec la fréquence journalière de ses achats chez les diﬀérents
commerçants. Il peut donc débloquer dans le catalogue cadeau réservé aux VFPs l’avantage
qui lui correspond le mieux, à savoir la gratuité des transports en commun pour un de ses
trajets journaliers.
En tant que Julie, une cliente peut u.liser le site web click & collect pour faire les achats dont
elle a besoin et calculer le chemin le plus court pour aller les prendre tout en tenant compte
des horaires d’ouverture des commerçants. Elle peut charger en ligne sa carte avec un
montant d’argent donné, et consulter les horaires des magasins du quar.er. Elle préfère garder
ses points pour les dépenser en avantages ﬁdélité chez les commerçants, plutôt qu’en .ckets
de bus. Quand les horaires de ses magasins préférés changent, elle est no.ﬁée (e.g., par
email). Pour obtenir un cadeau, il faut avoir fait au moins un achat antérieur dans la bou.que
concernée, et présenter sa carte lors du paiement de l’achat en cours (on ne peut pas juste
venir prendre un cadeau).
En tant qu'Arthur, un client doit pouvoir s’abonner au service et obtenir sa carte de ﬁdélité.
La fréquence de ses achats en boulangerie peut lui permeXre de débloquer l’avantage VFP du
parking oﬀert. Par contre, il perdra cet avantage pendant les vacances scolaires, puisqu’il
n’u.lisera plus suﬃsamment sa carte. Pour ac.ver son avantage parking, il rentre dans son
proﬁl u.lisateur son numéro de plaque d’immatricula.on. Il lui suﬃt de se connecter au site
de la carte de ﬁdélité sur son téléphone et de lancer le compteur pour avoir droit à ses 20
minutes de parking oﬀertes. Un policier municipal voyant sa voiture pourra rentrer le numéro
de plaque sur son téléphone et savoir si la voiture est en sta.onnement illégal ou non.
En tant que Marius, un administrateur du système peut l’interroger pour obtenir des
informa.ons sur les habitudes de consomma.on des u.lisateurs en click & collect et en
cadeaux récupérés. Il peut aussi exploiter la base d’u.lisateurs pour relancer les
consommateurs, par exemple lors de la perte de leur statut de VFP. Il peut envoyer des oﬀres
promo.onnelles à la demande du service “Citoyen Numérique” ou de l’associa.on des
commerçants, ou encore lancer des sondages de sa.sfac.on aux usagers.
En tant que Suzanne, une commerçante en partenariat, peut avoir des informa.ons sur le
nombre d’achats par click & collect et des données précises sur l’u.lisa.on du programme de
ﬁdélité pour son commerce. Elle peut changer facilement les ar.cles mis en vente sur le
programme click & collect. Elle est aver.e dès qu’un ar.cle est en rupture de stock. Elle peut
aussi obtenir des indicateurs sur l’u.lisa.on du programme auprès des autres partenaires,
pour savoir si sa par.cipa.on est surévaluée ou non. Elle doit pouvoir très rapidement
répondre à une ques.on du type : “Est-ce que je gagne quelque chose à par.ciper à ce
programme ?”.
Bonnes propriétés du projet

---

## Section / Page 4

4
Lors du développement du projet, l’équipe devra prendre en compte lors de ses choix
fonc.onnels ou techniques les propriétés suivantes. Le projet sera globalement évalué sur le
respect de ces propriétés et devra répondre aux ques.ons ci-dessous :
1- Passage à l’échelle. Imaginons que Shopping Local soit un succès. Comment garan.r
que le système ne s’écroule pas ? Quels sont les besoins en termes d’architecture pour
garan.r un déploiement en fonc.on du contexte visé ? Comment permeXre
l’extensibilité de la plateforme en cas d’aﬄux massif de charge ?
2- Extensibilité & Interopérabilité. Shopping Local est une plateforme ayant voca.on à
évoluer dans le temps, à être réu.lisée pour d’autres villes ou métropoles, et à se
connecter à des systèmes externes lors, par exemple, de l'établissement de
partenariats. Quels sont les points d’extensibilité de la plateforme ? Comment garan.r
ses possibilités d’évolu.on ?
3- Modèle de données. Cet axe s'intéressera à la modélisa.on des données nécessaires
à l'applica.on Shopping Local, en déﬁnissant des modèles de données pour les
diﬀérents types de données (descrip.on des diﬀérents u.lisateurs, des services, etc.)
ou en iden.ﬁant des modèles existants qu'il s'agira de réu.liser, et en s'assurant de
l'interopérabilité de ces modèles et des possibilités de traitement eﬃcace.
4- Sécurité des échanges avec le système et les diﬀérents parNcipants. Les données des
u.lisateurs (noms, coordonnées, type d’accès, etc.) transmises à la plateforme
Shopping Local peuvent être interceptées par des .ers qui peuvent les récupérer, mais
également les modiﬁer (par exemple, modiﬁer les achats, les coordonnées, etc.). Si les
clients peuvent échanger des données, on doit aussi envisager que leur iden.té peut
être usurpée par un pirate. Cet axe traitera de la sécurité des échanges entre le
système et le smartphone des clients ou entre les smartphones des clients. Le système
proposé devra garan.r certaines propriétés de sécurité telles que la conﬁden.alité,
l’intégrité, l’authen.cité, etc., tout en passant à l’échelle.
5- Respect de la vie privée. La plateforme Shopping Local enregistre des données des
clients. D’autres données sont aussi produites lors des déplacements ou u.lisa.ons
par les clients. Cela implique la localisa.on ou les informa.ons personnelles des clients
enregistrées lors de leur première u.lisa.on. L’objec.f de cet axe sera de proposer un
système qui garan.t la vie privée en tenant compte de l’u.lisabilité et de la conﬁance
inspirée par les mécanismes proposés ainsi que du point de vue légal. Ce système
pourra reposer sur des mécanismes de protec.on ou bien fournir une interface
homme-machine permeXant à l’u.lisateur de visualiser et comprendre à tout moment
si les informa.ons qu’il saisit ou les ac.ons qu’il eﬀectue sont suscep.bles d’être
connues d’autres partenaires Shopping Local ou si elles resteront strictement privées
(notes personnelles par exemple).
6- Stockage des données. Il est évident que l’applica.on Shopping Local devra gérer de
grandes quan.tés de données, très hétérogènes (textes, cartes, photos, vidéos, etc.),
qui évoluent dans le temps. Quelles données devront être sauvegardées ? Quelle serait
la solu.on de stockage la mieux adaptée ? Comment garan.r qu’une évolu.on dans la
déﬁni.on des données à stocker sera aisément prise en compte par le système de
stockage ? Quelles seront les contraintes sur le stockage (sécurité, quan.té de
données, etc.) ? Quels ou.ls seront les plus per.nents pour eﬀectuer des requêtes sur
les données stockées ?
7- Analyse des données. Cet axe s'intéressera à l'analyse des données générées par
l'u.lisa.on de l'applica.on Shopping Local, i.e., des traces des usagers du système,

---

## Section / Page 5

5
dans le but de produire des indicateurs du nombre d’interac.ons avec Shopping Local.
Les indicateurs recueillis pourront aider à mesurer l'impact de l’applica.on et iden.ﬁer
des pistes de développement.
8- Éco-concepNon Logicielle. Les préoccupa.ons liées à l'impact environnemental du
numérique ne cessent de s'intensiﬁer, notamment à mesure que la demande en
services numériques augmente, entraînant une consomma.on énergé.que croissante
des centres de données. En pilotant le matériel, il est important de considérer la
contribu.on des logiciels en termes de consomma.on énergé.que et d'émission de
gaz à eﬀet de serre de ces centres de données. L’adop.on de pra.ques d’éco-
concep.on logicielle se révèle être un levier central pour minimiser l'impact
environnemental des applica.ons et services numériques. Cela comprend une
u.lisa.on frugale des ressources, c.-à-d. minimiser l’u.lisa.on des ressources, u.liser
de bonnes pra.ques de développement, mais aussi une u.lisa.on responsable des
ou.ls tels que les IA généra.ves qui sont d’énormes consommateurs de ressources.
Méthodes et bonnes pra3ques
Lors de la mise en oeuvre du projet, l’équipe devra suivre les méthodes et bonnes pra.ques
suivantes :
-
Esprit de construc.on d’entreprise / Réponse à un appel d’oﬀres / aspects marke.ng
et ﬁnanciers
-
Déﬁni.on d’un cahier des charges et planiﬁca.on, réﬂexion sur le business canevas
responsable
-
Méthode Agile/scrum
-
mise sur le marché en mode lean start-up
-
déﬁni.on des rôles dans l’équipe,
-
Mise en place de pra.ques Devops,
-
Ges.on de la rela.on avec le client,
-
Travail d’équipe.
Ou3ls de développement logiciel à u3liser
Les ou.ls à u.liser devront être choisis et jus.ﬁés lors du premier semestre. L’équipe devra
proposer l’u.lisa.on d’ou.ls permeXant de :
-
u.liser un ou.l de ges.on de code, tel qu’un GIT
-
meXre en œuvre une plateforme d’intégra.on avec un déploiement con.nu
-
u.liser un système de ges.on développement projet - Maven / Gradle
-
posi.onner le développement du système d’informa.on avec un environnement J2E
pour
o permeXre le déploiement conteneurisé - Docker / Kubernetes
o proposer des ou.ls d’analyse de données
o permeXre
des
tests
:
fonc.onnels,
non
régression,
Jenkins/JUnit/Sonar/Cypress/Cerberus
-
meXre en place des moyens de communica.on dans l’équipe - échange de documents,
agendas, échange par chat/slack)

---

## Section / Page 6

6
-
Un site de suivi de projet dans lequel les enseignants pourront retrouver l’ensemble
des documents (livrables, guides, docs internes, le repor.ng c-a-d les temps d’ac.vité
individuels, et la planiﬁca.on) - privilégier les pdf - aXen.on aux noms des documents
et à leur organisa.on.
Contexte Technologique
• Les cartes seront de simples cartes plas.ﬁées avec un QR-code unique par abonné au
système qu’il faudra présenter à chaque achat fait chez un commerçant partenaire
(scanner via l'applica.on web) ; les u.lisateurs pourront également accéder à leur carte
directement depuis l'applica.on web. La base de données u.lisée pour faire persister les
données appar.ent à la famille SQL ;
• Le système d’informa.on u.lise principalement la technologie J2E pour (i) la déﬁni.on
des composants fonc.onnels et (ii) la persistance des données ;
• Les services partenaires (e.g., interface avec le système d’informa.on de la ville, avec une
banque) seront simulés ;
• L’eﬀort est à meXre à la fois sur le backend de votre système (les services à disposi.on
pour rendre les fonc.onnalités dont le client a besoin) et sur le frontend.
Rela3vement à l’u3lisa3on de l’IA
Conformément au règlement des études, il vous faudra préciser ce qui a été généré par une
intelligence ar.ﬁcielle, que cela concerne votre code ou vos rapports : L’obliga*on de toujours
bien dis*nguer, dans les produc*ons des étudiants, ce qui leur revient en propre de ce qu’ils
ont emprunté à d’autres, en citant systéma*quement les auteurs et leurs sources, vaut aussi
pour les contenus générés par les ou*ls d’intelligence ar*ﬁcielle (IA), tels que Chat-GPT, Claude
ou DALL-E, qu’il est interdit de présenter comme une œuvre humaine. Les textes générés par
les ou*ls d’intelligence ar*ﬁcielle sont des textes certes crédibles, mais ils peuvent contenir des
propos inexacts ou biaisés. Leur fonc*onnement repose sur l’appren*ssage profond, basé sur
un entrainement à par*r de milliards de textes disponibles sur internet. En tant qu’u*lisateur,
il n’est donc pas possible de retrouver les sources à l’origine des textes proposés.
Par ailleurs, dans le contexte de l’éco-concep.on, vous préciserez aussi si vous vous êtes servi
de l’intelligence ar.ﬁcielle pour d’autres pra.ques, e.g. debug.
Travail à eﬀectuer et calendrier
Au semestre S3, vous devrez :
-
prendre en main le sujet et répondre à un appel d’oﬀres en 3 semaines (R1). La réponse
con.endra :
• les CV de l’équipe et la répar..on des rôles ;
• Une première analyse du sujet dans laquelle vous iden.ﬁerez toutes les
fonc.onnalités mé.er à réaliser ;
• des premiers choix jus.ﬁés d’ou.ls logiciels ;
• un diagramme de GanX sur l’année
• le coût détaillé du projet qui comprendra sa réalisa.on, mais aussi son exploita.on et
sa maintenance en fonc.on du segment de client

---

## Section / Page 7

7
La solu.on sera défendue par le groupe lors de la troisième séance du S3
-
choisir, jus.ﬁer et installer l’ensemble des ou.ls logiciels nécessaires pour réaliser le
projet (R2)
-
Évaluer la rentabilité de l’inves.ssement calculer le ROI, la Valeur Actuelle neXe (R3)
-
proposer une première architecture (R4) contenant une première
-
vue fonc.onnelle
o diagramme des cas d’u.lisa.on
o diagramme des composants avec leur interface et les paramètres
-
vue développement
o diagramme de classes des objets mé.ers
o modèle rela.onnel de stockage - aXen.on aux requêtes ayant un sens vis-à-vis
des fonc.onnalités à développer dans le système
o explica.on du mapping objet-rela.onnel
-
vue déploiement
o diagramme de déploiement des composants sur les serveurs physiques
-
jus.ﬁer votre architecture du point de vue des propriétés aXendues pour le système
logiciel : Réu.lisa.on, Maintenabilité, Accessibilité, Documenta.on, Performances.
-
réaliser un (au choix) des composants logiciels avec les ou.ls choisis jusqu'au
déploiement et aux tests.
-
Pitcher votre projet : proposi.on de valeur, choix marke.ng, aspects ﬁnanciers,
engagements RSE
CeXe première version sera présentée oralement par le groupe lors de la dernière séance du
S3.
Le calendrier du S3 et S4 est le suivant :
Anne E.en pour le groupe 1
Laurence Duchien pour le groupe 2
François Secchi sur les deux groupes
Jérémy Woirhaye sur les deux groupes
Présenta.on orale – présence de tous les enseignants
Groupe 1
-
2/09- 16h-18h - Distribu.on du sujet
-
7/09 - 10h15-12h15 - Travail sur le cahier des charges
-
9/09 – 16h-18h- Travail sur le cahier des charges
-
18/09 - 18h rendu 1
-
21/09 – 10h15-12h15 PrésentaNon orale du cahier des charges – Rendu 1 – amphi
turing
-
28/09 – 10h15-12h15 - Choix et mise en place des ou.ls logiciels
-
5/10 - 10h15-12h15 - Choix et mise en place des ou.ls logiciels
-
12/10 - 10h15-12h15 - Fonc.onnalités & Architecture + rendu 2
-
19/10 - pas de Glop - semaine IA
-
26/10 - Interrup.on pédagogique
-
2/11 - 10h15-12h15 - Fonc.onnalités & Architecture
-
9/11 - 10h15-12h15 - Fonc.onnalités & Architecture
-
16/11 - 10h15-12h15-  Fonc.onnalités & Architecture

---

## Section / Page 8

8
-
23/11 - 10h15-12h15 - Fonc.onnalités & Architecture
-
30/11 - 10h15-12h15 - Fonc.onnalités & Architecture + rendu 3
-
7/12 - 10h15-12h15 - Fonc.onnalités & Architecture
-
14/12 - 10h15-12h15- Fonc.onnalités & Architecture
-
18/12 - 18h -  Rendu 4 -
-
04/1 - 10h15-12h15 - PrésentaNon orale Rendu 4
-
11/1 - 10h15-12h15 - Fonc.onnalités & Architecture
-
18/1 - 10h15-12h15 - Mise en place des ou.ls logiciels
-
25/1 - 10h15-12h15 - Fonc.onnalités & Architecture
-
01/2 - 10h15-12h15 - Fonc.onnalités & Architecture
-
8/02 - 10h15-12h15 - Fonc.onnalités & Architecture
-
15/02- 10h15-12h15 - Fonc.onnalités & Architecture
-
22/02- 10h15-12h15 - Déploiement
-
01/03 - 10h15-12h15 - Interrup.on pédagogique
-
08/03 - 10h15-12h15 - Fonc.onnalités & Architecture
-
15/03 - 10h15-12h15 - Fonc.onnalités & Architecture
-
19/03 - Rendu 5
-
22/03 8h-12h - PrésentaNon orale Rendu 5
Groupe 2
-
02/09- 16h-18h - Distribu.on du sujet
-
7/09 - 8h-10h - Travail sur le cahier des charges
-
14/09 – 8h-10h- Travail sur le cahier des charges
-
18/09 - 18h rendu 1
-
21/09 – 8h-10h PrésentaNon orale du cahier des charges – Rendu 1 – Amphi turing
-
28/09 – 8h-10h - Choix et mise en place des ou.ls logiciels
-
5/10 - 8h-10h - Choix et mise en place des ou.ls logiciels
-
12/10 - 8h-10h - Fonc.onnalités & Architecture + rendu 2
-
19/10 - pas de Glop - semaine IA
-
26/10 - Interrup.on pédagogique
-
2/11 - 8h-10h - Fonc.onnalités & Architecture
-
9/11 - 8h-10h - Fonc.onnalités & Architecture
-
16/11 - 8h-10h-  Fonc.onnalités & Architecture
-
23/11 - 8h-10h - Fonc.onnalités & Architecture
-
30/11 - 8h-10h - Fonc.onnalités & Architecture + rendu 3
-
7/12 - 8h-10h - Fonc.onnalités & Architecture
-
14/12 - 8h-10h- Fonc.onnalités & Architecture
-
18/12 - 18h -  Rendu 4 -
-
04/1 - 8h-12h - PrésentaNon orale Rendu 4
-
11/1 - 8h-10h - Fonc.onnalités & Architecture
-
18/1 - 8h-10h - Mise en place des ou.ls logiciels
-
25/1 - 8h-10h - Fonc.onnalités & Architecture
-
01/2 - 8h-10h - Fonc.onnalités & Architecture
-
8/02 - 8h-10h - Fonc.onnalités & Architecture
-
15/02- 8h-10h - Fonc.onnalités & Architecture
-
22/02- 8h-10h - Déploiement
-
01/03 - 8h-10h - Interrup.on pédagogique
-
08/03 - 8h-10h - Fonc.onnalités & Architecture

---

## Section / Page 9

9
-
15/03 - 8h-10h - Fonc.onnalités & Architecture
-
19/03 - 18h - Rendu 5
-
22/03 8h-12h - PrésentaNon orale Rendu 5

---
