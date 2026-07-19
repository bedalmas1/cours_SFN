# De la donnée capteur à la décision opérationnelle

## Qualité, confiance et incertitude dans une pipeline IoT

**École de l'air et de l'espace - Module de 8 séquences de 4 h**

## Intention pédagogique

Former des décideurs capables d'exercer un esprit critique face aux données, aux indicateurs et aux décisions
qu'une pipeline de données peut soutenir ou fragiliser.
Données capteurs imparfaites -> pipeline de traitement -> indicateurs -> décision
opérationnelle -> niveau de confiance, incertitude et risques

## 1. Contexte général
Ce cours s'inscrit dans un projet plus large autour d'une chaîne IoT : des Arduino équipés de shields LoRa produisent
ou transmettent des données de capteurs, qui sont ensuite récupérées, transformées, analysées et utilisées pour
éclairer une prise de décision.
Le cours est destiné à des officiers ou élèves officiers de l'École de l'air et de l'espace. L'objectif n'est pas de former
des experts en ETL, en programmation ou en infrastructure informatique, mais de développer une compréhension
critique du rôle des pipelines de données dans la qualité d'une décision opérationnelle.
> **Question centrale**
  Les données disponibles permettent-elles de prendre une décision fiable : maintenir l'activité prévue, déclencher
  une inspection, protéger du matériel, différer une opération ou demander une vérification terrain ?

## 2. Use case opérationnel fil rouge
Le scénario pédagogique retenu est celui d'une base aérienne projetée équipée de capteurs environnementaux
simples. Des capteurs Arduino/LoRa mesurent régulièrement la température dans plusieurs zones critiques :
- stockage batteries de drones ;
- shelter transmissions ;
- local informatique tactique ;
- zone de maintenance légère ;
- abri matériel optronique.
Dans la première version du cours, on suppose que le broker MQTT contient déjà des données. Les étudiants
travaillent sur un broker simulé, pré-rempli avec des messages de température. Le scénario permet de travailler des
situations réalistes sans données sensibles : capteur défaillant, données manquantes, dépassement de seuil,
indicateur trompeur, contradiction entre capteurs, ou problème de confiance dans le flux de données.

## 3. Objectifs pédagogiques
1. Comprendre le rôle d'un broker MQTT dans une architecture IoT.
2. Expliquer comment une donnée capteur brute devient un indicateur décisionnel.
3. Extraire des messages depuis un broker simulé et conserver les données brutes.
4. Parser et structurer des messages JSON.
5. Identifier les erreurs de données : valeurs manquantes, doublons, timestamps incohérents, unités incorrectes,
     valeurs aberrantes.
6. Transformer des données brutes en table exploitable.
7. Produire des indicateurs simples : moyenne, maximum, durée de dépassement, taux de données manquantes,
     nombre de rejets.
8. Interpréter ces indicateurs dans un contexte opérationnel.
9. Identifier les indicateurs utiles, insuffisants ou trompeurs.
10. Évaluer le niveau de confiance associé à une décision.
11. Formuler une recommandation opérationnelle argumentée, avec limites et vérifications terrain nécessaires.
## 4. Positionnement pédagogique
Le cours n'est pas centré sur la maîtrise technique exhaustive des outils. Les outils servent de support pour
comprendre les effets d'une chaîne de traitement sur la décision.
Chaque séance suit la logique suivante :

   Concept technique -> conséquence sur la donnée -> conséquence sur l’indicateur -> conséquence
   sur la décision -> niveau de confiance

  Exemple
  Doublon -> message compté deux fois -> durée d'alerte surestimée -> inspection déclenchée à tort -> confiance
  réduite.

## 5. Architecture pédagogique retenue
Dans la première version du cours, il n'y a pas de flux continu réel. On utilise un broker MQTT simulé, déjà rempli avec
des données de température.

   Broker MQTT Mosquitto pré-rempli
       -> extraction des messages retained
       -> fichier brut JSONL
       -> transformation Python
       -> fichier propre CSV / Parquet
       -> analyse et visualisation
       -> recommandation opérationnelle

Exemples de topics MQTT :

   airbase/batch001/battery-shelter-01/temperature/0000
   airbase/batch001/battery-shelter-01/temperature/0001
   airbase/batch001/comms-shelter-01/temperature/0000
   airbase/batch001/maintenance-zone-01/temperature/0000

## 6. Exemple de message capteur
   {
       "batch_id": "mission-readiness-001",
       "message_id": "battery-shelter-01-0042",
       "site_id": "base-projetee-alpha",
       "zone": "battery-shelter-01",
       "asset_type": "drone_battery_storage",
       "sensor": "temperature",
       "measured_at": "2026-10-12T09:35:00Z",
       "value": 34.8,
       "unit": "celsius",
       "sequence": 42

   }

