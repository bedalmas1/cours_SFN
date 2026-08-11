# Guide enseignant — Séquence 4

> **Conducteur opérationnel.** Pour chaque étape : afficher la diapositive indiquée, poser la question, laisser une réponse argumentée, puis faire exécuter les commandes. Les réponses ci-dessous sont les arguments attendus ; accepter toute formulation qui cite une preuve, une limite et une vérification.

## Règle de conduite et commandes

Toutes les commandes partent de la racine du dépôt. Commandes de préparation :

```bash
python3 -m pip install -r sessions/s04_data_quality_uncertainty/requirements.txt
export PYTHONPATH=src
python3 -m pytest -q
python3 tests/validate_s04_artifacts.py
```

Attendus : tests sans échec, `19 lignes propres; 5 lignes rejetées`, silence réel signalé sur `battery-shelter-01` uniquement, `S04 valide`. Mode broker :

```bash
docker compose -f docker/docker-compose.yml up -d --wait
python3 -m iot_decision.mqtt_tools seed data/samples/batch002_quality_messages.jsonl
python3 -m iot_decision.mqtt_tools extract /tmp/s04_teacher_check.jsonl --topic airbase/batch002/#
wc -l /tmp/s04_teacher_check.jsonl
```

Attendu : 24 enveloppes. Repli sans broker : utiliser directement `data/samples/batch002_quality_messages.jsonl`. Fin de séance : `docker compose -f docker/docker-compose.yml down`.

## Carte des diapositives

Afficher successivement : **« Accroche — une alerte apparaît »** (vote), **« Quatre qualités d'une donnée »**, **« Activité B / TP 1 — champs manquants, unités, valeurs impossibles »**, **« Débrief — quelles erreurs sont graves ? »**, **« Rejet, correction, quarantaine »**, **« Activité D / TP 2 — produire clean.csv et rejected.csv »**, **« Incident injecté — le silence de battery-shelter-01 »**, **« Silence réel ou effet du filtrage ? »**, **« Activité F — brief et vote final »**, **« Activité G — synthèse individuelle »**.

## Finalité et usage

Cette séquence installe le réflexe central du cours pour la qualité : une valeur numériquement présente n'est pas encore une valeur validée, et un silence dans les données n'est pas toujours un silence réel. Les étudiants doivent décider si l'alerte température du stockage batteries est exploitable en l'état, avec quelle confiance, sachant qu'un silence de vingt minutes précède directement la valeur haute et qu'aucune ligne rejetée ne l'explique.

Une réponse recevable associe action, confiance argumentée, deux preuves retrouvables, deux incertitudes et une vérification prioritaire terrain. Une certitude fondée sur la seule valeur de 36,2 °C, sans mention du silence qui la précède, ou une confusion entre silence réel et ligne rejetée, ne peut pas l'être.

- Toutes les commandes partent de la racine du dépôt dans un terminal Bash.
- Chaque question ci-dessous possède une direction d'animation et une réponse argumentée.
- Après chaque activité : **décision, confiance, preuve, incertitude, limite, vérification**.

## Conducteur — 240 minutes

| Temps | Conduite | Objectif | Trace |
|---|---|---|---|
| 0:00–0:15 | accroche et vote | révéler ce qu'une alerte seule ne prouve pas | choix, confiance, manque |
| 0:15–0:45 | validité, complétude, cohérence, précision | distinguer quatre qualités et leurs pièges | fiche concept annotée |
| 0:45–1:30 | TP 1 : champs manquants, unités, valeurs impossibles | classer et nommer chaque erreur | tableau des rejets |
| 1:30–1:55 | débrief | hiérarchiser la gravité décisionnelle des erreurs | classement argumenté |
| 1:55–2:05 | pause | — | — |
| 2:05–2:30 | rejet, correction, quarantaine, incertitude | choisir la bonne réponse à une anomalie | classement des opérations |
| 2:30–3:15 | TP 2 : produire clean.csv et rejected.csv | séparer propre et rejeté, sans corriger | CSV et JSON reproductibles |
| 3:15–3:40 | incident : silence critique | distinguer silence réel et silence expliqué | verdict par zone |
| 3:40–3:55 | brief et vote final | qualifier la confiance dans l'alerte | note ≤150 mots |
| 3:55–4:00 | exit ticket | transfert individuel | trois phrases |

