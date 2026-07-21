# Exercices — Séquence 1

Chaque activité se termine par mini-décision, confiance, preuve, incertitude et limite.

## Comment lire les exercices avec le guide étudiant

Ce fichier organise toute la séance en activités **A à I**. Le `guide_etudiant.md` regroupe les quatre productions techniques sous les titres **TP 1 à TP 4**. Les correspondances sont les suivantes :

| Activité | Section du guide étudiant | Rôle dans le parcours |
|---|---|---|
| A | Vote initial | décision avant les données |
| B–C | Apports guidés + début du TP 1 | chaîne de données et observation du broker |
| D | TP 1 | extraction du JSONL brut |
| E | Transition TP 1 → TP 2 | brut, transformé, exploitable |
| F | TP 2 | transformation et contrôle du CSV |
| G | TP 3 | graphique et critique de l’indicateur |
| H | TP 4 + vote final | recommandation et décision révisée |
| I | Exit ticket | synthèse individuelle |

Les activités B, C et E préparent ou encadrent les TP : elles ne constituent pas des TP supplémentaires.

## A. Situation initiale et vote — 15 min

Une activité de maintenance drone est prévue à 14 h 00 sur une base aérienne projetée. La supervision signale une possible hausse de température dans le stockage batteries. Les données sont disponibles dans le broker MQTT, mais aucune analyse consolidée n’a encore été réalisée. Une vérification terrain prendrait 30 minutes; reporter l’activité a un coût opérationnel.

Sans consulter les données, choisissez : **A. maintenir l’activité; B. déclencher une inspection terrain; C. mettre temporairement la zone en sécurité; D. données insuffisantes pour décider.** Notez décision, confiance, raison principale et information prioritaire manquante. Comparez en binôme les risques de chaque choix. **Trace:** journal “avant pipeline”.

## B. Lire la chaîne — 30 min

Reliez message, donnée structurée, indicateur et décision. Pour chaque flèche, proposez une erreur et son effet. Peut-on agir sur la seule présence de messages?

## C. Observer le broker — 25 min

Repérez topic, zones, payload, `measured_at`, `received_at` et retained. Expliquez pourquoi “reçu maintenant” ne signifie pas “mesuré maintenant”. **Trace:** “j’observe / je conclus”.

## D. Extraire sans altérer — 45 min

```powershell
# Mode MQTT
python -m iot_decision.mqtt_tools extract data/raw/batch001_raw.jsonl
# Repli hors broker
python -m iot_decision.baseline_cli extract-sample data/samples/batch001_messages.jsonl data/raw/batch001_raw.jsonl
```

Vérifiez effectif, première/dernière ligne et trois métadonnées de traçabilité. N’éditez pas le brut.

## Pause — 10 min

## E. Brut, transformé, exploitable — 25 min

Classez: conserver le payload; renommer une zone; convertir une unité; calculer un maximum; supprimer; tracer un seuil. Lesquelles changent la preuve? **Incident:** les mesures ont-elles une fraîcheur comparable? Ne corrigez rien.

## F. Transformer — 40 min

```powershell
python -m iot_decision.baseline_cli transform data/raw/batch001_raw.jsonl data/processed/batch001_measurements.csv
```

Contrôlez colonnes, effectif, cinq zones, unités et temps. Reliez une ligne CSV à sa source. Qu’est-ce qui est plus lisible sans être devenu plus vrai?

## G. Visualiser — 25 min

```powershell
python -m iot_decision.visualize_baseline data/processed/batch001_measurements.csv sessions/s01_baseline_pipeline/slides/figures/batch001_max_by_zone.png
```

Vérifiez titre-question, unité, seuil et lisibilité. Écrivez séparément une observation et une interprétation.

## H. Décider, voter, contester — 20 min

Rédigez la recommandation, revotez entre les mêmes options A à D avec confiance, puis identifiez l’hypothèse qui pourrait renverser la décision. Remettez la note ≤120 mots et expliquez l’écart entre votes.

## I. Exit ticket — 5 min

« La pipeline permet d’affirmer… »; « elle ne permet pas… »; « avant une action irréversible, je vérifierais… ».
