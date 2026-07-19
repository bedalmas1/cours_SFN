# Exercices — Séquence 1

Chaque activité se termine par mini-décision, confiance, preuve, incertitude et limite.

## A. Situation initiale et vote — 15 min

Sans données, notez décision, confiance, raison principale et information prioritaire manquante. Comparez en binôme les risques. **Trace:** journal “avant pipeline”.

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

Rédigez la recommandation, revotez avec confiance, puis identifiez l’hypothèse qui pourrait renverser la décision. Remettez la note ≤120 mots et expliquez l’écart entre votes.

## I. Exit ticket — 5 min

« La pipeline permet d’affirmer… »; « elle ne permet pas… »; « avant une action irréversible, je vérifierais… ».
