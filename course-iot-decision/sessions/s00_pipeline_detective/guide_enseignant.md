# Guide enseignant — Séquence 0 (maître du jeu)

> **Conducteur opérationnel.** Ce guide contient la fiche maître du jeu (scriptée) : ne jamais la laisser accessible aux cellules. Toute requête posée par une cellule reçoit exactement la réponse scriptée ci-dessous, quelle que soit la cellule qui la pose : le monde est unique et partagé, seul l'ordre et le choix des requêtes varient d'une cellule à l'autre.

## Finalité et usage

La séquence 0 précède la séquence 1 et ne dépend d'aucun ordinateur. Elle installe, par le jeu, la question qui structure tout le cours : des informations imparfaites suffisent-elles à décider ? Elle change délibérément de terrain par rapport aux séquences 1 à 8 : il n'y a ici ni capteur, ni broker, ni MQTT, ni température. Le cas est une **fusion de renseignement avant l'entrée d'une patrouille dans un secteur**, construite à partir de rapports d'observation, d'interceptions radio et de témoignages. Cette différence de surface est volontaire : elle évite que les étudiants aient l'impression de refaire par avance la séquence 1 ou les incidents des séquences 2, 4, 5 et 7, tout en travaillant exactement le même raisonnement de fond.

Décision de référence : ne pas dérouter ni annuler l'entrée de la patrouille sur la seule foi de l'observation du poste Nord, très probablement figée depuis une panne technique et jamais reconfirmée ; renforcer ou vérifier en priorité ce poste avant l'entrée en secteur ; ne pas compter l'interception dupliquée comme deux confirmations indépendantes ; rejeter le témoignage aberrant de l'informateur local ; ne pas conclure sur la patrouille avancée une fois l'ordre de bataille mis à jour. Confiance modérée sur ce diagnostic, faible sur tout ce qui n'a pas été vérifié. Une autre action est recevable si son périmètre, ses preuves et son coût d'erreur sont défendus.

## Matériel du maître du jeu

- cette fiche maître du jeu (ci-dessous), imprimée et gardée hors de vue des cellules ;
- le stock de jetons et d'enveloppes par cellule (voir `instructions_avant_seance.md`) ;
- un dé à six faces, pour le délai des vérifications terrain uniquement — il ne modifie jamais le contenu d'une réponse ;
- une horloge de mission visible, distincte de l'heure réelle de la séance.

## Le scénario

15 h 58, heure de mission. Le poste d'observation fixe Nord signale par radio un mouvement de véhicules blindés inhabituel à 6 km au nord du point de contrôle. Une patrouille amie doit pénétrer dans ce secteur à 17 h 00, heure de mission, pour une reconnaissance programmée. Le commandement doit décider avant cette heure s'il faut : **A** laisser la patrouille entrer dans le secteur comme prévu, sans mesure particulière ; **B** renforcer la surveillance ou envoyer une reconnaissance ciblée avant l'entrée de la patrouille ; **C** reporter ou dérouter la patrouille par précaution ; **D** déclarer le renseignement insuffisant et exiger un recoupement supplémentaire avant toute décision.

Cinq sources composent le dispositif de renseignement : poste d'observation fixe Nord, écoute radio et interception, témoignage d'un informateur local, poste frontalier allié, patrouille avancée.

## Horloge de mission et budget

Chaque cellule reçoit **10 jetons** pour toute la partie, non renouvelés. L'horloge de mission démarre à 15 h 58 ; la décision est attendue avant 17 h 00. Les requêtes d'information (dernier rapport, ordre de bataille, historique, journal, comparaison, indice, transmissions) sont instantanées sur l'horloge de mission et ne coûtent que des jetons. Seule la **vérification terrain** (envoi d'une reconnaissance) fait avancer l'horloge de mission : lancez le dé devant la cellule au moment de l'achat et appliquez :

| Dé | Délai ajouté à l'horloge de mission |
|---|---|
| 1–2 | 10 min |
| 3–4 | 20 min |
| 5–6 | 30 min |

Si l'horloge de mission d'une cellule dépasse 17 h 00 avant qu'elle n'ait ouvert son enveloppe de décision, imposez l'action **C** par défaut pour cette cellule (le commandement reprend la main faute de décision à temps) et notez-le comme un résultat pédagogique, pas comme une pénalité arbitraire.

