# Guide enseignant — Séquence 6

> **Conducteur opérationnel.** Pour chaque étape : afficher la diapositive indiquée, poser la question, laisser une réponse argumentée, puis seulement exécuter les commandes. Les réponses ci-dessous sont les arguments attendus ; accepter toute formulation qui cite une preuve, une limite et une vérification.

## Règle de conduite et commandes

Toutes les commandes partent de la racine du dépôt. Aucun broker n'est requis : cette séquence travaille sur `data/processed/batch002_measurements_clean.csv`, déjà produit par la séquence 4.

```bash
python3 -m pip install -r sessions/s06_visualization_decision_briefing/requirements.txt
export PYTHONPATH=src
python3 -m pytest -q
python3 tests/validate_s06_artifacts.py
```

Attendus : tests sans échec, `battery-shelter-01: 1/3 mesure(s) >= 35 °C, maximum 36.2 °C`, `Niveau de confiance : faible` pour `battery-shelter-01`, `Niveau de confiance : moyenne` pour `comms-shelter-01`, `S06 valide`.

**Point de vigilance : ne jamais qualifier l'échelle tronquée de « fausse » et l'échelle complète de « vraie ».** Les deux graphiques affichent des valeurs exactes ; seule la mise en forme change l'impression produite.

## Carte des diapositives

Afficher successivement : **« Bienvenue dans la séquence 6 »**, **« Le scénario — le même incident, deux images »** (premier graphique, vote), **« Second graphique — mêmes données »**, **« Échelle / Seuil / Annotation / Incertitude visuelle »**, **« Démonstration — produire les deux mises en forme »**, **« TP 1 — Courbe temporelle par zone »**, **« Débrief — graphique utile ou trompeur ? »**, **« Briefing décisionnel »**, **« Démonstration — la note de briefing »**, **« TP 2 — 2 visualisations et une mini-note »**, **« Jeu de rôle »**, **« Brief oral »**, **« Questions contradictoires du commandement »**, **« Activité — Synthèse individuelle »**.

## Finalité et usage

Cette séquence relie deux moitiés d'une même idée. Le matin : la même série de trois mesures produit deux impressions opposées selon l'échelle, le seuil affiché et le traitement du silence de vingt minutes — rien n'est recalculé, tout vient de la mise en forme. L'après-midi : un graphique honnête ne suffit toujours pas seul ; il doit s'accompagner d'une note de briefing qui nomme explicitement le message principal, la limite, le niveau de confiance et la vérification recommandée. Les étudiants doivent finir la séance capables de construire, et de défendre à l'oral face à des questions contradictoires, un brief complet sur une zone de leur choix.

Décision de référence : présenter systématiquement la version à échelle complète, seuil et silences annotés, accompagnée de sa note de briefing. Confiance faible pour `battery-shelter-01` (silence non expliqué avant la seule mesure haute), confiance moyenne pour les zones sans franchissement de seuil.

- Toutes les commandes partent de la racine du dépôt dans un terminal Bash.
- Chaque question ci-dessous possède une direction d'animation et une réponse argumentée.
- Après chaque activité : **décision, confiance, preuve, incertitude, limite, vérification**.

## Conducteur — 240 minutes

| Temps | Conduite | Objectif | Trace |
|---|---|---|---|
| 0:00–0:15 | accroche : deux graphiques, un incident | révéler que l'impression change sans que les données changent | choix, confiance, information tronquée identifiée |
| 0:15–0:45 | échelle, seuil, annotation, incertitude visuelle | nommer les leviers de mise en forme | fiche concept annotée |
| 0:45–1:30 | TP 1 : courbe temporelle par zone | produire les deux mises en forme sur une autre zone | deux images comparées |
| 1:30–1:55 | débrief : graphique utile ou trompeur ? | expliciter ce qu'un choix de mise en forme peut cacher | classement argumenté |
| 1:55–2:05 | pause | — | — |
| 2:05–2:30 | briefing décisionnel, message principal, limites | poser le vocabulaire de la note | fiche concept annotée |
| 2:30–3:15 | TP 2 : 2 visualisations et une mini-note | construire un mini-rapport complet | mini-rapport ≤100 mots |
| 3:15–3:40 | brief oral | défendre le mini-rapport en 3 minutes | prestation orale |
| 3:40–3:55 | questions contradictoires du commandement | résister à la contestation ciblée | réponses argumentées |
| 3:55–4:00 | exit ticket | transfert individuel | trois phrases |

