# Guide enseignant — Séquence 2

## Intention et compétence décisionnelle

La séquence 1 montrait qu’une pipeline produit une preuve limitée. La séquence 2 revient à la source : avant parsing et nettoyage, il faut établir ce que l’on a réellement observé et par rapport à quel attendu. La compétence principale est de **borner une décision par la couverture démontrée**, sans confondre réponse du broker, présence d’un retained, fonctionnement du capteur et complétude métier.

**Question directrice : à la fin, les étudiants doivent être capables de décider si l’état observé du broker couvre suffisamment les zones critiques pour soutenir une analyse, avec confiance et limites explicites.**

Pièges : broker accessible = source fiable ; retained = récent ; silence = état normal ou panne certaine ; filtre = topic ; quatre messages = lot complet ; 80 % = suffisant indépendamment de la criticité ; référentiel supposé parfait.

## Objectifs évaluables

Conceptuels : expliquer publisher/broker/subscriber ; distinguer topic, filtre, payload et retained ; définir lot et complétude relativement à un attendu. Pratiques : explorer une branche ; inventorier les métadonnées ; comparer observé/attendu ; détecter une absence. Décisionnels : borner le périmètre ; qualifier la confiance ; proposer une vérification discriminante et une action réversible.

## Repères du parcours étudiant

Le `guide_etudiant.md` est le support étudiant unique : réflexion, TP, traces et exit ticket y sont réunis.

| Activité | Repère | Fonction |
|---|---|---|
| A | Vote initial | révéler les critères implicites de fiabilité |
| B–C | Apports + TP 1 | modèle MQTT et observation contrôlée |
| D | TP 2 | inventaire reproductible |
| E | Transition | construire le dénominateur de complétude |
| F–G | TP 3 | comparer puis injecter l’absence |
| H | TP 4 | brief, contradiction et vote final |
| I | Exit ticket | fixer portée, non-conclusion et vérification |

## Déroulé exact — 240 min

| Temps | Activité | Objectif | Modalité | Trace |
|---|---|---|---|---|
| 0:00–0:15 | A — situation + vote | révéler les hypothèses | individuel/binôme | choix, confiance, manque |
| 0:15–0:35 | B — architecture MQTT | attribuer les rôles | apport dialogué | schéma annoté |
| 0:35–0:45 | topic vs filtre | éviter l’absence fabriquée | prédiction | filtres testés |
| 0:45–1:05 | retained et limites | séparer disponibilité/fraîcheur | exemple guidé | vrai/faux justifié |
| 1:05–1:25 | C / TP 1 — exploration | observer sans surconclure | binômes | observe/conclus |
| 1:25–1:55 | D / TP 2 — inventaire | décrire le broker | manipulation | CSV + matrice zones |
| 1:55–2:05 | pause | — | — | — |
| 2:05–2:30 | E — lot/attendu/métadonnées | définir complétude | cartes + débat | définition bornée |
| 2:30–3:00 | F / TP 3 — comparaison | construire attendu/observé | binômes | matrice + taux |
| 3:00–3:15 | revue croisée | tester filtre et preuve | pairs | objection écrite |
| 3:15–3:40 | G — incident optronique | raisonner sur le silence | injection | hypothèses/vérifications |
| 3:40–3:52 | H / TP 4 — brief | recommander sans généraliser | rôles data/décideur | note ≤120 mots |
| 3:52–3:55 | vote final | mesurer la révision | individuel | choix + confiance |
| 3:55–4:00 | I — exit ticket | stabiliser le réflexe | individuel | trois phrases |

## Conduite détaillée

### A — Situation et vote

**Préparer :** cartes A–D et fiche action/confiance/preuve/manque. **Conduire :** lire la situation sans afficher les fichiers ; vote silencieux puis échange. **Relancer :** « quelle propriété du broker soutient votre choix ? » et « quel coût aurait une zone oubliée ? ». **Débloquer :** proposer le canevas sans révéler cinq topics attendus. **Débriefer :** distinguer disponibilité technique et suffisance opérationnelle.

### B — Modèle MQTT

**Préparer :** schéma publisher → broker → subscriber. **Conduire :** attribuer à chaque binôme un composant et lui faire nommer entrée, sortie, connaissance et ignorance. **Relancer :** « qui connaît la liste des capteurs attendus ? ». **Débloquer :** donner les étiquettes, pas les définitions. **Débriefer :** MQTT transporte et distribue ; le contrat métier vient d’ailleurs.

### C / TP 1 — Explorer

**Préparer :** broker seedé ou JSONL ; masquer le référentiel. **Conduire :** faire prédire le résultat de `airbase/batch002/#`, puis extraire. Exiger le filtre dans le journal. **Relancer :** « ceci est-il dans le topic, l’enveloppe ou le payload ? ». **Blocage technique :** vérifier `PYTHONPATH`, Docker, port, topic, puis passer au JSONL après deux essais. **Débriefer :** un filtre définit le champ de vision.

### D / TP 2 — Inventorier

