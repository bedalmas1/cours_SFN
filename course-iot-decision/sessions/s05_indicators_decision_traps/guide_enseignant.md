# Guide enseignant — Séquence 5

> **Conducteur opérationnel.** Pour chaque étape : afficher la diapositive indiquée, poser la question, laisser une réponse argumentée, puis seulement exécuter les commandes. Les réponses ci-dessous sont les arguments attendus ; accepter toute formulation qui cite une preuve, une limite et une vérification.

## Règle de conduite et commandes

Toutes les commandes partent de la racine du dépôt. Aucun broker n'est requis : cette séquence travaille sur des fichiers déjà produits par la séquence 1.

```bash
python3 -m pip install -r sessions/s05_indicators_decision_traps/requirements.txt
export PYTHONPATH=src
python3 -m pytest -q
python3 tests/validate_s05_artifacts.py
```

Attendus : tests sans échec, `moyenne globale: 30.75 °C`, `battery-shelter-01` signalée comme zone masquée, `battery-shelter-01: score 71/100 -> inspection recommandée`, `fuel-storage-01: score 62/100 -> aucune action requise`, `S05 valide`.

**Règle impérative : `src/iot_decision/risk_score.py` ne doit être ni projeté ni évoqué avant 2:45.** Ce fichier est l'objet de la révélation du débrief, pas un support de cours.

## Carte des diapositives

Afficher successivement : **« Accroche — la moyenne de la base est normale »** (vote), **« Un indicateur est un choix de compression »**, **« Activité B / TP 1 — indicateurs et zone masquée »**, **« Débrief — que cache toujours un indicateur ? »**, **« Du calcul transparent au calcul opaque »**, **« Activité D / TP 2 — interroger le score sans le lire »**, **« Incident injecté — fuel-storage-01 »**, **« Ce que le score n'a jamais appris »**, **« Procès à trois »**, **« Activité F — synthèse individuelle »**.

## Finalité et usage

Cette séquence relie deux moitiés d'une même idée. Le matin : un indicateur, même le plus simple, compresse la réalité et peut masquer un risque — la moyenne de 30,75 °C masque `battery-shelter-01` à 35,4 °C. L'après-midi : un modèle automatique fait exactement la même compression, en pire, car on ne peut plus la décomposer à la main, et parce que ses hypothèses de calibration peuvent silencieusement ne plus tenir sur un cas nouveau. Les étudiants doivent finir la séance capables de dire quel indicateur, ou quel processus de décision, mérite réellement leur confiance.

Décision de référence : aucun indicateur unique ne suffit seul ; combiner maximum par zone et vérification humaine pour toute zone nouvelle ou atypique avant de suivre un score automatique. Confiance moyenne pour les cinq zones connues, faible pour toute zone hors du périmètre de calibration.

- Toutes les commandes partent de la racine du dépôt dans un terminal Bash.
- Chaque question ci-dessous possède une direction d'animation et une réponse argumentée.
- Après chaque activité : **décision, confiance, preuve, incertitude, limite, vérification**.

## Conducteur — 240 minutes

| Temps | Conduite | Objectif | Trace |
|---|---|---|---|
| 0:00–0:15 | accroche et vote | révéler ce qu'une moyenne seule ne prouve pas | choix, confiance, manque |
| 0:15–0:40 | moyenne, maximum, seuil | nommer la compression d'un indicateur simple | fiche concept annotée |
| 0:40–1:10 | TP 1 : indicateurs et zone masquée | calculer et retrouver la zone cachée par la moyenne | tableau d'indicateurs |
| 1:10–1:30 | débrief | expliciter ce qu'un indicateur cache toujours | classement argumenté |
| 1:30–1:55 | du transparent à l'opaque | relier modèle et indicateur, poser le vocabulaire | fiche concept annotée |
| 1:55–2:05 | pause | — | — |
| 2:05–2:45 | TP 2 : interroger le score | utiliser un score sans lire sa logique | journal de requêtes |
| 2:45–3:10 | incident : fuel-storage-01 | diagnostiquer un score hors calibration | verdict argumenté |
| 3:10–3:40 | procès à trois | confronter moyenne, maximum et score | plaidoiries et arbitrage |
| 3:40–3:55 | restitution | justifier le processus de décision retenu | note ≤150 mots |
| 3:55–4:00 | exit ticket | transfert individuel | trois phrases |

## 1. Accroche et vote initial — 15 min

**Afficher :** la diapositive d'accroche. Ne montrer ni fichier ni chiffre.

> « La température moyenne de la base est normale. »