## Catalogue des requêtes et coûts

| Requête | Coût | Portée |
|---|---:|---|
| Dernier rapport d'une source | 1 jeton | une source |
| Ordre de bataille et plan de couverture | 1 jeton | tout le secteur, achat unique valable toute la partie |
| Historique des rapports des dernières 24 h d'une source | 2 jetons | une source |
| Journal des incidents affectant une source | 2 jetons | une source |
| Comparaison avec une source témoin | 1 jeton | tout le secteur |
| Indice de menace consolidé | 1 jeton | tout le secteur |
| Journal des transmissions radio | 2 jetons | tout le secteur |
| Vérification terrain d'une source (reconnaissance) | 3 jetons + délai dé | une source |

**Condition d'accès aux deux requêtes de synthèse.** « Comparaison avec une source témoin » et « Indice de menace consolidé » ne sont accessibles qu'après l'achat d'au moins deux requêtes individuelles (dernier rapport, historique ou journal des incidents) portant sur deux sources différentes — condition cumulée sur l'ensemble de la partie, budget commun aux deux rounds. Si une cellule les demande avant d'avoir rempli cette condition, répondez : « Cette synthèse n'est communiquée qu'après vérification d'au moins deux sources individuelles distinctes. », sans révéler laquelle des deux requêtes manque ni orienter son choix. Cette règle empêche une cellule de fermer son enquête en deux achats sans jamais interroger le poste Nord ou les autres sources individuellement.

## Dossier initial et fiche de classification de référence

Avant tout achat de requête, chaque cellule reçoit le dossier initial (deux fiches de référence — ordre de mission écrit, carte texte du secteur — et huit pièces à trier), reproduit intégralement dans la section « Dossier initial d'investigation » de `guide_etudiant.md`. Ce dossier est fixe et identique pour toutes les cellules ; il ne fait l'objet d'aucune réponse scriptée supplémentaire de votre part pendant la phase de tri : si une cellule demande un complément sur une pièce du dossier, répondez « le dossier ne contient rien de plus que ce qui est écrit ; toute information supplémentaire s'achète auprès du MJ », sans détailler ni orienter le tri.

Classification de référence, à ne jamais révéler avant la synthèse finale :

| Pièce | Classification | Ce qu'elle prépare |
|---|---|---|
| 1 — Fiche organique du dispositif | Utile | Situe les cinq sources et laisse deviner, sans le dire, que les stations d'écoute A/B partagent un même flux de collecte (piège 2) et que la fiche de la patrouille avancée date de 20 jours (cohérent avec l'ordre de bataille avant twist, piège 4) |
| 2 — Mémo doctrine fiabilité | Utile | Doctrine générale, transférable à toute mission : pousse à vérifier la maintenance d'un poste figé (piège 1) et à ne jamais recouper un doublon d'interception comme deux preuves (piège 2) |
| 3 — Fiche de contact de l'informateur local | Utile | Signale une source jamais réévaluée depuis son recrutement, sans dire qu'elle sera aberrante (prépare le piège 3) |
| 4 — Rappel sécurité sur les délais | Utile | Prépare l'arbitrage budget/horloge de mission (piège 8) |
| 5 — Bulletin météo secteur Sud | Bruit | Concerne un secteur différent, sans lien avec la décision |
| 6 — Note logistique carburant | Bruit | Administratif, sans impact sur le diagnostic de menace |
| 7 — Calendrier de maintenance générique | Ambiguë | Évoque une rotation de maintenance possible sans confirmer ni infirmer un incident précis sur le poste Nord ce mois-ci ; une cellule peut légitimement la classer utile ou bruit tant qu'elle n'a pas acheté le journal des incidents |
| 8 — Note manuscrite non signée sur l'informateur | Ambiguë | Rumeur non sourcée qui pointe déjà vers le piège 3 sans le confirmer ; à ne pas traiter comme une preuve, seulement comme une piste à vérifier |

Une cellule n'est pas censée retrouver cette classification exacte pendant la phase de tri : l'objectif est qu'elle discute, hésite sur les deux pièces ambiguës, et en tire un plan d'achat qui privilégie le poste Nord, la vérification croisée de l'informateur et la question du doublon d'interception. Une cellule qui classe tout comme « utile » sans distinction, ou qui ignore les deux pièces ambiguës dans son plan d'achat, est un signal à noter pour la synthèse.