## 7. Outils retenus
Catégorie                  Outils                                Rôle

Infrastructure             VPS Ubuntu, Docker, Docker Compose,   Héberger le laboratoire, lancer les services,
                           Mosquitto                             simuler le broker MQTT.

Données simulées           Messages MQTT retained                Simuler un broker déjà rempli avec un topic
                                                                 par mesure.

Travail depuis iPad        Safari, OVH Cloud Shell,              Administrer le VPS et accéder aux
                           Termius/Blink/Shelly                  interfaces web.

Développement              code-server, JupyterLab, Git/GitHub   Coder, explorer les données, versionner et
                                                                 distribuer les supports.

ETL et analyse             Python, paho-mqtt, pandas, DuckDB     Extraire, parser, nettoyer, agréger et
                                                                 analyser les données.

Stockage et visualisation  JSONL, CSV, Parquet, matplotlib       Conserver le brut, produire des sorties
                                                                 propres et visualiser les résultats.

Optionnel                  Node-RED, Pydantic, pytest, pyarrow,  Visualiser les flux, valider les messages,
                           python-dotenv                         tester et exporter plus proprement.

## 8. Outils volontairement écartés
Pour garder le cours léger et centré sur la décision, on évite dans cette version : KNIME, Kafka, Spark, Airflow,
Kubernetes, PostgreSQL, Grafana et TimescaleDB. Ces outils peuvent être pertinents dans des contextes industriels,
mais risquent de détourner le cours vers l'infrastructure au lieu de servir l'objectif principal.

## 9. Déroulé détaillé des 8 séquences
### Séquence 1 - Introduction et pipeline baseline
Objectif général : Comprendre le scénario opérationnel et construire une première pipeline simple de bout en bout.

Temps                                Activité

0:00-0:15                            Situation initiale : faut-il maintenir l'activité prévue sur la base
                                     projetée ?

0:15-0:45                            Concepts : donnée, indicateur, décision, confiance, incertitude

0:45-1:10                            Démonstration : broker MQTT simulé et messages de température

1:10-1:55                            TP : extraire les messages vers batch001_raw.jsonl

1:55-2:05                            Pause

2:05-2:30                            Concepts : brut, transformé, exploitable

2:30-3:10                            TP : parser les JSON et produire un CSV propre minimal

3:10-3:35                            Visualisation simple de la température par zone

3:35-3:55                            Décision : peut-on maintenir l'activité ?

3:55-4:00                            Synthèse

Question décisionnelle : Que peut-on déjà décider avec cette pipeline minimale ? Et que ne peut-on pas encore
conclure ?

Livrables : batch001_raw.jsonl ; batch001_measurements.csv ; graphique simple ; première recommandation
opérationnelle.

Engagement : Vote initial puis vote final pour observer l’effet du pipeline sur la décision.

### Séquence 2 - Comprendre la source : broker, topics et messages
Objectif général : Comprendre ce que contient réellement le broker et ce que l'on risque de mal interpréter dès
l'extraction.

Temps                                Activité

0:00-0:15                            Accroche : le broker est-il une source fiable ?

0:15-0:45                            Concepts : MQTT, broker, topic, payload, retained message

0:45-1:20                            Exploration guidée des topics

1:20-1:55                            Exercice : inventaire des zones, capteurs et messages

1:55-2:05                            Pause

2:05-2:30                            Concepts : lot, complétude, métadonnées

2:30-3:15                            Exercice : vérifier si le lot est complet

3:15-3:40                            Incident injecté : un capteur attendu est absent

3:40-3:55                            Brief décisionnel : peut-on conclure ?

3:55-4:00                            Synthèse

Question décisionnelle : Avant même de nettoyer les données, peut-on savoir si le lot est suffisant pour soutenir une
décision ?

Livrables : Inventaire des messages ; tableau zones/capteurs ; diagnostic de complétude ; note courte sur les limites
du brut.

Engagement : Binômes : équipe data et décideur qui pose des questions critiques.

### Séquence 3 - Parsing, structuration et traçabilité
Objectif général : Transformer des messages techniques en données structurées tout en gardant la capacité de
revenir à la source.

Temps      Activité

0:00-0:15  Situation : une décision contestée doit être justifiée a posteriori

0:15-0:45  Concepts : traçabilité, donnée brute, donnée structurée

0:45-1:25  TP : parser les payloads JSON

1:25-1:55  TP : construire une table structurée

1:55-2:05  Pause

2:05-2:30  Concepts : auditabilité, identifiants, horodatage

2:30-3:10  Exercice : relier chaque ligne propre au message brut