## 1. Accroche et vote initial — 15 min

**Afficher :** la diapositive d'accroche. Ne montrer ni fichier ni chiffre.

> Une supervision signale : « `battery-shelter-01` a atteint 36,2 °C, au-dessus du seuil habituel. » Aucune autre information n'est donnée.

| Question | Direction | Réponse et arguments |
|---|---|---|
| Que décidez-vous ? | Exiger un choix provisoire et séparer choix/confiance. | Plusieurs choix sont défendables. Une seule valeur, sans historique ni contrôle qualité, autorise la prudence, pas la certitude. |
| Quelle preuve avez-vous réellement ? | Faire barrer les faits inventés. | Une valeur unique annoncée ; rien sur sa fraîcheur, sa validité, ni sur ce qui a précédé. |
| Une valeur numérique est-elle automatiquement une donnée valide ? | Distinguer présence et validité. | Non : elle peut porter une unité incohérente, un champ manquant ailleurs dans le message, ou une valeur hors de toute plausibilité physique. |
| Quel est le coût d'une erreur ? | Distinguer faux négatif/faux positif. | Ignorer une vraie hausse expose le matériel ; réagir à une donnée corrompue mobilise inutilement une vérification terrain. |

Débrief : une alerte peut être vraie, fausse, ou simplement non qualifiée. Ces trois cas n'appellent pas la même action.

## 2. Quatre qualités d'une donnée — 30 min

**Afficher :** la diapositive des quatre concepts. Faire annoter un exemple avant de révéler la définition.

| Concept | Définition | Piège fréquent | Effet décisionnel |
|---|---|---|---|
| Validité | La ligne respecte les règles déclarées : champ présent, unité connue, valeur dans une plage plausible. | Confondre « le champ existe » et « le champ est correct ». | Une ligne invalide ne doit jamais entrer dans un calcul sans être signalée. |
| Complétude | Tout ce qui était attendu est effectivement arrivé, sur la période considérée. | Confondre une ligne rejetée avec un message jamais reçu. | Un vrai manque et un rejet appellent des vérifications différentes. |
| Cohérence | Les champs d'une même ligne, ou de lignes voisines, ne se contredisent pas. | Ignorer qu'un horodatage de mesure postérieur à sa réception est impossible. | Une incohérence temporelle invalide la ligne entière, pas seulement la date. |
| Précision | La mesure reflète un ordre de grandeur physiquement crédible pour ce contexte. | Croire qu'une valeur numérique plausible est forcément exacte. | Aucun contrôle automatique ne peut ici démontrer l'exactitude physique, seulement écarter l'impossible. |

Questions : à quelle qualité appartient chaque erreur de la démonstration suivante ? Une ligne peut-elle être valide sans être complète pour sa zone ? Peut-on avoir une zone complète mais dont une ligne est invalide ? Sources : `src/iot_decision/quality.py` (bornes documentées dans le code).

## 3. TP 1 — Champs manquants, unités, valeurs impossibles — 45 min

**Afficher :** la diapositive de démonstration, puis celle du travail.

```bash
export PYTHONPATH=src
python3 -c "from iot_decision.quality import load_raw, flatten, validate_row; rows=[flatten(e) for e in load_raw('data/samples/batch002_quality_messages.jsonl')]; [print(r['message_id'], validate_row(r)) for r in rows if validate_row(r)]"
```

Attendu : cinq lignes signalées, une par type d'erreur. Ne pas révéler tout de suite laquelle correspond à quelle zone : faire deviner à partir du seul message d'erreur.