| Question | Direction | Réponse et arguments |
|---|---|---|
| Que décidez-vous ? | Exiger un choix provisoire et séparer choix/confiance. | Plusieurs choix sont défendables. Une moyenne seule ne dit rien de la dispersion entre zones. |
| Une moyenne « normale » exclut-elle un problème localisé ? | Faire objecter avant tout calcul. | Non : une moyenne peut rester basse même si une zone isolée dépasse un seuil critique. |
| Quelle information manque le plus ? | Exiger une observation précise, pas un vague doute. | La distribution par zone, pas seulement le résumé global. |
| Quel est le coût d'une erreur ? | Distinguer faux négatif/faux positif. | Se fier à une moyenne rassurante peut masquer un vrai risque localisé ; décomposer systématiquement coûte du temps. |

Débrief : une moyenne n'est ni fausse ni trompeuse en soi — elle répond à une question différente de « une zone est-elle en danger ? ».

## 2. Un indicateur est un choix de compression — 25 min

**Afficher :** la diapositive des concepts du matin.

| Concept | Définition | Piège fréquent | Effet décisionnel |
|---|---|---|---|
| Moyenne | Résumé unique de toutes les valeurs. | La croire représentative de chaque zone individuellement. | Peut masquer une zone très au-dessus du reste. |
| Maximum | La valeur la plus haute observée, par zone. | L'interpréter comme une tendance plutôt qu'un pic ponctuel. | Signale une zone précise, mais rien sur la durée. |
| Seuil | Une valeur de référence pédagogique pour discuter d'une action. | Le confondre avec une norme officielle. | Change ce qui compte comme franchissement. |
| Compression | Toute réduction de plusieurs valeurs à une seule. | Croire qu'une compression plus simple est toujours moins fiable, ou l'inverse. | Chaque compression cache quelque chose de spécifique ; le mesurer avant de choisir. |

Questions : quelles informations disparaissent quand quinze mesures deviennent une seule moyenne ? Le maximum et la moyenne peuvent-ils raconter des histoires contradictoires sur le même lot ?

## 3. TP 1 — Indicateurs et zone masquée — 30 min

**Afficher :** la démonstration puis le travail.

```bash
export PYTHONPATH=src
python3 -m iot_decision.indicators_cli data/processed/batch001_measurements.csv
```

Attendu : moyenne globale 30,75 °C, cinq maxima par zone, `battery-shelter-01` signalée comme zone masquée, durée observée au-dessus du seuil : 0 minute.

| Question | Direction | Réponse et arguments |
|---|---|---|
| La moyenne franchit-elle le seuil pédagogique ? | Faire lire le chiffre exact. | Non : 30,75 °C contre un seuil de 35 °C. |
| Quelle zone franchit pourtant ce seuil ? | Faire citer le maximum exact. | `battery-shelter-01`, avec un maximum de 35,4 °C. |
| Pourquoi la durée au-dessus du seuil est-elle nulle ? | Interdire la surconclusion. | Une seule mesure franchit le seuil ; on ne peut pas encore parler de dépassement prolongé. |
| Recalculer la moyenne d'une zone à la main change-t-il le résultat affiché ? | Faire vérifier concrètement. | Non : le calcul est transparent et vérifiable ligne par ligne, contrairement à ce que produira le score de l'après-midi. |

## 4. Débrief — que cache toujours un indicateur ? — 20 min

**Afficher :** la diapositive de débrief.

| Question | Direction | Réponse et arguments |
|---|---|---|
| La moyenne et le maximum racontent-ils la même histoire ici ? | Faire comparer explicitement. | Non : la moyenne rassure, le maximum alerte sur une seule zone. |
| Un indicateur plus simple est-il toujours moins fiable ? | Refuser l'automatisme. | Non : la moyenne n'est pas fausse, elle répond juste à une question différente de celle qui intéresse le décideur ici. |
| Que faudrait-il ajouter pour ne plus être surpris par une zone masquée ? | Faire proposer une pratique, pas une formule magique. | Toujours accompagner un résumé global d'une décomposition par zone avant de conclure. |

## 5. Du calcul transparent au calcul opaque — 25 min

**Afficher :** la diapositive de transition vers l'après-midi.

| Concept | Définition | Piège fréquent | Effet décisionnel |
|---|---|---|---|
| Modèle / score automatique | Une fonction qui transforme des mesures en recommandation, sans que sa logique soit lue au moment de la décision. | Croire qu'un score est plus objectif parce qu'il est automatique. | Un score reproduit et cache les choix de son concepteur, comme une moyenne cache une dispersion. |
| Biais d'automatisation | Accorder plus de confiance à une machine qu'à un calcul qu'on pourrait pourtant vérifier soi-même. | Ne jamais remettre en cause un score qui « a toujours eu raison » jusqu'ici. | Empêche de détecter le moment où le score sort de son domaine de validité. |
| Sur-apprentissage / calibration figée | Une règle réglée une fois sur un jeu de cas précis, jamais revue depuis. | Supposer que la règle s'applique universellement. | Le score peut devenir silencieusement faux sur un cas qu'il n'a jamais vu. |
| Dérive | L'écart entre les conditions actuelles et celles sur lesquelles un score a été calibré. | Ne la remarquer qu'après l'incident. | Justifie de toujours vérifier le périmètre de calibration avant de faire confiance à un score. |

