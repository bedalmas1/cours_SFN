# Guide enseignant — Séquence 7

> **Conducteur opérationnel.** Pour chaque étape : afficher la diapositive indiquée, poser la question, laisser une réponse argumentée, puis seulement exécuter les commandes. Les réponses ci-dessous sont les arguments attendus ; accepter toute formulation qui cite une preuve, une limite et une vérification.

## Règle de conduite et commandes

Toutes les commandes partent de la racine du dépôt. Cette séquence est la première depuis la séquence 2 à nécessiter Docker : elle démarre deux brokers Mosquitto en parallèle (ouvert et protégé) pour la démonstration du matin, puis travaille hors broker sur un fichier JSONL l'après-midi.

```bash
python3 -m pip install -r sessions/s07_security_trust_robustness/requirements.txt
export PYTHONPATH=src
docker compose -f docker/docker-compose.yml up -d --wait mosquitto mosquitto-protected
python3 -m pytest -q
python3 tests/validate_s07_artifacts.py
```

Attendus : tests sans échec, diagnostic `1 doublon(s) exact(s)`, `1 candidat(s) de rejeu`, `1 incohérence(s) temporelle(s)`, `silence non expliqué maximal 15 min`, `suspicion data/cyber: probabilité forte, impact élevé`, `S07 valide`.

**Point de vigilance : les identifiants `capteur-lora` / `superviseur` du broker protégé sont documentés en clair dans `docker/mosquitto/README.md` pour un usage strictement local (`127.0.0.1`). Ne jamais les présenter comme un modèle de gestion de secrets en production.**

## Carte des diapositives

Afficher successivement : **« Bienvenue dans la séquence 7 »**, **« Le scénario — des messages incohérents »** (vote), **« Intégrité / Authentification / ACL / Injection / Rejeu »**, **« Démonstration — broker ouvert vs broker protégé »**, **« Ce que révèle la démonstration »**, **« Exercice — identifier les vulnérabilités »**, **« Débrief — ce que l'ACL protège »**, **« Confiance dans la source / dans le traitement »**, **« Démonstration — diagnostiquer un lot suspect »**, **« Activité — Analyse d'un lot suspect »**, **« Matrice des risques data/cyber »**, **« Décision — peut-on agir sur ces données ? »**, **« Activité — Synthèse individuelle »**.

## Finalité et usage

Cette séquence relie deux moitiés d'une même idée. Le matin : l'authentification et l'ACL protègent des catégories précises et limitées d'abus — connexion anonyme, dépassement de périmètre — mais un abus de droits sur un compte pourtant authentifié échoue **silencieusement**, sans jamais alerter l'émetteur. L'après-midi : un message peut franchir tous les contrôles de qualité de la séquence 4 (champ, unité, plage, horodatage futur) et rester malgré tout un rejeu, détectable seulement en croisant son identité avec celle d'autres messages. Les étudiants doivent finir la séance capables de classer plusieurs hypothèses concurrentes par probabilité et impact, et de décider s'il est raisonnable d'agir sur un lot dont la chaîne n'est pas qualifiée.

Décision de référence : ne pas agir directement sur `batch004_suspect_scenario.jsonl` ; isoler le lot, vérifier l'identité et la source des messages suspects avant toute décision opérationnelle.

- Toutes les commandes partent de la racine du dépôt dans un terminal Bash.
- Chaque question ci-dessous possède une direction d'animation et une réponse argumentée.
- Après chaque activité : **décision, confiance, preuve, incertitude, limite, vérification**.

## Conducteur — 240 minutes

| Temps | Conduite | Objectif | Trace |
|---|---|---|---|
| 0:00–0:15 | accroche : messages incohérents | révéler qu'une valeur plausible ne garantit rien sur l'identité du message | choix, confiance, information manquante |
| 0:15–0:45 | intégrité, authentification, ACL, injection, rejeu | poser le vocabulaire de sécurité relié à la décision | fiche concept annotée |
| 0:45–1:25 | démonstration : broker ouvert vs protégé | observer un refus explicite et un rejet silencieux | tableau de résultats observés |
| 1:25–1:55 | exercice : vulnérabilités d'une chaîne MQTT | relier chaque protection à ce qu'elle couvre, ou non | liste de vulnérabilités annotée |
| 1:55–2:05 | pause | — | — |
| 2:05–2:30 | confiance dans la source, confiance dans le traitement | distinguer deux confiances jamais garanties par les mêmes contrôles | fiche concept annotée |
| 2:30–3:15 | analyse d'un lot suspect | diagnostiquer sans recalculer, seulement en croisant les signaux | diagnostic complet |
| 3:15–3:40 | matrice des risques data/cyber | classer quatre hypothèses par probabilité et impact | matrice remplie |
| 3:40–3:55 | décision : peut-on agir sur ces données ? | recommander en connaissance des limites de la chaîne | recommandation argumentée |
| 3:55–4:00 | exit ticket | transfert individuel | trois phrases |