| Question | Direction | Réponse et arguments |
|---|---|---|
| Combien d'erreurs différentes trouvez-vous ? | Exiger un décompte avant lecture du code. | Quatre types de contrôle ligne à ligne : champ manquant, unité incohérente, valeur hors plage, incohérence temporelle ; plus un doublon exact détecté séparément. |
| Quel champ manque exactement, et où ? | Faire citer message_id et champ. | `it-room-01-0002` : le champ `unit` est absent du payload. Sans lui, aucune comparaison n'est possible. |
| Quelle unité est incohérente ? | Faire recalculer approximativement en Celsius. | `maintenance-zone-01-0002` : 86,9 °F, soit environ 30,5 °C ; la valeur est plausible, seule l'unité déclarée est fautive. |
| Quelle valeur est hors plage, et pourquoi ces bornes ? | Rappeler qu'elles sont pédagogiques. | `optronics-shelter-01-0002` : 214,7, hors des bornes -10..60 °C choisies pour cette séance ; en réel, ces bornes seraient fixées avec le responsable du matériel. |
| Quelle incohérence temporelle observez-vous ? | Faire comparer les deux horloges. | `it-room-01-0003` : mesure déclarée à 10 h 15, reçue à 9 h 55 ; une mesure ne peut pas être reçue avant d'avoir eu lieu. |
| Faut-il corriger une de ces lignes pour la sauver ? | Interdire toute correction silencieuse. | Non : chaque ligne est rejetée avec sa raison exacte ; corriger reviendrait à remplacer une observation par une hypothèse. |

## 4. Débrief — quelles erreurs sont graves pour la décision ? — 25 min

**Afficher :** la diapositive de débrief.

| Question | Direction | Réponse et arguments |
|---|---|---|
| Les cinq erreurs ont-elles la même gravité ? | Refuser une réponse uniforme. | Non : une valeur hors plage physique menace directement un calcul de maximum ; un champ manquant bloque une comparaison ; un doublon peut gonfler un décompte s'il n'est pas détecté. |
| Quelle erreur aurait le plus faussé un maximum par zone si elle n'avait pas été rejetée ? | Faire chiffrer l'écart. | La valeur de 214,7 aurait dominé toute agrégation de `optronics-shelter-01`, masquant les valeurs réelles de la zone. |
| Le doublon exact change-t-il un décompte s'il n'est pas retiré ? | Relier à la séquence 3. | Oui : il compterait deux fois le même événement, contrairement à un candidat doublon de la séquence 3, où l'identité même du message reste incertaine. |
| Une ligne rejetée est-elle perdue pour l'analyse ? | Nuancer. | Non : elle reste dans `rejected.csv` avec sa raison ; elle est exclue du calcul, pas du dossier de preuve. |

## 5. Pause — 10 min

Au retour : « propre » et « présent » ne sont pas synonymes. Une ligne peut être présente dans le brut et absente du propre.

## 6. Rejet, correction, quarantaine, incertitude — 25 min

**Afficher :** la diapositive des opérations possibles.

| Concept | Définition | Piège | Effet décisionnel |
|---|---|---|---|
| Rejet | Écarter une ligne du calcul, en conservant sa trace et sa raison. | L'oublier au lieu de la documenter. | Permet d'auditer plus tard pourquoi une ligne n'a pas compté. |
| Correction | Remplacer une valeur par une valeur jugée plus probable. | La faire silencieusement, sans trace ni règle explicite. | Ce cours ne corrige jamais automatiquement : toute correction devient une hypothèse à assumer publiquement. |
| Quarantaine | Isoler une ligne douteuse sans la rejeter ni la valider, en attendant une vérification. | La laisser indéfiniment sans suite. | Utile pour une anomalie ambiguë qu'aucune règle simple ne peut trancher seule. |
| Incertitude | Ce que l'on ne sait pas encore, et qui pourrait changer l'action. | La traiter comme une liste abstraite sans conséquence. | Une incertitude utile désigne une vérification concrète, pas un doute vague. |

Questions : pourquoi ce cours choisit-il le rejet plutôt que la correction pour les cinq lignes du TP 1 ? Dans quel cas une quarantaine serait-elle plus appropriée qu'un rejet ferme ? Le silence de `battery-shelter-01` relève-t-il du rejet, de la correction, ou d'aucun des deux ?

## 7. TP 2 — Produire clean.csv et rejected.csv — 45 min

**Afficher :** la démonstration, puis le travail.