## 1. Accroche et vote initial — 15 min

**Afficher :** le premier graphique (`battery_misleading.png`). Ne montrer ni les données brutes ni le second graphique.

> Une cellule de supervision transmet ce graphique pour justifier une inspection immédiate de `battery-shelter-01`.

| Question | Direction | Réponse et arguments |
|---|---|---|
| Que décidez-vous sur la seule base de ce graphique ? | Exiger un choix provisoire et séparer choix/confiance. | Plusieurs choix sont défendables ; beaucoup de groupes choisissent l'inspection immédiate devant une pente aussi nette. |
| Que vous laisse croire l'axe vertical ? | Faire lire les bornes exactes de l'axe. | L'axe va de 34 à 36,5 °C : toute variation, même faible en valeur absolue, occupe la totalité du graphique. |
| Quelle information ce graphique ne montre-t-il pas ? | Exiger une observation précise. | Aucun seuil affiché, aucune indication du temps écoulé entre les mesures, aucun signalement d'un silence entre les points. |
| Quel est le coût d'une erreur ici ? | Distinguer faux positif/faux négatif. | Déclencher une inspection sur une fausse alarme coûte du temps et du crédit à la cellule data ; ignorer un vrai risque parce que le graphique semblait anodin coûte potentiellement plus cher. |

Débrief : ce graphique ne contient aucune valeur fausse. Ce qui trompe est entièrement dans l'échelle et dans ce qui n'est pas montré.

## 2. Échelle, seuil, annotation, incertitude visuelle — 30 min

**Afficher :** le second graphique (`battery_honest.png`), puis la diapositive des quatre concepts.

| Concept | Définition | Piège fréquent | Effet décisionnel |
|---|---|---|---|
| Échelle | Bornes et étendue choisies pour un axe. | Tronquer l'axe autour des valeurs observées. | Amplifie visuellement toute variation, même faible. |
| Seuil | Valeur de référence pour discuter d'une action, affichée ou non sur le graphique. | L'omettre, ou le présenter comme une norme officielle. | Sans seuil visible, le lecteur doit deviner ce qui compte comme franchissement. |
| Annotation | Texte, flèche ou zone surlignée ajoutés pour désigner ce que les données seules ne montrent pas. | Croire qu'un graphique sans annotation est plus objectif. | Son absence transforme un doute en fausse évidence. |
| Incertitude visuelle | Représentation explicite d'un silence, d'une zone non mesurée ou d'une mesure isolée. | Relier deux points par un trait continu malgré un vide de données entre eux. | Un trait continu sur un silence de 20 minutes fait paraître régulière une évolution jamais observée. |

Questions : les deux graphiques contiennent-ils une seule valeur différente ? Un trait qui relie deux points affirme-t-il quelque chose sur ce qui s'est passé entre eux ?

## 3. TP 1 — Courbe temporelle par zone — 45 min

**Afficher :** la démonstration puis le travail.

```bash
export PYTHONPATH=src
python3 -m iot_decision.visualize_briefing data/processed/batch002_measurements_clean.csv comms-shelter-01 /tmp/comms_misleading.png /tmp/comms_honest.png
```

Attendu : sur `comms-shelter-01` (aucune mesure au-dessus du seuil, aucun silence non expliqué), l'écart entre les deux mises en forme est nettement plus faible que sur `battery-shelter-01`.

| Question | Direction | Réponse et arguments |
|---|---|---|
| L'écart entre les deux mises en forme est-il le même sur toutes les zones ? | Faire comparer explicitement à `battery-shelter-01`. | Non : il est maximal quand un seuil est franchi après un silence non expliqué, minimal sur une zone stable sans silence. |
| Pourquoi l'écart est-il faible sur `comms-shelter-01` ? | Faire nommer la cause précise. | Aucune mesure ne franchit le seuil et les mesures sont régulières : il n'y a rien à dissimuler ni à exagérer. |
| Une échelle complète (0 à 40 °C) est-elle toujours le bon choix ? | Nuancer, refuser une règle absolue. | Pas nécessairement : sur une zone très stable, elle peut écraser une variation réellement significative. Le choix dépend du seuil de décision pertinent. |