Le tri ne s'arrête pas à la classification globale des huit pièces : certaines pièces classées « utile » (2 et 4) mélangent volontairement, à l'intérieur du même document, un contenu décisif et du remplissage purement administratif (rappels de procédure, archivage, exercices incendie...). Une cellule qui cite un point administratif comme une preuve dans son brief final, ou qui n'arrive pas à distinguer les points 1 à 3 du mémo de doctrine (pièce 2) des points 4 à 6, n'a pas terminé son tri : c'est le même réflexe de lecture qu'il faudra appliquer aux réponses scriptées du MJ pendant les rounds.

## Fiche maître du jeu — réponses scriptées

### Dernier rapport (connu à 15 h 58)

| Source | Réponse à lire ou paraphraser |
|---|---|
| Poste d'observation fixe Nord | Mouvement de véhicules blindés signalé à 6 km au nord du point de contrôle, rapport reçu à 15:58, aucune confirmation depuis. |
| Écoute radio et interception | Message intercepté évoquant un déplacement de colonne, deux confirmations radio reçues à 15:57. |
| Témoignage d'un informateur local | 200 véhicules blindés signalés sur l'axe secondaire, rapport reçu à 15:55. |
| Poste frontalier allié | Secteur calme, aucun mouvement signalé, rapport reçu à 15:56. |
| Patrouille avancée | Aucun rapport reçu ce cycle. |

### Historique des rapports des dernières 24 h

| Source | Réponse à lire ou paraphraser |
|---|---|
| Poste d'observation fixe Nord | 08:00 secteur calme ; 11:00 calme ; 14:05 mouvement signalé, avec une chute de fiabilité de l'optique consignée au même moment ; puis 14:05, 14:20, 14:50, 15:20 et 15:58 : toujours le même rapport — l'observation n'a plus été renouvelée depuis 14 h 05. |
| Écoute radio et interception | 08:00 rien ; 11:00 rien ; 14:00 rien ; 15:57 message intercepté par la station A ; 15:57 le même message intercepté quelques secondes plus tard par la station B, sur une fréquence relais différente. |
| Témoignage d'un informateur local | 08:00 aucun contact ; 11:00 aucun contact ; 14:00 aucun contact ; 15:55 200 véhicules signalés — rupture isolée, aucune observation intermédiaire cohérente. |
| Poste frontalier allié | 08:00 calme ; 11:00 calme ; 14:00 calme ; 15:56 calme — aucune variation. |
| Patrouille avancée | Aucun rapport sur les dernières 24 h. |

### Journal des incidents affectant une source

| Source | Réponse à lire ou paraphraser |
|---|---|
| Poste d'observation fixe Nord | 14:05 — panne d'alimentation de la lunette de guet signalée par l'équipe technique ; poste maintenu en observation dégradée depuis, sans confirmation humaine indépendante. |
| Écoute radio et interception | Aucun incident récent enregistré. |
| Témoignage d'un informateur local | Aucun antécédent d'incident ; informateur en contact depuis 3 mois, fiabilité non réévaluée récemment. |
| Poste frontalier allié | Aucun incident récent enregistré. |
| Patrouille avancée | Dernier contact il y a 9 jours pour relève de matériel, motif non précisé dans ce journal (voir ordre de bataille). |

### Vérification terrain (reconnaissance, après application du délai de dé)

| Source | Réponse à lire ou paraphraser |
|---|---|
| Poste d'observation fixe Nord | Reconnaissance effectuée : secteur calme, aucun mouvement de véhicule constaté. La lunette de guet du poste est toujours signalée en panne d'alimentation. |
| Écoute radio et interception | Aucune nouvelle interception ne confirme un déplacement de colonne au-delà du message initial. |
| Témoignage d'un informateur local | Aucune trace de colonne blindée sur l'axe secondaire ; la route ne permettrait de toute façon pas le passage d'un tel volume. |
| Poste frontalier allié | Secteur confirmé calme sur place. |
| Patrouille avancée | Aucun élément de la patrouille localisé sur sa dernière position connue, quel que soit le moment de la vérification. |

