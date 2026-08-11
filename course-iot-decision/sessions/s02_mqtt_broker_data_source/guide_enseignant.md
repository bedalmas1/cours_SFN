# Guide enseignant — Séquence 2

> **Conducteur opérationnel.** Afficher la diapositive indiquée, poser la question, faire justifier par un champ ou un fichier, puis exécuter la commande. Les réponses attendues donnent les arguments de débrief.

## Carte des diapositives

Afficher successivement : **« Activité A — Le broker répond : que décidez-vous ? »**, **« MQTT sépare publication, distribution et consommation »**, **« Le filtre définit votre champ de vision »**, **« Retained signifie “dernier état disponible” »**, **« TP 1 — Extraire la branche batch002 »**, **« TP 2 — Produire l'inventaire reproductible »**, **« Activité E — Classez les affirmations »**, **« TP 3 — Affichez d'abord les cinq attendus »**, **« Incident injecté — le capteur optronique attendu est absent »**, **« Le silence admet plusieurs causes concurrentes »**, **« TP 4 — Le brief tient en cinq éléments vérifiables »**, **« Vote final »**, **« Exit ticket »**.

## Finalité et usage

La séquence revient à la source : avant nettoyage, il faut établir ce qui fut réellement observé et par rapport à quel attendu. Les étudiants doivent décider si l'état observé du broker couvre suffisamment les zones critiques pour soutenir une analyse, sans confondre connexion, retained, fonctionnement du capteur et complétude métier.

Décision de référence : poursuivre l'analyse sur les quatre zones observées, ne pas généraliser à toute la base, vérifier en priorité la chaîne ou le terrain optronique. Confiance faible pour la couverture globale. Une autre action est recevable si son périmètre, ses preuves et son coût d'erreur sont défendus.