## 4. Débrief — graphique utile ou trompeur ? — 25 min

**Afficher :** la diapositive de débrief.

| Question | Direction | Réponse et arguments |
|---|---|---|
| Un graphique à échelle tronquée est-il toujours trompeur ? | Refuser l'automatisme. | Non : il devient un problème seulement lorsqu'il accompagne une décision sans indication de ses bornes réelles ni du seuil pertinent. |
| Que faudrait-il exiger systématiquement avant de projeter un graphique devant un décideur pressé ? | Faire proposer une pratique. | Vérifier les bornes de l'axe, la présence du seuil, et si un trait continu masque un silence de données. |
| Le silence de vingt minutes change-t-il la valeur maximale mesurée ? | Distinguer donnée et confiance. | Non : le maximum reste 36,2 °C. Le silence change uniquement la confiance qu'on peut accorder à ce que cette mesure signifie. |

## 5. Briefing décisionnel, message principal, limites — 25 min

**Afficher :** la diapositive de transition puis les concepts de l'après-midi.

| Concept | Définition | Piège fréquent | Effet décisionnel |
|---|---|---|---|
| Briefing décisionnel | Communication courte reliant une observation à une décision recommandée, sans faire l'impasse sur ses limites. | Présenter seulement le graphique le plus frappant. | Sans note explicite, deux lecteurs peuvent tirer deux niveaux de confiance opposés du même graphique. |
| Message principal | Ce que l'observation permet d'affirmer, avec ses chiffres. | Le formuler de façon vague ou sans chiffre. | Un message chiffré et retrouvable peut être vérifié ; un message vague ne peut être ni confirmé ni infirmé. |
| Limite | Ce que l'observation ne permet pas encore de conclure. | L'omettre, ou la formuler de façon si vague qu'elle ne change rien à la décision. | Une limite précise oriente directement la vérification à mener. |

Questions : le niveau de confiance d'une note peut-il être choisi à la main, ou doit-il découler d'une règle appliquée systématiquement ?

## 6. TP 2 — 2 visualisations et une mini-note — 45 min

**Afficher :** la démonstration puis le travail.

```bash
export PYTHONPATH=src
python3 -m iot_decision.briefing_cli data/processed/batch002_measurements_clean.csv battery-shelter-01
```

Attendu : `battery-shelter-01: 1/3 mesure(s) >= 35 °C, maximum 36.2 °C`, limite citant le vide de 20 min, `Niveau de confiance : faible`, vérification terrain recommandée.

| Question | Direction | Réponse et arguments |
|---|---|---|
| La note et le graphique honnête racontent-ils la même histoire ? | Faire comparer explicitement. | Oui : les deux signalent le même silence et la même confiance faible, sous deux formes différentes. |
| Pourquoi `comms-shelter-01` reçoit une confiance « moyenne » et non « faible » ? | Refuser la surinterprétation. | Aucune mesure n'y franchit le seuil : la règle ne signale pas un danger qui n'existe pas dans les données. |
| Le mini-rapport doit-il inclure le graphique trompeur ? | Faire justifier le choix. | Le conserver comme pièce de comparaison est utile en débrief, mais seul le graphique honnête doit accompagner la recommandation. |

## 7. Jeu de rôle et brief oral — 25 min

**Afficher :** la diapositive du jeu de rôle. Distribuer les rôles : cellule data, décideur pressé, red team ; permuter les rôles à chaque passage.

| Question | Direction | Réponse et arguments |
|---|---|---|
| Quelle est la seule phrase que le décideur pressé doit retenir ? | Exiger une priorisation explicite. | Le message principal chiffré, jamais une description générale du graphique. |
| Que doit chercher la red team en priorité ? | Orienter vers les quatre leviers vus le matin. | L'échelle, la présence du seuil, une annotation manquante, un silence non signalé. |

## 8. Questions contradictoires du commandement — 15 min

**Afficher :** la diapositive des questions contradictoires.