## 1. Accroche et vote initial — 15 min

**Afficher :** la diapositive du scénario. Montrer un extrait de `comms-shelter-01` (deux messages : un avec horodatage futur, un qui semble revenir sur une mesure déjà vue). Ne pas encore exécuter le diagnostic.

| Question | Direction | Réponse et arguments |
|---|---|---|
| Que décidez-vous sur la seule base de ce constat ? | Exiger un choix provisoire et séparer choix/confiance. | Plusieurs choix sont défendables ; beaucoup de groupes proposent d'isoler la zone concernée. |
| La valeur mesurée elle-même est-elle en cause ? | Faire vérifier explicitement. | Non : les deux valeurs sont dans une plage parfaitement normale pour la zone. |
| Que pourrait alors signaler cette incohérence, si ce n'est pas la mesure ? | Orienter vers l'identité du message plutôt que sa valeur. | Un problème dans le message lui-même : son horodatage, son unicité, ou son identité. |

Débrief : une valeur plausible ne garantit rien sur l'identité ou la fraîcheur réelle du message qui la porte.

## 2. Intégrité, authentification, ACL, injection, rejeu — 30 min

**Afficher :** la diapositive des cinq concepts.

| Concept | Définition | Piège fréquent | Effet décisionnel |
|---|---|---|---|
| Intégrité | Garantie qu'un message reçu est identique à celui émis. | La confondre avec l'exactitude de la mesure d'origine. | Un message intègre peut transporter une valeur fausse dès la source. |
| Authentification | Vérification de l'identité d'un client avant connexion. | Croire qu'un broker local (`127.0.0.1`) n'en a pas besoin. | Sans elle, tout client atteignant le port peut se faire passer pour un capteur légitime. |
| ACL | Permissions précises par utilisateur et par topic. | Croire que l'authentification seule suffit. | Un compte authentifié mais non restreint accède à tout. |
| Injection | Message introduit qui ne provient d'aucun capteur légitime. | Supposer qu'il sera forcément une valeur absurde. | Une valeur plausible injectée influence une décision comme un message authentique. |
| Rejeu | Republication d'un message déjà vu, sous une identité différente. | Le chercher uniquement parmi les messages strictement identiques. | Fait réapparaître une mesure ancienne à un moment où elle ne reflète plus la situation réelle. |

Questions : un contrôle qui vérifie qu'un horodatage n'est pas dans le futur suffit-il à détecter un rejeu ? Pourquoi un broker strictement local peut-il quand même être attaqué ?

## 3. Démonstration — broker ouvert vs broker protégé — 40 min

**Afficher :** la démonstration, puis exécuter en direct.

```bash
docker compose -f docker/docker-compose.yml up -d --wait mosquitto mosquitto-protected
mosquitto_pub -h 127.0.0.1 -p 1883 -t airbase/test -m hello   # anonyme, broker ouvert
mosquitto_pub -h 127.0.0.1 -p 1884 -t airbase/test -m hello   # anonyme, broker protégé
```

Attendu : la première commande réussit silencieusement ; la seconde échoue avec `Connection Refused: not authorised`.

```bash
mosquitto_pub -h 127.0.0.1 -p 1884 -u capteur-lora -P s07-capteur-demo -t airbase/test -m hello   # ACL autorise
mosquitto_pub -h 127.0.0.1 -p 1884 -u superviseur -P s07-superviseur-demo -t airbase/test -m hello   # ACL refuse
```

Attendu : les deux commandes se terminent **sans erreur visible**, mais seul le premier message est réellement délivré ; un abonné autorisé (`superviseur`) ne voit jamais apparaître le second.

| Question | Direction | Réponse et arguments |
|---|---|---|
| Le refus anonyme sur le broker protégé est-il explicite ou silencieux ? | Faire lire le message d'erreur exact. | Explicite : `Connection Refused: not authorised`, visible immédiatement par l'émetteur. |
| Le rejet du message de `superviseur` par l'ACL est-il explicite ou silencieux ? | Faire comparer les deux codes de sortie. | Silencieux : la commande se termine avec succès apparent ; seul un abonné autorisé peut constater l'absence du message. |
| Quelle conséquence pratique cette différence a-t-elle pour la supervision d'une flotte de capteurs ? | Faire formuler une pratique. | Surveiller les journaux du broker et la réception effective, pas seulement le code de retour des clients publieurs. |

## 4. Exercice — identifier les vulnérabilités d'une chaîne MQTT — 30 min

**Afficher :** l'exercice puis le débrief.