3:10-3:35  Incident injecté : deux messages semblent identiques

3:35-3:55  Décision : peut-on justifier l'indicateur produit ?

3:55-4:00  Synthèse

Question décisionnelle : Quelles informations doivent absolument être conservées pour pouvoir justifier une décision
plus tard ?

Livrables : batch001_structured.csv ; schéma de données commenté ; justification des champs conservés.

Engagement : Mini-débat : supprime-t-on les données brutes une fois le CSV propre produit ?

### Séquence 4 - Qualité des données et incertitude
Objectif général : Comprendre que la qualité des données conditionne directement le niveau de confiance dans la
décision.

Temps      Activité

0:00-0:15  Accroche : une alerte température apparaît dans une zone critique

0:15-0:45  Concepts : validité, complétude, cohérence, précision

0:45-1:30  TP : champs manquants, unités incorrectes, valeurs impossibles

1:30-1:55  Débrief : quelles erreurs sont graves pour la décision ?

1:55-2:05  Pause

2:05-2:30  Concepts : rejet, correction, quarantaine, incertitude

2:30-3:15  TP : produire clean.csv et rejected.csv

3:15-3:40  Incident injecté : période critique avec données manquantes

3:40-3:55  Brief : niveau de confiance dans l'alerte

3:55-4:00  Synthèse

Question décisionnelle : À partir de quel niveau d'erreur la donnée devient-elle insuffisante pour prendre une
décision fiable ?

Livrables : batch002_measurements_clean.csv ; batch002_rejected.csv ; rapport qualité ; niveau de confiance
associé.

Engagement : Échelle de confiance : 0 impossible, 1 faible, 2 modérée, 3 forte.

### Séquence 5 - Indicateurs, agrégations et pièges décisionnels
Objectif général : Montrer que les indicateurs simplifient la réalité et peuvent masquer un risque.

Temps      Activité

0:00-0:15  Accroche : la température moyenne de la base est normale

0:15-0:45  Concepts : moyenne, maximum, seuil, durée de dépassement

0:45-1:30  TP : calculer les indicateurs globaux et par zone

1:30-1:55  Débrief : quels indicateurs racontent des histoires différentes ?

1:55-2:05  Pause

2:05-2:30  Concepts : agrégation trompeuse, perte d'information

2:30-3:15  Exercice : retrouver une zone critique masquée par la moyenne

3:15-3:40  Challenge : choisir seulement 3 indicateurs pour le décideur

3:40-3:55  Restitution : justification des indicateurs retenus

3:55-4:00  Synthèse

Question décisionnelle : Quel indicateur est réellement pertinent pour décider de maintenir ou non l'activité ?
Livrables : Tables d'indicateurs ; indicateur trompeur identifié ; recommandation sur les indicateurs à suivre.
Engagement : Procès de l'indicateur : un groupe défend la moyenne globale, un autre l'attaque, un troisième arbitre.

### Séquence 6 - Visualisation et communication au décideur
Objectif général : Produire une visualisation claire sans sur-vendre la certitude.

Temps      Activité

0:00-0:15  Accroche : deux graphiques donnent une impression différente du
           même incident

0:15-0:45  Concepts : échelle, seuil, annotation, incertitude visuelle

0:45-1:30  TP : courbe temporelle par zone

1:30-1:55  Débrief : graphique utile ou trompeur ?

1:55-2:05  Pause

2:05-2:30  Concepts : briefing décisionnel, message principal, limites

2:30-3:15  TP : produire 2 visualisations et une mini-note

3:15-3:40  Brief oral : 3 minutes par groupe

3:40-3:55  Questions contradictoires du commandement

3:55-4:00  Synthèse

Question décisionnelle : Comment présenter une alerte sans donner une impression excessive de certitude ?
Livrables : 2 à 3 graphiques ; mini-rapport opérationnel ; niveau de confiance explicite ; recommandation.
Engagement : Jeu de rôle : cellule data, décideur pressé et red team.

### Séquence 7 - Confiance, sécurité et robustesse de la chaîne
Objectif général : Relier sécurité, intégrité des données et qualité de décision.

Temps      Activité

0:00-0:15  Accroche : le flux contient des messages incohérents

0:15-0:45  Concepts : intégrité, authentification, ACL, injection, rejeu

0:45-1:25  Démonstration : broker ouvert vs broker protégé

1:25-1:55  Exercice : identifier les vulnérabilités d'une chaîne MQTT

1:55-2:05  Pause

2:05-2:30  Concepts : confiance dans la source, confiance dans le traitement

2:30-3:15  Analyse d’un lot suspect : doublons, timestamps, ruptures

3:15-3:40  Matrice : incident réel, panne capteur, problème réseau, suspicion
           data