| Question | Direction | Réponse et arguments |
|---|---|---|
| « Si je vous impose l'autre mise en forme de la même zone, votre recommandation change-t-elle ? » | Refuser une réponse évasive. | Non pour la recommandation finale, si elle repose sur la note de briefing et non sur l'impression du graphique seul. |
| « Qu'est-ce qui, dans ce graphique, n'est pas une mesure mais un choix de votre part ? » | Exiger une réponse précise et nommée. | Les bornes de l'axe, la présence ou l'absence du seuil, la décision de rompre ou non le trait au niveau du silence. |

## Exit ticket — 5 min

**Afficher :** la diapositive finale. Réponse individuelle sans écran.

| Amorce | Direction | Réponse et argument |
|---|---|---|
| Un graphique honnête, sur ces données, doit toujours montrer… | Exiger les quatre leviers. | Une échelle justifiée, le seuil pertinent, les silences annotés, sans trait continu sur un vide de données. |
| Un graphique peut rester exact et pourtant donner une impression fausse quand… | Rejeter la généralisation vague. | Son échelle est tronquée ou qu'un silence de données est masqué par un trait continu, même si chaque valeur affichée est correcte. |
| Avant de projeter un graphique devant un décideur, je vérifierais… | Exiger une action concrète. | Les bornes de l'axe, le seuil affiché, et si un silence de données est visible ou dissimulé par la mise en forme. |

## Dépannage et clôture technique

| Symptôme | Commande ou contrôle | Décision pédagogique |
|---|---|---|
| Import impossible | `pwd`, puis `export PYTHONPATH=src` | Après deux essais, passer au repli et consigner la provenance. |
| Fichier de mesures absent | `test -f data/processed/batch002_measurements_clean.csv` | Regénérer depuis la séquence 4 si nécessaire ; ne jamais inventer de valeurs. |
| Figure impossible | vérifier `matplotlib` et le chemin de sortie | Maintenir le brief oral avec les seules notes de `briefing_cli`. |
| Confusion entre les deux graphiques en séance | reprojeter les deux images côte à côte | Toujours faire nommer explicitement le levier de mise en forme en cause avant de trancher. |

Validation finale à exécuter :

```bash
python3 tests/validate_s06_artifacts.py
```

## Critères observables

L'étudiant distingue une variation réelle d'une variation amplifiée par l'échelle ; identifie si un seuil est affiché et s'il est présenté comme pédagogique ; repère un trait continu masquant un silence de données ; produit une note de briefing avec les quatre champs requis ; choisit le graphique honnête pour accompagner sa recommandation ; résiste aux questions contradictoires en nommant le levier de mise en forme précis plutôt qu'en défendant le graphique en bloc.

## Sources

Bornes de seuil et règle de confiance documentées dans `src/iot_decision/briefing.py` ; références de visualisation décisionnelle en fin de diaporama.

## Questions étudiantes — réponses argumentées

| Question | Argument attendu |
|---|---|
| Le premier graphique est-il un mensonge ? | Non au sens strict : aucune valeur n'est inventée. C'est un choix de cadrage qui mérite d'être justifié ou corrigé, pas une falsification. |
| Faut-il toujours utiliser l'échelle complète ? | Non : la règle est de justifier le choix d'échelle au regard du seuil de décision pertinent, pas d'imposer une échelle unique en toute circonstance. |
| La note de briefing remplace-t-elle le graphique ? | Non : les deux se complètent. Le graphique montre, la note nomme explicitement ce que le graphique ne peut pas garantir seul. |
| Peut-on avoir une confiance « faible » sans silence de données ? | Pas avec les règles de ce module : ici, la confiance faible découle précisément de la combinaison franchissement de seuil + silence non expliqué. |

Commandes à exécuter et commenter :

```bash
python3 -m iot_decision.briefing_cli data/processed/batch002_measurements_clean.csv battery-shelter-01
python3 -m iot_decision.briefing_cli data/processed/batch002_measurements_clean.csv comms-shelter-01
python3 -m iot_decision.visualize_briefing data/processed/batch002_measurements_clean.csv battery-shelter-01 sessions/s06_visualization_decision_briefing/slides/figures/battery_misleading.png sessions/s06_visualization_decision_briefing/slides/figures/battery_honest.png
python3 tests/validate_s06_artifacts.py
```