```bash
export PYTHONPATH=src
python3 -m iot_decision.quality_cli \
  data/samples/batch002_quality_messages.jsonl \
  data/processed/batch002_measurements_clean.csv \
  data/processed/batch002_rejected.csv \
  data/processed/batch002_quality_report.json
head -n 3 data/processed/batch002_measurements_clean.csv
cat data/processed/batch002_rejected.csv
```

Attendu : 19 lignes propres, 5 lignes rejetées avec leur raison en dernière colonne.

| Question | Direction | Réponse et arguments |
|---|---|---|
| Pourquoi la commande produit-elle trois fichiers en un seul appel ? | Relier à la traçabilité. | Les trois sorties partagent la même source et le même calcul : les produire ensemble évite un désaccord entre elles. |
| Le fichier rejeté contient-il les mêmes colonnes que le fichier propre ? | Faire compter les colonnes. | Les mêmes douze, plus une treizième : la raison de rejet, absente du fichier propre par construction. |
| Que se passerait-il si l'on supprimait `rejected.csv` après la séance ? | Faire objecter. | On perdrait la preuve que ces lignes ont existé et pourquoi elles ont été écartées ; une contestation deviendrait impossible à instruire. |
| Le fichier propre est-il exempt de toute erreur ? | Interdire la surconfiance. | Non : il est exempt des cinq erreurs détectées par ces quatre contrôles précis, pas de toute erreur imaginable. |

## 8. Incident — le silence de battery-shelter-01 — 25 min

**Afficher :** l'incident à 3 h 15, sans révéler d'abord lequel des quatre silences détectés est réel.

```bash
python3 -m json.tool data/processed/batch002_quality_report.json
```

Attendu : quatre zones avec un silence détecté ; un seul porte `"explained_by_rejection": false`.

| Question | Direction | Réponse et arguments |
|---|---|---|
| Combien de silences le rapport signale-t-il ? | Faire lire le JSON avant de commenter. | Quatre : `battery-shelter-01`, `it-room-01`, `maintenance-zone-01`, `optronics-shelter-01`. |
| Un silence signalé est-il toujours un vrai manque de message ? | Refuser l'automatisme. | Non : il faut vérifier si une ligne rejetée de la même zone tombe dans la fenêtre du silence. |
| Lequel des quatre silences n'est expliqué par aucun rejet ? | Faire croiser `rejected.csv` et le silence. | `battery-shelter-01` : aucune ligne rejetée pour cette zone : le silence de vingt minutes est réel, sans message reçu. |
| Que prouvent les trois autres silences ? | Nuancer sans les écarter. | Qu'une ligne a bien été reçue puis rejetée pendant cette fenêtre : ce n'est pas un manque de transmission, mais un manque de qualité déjà documenté. |
| Le silence réel de `battery-shelter-01` précède-t-il ou suit-il la valeur de 36,2 °C ? | Faire situer temporellement. | Il précède directement : la dernière mesure propre avant le silence est 34,6 °C à 9 h 45, puis rien jusqu'à 36,2 °C à 10 h 05. |
| Quelle hypothèse ce silence laisse-t-il ouverte ? | Lister sans trancher. | Panne de capteur, coupure de transmission, filtre d'extraction incorrect, ou hausse réelle et progressive simplement non enregistrée. |

## 9. Brief décisionnel et vote final — 15 min

**Afficher :** la diapositive du brief. Prévoir cinq minutes d'écriture, quatre de contradiction, trois de révision, puis le vote. Le brief de 150 mots contient action, confiance, deux preuves retrouvables, deux incertitudes et vérification prioritaire.

| Question | Direction | Réponse et arguments |
|---|---|---|
| Quelle action proposez-vous exactement ? | Refuser « surveiller » sans échéance ni acteur. | Vérification terrain prioritaire du stockage batteries avant 14 h, en parallèle d'une inspection de la chaîne de collecte pour cette zone. |
| Où retrouve-t-on chaque preuve ? | Exiger fichier et champ. | `batch002_quality_report.json` pour le silence et son statut ; `batch002_measurements_clean.csv` pour la valeur de 36,2 °C. |
| Pourquoi ce niveau de confiance ? | Refuser le pourcentage décoratif. | Faible : la valeur haute est réelle et propre, mais rien n'explique les vingt minutes de silence qui la précèdent. |
| Quelle vérification réduit le mieux l'incertitude ? | Comparer délai et pertinence. | Une mesure terrain ou un contrôle de la chaîne de collecte pour `battery-shelter-01`, en priorité sur les trois autres zones dont le silence est déjà expliqué. |
| Pourquoi le vote a-t-il changé, ou non ? | Comparer les raisonnements. | Changement si le silence réel modifie l'action envisagée au vote initial ; stabilité si le doute était déjà présent. |