| Question | Direction | Réponse et arguments |
|---|---|---|
| Le broker ouvert accepte-t-il des clients anonymes ? Que permet cela à un tiers ? | Faire nommer le risque précis. | Oui ; un tiers peut publier ou lire n'importe quel topic sans jamais s'identifier. |
| Une ACL empêche-t-elle un compte compromis de lire les topics d'une autre zone ? | Faire vérifier sur le fichier `acl.conf`. | Oui pour la lecture hors périmètre déclaré ; non pour tout ce que l'ACL autorise déjà à ce compte. |
| Les mots de passe et les messages transitent-ils chiffrés dans ce laboratoire ? | Refuser toute affirmation non vérifiée sur le TLS. | Non : ce laboratoire n'active pas TLS ; seul le port lié à `127.0.0.1` limite l'exposition. |
| Un message parfaitement authentifié et autorisé peut-il quand même être un rejeu ? | Relier à l'activité de l'après-midi. | Oui : l'authentification et l'ACL vérifient qui envoie, jamais si ce contenu a déjà été envoyé. |

## 5. Confiance dans la source, confiance dans le traitement — 25 min

**Afficher :** la diapositive de transition puis les deux concepts.

| Concept | Définition | Piège fréquent | Effet décisionnel |
|---|---|---|---|
| Confiance dans la source | Certitude que le message provient bien du capteur, de la zone et de l'instant annoncés. | L'assimiler à la plausibilité de la valeur mesurée. | Une source usurpée peut transmettre une valeur parfaitement crédible. |
| Confiance dans le traitement | Certitude que la pipeline qui reçoit le message ne l'altère pas et ne masque pas ses anomalies. | Croire qu'un contrôle qualité (séquence 4) couvre les anomalies de sécurité. | Un traitement qui ne croise jamais l'identité des messages ne peut détecter un rejeu. |