### Requêtes globales

Avant de lire les deux réponses marquées *(soumise à condition)*, vérifiez que la cellule a bien acheté au moins deux requêtes individuelles sur deux sources différentes ; sinon appliquez le refus scripté de la section « Catalogue des requêtes et coûts ».

- **Ordre de bataille et plan de couverture (avant le twist) :** « Cinq éléments sont officiellement engagés sur le dispositif : poste d'observation fixe Nord, écoute radio, informateur local, poste frontalier allié et patrouille avancée. La patrouille avancée est marquée active, dernier contact confirmé il y a 20 jours. »
- **Comparaison avec une source témoin** *(soumise à condition)* : donnez directement le rapport du poste frontalier allié (secteur calme, stable) en le présentant comme référence d'un secteur sans anomalie connue.
- **Indice de menace consolidé** *(soumise à condition)* : « L'indice de menace consolidé du secteur est de 25 sur 100, jugé faible ; il agrège observation, interception et renseignement humain sur une échelle commune et ne signale aucune source en alerte. » Ne donnez aucun détail de calcul si on vous le demande : « la méthode de consolidation n'est pas communiquée à ce niveau. »
- **Journal des transmissions radio :** « Une transmission non identifiée a été captée brièvement sur une fréquence voisine à 15 h 40, sans échange suivi. Aucune autre anomalie de trafic sur la période. »

## Twist injecté — à annoncer à 1 h 35 à toutes les cellules simultanément

Interrompez toutes les cellules en même temps, sans attendre qu'elles le demandent, et annoncez :

> « Mise à jour de l'ordre de bataille : la patrouille avancée a été officiellement redéployée hors secteur la semaine dernière pour une mission distincte. Son silence était donc attendu et documenté depuis le 06/10. »

Cette annonce est gratuite et identique pour toutes les cellules. Elle referme définitivement la question de la patrouille avancée et doit libérer du budget d'investigation pour l'incident principal.

## Cheminement de raisonnement attendu (solution du jeu)

Cette section donne la marche à suivre idéale, comme la solution d'un escape game : c'est le fil que vous cherchez à retrouver, morceau par morceau, dans le journal de bord de chaque cellule pendant les rounds et à la restitution. Aucune cellule ne doit suivre ce chemin à la lettre ni dans cet ordre exact ; il sert à repérer où une cellule est bloquée, où elle va trop vite, et à préparer vos relances.

