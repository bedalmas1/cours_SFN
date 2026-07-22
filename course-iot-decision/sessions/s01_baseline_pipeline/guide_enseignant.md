# Guide enseignant — Séquence 1

> **Conducteur opérationnel.** Pour chaque étape : afficher la diapositive indiquée, poser la question, laisser une réponse argumentée, puis faire exécuter les commandes. Les réponses ci-dessous sont les arguments attendus ; accepter toute formulation qui cite une preuve, une limite et une vérification.

## Règle de conduite et commandes

Toutes les commandes partent de la racine du dépôt. Les commandes de préparation sont :

```powershell
python -m pip install -r sessions/s01_baseline_pipeline/requirements.txt
$env:PYTHONPATH=src
python -m pytest -q
python tests/validate_s01_artifacts.py
docker compose -f docker/docker-compose.yml up -d --wait
python -m iot_decision.mqtt_tools seed data/samples/batch001_messages.jsonl
python -m iot_decision.mqtt_tools extract C:\tmp\s01_teacher_check.jsonl
(Get-Content C:\tmp\s01_teacher_check.jsonl).Count
Get-Content C:\tmp\s01_teacher_check.jsonl -First 1
```

Attendus : tests sans échec, validateur `S01 valide`, 15 enveloppes JSONL et cinq zones. Repli broker :

```powershell
python -m iot_decision.baseline_cli extract-sample data/samples/batch001_messages.jsonl data/raw/batch001_raw.jsonl
```

Fin de séance : `docker compose -f docker/docker-compose.yml down`.

## Carte des diapositives

Afficher successivement : **« Avant de regarder les données : votre décision »** (vote), **« Une donnée n'est pas encore une décision »**, **« Lire une chaîne de données comme une chaîne de responsabilités »**, **« Confiance et incertitude : deux questions différentes »**, **« Comprendre MQTT sans devenir administrateur réseau »**, **« Retained : le piège de la fraîcheur »**, **« Activité D / TP 1 — Extraction contrôlée »**, **« Brut, transformé, exploitable »**, **« Activité F / TP 2 — Du JSONL vers le CSV »**, **« Activité G / TP 3 — Produire et critiquer le graphique »**, **« Activité H / TP 4 — Le brief décisionnel »**, **« Activité I — Synthèse individuelle »**.

## Finalité et usage

Cette séquence installe le réflexe du cours : une pipeline transforme la portée de la preuve disponible pour agir. À la fin, les étudiants doivent décider si les mesures justifient de maintenir l'activité de maintenance drone prévue à 14 h, de déclencher une inspection, de sécuriser temporairement la zone ou de déclarer les données insuffisantes.

Une réponse recevable associe action, confiance argumentée, deux preuves retrouvables, deux incertitudes et vérification prioritaire. Une inspection ou un maintien sous réserve peuvent être défendus ; une certitude fondée sur le seul maximum, un seuil supposé normatif ou un retained ancien ne le peut pas.

- Les numéros renvoient au PDF de 48 diapositives.
- Toutes les commandes partent de la racine du dépôt dans PowerShell.
- Chaque question ci-dessous possède une direction d'animation et une réponse argumentée.
- Après chaque activité : **décision, confiance, preuve, incertitude, limite, vérification**.

## Préparation technique complète

```powershell
python -m pip install -r sessions/s01_baseline_pipeline/requirements.txt
$env:PYTHONPATH=src
python -m pytest -q
python tests/validate_s01_artifacts.py
```

Référence : `8 passed`, puis `15 messages conservés`, `15 mesures écrites` et `S01 valide: données, pipeline, figure et notebook exécutables.` Un avertissement `zmq` sous Windows est non bloquant si `S01 valide` apparaît.

Mode MQTT :

```powershell
docker compose -f docker/docker-compose.yml up -d --wait
python -m iot_decision.mqtt_tools seed data/samples/batch001_messages.jsonl
python -m iot_decision.mqtt_tools extract C:\tmp\s01_teacher_check.jsonl
(Get-Content C:\tmp\s01_teacher_check.jsonl).Count
Get-Content C:\tmp\s01_teacher_check.jsonl -First 1
```

Attendu : 15 enveloppes. Le broker anonyme reste sur `127.0.0.1`. Arrêt :