Question : un message peut-il franchir tous les contrôles de qualité de la séquence 4 et rester un rejeu ? (Réponse attendue : oui, et l'activité suivante le démontre.)

## 6. Analyse d'un lot suspect — 45 min

**Afficher :** la démonstration puis le travail.

```bash
export PYTHONPATH=src
python3 -m iot_decision.chain_trust_cli data/samples/batch004_suspect_scenario.jsonl
```

Attendu : `1 doublon(s) exact(s)`, `1 candidat(s) de rejeu`, `1 incohérence(s) temporelle(s)`, `silence non expliqué maximal 15 min`.

| Question | Direction | Réponse et arguments |
|---|---|---|
| Quelle mesure porte le candidat de rejeu ? | Faire retrouver la ligne exacte dans le JSONL. | `comms-shelter-01`, 29,3\,°C mesurée à 09:40, republiée sous `comms-shelter-01-replay-x` à 10:10. |
| Cette mesure aurait-elle été rejetée par les contrôles de la séquence 4 ? | Faire vérifier chaque contrôle un par un. | Non : aucun champ manquant, unité correcte, valeur dans la plage, horodatage de mesure antérieur à la réception. |
| Un seul de ces quatre signaux, pris isolément, aurait-il suffi à alerter ? | Refuser une réponse binaire globale. | Le doublon exact et l'incohérence temporelle sont chacun détectables seuls ; le candidat de rejeu ne l'est que par recoupement d'identité, jamais par un contrôle ligne à ligne. |

## 7. Matrice des risques data/cyber — 25 min

**Afficher :** la matrice.

| Hypothèse | Probabilité | Impact | Justification |
|---|---|---|---|
| Suspicion data/cyber | forte | élevé | candidat de rejeu + incohérence temporelle |
| Problème réseau | forte | moyen | silence non expliqué de 15 min |
| Panne capteur | moyenne | moyen | 1 retransmission exacte détectée |
| Incident réel | faible | élevé | aucun franchissement de seuil observé |

| Question | Direction | Réponse et arguments |
|---|---|---|
| Ces quatre hypothèses s'excluent-elles mutuellement ? | Refuser l'exclusivité. | Non : un problème réseau et une suspicion data/cyber peuvent coexister sur le même lot. |
| Pourquoi « incident réel » reste-t-elle en dernière position malgré un impact élevé ? | Faire relier probabilité et impact séparément. | Parce qu'aucune valeur mesurée ne franchit un seuil : rien dans ce lot ne soutient cette hypothèse en probabilité, même si sa gravité potentielle reste élevée. |

## 8. Décision — peut-on agir sur ces données ? — 15 min

**Afficher :** la diapositive de décision.

| Question | Direction | Réponse et arguments |
|---|---|---|
| Peut-on agir directement sur ce lot ? | Exiger une réponse tranchée et justifiée. | Non : isoler le lot, vérifier l'identité et la source des messages suspects avant toute décision opérationnelle. |
| Cette recommandation revient-elle à rejeter le lot ? | Nuancer. | Non : elle retarde son usage jusqu'à vérification, elle ne le disqualifie pas définitivement. |

## Exit ticket — 5 min

**Afficher :** la diapositive finale. Réponse individuelle sans écran.

| Amorce | Direction | Réponse et argument |
|---|---|---|
| Un message peut être valide au sens de la séquence 4 et pourtant… | Exiger la distinction qualité/sécurité. | Rester un rejeu ou une injection, car ces contrôles ne vérifient jamais l'identité d'un message entre eux. |
| L'authentification protège contre… ; l'ACL protège en plus contre… | Exiger les deux catégories distinctes. | La connexion anonyme non autorisée ; le dépassement du périmètre d'un compte pourtant authentifié. |
| Avant d'agir sur un lot dont la chaîne n'est pas qualifiée, je vérifierais… | Exiger une action concrète. | L'identité et la source des messages suspects, en priorité ceux signalés par un recoupement, pas seulement par un contrôle de valeur. |

## Dépannage et clôture technique

| Symptôme | Commande ou contrôle | Décision pédagogique |
|---|---|---|
| Broker protégé ne démarre pas (exit 13) | `docker logs iot-decision-mosquitto-protected` | Vérifier que les montages de `acl.conf`/`passwd` ne sont pas en lecture seule (`:ro`) ; l'entrypoint doit pouvoir en ajuster les permissions. |
| Import impossible | `pwd`, puis `export PYTHONPATH=src` | Après deux essais, passer au repli et consigner la provenance. |
| Fichier suspect absent | `test -f data/samples/batch004_suspect_scenario.jsonl` | Ne jamais inventer de valeurs ; fournir directement la sortie CLI de référence. |
| Un étudiant conclut au bug plutôt qu'à un rejeu | reprojeter la ligne JSONL du candidat de rejeu | Faire vérifier chaque contrôle de la séquence 4 un par un sur cette ligne précise. |

Validation finale à exécuter :

```bash
python3 tests/validate_s07_artifacts.py
docker compose -f docker/docker-compose.yml down
```

## Critères observables

L'étudiant distingue intégrité, authentification et ACL sans les confondre ; observe qu'un refus de connexion est explicite alors qu'un rejet ACL au niveau d'un message est silencieux ; identifie qu'un candidat de rejeu peut franchir tous les contrôles de qualité de la séquence 4 ; classe les quatre hypothèses par probabilité et impact sans les traiter comme mutuellement exclusives ; recommande d'isoler plutôt que de rejeter ou d'ignorer le lot.

## Sources

Configuration ACL et identifiants documentés dans `docker/mosquitto/README.md` ; règles de diagnostic documentées dans `src/iot_decision/chain_trust.py` ; références de sécurité IoT en fin de diaporama.

## Questions étudiantes — réponses argumentées

| Question | Argument attendu |
|---|---|
| Pourquoi le rejet ACL est-il silencieux alors que le refus de connexion est explicite ? | Le protocole MQTT distingue l'établissement de connexion, qui peut être refusé avec un code visible, du traitement d'un message publié, où le broker peut appliquer une ACL sans notifier l'émetteur. |
| `capteur-lora` et `superviseur` sont-ils des comptes réels ? | Non : des identifiants pédagogiques strictement locaux, documentés en clair dans `docker/mosquitto/README.md`, à ne jamais réutiliser au-delà de ce laboratoire. |
| Le module `chain_trust.py` recalcule-t-il de nouveaux contrôles ? | Non : il relit uniquement les signaux déjà produits par `quality.classify` et `traceability.duplicate_candidates`, puis les relie à des hypothèses. |
| Pourquoi la même mesure republiée compte-t-elle comme un rejeu et pas comme un doublon exact ? | Parce que son identifiant de message et son topic diffèrent de l'original : seule la comparaison de l'identité métier (zone, capteur, horodatage, valeur) révèle le lien, pas la clé de doublon exact. |

Commandes à exécuter et commenter :

```bash
docker compose -f docker/docker-compose.yml up -d --wait mosquitto mosquitto-protected
mosquitto_pub -h 127.0.0.1 -p 1883 -t airbase/test -m hello
mosquitto_pub -h 127.0.0.1 -p 1884 -t airbase/test -m hello
mosquitto_pub -h 127.0.0.1 -p 1884 -u capteur-lora -P s07-capteur-demo -t airbase/test -m hello
mosquitto_pub -h 127.0.0.1 -p 1884 -u superviseur -P s07-superviseur-demo -t airbase/test -m hello
python3 -m iot_decision.chain_trust_cli data/samples/batch004_suspect_scenario.jsonl
python3 tests/validate_s07_artifacts.py
docker compose -f docker/docker-compose.yml down
```