## 10. Exit ticket — 5 min

**Afficher :** la diapositive finale. Réponse individuelle sans écran.

| Amorce | Direction | Réponse et argument |
|---|---|---|
| Le contrôle qualité permet d'affirmer que… | Exiger périmètre et trace. | 19 des 24 messages respectent les quatre contrôles retenus ; les 5 autres sont documentés avec leur raison exacte. |
| Il ne permet pas d'affirmer que… | Rejeter « tout est fiable ». | Ni la calibration des capteurs, ni la cause du silence de `battery-shelter-01`, ni l'état réel actuel de la zone. |
| Avant une action irréversible, je vérifierais… | Exiger une vérification discriminante. | L'état terrain de `battery-shelter-01` pendant, ou immédiatement après, la période de silence. |

## Dépannage et clôture technique

| Symptôme | Commande ou contrôle | Décision pédagogique |
|---|---|---|
| Import impossible | `pwd`, puis `export PYTHONPATH=src` | Après deux essais, passer au repli et consigner la provenance. |
| Broker inaccessible | `docker compose -f docker/docker-compose.yml ps` | Utiliser directement l'échantillon ; préserver le raisonnement. |
| CSV rejeté vide de façon inattendue | Relire `validate_row` et l'ordre des contrôles | Un champ manquant masque les autres anomalies de la même ligne : c'est le comportement attendu. |
| Figure impossible | vérifier `matplotlib` et le chemin de sortie | Maintenir le débat sur le silence avec le seul rapport JSON. |

Validation finale à exécuter :

```bash
python3 tests/validate_s04_artifacts.py
```

## Critères observables

L'étudiant nomme précisément les quatre types d'erreur ; ne corrige jamais silencieusement ; sépare propre et rejeté de façon traçable ; distingue un silence réel d'un silence expliqué par un rejet ; relie le silence de `battery-shelter-01` à la valeur haute qui le suit ; formule une action bornée ; justifie sa confiance ; propose une vérification terrain réalisable.

## Sources

Bornes de plausibilité et contrôles documentés dans `src/iot_decision/quality.py` ; méthode de détection de silence dans `detect_gaps` et `diagnose`.

## Questions étudiantes — réponses argumentées

| Question | Argument attendu |
|---|---|
| Pourquoi -10 et 60 °C et pas d'autres bornes ? | Ce sont des bornes pédagogiques choisies pour cette séance, pas une spécification du matériel réel. |
| Un champ manquant et une unité incohérente sont-ils la même gravité ? | Non : l'un bloque toute interprétation, l'autre laisse une valeur plausible mais mal étiquetée. |
| Pourquoi ne pas convertir 86,9 °F en Celsius plutôt que rejeter ? | Convertir silencieusement masquerait l'erreur de configuration qui a produit cette unité ; le rejet la rend visible. |
| Un silence expliqué par un rejet est-il sans importance ? | Non : il reste un signal de qualité de la source à surveiller, seulement pas un signal d'absence de transmission. |
| Peut-on affirmer que battery-shelter-01 est en panne ? | Non : le silence a plusieurs causes possibles ; seule une vérification terrain ou technique peut trancher. |

Commandes à exécuter et commenter :

```bash
python3 -m iot_decision.quality_cli data/samples/batch002_quality_messages.jsonl data/processed/batch002_measurements_clean.csv data/processed/batch002_rejected.csv data/processed/batch002_quality_report.json
python3 -m iot_decision.visualize_quality data/processed/batch002_measurements_clean.csv data/processed/batch002_rejected.csv sessions/s04_data_quality_uncertainty/slides/figures/batch002_quality_timeline.png
python3 tests/validate_s04_artifacts.py
```