```powershell
docker compose -f docker/docker-compose.yml down
```

Plan de repli :

```powershell
$env:PYTHONPATH=src
python -m iot_decision.baseline_cli extract-sample data/samples/batch001_messages.jsonl data/raw/batch001_raw.jsonl
python -m iot_decision.baseline_cli transform data/raw/batch001_raw.jsonl data/processed/batch001_measurements.csv
python -m iot_decision.visualize_baseline data/processed/batch001_measurements.csv sessions/s01_baseline_pipeline/slides/figures/batch001_max_by_zone.png
python tests/validate_s01_artifacts.py
```

Consigner le changement de provenance si le repli remplace le broker.

## Conducteur — 240 minutes

| Temps | Conduite | Slides | Trace |
|---|---|---|---|
| 0:00–0:15 | mission et vote | 7–10 | vote, confiance, manque |
| 0:15–0:45 | donnée → décision | 11–16 | chaîne annotée |
| 0:45–1:10 | MQTT, topic, payload, retained | 18–23 | observe/conclus |
| 1:10–1:40 | TP 1 : extraction | 24–25 | JSONL contrôlé |
| 1:40–1:55 | fraîcheur et restitution | 26–28 | décision révisée |
| 1:55–2:05 | pause | 30 | — |
| 2:05–2:30 | brut/transformé/exploitable | 29, 31–32 | classement |
| 2:30–3:10 | TP 2 : CSV | 33–34 | CSV traçable |
| 3:10–3:35 | TP 3 : graphique | 35, 37–40 | PNG + limite |
| 3:35–3:55 | TP 4 : brief et revote | 41, 43–45 | note ≤120 mots |
| 3:55–4:00 | exit ticket | 47 | trois phrases |

## 1. Mission et vote — 15 min

**Afficher :** 7 à 10. Ne montrer ni fichier ni graphique. Lecture, vote individuel A–D, confiance de 0 à 100 %, puis échange en binôme.

| Question | Direction | Réponse et arguments |
|---|---|---|
| Quelle décision prenez-vous maintenant ? | Exiger un choix provisoire et séparer choix/confiance. | Plusieurs choix sont défendables. Le signal non consolidé autorise une action prudente et réversible, pas une conclusion thermique certaine. |
| Quelle preuve avez-vous réellement ? | Faire barrer les faits inventés. | Seulement une hausse possible signalée et l'existence annoncée de données ; aucune valeur, fraîcheur, couverture ou qualité n'est démontrée. |
| Quelle information renverserait votre choix ? | Exiger une observation précise. | Mesure récente batteries, durée, horodatage fiable, état terrain ou couverture. Elle doit agir directement sur le risque de poursuivre ou d'interrompre. |
| Quel est le coût d'une erreur ? | Distinguer faux négatif/faux positif. | Ignorer une hausse peut menacer matériel et mission ; interrompre à tort coûte du temps. Ce compromis impose confiance et réversibilité. |

## 2. Chaîne de responsabilité — 30 min

**Afficher :** 11 à 16. Attribuer une flèche de `capteur → message → donnée → indicateur → décision` à chaque binôme.

| Question | Direction | Réponse et arguments |
|---|---|---|
| Qu'entre-t-il et que sort-il à cette étape ? | Exiger objets et traces précis. | Phénomène → mesure → payload/topic → colonnes → résumé → action. Chaque passage peut perdre ou ajouter du contexte. |
| Quelle erreur peut naître ici ? | Exiger mécanisme puis conséquence. | Biais capteur, mauvais topic, temps faux, conversion erronée, maximum trompeur ; l'erreur devient opérationnelle si elle change le risque perçu ou l'action. |
| Une donnée est-elle déjà une décision ? | Faire nommer les éléments manquants. | Non : question, référentiel, seuil autorisé, coûts d'erreur et limites. Une valeur identique peut mener à des actions différentes selon le contexte. |
| Confiance et incertitude sont-elles opposées ? | Demander une phrase pour chacune. | Non. L'incertitude décrit l'inconnu ; la confiance qualifie la suffisance pour une action. Une conclusion limitée peut être solide malgré une incertitude globale. |
| La présence de messages suffit-elle pour agir ? | Refuser oui/non sans périmètre. | Elle prouve une disponibilité dans l'extraction, pas fraîcheur, exactitude, exhaustivité ni adéquation décisionnelle. |