| # | Question que la cellule doit se poser | Vérification qui y répond | Raisonnement attendu | Piège associé |
|---:|---|---|---|---|
| 1 | Le dossier initial oriente-t-il le plan d'achat vers le poste Nord, l'informateur et le doublon d'interception ? | Tri des huit pièces du dossier initial | Le mémo doctrine et la fiche de contact de l'informateur pointent déjà les zones à risque ; les deux pièces de bruit (météo, logistique) doivent être écartées sans faire perdre de budget ; les deux pièces ambiguës appellent une vérification, pas une conclusion immédiate | — |
| 2 | Le signalement de 15 h 58 est-il daté et confirmé, ou juste alarmant ? | Dernier rapport, puis historique 24 h du poste d'observation fixe Nord | Un signalement choquant sans confirmation n'est qu'un signal, pas une preuve ; il faut d'abord savoir depuis quand il est tenu pour vrai | 1 |
| 3 | Pourquoi l'observation ne change plus depuis 14 h 05 ? | Historique 24 h : le rapport est identique à chaque créneau depuis 14 h 05 | Une observation qui cesse de varier juste après un évènement technique suggère une panne de remontée, pas forcément une situation stable | 1 |
| 4 | Existe-t-il une explication technique à ce blocage ? | Journal des incidents du poste d'observation fixe Nord | La panne d'alimentation de la lunette à 14 h 05 donne une cause plausible, à mettre en balance avec un vrai mouvement de troupes ; c'est aussi la vérification qui tranche la pièce ambiguë du calendrier de maintenance générique | 1 |
| 5 | L'enjeu de l'entrée de la patrouille justifie-t-il le coût d'une vérification terrain ? | Arbitrage budget/horloge de mission, puis reconnaissance sur le poste Nord | Le coût d'une patrouille exposée à tort dépasse le coût de 3 jetons et d'un délai de reconnaissance ; la vérification confirme un secteur calme, la panne était d'observation, pas de menace | 1, 8 |
| 6 | L'incident du poste Nord dit-il quelque chose des quatre autres sources ? | Dernier rapport des quatre autres sources | Un incident localisé ne dispense pas de couvrir tout le dispositif annoncé ; la fusion de renseignement porte sur cinq sources, pas une seule | — |
| 7 | L'interception radio est-elle vraiment confirmée deux fois ? | Historique de l'écoute radio : même message, deux stations, deux fréquences relais | Deux traces d'une même interception relayée ne sont pas deux preuves indépendantes ; le dossier initial l'annonçait déjà en signalant que les stations A et B partagent un même flux de collecte | 2 |
| 8 | 200 véhicules blindés sur l'axe secondaire : à corriger ou à rejeter ? | Historique et vérification terrain du témoignage de l'informateur local | Un chiffre physiquement invraisemblable au vu du terrain s'écarte du raisonnement, il ne se recoupe pas avec le reste comme une preuve ordinaire ; la note manuscrite non signée du dossier initial le laissait pressentir sans le confirmer | 3 |
| 9 | Le silence de la patrouille avancée signifie-t-il une capture ou une panne ? | Ordre de bataille et plan de couverture (avant le twist) | L'ordre de bataille initial montre la patrouille active : le silence reste ambigu entre incident et absence de rapport à transmettre, une conclusion doit rester en suspens | 4 |
| 10 | Que change l'annonce du MJ à 1 h 35 ? | Twist : mise à jour de l'ordre de bataille | La question de la patrouille avancée se referme ; le budget qui lui était réservé doit être redirigé vers l'incident principal | 5 |
| 11 | L'indice de menace à 25/100 suffit-il à conclure que le secteur est sûr ? | Indice de menace consolidé, confronté aux résultats source par source déjà obtenus | Un indice agrégé peut rester rassurant en absorbant une source figée et une source aberrante ; il ne remplace jamais la lecture source par source | 6 |
| 12 | La transmission non identifiée change-t-elle l'analyse ? | Journal des transmissions radio | À signaler dans le brief, mais sans suite confirmée elle ne doit pas absorber le budget restant | 7 |
| 13 | Reste-t-il assez de budget et de temps avant l'entrée de la patrouille ? | Suivi du budget de jetons et de l'horloge de mission | Prioriser la vérification qui a le plus changé le diagnostic (poste Nord) plutôt que de tout vérifier sur le terrain ; le rappel de sécurité sur les délais, dans le dossier initial, préparait déjà cet arbitrage | 8 |
| 14 | Le brief final peut-il être défendu avec ce qui a été réuni ? | Grille de verrouillage puis brief dans l'enveloppe | Action B, périmètre poste Nord en priorité, confiance modérée, deux preuves (historique figé + reconnaissance confirmant le calme), deux incertitudes (fiabilité durable de l'informateur, origine de la transmission non identifiée), une vérification prioritaire restante | — |

Une cellule qui n'a pas parcouru toutes les étapes n'a pas échoué : le budget limité rend cette exhaustivité volontairement difficile. Le débrief de synthèse doit faire ressortir quelles étapes ont été sautées et ce que cela a coûté à la décision finale.

## Conducteur — 180 minutes

| Temps | Conduite | Trace attendue |
|---|---|---|
| 0:00–0:15 | brief mission, formation des cellules, remise du budget et du catalogue | choix initial, confiance avant enquête |
| 0:15–0:35 | remise et tri du dossier initial | fiche de tri, plan d'achat initial |
| 0:35–0:45 | concepts éclair : ce qui peut rendre un renseignement non fiable, sans dévoiler le scénario | liste de pièges possibles évoqués par les cellules |
| 0:45–1:20 | round 1 d'investigation | journal de bord, requêtes achetées |
| 1:20–1:35 | pause | — |
| 1:35–1:50 | twist injecté puis relance | mise à jour du journal |
| 1:50–2:15 | round 2 d'investigation | journal de bord complété |
| 2:15–2:35 | rédaction et ouverture de l'enveloppe de décision | grille de verrouillage remplie, brief rédigé |
| 2:35–2:55 | restitution par cellule | brief oral, décision, confiance |
| 2:55–3:00 | synthèse et révélation de la fiche complète | comparaison décision/référence |