- Les numéros renvoient au PDF de 60 diapositives (la version augmentée ajoute quatre diapositives d'auto-vérification pour la relecture autonome).
- Toutes les commandes partent de la racine du dépôt dans un terminal Bash.
- Ne révéler ni les cinq attendus ni l'absence optronique avant les moments indiqués.
- Chaque question possède ci-dessous direction et réponse argumentée.

## Préparation technique complète

```bash
python3 -m pip install -r sessions/s02_mqtt_broker_data_source/requirements.txt
export PYTHONPATH=src
python3 -m pytest -q
python3 tests/validate_s02_artifacts.py
```

Référence : `8 passed`; puis `4/5 topics attendus observés`, `lot complet: non; confiance: faible`, le topic optronique absent et `S02 valide: inventaire reproductible et capteur optronique absent détecté.`

Mode broker :

```bash
docker compose -f docker/docker-compose.yml up -d --wait
python3 -m iot_decision.mqtt_tools seed data/samples/batch002_retained_messages.jsonl
python3 -m iot_decision.mqtt_tools extract /tmp/s02_teacher_check.jsonl --topic airbase/batch002/#
wc -l /tmp/s02_teacher_check.jsonl
head -n 1 /tmp/s02_teacher_check.jsonl
```

Attendu : quatre enveloppes. Ne pas annoncer « quatre sur cinq ». Arrêt :

```bash
docker compose -f docker/docker-compose.yml down
```

Plan de repli complet :

```bash
Copy-Item data/samples/batch002_retained_messages.jsonl data/raw/batch002_observed.jsonl -Force
python3 -m iot_decision.source_inventory_cli data/raw/batch002_observed.jsonl data/samples/batch002_expected_sensors.csv data/processed/batch002_inventory.csv data/processed/batch002_completeness.json
python3 tests/validate_s02_artifacts.py
```

## Conducteur — 240 minutes

| Temps | Conduite | Slides | Trace |
|---|---|---|---|
| 0:00–0:15 | situation et vote | 2–6 | choix, confiance, manque |
| 0:15–0:45 | rôles MQTT, topic et filtre | 7–11 | tableau des responsabilités |
| 0:45–1:05 | payload, enveloppe, retained | 12–15 | vrai/faux argumenté |
| 1:05–1:25 | TP 1 : extraction | 17–22 | observe/conclus |
| 1:25–1:55 | TP 2 : inventaire | 23–30 | CSV + mini-décision |
| 1:55–2:05 | pause | 31 | — |
| 2:05–2:30 | lot, attendu, complétude | 32–37 | classement |
| 2:30–3:15 | TP 3 : matrice et revue | 38–44 | matrice + taux |
| 3:15–3:40 | incident optronique | 45–50 | hypothèses/vérification |
| 3:40–3:55 | TP 4 : brief et vote | 51–56 | brief révisé |
| 3:55–4:00 | synthèse | 57–59 | exit ticket |

## 1. Vote initial — 15 min

**Afficher :** 2 à 6. Ne montrer aucun fichier. Choix A couverture suffisante, B inspection ciblée, C suspendre la conclusion globale, D impossible sans inventaire.

| Question | Direction | Réponse et arguments |
|---|---|---|
| Que décidez-vous ? | Exiger choix et confiance séparés. | C ou D sont les plus prudents, mais B peut être défendu. Une connexion et des retained ne démontrent pas le périmètre observé. |
| Quelle preuve est disponible ? | Interdire les faits non lus. | Le broker répond et contient des retained ; ni nombre, zones, fraîcheur ni exhaustivité ne sont connus. |
| Quelle information manque en priorité ? | Exiger un dénominateur ou périmètre. | La liste autorisée des topics/zones attendus et l'inventaire observé ; sans comparaison, « complet » n'a pas de sens. |
| Quel coût aurait une zone oubliée ? | Relier au scénario. | Une conclusion globale pourrait ignorer un risque matériel localisé ; le pourcentage global peut masquer une zone critique à 0 %. |

## 2. Qui sait quoi dans MQTT ? — 30 min

**Afficher :** 7 à 11. Attribuer publisher, broker et subscriber à des groupes ; faire compléter entrée, sortie, sait, ignore, erreur et effet décisionnel.

| Question | Direction | Réponse et arguments |
|---|---|---|
| Qui choisit le topic ? | Faire remonter à la publication. | Le publisher ou sa configuration choisit le topic ; le broker le route sans vérifier sa vérité métier. |
| Qui conserve un retained ? | Distinguer décision de publication et stockage. | Le publisher demande le retained ; le broker conserve le dernier message retained du topic selon le protocole. |
| Qui connaît la liste métier attendue ? | Demander si MQTT possède ce concept. | Ni le protocole ni le broker ; un référentiel métier externe définit les capteurs/zones attendus. |
| Le broker valide-t-il le payload ? | Opposer transport et sémantique. | Non par défaut. Il transporte des octets ; schéma, unité, cohérence et plausibilité relèvent de la chaîne applicative. |
| Topic et filtre sont-ils identiques ? | Faire écrire un exemple de chaque. | Non. Le topic est publié sans joker ; le filtre d'abonnement peut utiliser `+` ou `#` et définit le champ de vision du subscriber. |
| Que recevra `airbase/batch002/#` ? | Faire prédire avant l'extraction. | Les messages disponibles dont le topic commence par cette branche, notamment les retained correspondants ; pas un historique complet ni des topics hors branche. |

## 3. Payload, enveloppe et retained — 20 min

**Afficher :** 12 à 15. Faire répondre au vrai/faux avant de révéler les arguments.

| Question | Direction | Réponse et arguments |
|---|---|---|
| Quel champ vient du capteur et lequel de l'extraction ? | Faire pointer les deux niveaux. | `measured_at` est déclaré dans le payload ; `received_at` est ajouté lors de l'observation. Ils répondent à deux horloges différentes. |
| Retained signifie-t-il récent ? | Demander la preuve temporelle. | Faux. Il indique le dernier message retained disponible, sans borne d'âge. La fraîcheur exige un horodatage fiable et une règle métier. |
| Un retained prouve-t-il que le capteur fonctionne maintenant ? | Proposer un capteur éteint après publication. | Non. Le broker peut encore servir son dernier état après l'arrêt du capteur. |
| Un abonnement rejoue-t-il tout l'historique ? | Distinguer retained et journal. | Non. MQTT n'est pas par lui-même un stockage historique ; on reçoit les publications futures et les retained correspondants. |
| Qu'autorise une enveloppe bien formée ? | Borner la conclusion. | Elle autorise parsing et traçabilité de l'observation, pas validation physique ou complétude métier. |

## 4. TP 1 — Explorer — 20 min

**Afficher :** 17–22. Faire prédire, extraire, contrôler, puis interpréter.

```bash
export PYTHONPATH=src
python3 -m iot_decision.mqtt_tools extract data/raw/batch002_observed.jsonl --topic airbase/batch002/#
test -f data/raw/batch002_observed.jsonl && echo "présent"
wc -l data/raw/batch002_observed.jsonl
head -n 1 data/raw/batch002_observed.jsonl
```

Repli :

```bash
Copy-Item data/samples/batch002_retained_messages.jsonl data/raw/batch002_observed.jsonl -Force
```

Attendu : `4 messages extraits`, `True`, `4`, puis une enveloppe avec topic, réception, retained et payload. Ne pas encore dire « 4/5 ».

| Question | Direction | Réponse et arguments |
|---|---|---|
| Combien de topics avez-vous observés ? | Exiger commande et effectif. | Quatre enveloppes/topics dans cette extraction ; la formulation reste liée au filtre et à l'instant d'observation. |
| Quel filtre définit le champ de vision ? | Faire recopier exactement. | `airbase/batch002/#`. Toute conclusion hors de cette branche serait sans preuve. |
| Quels champs appartiennent à l'enveloppe ou au payload ? | Faire annoter une ligne. | Topic, réception et retained décrivent l'observation ; zone/capteur/mesure et `measured_at` sont déclarés dans le payload. |
| Peut-on conclure à la complétude ? | Interdire le comptage sans attendu. | Non. Quatre est un numérateur sans dénominateur métier autorisé. |
| Quelle phrase est défendable ? | Imposer « observé avec… ». | « Quatre topics ont été observés avec le filtre `airbase/batch002/#` lors de cette extraction. » |

## 5. TP 2 — Construire l'inventaire — 30 min

**Afficher :** 23–30. La CLI produit déjà le diagnostic ; demander de contrôler le CSV avant d'ouvrir le JSON.

```bash
python3 -m iot_decision.source_inventory_cli data/raw/batch002_observed.jsonl data/samples/batch002_expected_sensors.csv data/processed/batch002_inventory.csv data/processed/batch002_completeness.json
test -f data/processed/batch002_inventory.csv && echo "présent"
head -n 5 data/processed/batch002_inventory.csv
tail -n +2 data/processed/batch002_inventory.csv | wc -l
tail -n +2 data/processed/batch002_inventory.csv | cut -d, -f1 | sort -u | wc -l
```

Attendu : quatre lignes et quatre topics uniques, zones batteries, transmissions, informatique et maintenance. Masquer encore le référentiel affiché et la zone absente.

| Question | Direction | Réponse et arguments |
|---|---|---|
| Quelles quatre zones sont observées ? | Faire citer CSV et topics. | Batteries, transmissions, informatique, maintenance ; chaque affirmation doit être reliée à sa ligne/topic. |
| Quelle colonne conserve le périmètre interrogé ? | Faire distinguer topic et zone. | Le topic complet conserve la branche et l'identité logique ; la zone seule agrégerait trop tôt. |
| Pourquoi conserver les deux horloges ? | Demander quel délai elles permettent d'étudier. | Elles séparent temps déclaré de mesure et temps d'observation, donc permettent d'évaluer fraîcheur et latence apparente. |
| Pourquoi « topics observés » plutôt que « capteurs fonctionnels » ? | Demander ce que l'extraction teste physiquement. | L'extraction constate des messages disponibles ; elle ne teste ni alimentation, calibration ni fonctionnement actuel. |
| Que perd-on en regroupant sous « température » ? | Faire supprimer mentalement topic/zone. | Localisation, identité du capteur, provenance, criticité et possibilité de contester l'agrégation. |
| L'inventaire est-il exhaustif ? | Exiger un référentiel avant réponse. | Il est exhaustif pour les quatre lignes effectivement extraites, pas nécessairement pour le besoin métier. |

## 6. Lot et complétude — 25 min

**Afficher :** 32–37. Garder le CSV attendu fermé pendant le classement, puis le révéler.

| Question | Direction | Réponse et arguments |
|---|---|---|
| Qu'est-ce qu'un lot MQTT ? | Refuser l'idée d'un objet protocolaire natif. | Un périmètre construit par filtre, fenêtre d'observation et règle de collecte ; MQTT ne fournit pas seul début, fin ou exhaustivité. |
| Complet par rapport à quoi ? | Écrire numérateur/dénominateur. | Aux topics attendus d'un référentiel autorisé, pour un site, une mission et une date définis. |
| « Quatre topics uniques » est-il observable ? | Faire citer le CSV. | Oui, comptage direct de l'inventaire. |
| « Toutes les zones attendues sont présentes » est-il observable ? | Exiger le dénominateur. | Vérifiable seulement par comparaison avec un référentiel attendu. |
| « Aucun message perdu » est-il démontrable ? | Chercher une preuve d'émission indépendante. | Non ici : il faudrait journaux publisher, séquences ou accusés permettant de comparer émis et reçu. |
| « Tous les retained sont récents » est-il démontrable ? | Chercher horloge et règle. | Pas par retained seul ; il faut `measured_at` fiable et seuil de fraîcheur métier. |
| Qui autorise le référentiel ? | Relier gouvernance et mission. | Responsable métier/technique compétent pour le site et la période ; le CSV est supposé valide ici, mais cette hypothèse reste une limite. |

## 7. TP 3 — Comparer attendu et observé — 45 min

**Afficher :** 38–44. Faire construire la matrice manuellement avant le diagnostic automatisé.

```bash
head -n 6 data/samples/batch002_expected_sensors.csv
tail -n +2 data/samples/batch002_expected_sensors.csv | wc -l
python3 -m json.tool data/processed/batch002_completeness.json
python3 -m json.tool data/processed/batch002_completeness.json
```

Attendu : cinq topics attendus, quatre observés, `complete=False`, confiance faible, topic optronique absent. Formulation : « 80 % des topics attendus observés », jamais « 80 % de la base sûre ».

| Question | Direction | Réponse et arguments |
|---|---|---|
| Quel est le numérateur ? | Faire pointer les intersections. | Quatre topics attendus effectivement observés. Un topic inattendu ne devrait pas augmenter ce numérateur. |
| Quel est le dénominateur ? | Faire citer source et autorité. | Cinq topics du référentiel supposé valide pour ce site et cette mission. |
| Quelle zone est absente ? | Exiger le topic complet. | Optronique : `airbase/batch002/optronics-shelter-01/temperature`. |
| Pourquoi 80 % peut-il tromper ? | Comparer global et zone. | Le taux global masque 0 % de couverture optronique ; la criticité n'est pas uniformément distribuée. |
| Le calcul exact rend-il le référentiel vrai ? | Séparer calcul et hypothèse. | Non. Le calcul peut être reproductible tout en reposant sur un référentiel obsolète ou non autorisé. |
| Que doit attaquer la revue croisée ? | Interdire l'attaque personnelle. | Filtre, fichiers, dénominateur, unicité, autorité du référentiel et formulation de la conclusion. |

## 8. Incident optronique — 25 min

**Afficher :** 45 seulement à 3:15, puis 46–49. Imposer plusieurs causes concurrentes avant toute action.

| Question | Direction | Réponse et arguments |
|---|---|---|
| Le capteur est-il en panne ? | Refuser la cause unique. | C'est une hypothèse compatible, pas une conclusion. Non-publication, retained supprimé, filtre, extraction ou référentiel peuvent produire le même silence. |
| Que prouve exactement le silence ? | Faire revenir à la matrice. | L'absence du topic dans cette observation avec ce filtre ; ni cause, ni température, ni état physique. |
| Quelle vérification distingue filtre et non-publication ? | Exiger deux hypothèses départagées. | Rejouer/élargir l'abonnement et consulter les journaux publisher/passerelle. Une observation hors filtre renforce l'erreur d'extraction ; aucune publication enregistrée renforce la non-publication. |
| Quelle vérification distingue chaîne et état thermique ? | Opposer données et terrain. | Journaux/configuration testent la chaîne ; mesure terrain indépendante teste l'état physique. L'une ne remplace pas l'autre. |
| Quelle vérification faire en premier ? | Comparer délai, valeur d'information et risque. | Une mesure terrain optronique est prioritaire si l'état matériel conditionne l'action immédiate ; en parallèle, journaux et filtre réduisent l'incertitude de chaîne à faible coût. |
| Peut-on remplacer l'absence par une température normale ? | Faire verbaliser la donnée inventée. | Non. Imputer « normal » transformerait un manque en preuve rassurante et créerait un faux négatif possible. |

## 9. TP 4 — Brief contradictoire — 15 min

**Afficher :** 51–56. Cinq minutes d'écriture, quatre d'interrogation, trois de révision, trois de vote. Le brief de 120 mots contient action, périmètre, confiance, deux preuves, deux incertitudes et vérification.

| Question | Direction | Réponse et arguments |
|---|---|---|
| Votre phrase vaut-elle pour quatre zones ou cinq ? | Faire surligner les preuves correspondantes. | Seulement quatre zones sont observées ; toute conclusion sur cinq généralise au-delà de la preuve. |
| Où retrouvez-vous vos deux preuves ? | Exiger fichier et champ/topic. | Inventaire CSV pour les quatre observés ; diagnostic/référentiel pour 4/5 et le topic absent. |
| Que signifie votre confiance ? | Relier au périmètre. | Confiance raisonnable dans l'inventaire limité ; faible pour la couverture globale, car une zone critique manque et la cause est inconnue. |
| Que ne savez-vous toujours pas ? | Chercher deux incertitudes décisionnelles. | Cause du silence et état thermique optronique ; également fraîcheur/autorité du référentiel selon le brief. |
| Quelle action reste réversible ? | Refuser l'inaction vague. | Continuer l'analyse des quatre zones, suspendre la conclusion globale et lancer une vérification optronique ciblée. |
| Quelle objection renverse votre recommandation ? | Faire jouer le décideur critique. | Si le référentiel est obsolète, l'absence peut être artificielle ; si l'optronique est critique et chaude, poursuivre sans terrain devient dangereux. |

## 10. Synthèse et exit ticket — 5 min

**Afficher :** 57–59. Réponse individuelle sans écran.

| Amorce | Direction | Réponse et argument |
|---|---|---|
| L'inventaire permet d'affirmer que… | Exiger filtre et périmètre. | Quatre topics précis ont été observés dans `airbase/batch002/#` et conservés de façon reproductible. |
| Il ne permet pas d'affirmer que… | Rejeter panne ou normalité sans preuve. | Ni complétude globale, ni fonctionnement actuel, ni température optronique, ni cause du silence. |
| Avant de conclure pour toute la base… | Exiger une action. | Vérifier le topic/chaîne optronique et, si l'enjeu l'impose, effectuer une mesure terrain. |

## Dépannage et validation finale

| Symptôme | Commande ou contrôle | Décision pédagogique |
|---|---|---|
| Import impossible | `pwd`, puis `export PYTHONPATH=src` | Deux essais, puis repli en consignant la provenance. |
| Broker inaccessible | `docker compose -f docker/docker-compose.yml ps` | Copier l'échantillon ; conserver le filtre dans le journal. |
| Extraction vide | vérifier seed, port et filtre | Ne pas révéler le référentiel pour résoudre un problème technique. |
| CSV absent | `test -e` sur JSONL et les quatre arguments CLI | Diagnostiquer dans l'ordre chemin, entrée, environnement. |
| JSON incohérent | reconstruire via `source_inventory_cli` | Ne pas éditer manuellement le diagnostic. |

```bash
python3 tests/validate_s02_artifacts.py
```

## Critères observables

L'étudiant borne le champ de vision par le filtre ; distingue enveloppe et payload ; formule « topics observés » ; construit le dénominateur ; localise le manque ; sépare absence et cause ; choisit une vérification discriminante ; produit une recommandation limitée et traçable.

## Sources

## Questions étudiantes — réponses argumentées

| Question | Argument attendu |
|---|---|
| Que prouve la connexion ? | Une disponibilité ponctuelle, jamais la complétude métier. |
| `#` est-il publié ? | Non, c'est un joker du filtre. |
| Le filtre donne-t-il tout l'historique ? | Non ; seulement les messages disponibles correspondant au filtre. |
| Que prouve retained ? | Un dernier message conservé disponible, pas sa fraîcheur. |
| Que prouve l'inventaire ? | Quatre topics observés avec ce filtre et cette extraction, pas quatre capteurs fonctionnels. |
| Complet par rapport à quoi ? | À un référentiel métier autorisé et daté. |
| Pourquoi 4/5 ne suffit pas ? | Une zone critique peut être à 0 % malgré 80 % global. |
| Le silence prouve-t-il une panne ? | Non : panne, publication, filtre, extraction et référentiel sont des hypothèses concurrentes. |
| Quelle vérification discrimine ? | Rejouer/élargir le filtre, consulter les journaux, vérifier retained/référentiel, puis terrain. |
| Décision finale ? | Analyse limitée aux quatre zones ; pas de conclusion globale ; vérification optronique prioritaire. |

Commandes à exécuter et commenter :

```bash
python3 -m iot_decision.mqtt_tools extract data/raw/batch002_observed.jsonl --topic airbase/batch002/#
test -f data/raw/batch002_observed.jsonl && echo "présent"
wc -l data/raw/batch002_observed.jsonl
head -n 1 data/raw/batch002_observed.jsonl
python3 -m iot_decision.source_inventory_cli data/raw/batch002_observed.jsonl data/samples/batch002_expected_sensors.csv data/processed/batch002_inventory.csv data/processed/batch002_completeness.json
test -f data/processed/batch002_inventory.csv && echo "présent"
head -n 5 data/processed/batch002_inventory.csv
tail -n +2 data/processed/batch002_inventory.csv | wc -l
tail -n +2 data/processed/batch002_inventory.csv | cut -d, -f1 | sort -u | wc -l
head -n 6 data/samples/batch002_expected_sensors.csv
tail -n +2 data/samples/batch002_expected_sensors.csv | wc -l
python3 -m json.tool data/processed/batch002_completeness.json
python3 tests/validate_s02_artifacts.py
```

Références complètes dans `latex/common/references.bib` et slide 60 : MQTT 5.0 (OASIS) et documentation officielle Eclipse Mosquitto pour topics, filtres, abonnements et retained.

## Note sur la version augmentée du support (relecture autonome)

Quatre diapositives « Auto-vérification avant de continuer » ont été ajoutées (16, 29, 37, 50) : elles rappellent des définitions déjà vues, sans révéler de nouveau résultat sur le cas d'étude, et peuvent être montrées en fin de section ou laissées à la relecture individuelle. La diapositive 59 (« Réponse à la question directrice ») reste, comme avant, le seul endroit qui révèle explicitement le résultat de référence (4/5, absence optronique, confiance faible) : à n'afficher qu'après le vote final et le rendu du brief de TP 4.