## 3. Source MQTT — 25 min

**Afficher :** 18 à 23. Montrer d'abord un seul message.

| Question | Direction | Réponse et arguments |
|---|---|---|
| Où sont topic, payload et métadonnées ? | Faire pointer les champs. | Topic : routage ; payload : mesure déclarée ; enveloppe : réception et retained. Provenance et autorité diffèrent. |
| Le topic prouve-t-il la zone physique ? | Opposer convention et terrain. | Non. C'est une adresse déclarée ; une configuration erronée peut publier sous le mauvais topic. |
| Reçu maintenant signifie-t-il mesuré maintenant ? | Comparer `received_at`/`measured_at`. | Non. L'un date l'observation, l'autre est déclaré par le producteur ; un retained reçu maintenant peut être ancien. |
| Que prouve retained ? | Faire compléter « dernier… disponible… ». | Le dernier message retained disponible pour le topic correspondant, pas la fraîcheur, le fonctionnement actuel ou l'absence de pertes. |
| Le brut est-il vrai ? | Distinguer trace et vérité physique. | Il préserve ce qui fut reçu mais peut être faux, ancien ou mal étiqueté. Sa force est la traçabilité. |

## 4. TP 1 — Extraire — 45 min

**Afficher :** 24 pour la démonstration, 25 pour le travail, 26–28 au débrief.

```powershell
$env:PYTHONPATH=src
python -m iot_decision.mqtt_tools extract data/raw/batch001_raw.jsonl
Test-Path data/raw/batch001_raw.jsonl
(Get-Content data/raw/batch001_raw.jsonl).Count
Get-Content data/raw/batch001_raw.jsonl -First 1
Get-Content data/raw/batch001_raw.jsonl | Select-Object -Last 1
```

Repli :

```powershell
python -m iot_decision.baseline_cli extract-sample data/samples/batch001_messages.jsonl data/raw/batch001_raw.jsonl
```

Attendu : fichier présent, 15 lignes. Ne jamais l'éditer pour corriger une anomalie.

| Question | Direction | Réponse et arguments |
|---|---|---|
| Quel contrôle prouve une trace produite ? | Exiger chemin, existence, effectif. | `Test-Path`, nombre de lignes et lecture d'une ligne établissent existence et forme ; le code retour seul ne décrit pas le contenu. |
| Quelle métadonnée retrouve la source ? | Faire citer le champ exact. | Topic complet, horodatages et identifiant relient la donnée à l'observation. |
| Pourquoi ne pas éditer le brut ? | Imaginer une contestation. | Une correction silencieuse détruit la preuve et confond source, transformation et jugement. |
| Les zones sont-elles temporellement comparables ? | Révéler 27 après extraction. | Non sans comparer les horloges. Une mesure ancienne informe l'historique mais soutient moins une décision actuelle. |
| Faut-il supprimer une donnée ancienne ? | Interdire l'automatisme. | Jamais du brut. Elle peut être exclue selon une règle explicite, tout en restant conservée et signalée. |

## 5. Brut, transformé, exploitable — 25 min

**Afficher :** 29, 31 et 32.

| Question | Direction | Réponse et arguments |
|---|---|---|
| Quelles opérations changent la preuve ? | Tester conserver, renommer, convertir, agréger, supprimer, tracer. | Renommer, convertir, agréger et supprimer changent la représentation ; tracer un seuil ajoute une convention. Toute règle doit être traçable. |
| Plus lisible signifie-t-il plus vrai ? | Citer une vérification absente. | Non. Le CSV ne calibre pas le capteur, ne valide pas la zone ni la fraîcheur. |
| Qu'est-ce qui rend la transformation défendable ? | Exiger trois propriétés. | Règle explicite, reproductibilité et lien source, complétés par des contrôles d'effectif. |

## 6. TP 2 — Transformer — 40 min

**Afficher :** 33–34.