Questions : en quoi un score automatique est-il une compression « de plus haut niveau » que la moyenne du matin ? Peut-on auditer un score aussi facilement qu'une moyenne ?

## 6. TP 2 — Interroger le score sans le lire — 40 min

**Afficher :** la démonstration puis le travail. Rappeler la règle impérative avant de commencer.

```bash
export PYTHONPATH=src
python3 -m iot_decision.risk_score_cli data/raw/batch001_raw.jsonl
```

Attendu : cinq zones scorées de 56 à 71/100 ; seule `battery-shelter-01` (71/100) dépasse le seuil de décision et reçoit « inspection recommandée ».

| Question | Direction | Réponse et arguments |
|---|---|---|
| Le score retrouve-t-il la même zone d'alerte que ce matin ? | Faire comparer aux résultats du TP 1. | Oui : `battery-shelter-01` ressort en tête, cohérent avec son maximum de 35,4 °C. |
| Pouvez-vous expliquer pourquoi le score de chaque zone est précisément celui-là ? | Refuser toute explication inventée. | Non, pas encore : la logique du score n'est volontairement pas lue à ce stade. |
| Utiliser un score qu'on ne comprend pas est-il déjà une erreur ? | Nuancer. | Pas en soi : c'est l'utiliser sans jamais le questionner, ni vérifier son périmètre, qui devient risqué. |

## 7. Incident — fuel-storage-01 — 25 min

**Afficher :** l'incident à 2:45.

> « Une nouvelle zone, `fuel-storage-01`, vient d'être équipée pour une mission de ravitaillement. »

```bash
python3 -m iot_decision.risk_score_cli data/samples/batch003_shift_scenario.jsonl
```

Attendu : `fuel-storage-01: score 62/100 -> aucune action requise`, indiscernable des zones sûres du matin (56 à 64/100).

| Question | Direction | Réponse et arguments |
|---|---|---|
| Le score de `fuel-storage-01` est-il inquiétant en apparence ? | Faire comparer aux scores des zones connues. | Non : 62/100 se situe dans la même fourchette que les zones jugées sûres. |
| Le stockage carburant a-t-il le même seuil de sécurité que les autres zones ? | Révéler le fait opérationnel manquant. | Non : un dépôt carburant a un seuil réel bien plus bas que 35 °C, à cause du risque de vapeurs inflammables. |
| Le score connaissait-il ce seuil différent ? | Faire ouvrir `risk_score.py` seulement maintenant. | Non : sa règle est fixe, calibrée une fois sur les cinq zones d'origine, avec un seuil unique de 35 °C jamais révisé. |
| Le score « s'est-il trompé » au sens d'un bug ? | Distinguer bug et défaut de conception. | Non : il a fait exactement ce pour quoi il a été construit, en dehors du domaine pour lequel il a été construit. |
| Que révèle ce cas sur la confiance à accorder à un score automatique ? | Relier au biais d'automatisation. | Un score mérite d'autant moins de confiance qu'il s'applique à un cas éloigné de sa calibration d'origine, silencieusement. |

## 8. Procès à trois — 30 min

**Afficher :** la diapositive du procès. Distribuer les rôles : un groupe défend la moyenne globale, un deuxième défend le score automatique, un troisième arbitre en confrontant les deux à la zone masquée du matin et à l'incident de l'après-midi.

| Question | Direction | Réponse et arguments |
|---|---|---|
| Quel argument fort peut défendre la moyenne ? | Exiger un cas où elle est suffisante. | Elle suffit pour une vue d'ensemble rapide, quand aucune zone individuelle n'est en cause. |
| Quel argument fort peut défendre le score ? | Exiger un cas où il est utile. | Il agrège plusieurs facteurs (maximum et durée) plus vite qu'un calcul manuel, sur des zones qu'il connaît. |
| Quel argument commun aux deux attaques les deux indicateurs ? | Faire formuler la thèse d'arbitrage. | Aucun des deux n'a été conçu pour signaler une situation hors de son périmètre : la moyenne masque une zone connue, le score masque une zone nouvelle. |
| Quel processus l'arbitre recommande-t-il ? | Exiger une proposition concrète. | Combiner systématiquement le maximum par zone (transparent) et une vérification humaine explicite pour toute zone nouvelle ou atypique avant de suivre un score. |

## 9. Restitution et synthèse — 20 min

**Afficher :** la restitution puis la synthèse. Les étudiants rédigent 150 mots maximum : processus de décision retenu, confiance, deux preuves, deux incertitudes, vérification prioritaire.