**Préparer :** matrice vierge. **Conduire :** une ligne par topic ; contrôler unicité, zone, capteur, deux horloges, retained. **Relancer :** « que perdez-vous si vous ne gardez que la zone ? ». **Débloquer :** montrer une ligne exemplaire, pas le tableau complet. **Débriefer :** l’inventaire est une preuve sur l’observé, pas sur l’exhaustivité.

### E — Définir lot et complétude

**Préparer :** cartes d’affirmations et référentiel encore fermé. **Conduire :** classer observable / nécessite attendu / non démontrable. Révéler ensuite le CSV attendu et son rôle. **Relancer :** « qui autorise ce référentiel et à quelle date ? ». **Débloquer :** écrire `complétude = observé ∩ attendu`, puis faire nommer le dénominateur. **Débriefer :** un taux sans périmètre masque les zones critiques.

### F / TP 3 — Comparer

**Préparer :** commande CLI testée. **Conduire :** faire produire la matrice manuellement, puis comparer au JSON. **Relancer :** « 4/5 décrit quoi exactement ? ». **Blocage :** vérifier chemins, en-têtes CSV et topic complet. **Débriefer :** valider 80 % global et 0 % optronique ; séparer exactitude du calcul et autorité de l’attendu.

### G — Incident absent

**Préparer :** garder le nom optronique jusqu’à 3:15. **Conduire :** révéler l’absence et imposer au moins trois hypothèses concurrentes. **Relancer :** « quelle observation départagerait panne et filtre erroné ? ». **Débloquer :** proposer catégories équipement / publication / transport / extraction / référentiel. **Débriefer :** le silence n’indique pas sa cause et n’est jamais une mesure normale.

### H / TP 4 — Brief et contradiction

**Préparer :** canevas décision-confiance-preuves-incertitudes-vérification. **Conduire :** rédaction silencieuse, interrogation par le décideur, inversion des rôles, vote final. **Relancer :** « votre phrase vaut-elle pour quatre zones ou cinq ? ». **Débloquer :** amorce « nous pouvons décrire…, mais pas conclure… ». **Débriefer :** accepter analyse partielle + vérification ciblée ; refuser généralisation à la base.

### I — Exit ticket

Faire répondre sans écran. Si « prouve » apparaît, demander le topic ou champ exact. Conserver les tickets pour ouvrir la séquence 3 sur la traçabilité.

## Script opérationnel détaillé des TP

Cette section sert de conducteur terminal. Toutes les commandes partent de la racine du dépôt. Ne projeter la sortie attendue qu’après la prédiction des étudiants.

### Avant TP 1 — Préparer la source sans révéler l’incident

Lancer et alimenter le broker avant l’arrivée des étudiants :

```powershell
docker compose -f docker/docker-compose.yml up -d --wait
$env:PYTHONPATH=src
python -m iot_decision.mqtt_tools seed data/samples/batch002_retained_messages.jsonl
```

**Sortie attendue :** `4 messages publiés`. Ne pas annoncer « quatre sur cinq » et ne pas ouvrir `batch002_expected_sensors.csv`.

Contrôle enseignant :

```powershell
python -m iot_decision.mqtt_tools extract C:\tmp\s02_teacher_check.jsonl --topic airbase/batch002/#
(Get-Content C:\tmp\s02_teacher_check.jsonl).Count
```

Attendu : quatre lignes. Si zéro : vérifier Docker, le port 1883, le seed et le filtre. Si Docker reste indisponible après deux essais, annoncer le passage au fichier de repli ; faire noter que ce changement de mode modifie la provenance de la trace.

### TP 1 — Chronologie d’animation, 20 min

1. **0–3 min, prédiction silencieuse.** Faire écrire effectif attendu et signification de `#`.
2. **3–8 min, extraction.** Les étudiants exécutent la commande du guide. Circuler et vérifier le dossier courant avant de corriger autre chose.
3. **8–12 min, contrôles.** Exiger `Test-Path`, nombre de lignes et première ligne.
4. **12–17 min, lecture.** Faire colorer mentalement topic, enveloppe et payload ; demander une preuve textuelle pour chaque réponse.
5. **17–20 min, mini-décision.** Faire compléter les six champs du journal.

Questions à poser dans cet ordre : « quel filtre avez-vous réellement utilisé ? », « combien de lignes avez-vous reçues ? », « où voyez-vous retained ? », « quelle horloge vient du capteur ? », « quelle phrase pouvez-vous défendre sans référentiel ? ».

Réponses attendues : filtre `airbase/batch002/#` ; quatre enveloppes ; retained dans l’enveloppe ; `measured_at` déclaré par le payload ; seule conclusion sûre : quatre topics observés avec ce filtre et cette extraction.

### TP 2 — Chronologie d’animation, 30 min

1. **0–5 min.** Faire lancer la CLI sur `data/raw/batch002_observed.jsonl`.
2. **5–10 min.** Faire confirmer la création des deux sorties avec `Test-Path`.
3. **10–18 min.** Faire afficher le CSV avec `Import-Csv`; interdire l’ouverture du JSON.
4. **18–24 min.** Faire compter lignes et topics uniques.
5. **24–30 min.** Revue croisée et mini-décision.