3:40-3:55  Décision : peut-on agir sur ces données ?

3:55-4:00  Synthèse

Question décisionnelle : Que vaut une décision opérationnelle si l'on ne peut pas qualifier la confiance dans la
chaîne de données ?

Livrables : Matrice des risques data/cyber ; diagnostic de confiance ; recommandations de sécurisation minimale.

Engagement : Classement des hypothèses par probabilité et impact.

### Séquence 8 - Mini-projet décisionnel final
Objectif général : Mettre les étudiants en situation complète avec un lot ambigu et une décision à défendre.

Temps      Activité

0:00-0:15  Brief mission : situation opérationnelle et décision attendue

0:15-0:35  Analyse rapide du lot et stratégie de traitement

0:35-1:30  Travail groupe : extraction, parsing, nettoyage

1:30-1:55  Travail groupe : indicateurs et visualisations

1:55-2:05  Pause

2:05-2:45  Travail groupe : note de décision

2:45-3:20  Préparation du brief oral

3:20-3:50  Restitutions courtes

3:50-4:00  Synthèse finale

Question décisionnelle : Quelle décision recommandez-vous, avec quel niveau de confiance, et quelles incertitudes
doivent être communiquées au décideur ?

Livrables : Dossier de traitement ; fichiers propres et rejetés ; visualisations ; note de décision ; présentation courte.

Engagement : Brief opérationnel : situation, données/indicateurs, décision/confiance, limites/vérifications.

## 10. Dispositifs d’engagement transversaux
Dispositif                Principe                                       Intérêt pédagogique

Vote avant / après        Décision intuitive au début, décision après    Montrer comment la pipeline confirme,
                          analyse à la fin.                              nuance ou change une décision.

Échelle de confiance      0 impossible, 1 faible, 2 modérée, 3 forte.    Forcer l’explicitation de l’incertitude.

Incident injecté          Capteur absent, timestamp incohérent,          Maintenir l’engagement et révéler les
                          mauvaise unité, pic isolé, doublon.            fragilités.

Red team                  Un groupe attaque la conclusion d’un autre Identifier ce qui pourrait rendre la décision

                          groupe.                                        fausse.

Brief décideur            Décision, confiance, arguments, limites,       Passer du résultat technique à la
                          action terrain.                                recommandation opérationnelle.

Comparaison de pipelines  Deux groupes font des choix de traitement      Mesurer l’effet des choix techniques sur la
                          différents.                                    décision.

One chart, one decision   Chaque graphique répond à une question         Éviter les visualisations décoratives ou
                          décisionnelle.                                 trompeuses.

Journal des choix         Tracer les choix de rejet, correction, seuil,  Rendre la décision auditable et défendable.
                          agrégation.

## 11. Compétences évaluées            Compétences attendues
 Dimension                          Extraire les messages MQTT ; sauvegarder les données brutes ;
 Compétences techniques minimales   parser le JSON ; nettoyer les données ; produire une table
                                    exploitable ; calculer des indicateurs simples ; visualiser les
 Esprit critique décisionnel        résultats.

                                    Recommander une décision ; expliciter le niveau de confiance ;
                                    identifier les données qui fragilisent la conclusion ; repérer les
                                    indicateurs trompeurs ; proposer des vérifications terrain.

## 12. Critères d’évaluation possibles  Attendu
                                     Relier les données capteurs à une situation opérationnelle.
 Critère                             Récupérer correctement les messages depuis le broker simulé.
 Compréhension du scénario           Conserver les données brutes et le lien avec les messages sources.
 Extraction                          Identifier erreurs, doublons, valeurs manquantes et incohérences.
 Traçabilité                         Produire une table exploitable et documentée.
 Qualité des données                 Choisir des indicateurs pertinents pour la décision.
 Transformation                      Produire des graphiques lisibles et non trompeurs.
 Indicateurs                         Formuler une décision opérationnelle claire.
 Visualisation                       Expliciter le niveau de confiance et les limites.
 Recommandation                      Identifier ce qui pourrait rendre la conclusion fausse.
 Incertitude
 Esprit critique

## 13. Message pédagogique central
> **À retenir**
  Une pipeline de données transforme des messages techniques en éléments de décision. Chaque choix de
  traitement peut augmenter ou diminuer la confiance dans la décision.

Les étudiants doivent comprendre que produire un graphique ne suffit pas. Il faut être capable d'expliquer ce que les
données permettent d'affirmer, ce qu'elles ne permettent pas de conclure, les incertitudes restantes, les risques
opérationnels, les vérifications nécessaires et le niveau de confiance de la recommandation.

---

Source : [syllabus_iot_decision_operationnelle.pdf](./syllabus_iot_decision_operationnelle.pdf)