```powershell
$env:PYTHONPATH=src
python -m iot_decision.baseline_cli transform data/raw/batch001_raw.jsonl data/processed/batch001_measurements.csv
Test-Path data/processed/batch001_measurements.csv
(Import-Csv data/processed/batch001_measurements.csv).Count
Import-Csv data/processed/batch001_measurements.csv | Format-Table -AutoSize
Import-Csv data/processed/batch001_measurements.csv | Group-Object zone | Select-Object Name,Count
```

Attendu : 15 lignes, cinq zones ; relier une ligne CSV à son JSONL.

| Question | Direction | Réponse et arguments |
|---|---|---|
| Quel champ vient du payload ou de l'enveloppe ? | Ouvrir les fichiers côte à côte. | Valeur, unité et `measured_at` viennent du contenu ; topic, `received_at` et retained décrivent l'observation. |
| Pourquoi garder topic et received_at ? | Demander quel audit disparaît. | Sans topic, perte du routage ; sans réception, impossibilité de comparer mesure et observation. |
| Le CSV prouve-t-il la justesse du capteur ? | Chercher une calibration exécutée. | Non. Le script structure ; il ne compare pas à une référence physique. |
| Que prouve 15 vers 15 ? | Borner strictement. | Aucune ligne perdue par cette transformation réussie ; rien sur les pertes avant extraction. |

## 7. TP 3 — Visualiser — 25 min

**Afficher :** 35 avant l'exécution, 37–39 pour lire, 40 pour contredire.

```powershell
python -m iot_decision.visualize_baseline data/processed/batch001_measurements.csv sessions/s01_baseline_pipeline/slides/figures/batch001_max_by_zone.png
Test-Path sessions/s01_baseline_pipeline/slides/figures/batch001_max_by_zone.png
```

| Question | Direction | Réponse et arguments |
|---|---|---|
| À quelle question répond le graphique ? | Exiger une interrogation. | « Quel maximum fut observé par zone dans le lot ? » Pas la durée, la tendance ou l'état actuel. |
| Que voyez-vous, interprétez-vous, recommandez-vous ? | Imposer trois phrases. | Valeur visible ; sens prudent relatif au seuil ; action conditionnelle. Cela sépare fait, jugement et décision. |
| Que masque le maximum ? | Demander trois pertes. | Temporalité, durée, fréquence, dispersion, fraîcheur et valeurs intermédiaires. |
| 35 °C est-il une norme ? | Identifier l'autorité. | Non, seuil pédagogique ; en réel il doit être validé selon matériel, durée et conditions. |
| Quel indicateur alternatif ? | Relier indicateur et incertitude. | Durée au-dessus du seuil, dernière valeur, médiane ou âge de mesure selon la question. |

## 8. TP 4 — Brief et vote final — 20 min

**Afficher :** 41, 43, 44 puis 45. Prévoir cinq minutes d'écriture, quatre de contradiction, trois de révision, puis le vote. Le brief de 120 mots contient action, confiance, deux preuves retrouvables, deux incertitudes et vérification prioritaire.

| Question | Direction | Réponse et arguments |
|---|---|---|
| Quelle action proposez-vous exactement ? | Refuser « surveiller » sans acteur, objet ni échéance. | Maintenir sous réserve, inspecter avant 14 h, sécuriser temporairement ou différer jusqu'à vérification. |
| Où retrouve-t-on chaque preuve ? | Exiger fichier, zone et champ. | JSONL, CSV ou graphique dérivé avec topic/zone et horodatage ; une preuve introuvable n'est pas auditable. |
| Quelle hypothèse renverserait la décision ? | Donner un rôle de contradicteur. | Mesure ancienne, capteur mal étiqueté, seuil inadapté ou pic isolé ; chacune change le rapport risque/action. |
| Pourquoi ce niveau de confiance ? | Refuser le pourcentage décoratif. | Il augmente avec couverture, fraîcheur, traçabilité et cohérence ; il baisse avec seuil non autorisé, ancienneté et absence de terrain. |
| Quelle vérification réduit le mieux le risque ? | Comparer information, délai, réversibilité. | Mesure terrain ciblée ou confirmation récente de la zone critique, choisie selon l'hypothèse qui renverse l'action. |
| Pourquoi le vote a-t-il changé, ou non ? | Comparer les raisonnements. | Changement si preuve/limite modifie l'action ; stabilité si la pipeline renforce ou borne le raisonnement. Une baisse de confiance peut être correcte. |