| Question | Direction | Réponse et arguments |
|---|---|---|
| Votre recommandation cite-t-elle un fichier et un chiffre précis ? | Exiger la source exacte. | `batch001_measurements.csv` pour la moyenne et les maxima ; le rapport du score pour `battery-shelter-01` et `fuel-storage-01`. |
| Votre confiance distingue-t-elle les zones connues de toute zone nouvelle ? | Refuser une confiance uniforme. | Oui : moyenne pour les cinq zones calibrées, faible pour toute zone hors périmètre tant qu'elle n'a pas été vérifiée. |
| Quelle vérification proposez-vous en priorité ? | Comparer coût et valeur d'information. | Une vérification terrain ou une recalibration du score pour `fuel-storage-01` avant toute nouvelle mission de ce type. |

## Exit ticket — 5 min

**Afficher :** la diapositive finale. Réponse individuelle sans écran.

| Amorce | Direction | Réponse et argument |
|---|---|---|
| Un indicateur, transparent ou automatique, permet d'affirmer que… | Exiger périmètre et trace. | Une zone connue et calibrée dépasse, ou non, un seuil donné, sur la base d'un calcul vérifiable. |
| Il ne permet pas d'affirmer que… | Rejeter la généralisation. | Qu'une zone nouvelle ou hors périmètre est sûre simplement parce que son score ne se distingue pas des zones connues. |
| Avant une décision automatisée, je vérifierais… | Exiger une vérification discriminante. | Le périmètre de calibration de l'indicateur ou du score, en particulier pour toute zone ou situation nouvelle. |

## Dépannage et clôture technique

| Symptôme | Commande ou contrôle | Décision pédagogique |
|---|---|---|
| Import impossible | `pwd`, puis `export PYTHONPATH=src` | Après deux essais, passer au repli et consigner la provenance. |
| Fichier de mesures absent | `test -f data/processed/batch001_measurements.csv` | Regénérer depuis la séquence 1 si nécessaire ; ne jamais inventer de valeurs. |
| Figure impossible | vérifier `matplotlib` et le chemin de sortie | Maintenir le procès avec les seules sorties CLI. |
| Un étudiant a ouvert `risk_score.py` trop tôt | consigner l'incident | Poursuivre sans réviser le score en séance ; en tenir compte pour ce binôme au débrief seulement. |

Validation finale à exécuter :

```bash
python3 tests/validate_s05_artifacts.py
```

## Critères observables

L'étudiant distingue moyenne, maximum et durée sans les confondre ; recalcule au moins un indicateur à la main ; interroge le score sans lire sa logique avant l'incident ; identifie que `fuel-storage-01` est hors du périmètre de calibration sans accuser le score d'un bug ; propose un processus combinant plusieurs indicateurs ; justifie une confiance différenciée selon le périmètre.

## Sources

Bornes, poids et seuil de décision du score documentés dans `src/iot_decision/risk_score.py`.

## Questions étudiantes — réponses argumentées

| Question | Argument attendu |
|---|---|
| Pourquoi la moyenne n'est-elle pas simplement fausse ? | Elle est exacte pour la question qu'elle pose ; elle ne pose simplement pas la question du décideur. |
| Le score est-il une intelligence artificielle ? | Non : une fonction déterministe fixe, sans apprentissage ni mise à jour, présentée comme boîte noire uniquement pendant l'exercice. |
| Pourquoi 62/100 pour `fuel-storage-01` est-il un problème si ce n'est pas le score le plus haut ? | Parce que ce n'est pas le classement qui compte mais l'absence de tout signal sur un seuil de sécurité différent, non connu du score. |
| Peut-on corriger le score pour qu'il connaisse ce nouveau seuil ? | Oui, en principe, mais cela reste une décision humaine explicite de recalibration, pas une correction automatique. |
| Quel indicateur choisir définitivement ? | Aucun seul : combiner les indicateurs transparents et une vérification humaine ciblée reste la réponse la plus défendable. |

Commandes à exécuter et commenter :

```bash
python3 -m iot_decision.indicators_cli data/processed/batch001_measurements.csv
python3 -m iot_decision.risk_score_cli data/raw/batch001_raw.jsonl
python3 -m iot_decision.risk_score_cli data/samples/batch003_shift_scenario.jsonl
python3 -m iot_decision.visualize_indicators data/processed/batch001_measurements.csv sessions/s05_indicators_decision_traps/slides/figures/batch001_masked_zone.png
python3 -m iot_decision.visualize_risk_score data/raw/batch001_raw.jsonl data/samples/batch003_shift_scenario.jsonl sessions/s05_indicators_decision_traps/slides/figures/batch003_risk_score_shift.png
python3 tests/validate_s05_artifacts.py
```