Il n'y a plus de marge tampon dédiée : ce temps a été redistribué vers le tri du dossier initial, qui constitue désormais le cœur de la séance. En cas de débordement, réduire la restitution à 2 minutes par cellule plutôt que le temps de tri ou d'investigation.

## 1. Brief mission et formation des cellules — 15 min

Présentez la situation, formez 3 à 4 cellules de 3 à 4 étudiants, distribuez budget et catalogue. Faites choisir, sans aucune requête posée : A, B, C ou D, avec un niveau de confiance de 0 à 3 (0 impossible, 1 faible, 2 modérée, 3 forte) et la preuve unique disponible à ce stade (le signalement du poste Nord, rien d'autre). Ne distribuez pas encore le dossier initial à ce stade : ce choix doit rester à l'aveugle.

## 2. Remise et tri du dossier initial — 20 min

Distribuez à chaque cellule le dossier initial complet (deux fiches de référence et huit pièces à trier, section « Dossier initial d'investigation » de `guide_etudiant.md`). Laissez les cellules lire, discuter et remplir leur fiche de tri puis leur plan d'achat, sans intervenir sur le contenu : si une cellule vous interroge sur une pièce, rappelez que le dossier ne contient rien de plus que ce qui est écrit et que tout complément s'achète. Circulez pour vérifier que chaque cellule produit bien un plan d'achat écrit avant la fin du créneau, mais ne validez ni n'invalidez son tri. Gardez la classification de référence (section dédiée ci-dessus) sous la main pour le débrief, sans vous y référer devant les cellules.

## 3. Concepts éclair — 10 min

Sans révéler le scénario, faites nommer collectivement des façons dont un renseignement peut tromper un observateur, en partant de ce que le tri du dossier vient de faire remonter : source silencieuse, observation ancienne présentée comme actuelle, double comptage d'une même information, témoignage invraisemblable, ordre de bataille obsolète, indice global qui masque une source en alerte, fausse piste sans conséquence. N'affirmez ni ne niez qu'un de ces cas se produira dans le jeu.

## 4. Round 1 d'investigation — 35 min

Circulez entre les cellules au poste MJ. Chaque requête suit le catalogue et reçoit la réponse scriptée correspondante, lue ou paraphrasée sans ajout ni omission. Exigez que chaque cellule enregistre, immédiatement après chaque réponse, un SITREP oral (dictaphone ou téléphone, écran éteint) : requête achetée, coût, réponse obtenue, ce qu'elle permet de conclure, ce qu'elle ne permet pas de conclure, confiance actualisée. N'exigez pas de journal papier : seule la grille de verrouillage et le brief final restent écrits.

## 5. Twist injecté et relance — 15 min

À 1 h 35, interrompez toutes les cellules et lisez l'annonce du twist (section dédiée ci-dessus). Laissez deux minutes aux cellules pour enregistrer un SITREP sur cette annonce avant de relancer le round 2.

## 6. Round 2 d'investigation — 25 min

Même fonctionnement que le round 1. Rappelez l'horloge de mission à mi-round si une cellule approche 17 h 00 sans avoir encore vérifié le poste d'observation fixe Nord.

## 7. Enveloppe de décision — 20 min

Chaque cellule remplit sa grille de verrouillage (section « Enveloppe de décision » de `guide_etudiant.md`) : elle doit nommer et justifier au moins **quatre problèmes distincts** rencontrés avant de pouvoir ouvrir son enveloppe et y déposer son brief final (action, périmètre, confiance, deux preuves, deux incertitudes, une vérification prioritaire restante). Ne validez l'ouverture qu'après vérification de la grille.

## 8. Restitution — 20 min

Chaque cellule présente en 3 minutes : action retenue, confiance, deux preuves citées, problème le plus déterminant identifié. Les autres cellules peuvent contester une preuve ou une confiance affichée, sans révéler leurs propres résultats.

## 9. Synthèse et révélation — 5 min

Révélez la fiche complète, la classification de référence du dossier initial et la décision de référence. Demandez à chaque cellule de comparer sa décision à l'aveugle (étape 1) à son plan d'achat post-dossier (étape 2) puis à sa décision finale : c'est ce contraste, plus que la fiche complète elle-même, qui doit clore la séance. Si le temps le permet, invitez une cellule à faire réécouter un court SITREP du round 1 : le contraste avec le brief final est souvent plus parlant qu'un résumé écrit. Passez en revue la taxonomie des pièges rencontrés :

1. observation ancienne présentée comme situation actuelle (poste d'observation fixe Nord) ;
2. interception dupliquée comptée comme deux confirmations indépendantes (écoute radio) ;
3. témoignage aberrant à rejeter, pas à intégrer (informateur local) ;
4. silence ambigu nécessitant l'ordre de bataille (patrouille avancée, avant twist) ;
5. ordre de bataille qui se met à jour et contredit une hypothèse déjà posée (twist) ;
6. indice de menace consolidé masquant des sources individuellement alarmantes ou aberrantes (indice global) ;
7. fausse piste sans conséquence réelle (transmission non identifiée) ;
8. coût en temps et en risque de la vérification terrain avant une échéance fixe (horloge de mission).

Demandez à chaque cellule combien de ces huit problèmes elle a effectivement identifiés et lesquels elle n'a pas eu le budget de vérifier. Signalez explicitement, sans s'y attarder, que ce même type de piège reviendra sous une forme technique dans les séquences suivantes (référentiel attendu en séquence 2, valeur aberrante en séquence 4, indicateur trompeur en séquence 5, fausse piste de sécurité en séquence 7) : la séance d'aujourd'hui les a fait raisonner sans outil, les séances à venir leur donneront l'outil.

## Dépannage pédagogique

| Situation | Conduite à tenir |
|---|---|
| Une cellule dépense tout son budget en round 1 | La laisser affronter le round 2 sans nouvelle information ; c'est un résultat pédagogique valable, à exploiter en synthèse. |
| Une cellule ne pose aucune requête sur le poste d'observation fixe Nord | Ne pas orienter directement ; à la restitution, faire remarquer l'écart entre l'incident déclencheur et l'absence de vérification. |
| Une cellule demande une requête hors catalogue | Répondre « cette information n'est pas disponible dans le système actuel », sans inventer de contenu. |
| Une cellule termine très en avance | Lui demander de rédiger une deuxième version du brief pour une audience différente (le commandant plutôt que la cellule de renseignement). |
| Une cellule dépasse 17 h 00 d'horloge de mission avant sa décision | Appliquer l'action C par défaut et le noter comme trace de débrief, pas comme sanction. |
| Une cellule débat sans fin sur le tri du dossier initial sans produire de plan d'achat | Recentrer avec « quelle est la seule requête que vous achèteriez si vous ne pouviez en poser qu'une ? », sans trancher vous-même le tri. |
| Une cellule oublie d'enregistrer un SITREP après une requête | Lui demander de le faire immédiatement de mémoire avant la requête suivante, sans revenir en arrière ni relire la réponse scriptée ; noter la lacune comme trace de débrief, pas comme sanction. |
| Une cellule classe toutes les pièces du dossier initial comme « utiles » sans distinction | Ne pas corriger pendant la phase de tri ; noter l'absence de discrimination pour la relancer en synthèse sur le coût réel de cette absence de tri (budget dispersé en round 1). |

## Critères observables

L'étudiant distingue un rapport reçu d'une situation actuelle ; ne compte pas une interception dupliquée comme deux confirmations indépendantes ; rejette un témoignage invraisemblable plutôt que de l'intégrer ; suspend sa conclusion sur une source silencieuse tant que l'ordre de bataille n'est pas vérifié ; met à jour sa confiance après le twist ; cite une preuve précise pour chaque problème nommé ; propose une vérification qui reste réalisable avant l'échéance de mission ; distingue, dans le dossier initial, une pièce utile d'une pièce de bruit avant de dépenser son budget.

## Sources

Ce jeu est un support pédagogique original du cours, sans source technique externe requise. Il reprend l'échelle de confiance et le format de brief décisionnel déjà utilisés dans `syllabus/syllabus_overall.md` et dans les séquences suivantes du cours, appliqués ici à un cas volontairement distinct du fil rouge capteurs/MQTT.