Commandes de diagnostic à projeter seulement si nécessaire :

```powershell
Import-Csv data/processed/batch002_inventory.csv | Format-Table topic,zone,sensor,retained
(Import-Csv data/processed/batch002_inventory.csv).Count
(Import-Csv data/processed/batch002_inventory.csv | Select-Object -ExpandProperty topic | Sort-Object -Unique).Count
```

Attendu : quatre lignes, quatre topics uniques, zones batteries/transmissions/informatique/maintenance. Si le CSV manque : vérifier `PYTHONPATH`, les quatre arguments et l’existence du JSONL. Si la CLI annonce 4/5, rappeler qu’elle produit déjà le diagnostic mais que la démarche manuelle doit précéder son interprétation.

Questions de débrief : « quelle colonne permet de réexécuter la contestation ? », « que prouve retained ? », « pourquoi le CSV ne prouve-t-il pas que le capteur fonctionne maintenant ? », « quelle formulation bornée inscrivez-vous dans le journal ? ».

### Activité E — Révéler le dénominateur, 25 min

Pendant les dix premières minutes, laisser le référentiel fermé. Faire classer les six affirmations des exercices. Exiger pour chacune : source nécessaire et verdict possible.

Révéler ensuite :

```powershell
Import-Csv data/samples/batch002_expected_sensors.csv | Format-Table topic,zone,sensor,criticality
```

Questions : « attendu par qui ? », « valide pour quel site ? », « à quelle date ? », « cinq lignes ont-elles le même poids opérationnel ? ». Réponse attendue : la complétude est relative à un référentiel métier autorisé ; la séance suppose ce CSV valide, mais cette hypothèse doit rester dans les limites.

### TP 3 — Chronologie d’animation, 55 min

1. **0–10 min.** Lire et questionner le référentiel, sans afficher le JSON diagnostic.
2. **10–25 min.** Construire manuellement la matrice cinq lignes.
3. **25–30 min.** Calculer 4/5 et couverture par zone.
4. **30–35 min.** Ouvrir le JSON et comparer.
5. **35–47 min.** Injecter officiellement l’absence optronique et construire les hypothèses.
6. **47–55 min.** Choisir une vérification prioritaire et écrire la mini-décision.

Commande de contrôle :

```powershell
Get-Content data/processed/batch002_completeness.json | ConvertFrom-Json | Format-List
```

Attendu : 4 observés, 5 attendus, `complete=False`, topic optronique absent, confiance faible. Faire écrire explicitement : « 80 % des topics attendus observés » et non « 80 % de la base sûre ».

Pour l’incident, ne valider une hypothèse que si elle est accompagnée d’une vérification discriminante. Exemples : élargir/rejouer le filtre pour tester l’extraction ; consulter journaux publisher/passerelle pour la publication ; confirmer la configuration retained ; joindre le responsable du référentiel ; réaliser une mesure terrain pour l’état physique.

### TP 4 — Chronologie d’animation, 15 min

1. **0–5 min.** Rédaction silencieuse avec le canevas obligatoire.
2. **5–9 min.** Le décideur pose les cinq questions du guide, sans proposer la réponse.
3. **9–12 min.** Révision du brief ; chaque preuve reçoit un nom de fichier ou un topic.
4. **12–15 min.** Vote final, confiance et écart avec le vote initial.

Critères immédiats : périmètre limité ; deux preuves retrouvables ; absence non assimilée à panne ; vérification optronique priorisée ; action réversible ou conditionnelle. Si un groupe écrit « toute la base », demander de surligner les cinq preuves correspondantes : l’absence de cinquième preuve doit conduire à la reformulation.

### Questions et réponses pour la synthèse

1. **Que prouve la connexion ?** Une disponibilité technique ponctuelle, pas la complétude métier.
2. **Que prouve un retained ?** Un dernier message retained disponible pour un topic correspondant, pas la fraîcheur.
3. **Que prouve l’inventaire ?** Le périmètre effectivement observé avec ce filtre et cette extraction.
4. **Comment établir la complétude ?** En comparant observé et attendu, avec un référentiel borné et autorisé.
5. **Que prouve le silence optronique ?** L’absence de topic dans l’observation, pas sa cause ni l’état thermique.
6. **Décision attendue ?** Continuer l’analyse sur quatre zones, ne pas généraliser, vérifier l’optronique, confiance faible pour la couverture globale.

## Résultat et décision attendus

Quatre topics retained sont observés contre cinq attendus ; l’optronique manque. Décision recommandée : poursuivre l’analyse limitée aux quatre zones, ne pas conclure pour toute la base, vérifier en priorité la chaîne ou le terrain optronique. Confiance faible pour la couverture globale. Preuves : inventaire 4/5 et topic attendu absent. Incertitudes : cause du silence et autorité/fraîcheur du référentiel.

## Sources

MQTT 5.0, OASIS Open (2019), sections topics, subscriptions et retained messages ; manuels officiels `mosquitto_sub` et `mosquitto_pub`, Eclipse Mosquitto. Les slides citent les URL et la bibliographie commune.