## 9. Exit ticket — 5 min

**Afficher :** 47. Réponse individuelle sans écran.

| Amorce | Direction | Réponse et argument |
|---|---|---|
| La pipeline permet d'affirmer que… | Exiger périmètre et trace. | Les 15 messages extraits ont été conservés, transformés et résumés de façon reproductible pour cinq zones observées. |
| Elle ne permet pas d'affirmer que… | Rejeter « tout est fiable ». | Ni exactitude physique, ni fraîcheur uniforme, ni autorité du seuil, ni sécurité opérationnelle : ces propriétés ne furent pas testées. |
| Avant une action irréversible, je vérifierais… | Exiger une vérification discriminante. | Fraîcheur et état terrain de la zone critique, plus autorité du seuil. |

## Dépannage et clôture technique

| Symptôme | Commande ou contrôle | Décision pédagogique |
|---|---|---|
| Import impossible | `Get-Location`, puis `$env:PYTHONPATH=src` | Après deux essais, passer au repli et consigner la provenance. |
| Broker inaccessible | `docker compose -f docker/docker-compose.yml ps` | Utiliser `extract-sample` ; préserver le raisonnement. |
| JSONL vide | `Test-Path data/raw/batch001_raw.jsonl`, puis comptage | Rejouer l'extraction ; ne pas analyser un fichier non contrôlé. |
| CSV absent | vérifier entrée et `PYTHONPATH` | Relier l'incident à la rupture de traçabilité. |
| Figure impossible | vérifier dépendance et chemin ; utiliser la figure fournie | Maintenir la critique de l'indicateur. |

Validation finale à exécuter :

```powershell
python tests/validate_s01_artifacts.py
```

## Critères observables

L'étudiant distingue observation, interprétation et décision ; conserve le brut ; relie une ligne à sa source ; critique maximum et seuil ; formule une action bornée ; justifie sa confiance ; nomme une incertitude capable de renverser l'action ; propose une vérification réalisable.

## Sources

## Questions étudiantes — réponses argumentées

| Question | Argument attendu |
|---|---|
| Quelle preuve avant extraction ? | Un signal de supervision, pas une mesure consolidée. |
| Peut-on agir sur la présence de messages ? | Non : il faut périmètre, fraîcheur, contexte, qualité et règle d'action. |
| Le topic est-il la mesure ? | Non, c'est une adresse ; la mesure est dans le payload. |
| Que signifie retained ? | Dernier message conservé disponible, pas forcément récent ni actuel. |
| `measured_at` contre `received_at` ? | Temps déclaré de mesure contre temps de réception ; l'écart borne la fraîcheur. |
| Quel contrôle prouve une trace ? | `Test-Path`, comptage, lecture d'une ligne, puis contrôle des champs. |
| Le CSV est-il plus vrai ? | Non, seulement plus lisible et comparable. |
| Que perd le maximum ? | Durée, ordre, trous et fraîcheur ; il ne montre qu'un pic observé. |
| Le seuil de 35 °C est-il une norme ? | Non, seuil pédagogique à faire valider par le métier. |
| Quelle recommandation est défendable ? | Une action bornée, confiance explicite, preuves retrouvables et vérification prioritaire. |

Commandes à exécuter et commenter :

```powershell
python -m iot_decision.baseline_cli transform data/raw/batch001_raw.jsonl data/processed/batch001_measurements.csv
Test-Path data/processed/batch001_measurements.csv
(Import-Csv data/processed/batch001_measurements.csv).Count
Import-Csv data/processed/batch001_measurements.csv | Format-Table -AutoSize
Import-Csv data/processed/batch001_measurements.csv | Group-Object zone | Select-Object Name,Count
python -m iot_decision.visualize_baseline data/processed/batch001_measurements.csv sessions/s01_baseline_pipeline/slides/figures/batch001_max_by_zone.png
Test-Path sessions/s01_baseline_pipeline/slides/figures/batch001_max_by_zone.png
python tests/validate_s01_artifacts.py
```

Références complètes dans `latex/common/references.bib` et slide 48 : MQTT 5.0 (OASIS), RFC 8259, ISO 8601, JCGM 100, documentation pandas/matplotlib et NISTIR 8286A.
