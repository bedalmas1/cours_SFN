# Guide étudiant — Séquence 4

## Mission

Une supervision signale que la zone `battery-shelter-01` a atteint 36,2 °C, au-dessus du seuil habituel. Vous disposez d'une fenêtre de 24 messages MQTT retained couvrant les cinq zones critiques autour de cette alerte. Certains de ces messages contiennent des erreurs : champ manquant, unité incohérente, valeur physiquement impossible, incohérence temporelle, ou doublon. D'autres périodes semblent silencieuses.

Vous devez séparer les messages exploitables des messages à rejeter, déterminer si les silences observés sont réels ou simplement dus à un rejet, puis décider si l'alerte est exploitable en l'état — avec quelle confiance.

## Parcours

1. Voter sans données sur la seule alerte annoncée.
2. Détecter et nommer les erreurs de contenu du lot.
3. Produire `clean.csv` et `rejected.csv`, sans jamais corriger une valeur.
4. Distinguer un silence réel d'un silence expliqué par un rejet.
5. Décider, qualifier la confiance et proposer une vérification.

À chaque étape, conservez une trace : action, confiance, preuve, incertitude, vérification.

## Parcours pédagogique — 4 h

Ce guide est votre support unique. Il alterne compréhension, manipulation, débat et décision.

| Temps | Étape | Trace attendue |
|---|---|---|
| 0:00–0:15 | Alerte et vote initial | choix, confiance, information manquante |
| 0:15–0:45 | Validité, complétude, cohérence, précision | fiche concept annotée |
| 0:45–1:30 | TP 1 — détecter les erreurs | tableau des rejets nommés |
| 1:30–1:55 | Débrief — quelles erreurs sont graves ? | classement argumenté |
| 1:55–2:05 | Pause | — |
| 2:05–2:30 | Rejet, correction, quarantaine, incertitude | classement des opérations |
| 2:30–3:15 | TP 2 — produire clean.csv et rejected.csv | CSV et rapport reproductibles |
| 3:15–3:40 | Incident — silence critique | verdict par zone |
| 3:40–3:55 | Brief et vote final | note ≤150 mots |
| 3:55–4:00 | Exit ticket | trois phrases individuelles |

## Règle d'exécution

Les blocs `bash` sont des commandes à copier-coller depuis la racine du dépôt `course-iot-decision`. Les blocs `python` sont de petits contrôles à exécuter dans un notebook ou un fichier temporaire. Après chaque commande, vérifiez l'absence d'erreur et notez le fichier produit ou modifié.

## Préparer l'environnement

```bash
python3 -m pip install -r sessions/s04_data_quality_uncertainty/requirements.txt
export PYTHONPATH=src
python3 -m pytest -q
```

Si l'enseignant utilise Docker :

```bash
docker compose -f docker/docker-compose.yml up -d --wait
python3 -m iot_decision.mqtt_tools seed data/samples/batch002_quality_messages.jsonl
```

## Vote initial

Sans consulter aucun fichier, choisissez une seule réponse à partir de la seule alerte annoncée :

- **A.** L'alerte est exploitable telle quelle.
- **B.** Il faut d'abord contrôler la qualité des données avant toute décision.
- **C.** Il faut maintenir l'activité par prudence en attendant.
- **D.** Il faut suspendre l'activité par prudence en attendant.

Notez une confiance de 0 à 100 %, votre raison principale et l'information qui vous manque le plus.

## TP 1 — Détecter les erreurs de contenu — 45 min

### Prédire avant de lire

Sur le fichier `data/samples/batch002_quality_messages.jsonl`, sans encore le parser en table, répondez :

1. Combien de messages attendez-vous, pour combien de zones ?
2. Quels types d'erreurs un message JSON peut-il contenir sans être syntaxiquement invalide ?
3. Une valeur numérique présente peut-elle être malgré tout incorrecte ? Comment le savoir ?

### Détecter

```bash
export PYTHONPATH=src
```

Exécutez ce contrôle dans un notebook ou un fichier Python temporaire :

```python
from iot_decision.quality import load_raw, flatten, validate_row

rows = [flatten(envelope) for envelope in load_raw("data/samples/batch002_quality_messages.jsonl")]
for row in rows:
    reason = validate_row(row)
    if reason:
        print(row["message_id"], "->", reason)
```

Relevez, pour chaque ligne signalée : le `message_id`, la raison exacte, et le champ ou la valeur en cause. Complétez un tableau à quatre colonnes : champ manquant ; unité incohérente ; valeur hors plage ; incohérence temporelle.

Questions à répondre :

1. Quelles bornes de valeur sont utilisées, et sont-elles une norme officielle ou un choix pédagogique ?
2. Pourquoi une ligne dont `measured_at` est postérieur à `received_at` est-elle impossible ?
3. Une de ces erreurs aurait-elle pu passer inaperçue dans un simple calcul de moyenne ou de maximum ? Laquelle, et avec quel effet ?

## Débrief — quelles erreurs sont graves pour la décision ? — 25 min

Classez les cinq erreurs détectées de la plus grave à la moins grave pour la décision sur `battery-shelter-01`, en justifiant chaque rang. Une erreur sur une autre zone que celle en alerte a-t-elle la même gravité qu'une erreur sur `battery-shelter-01` elle-même ?

## Rejet, correction, quarantaine — 25 min

Classez chacune des opérations suivantes en rejet, correction ou quarantaine, puis dites laquelle ce cours autorise pour une ligne invalide : convertir silencieusement une valeur Fahrenheit en Celsius ; retirer une ligne en conservant sa raison dans un fichier séparé ; laisser une ligne ambiguë de côté en attendant un avis humain ; remplacer un champ manquant par une valeur moyenne.

Incident à préparer : que prouve, et que ne prouve pas, un silence dans une chronologie de mesures ?

## TP 2 — Produire clean.csv et rejected.csv — 45 min

```bash
export PYTHONPATH=src
python3 -m iot_decision.quality_cli \
  data/samples/batch002_quality_messages.jsonl \
  data/processed/batch002_measurements_clean.csv \
  data/processed/batch002_rejected.csv \
  data/processed/batch002_quality_report.json
```

Contrôle :

```bash
tail -n +2 data/processed/batch002_measurements_clean.csv | wc -l
tail -n +2 data/processed/batch002_rejected.csv | wc -l
cat data/processed/batch002_rejected.csv
```

Attendu : 19 lignes propres, 5 lignes rejetées, chacune avec sa raison en dernière colonne. Vérifiez qu'aucune valeur n'a été modifiée dans `rejected.csv` par rapport au brut : seule une raison a été ajoutée.

Produisez ensuite la chronologie :

```bash
python3 -m iot_decision.visualize_quality \
  data/processed/batch002_measurements_clean.csv \
  data/processed/batch002_rejected.csv \
  sessions/s04_data_quality_uncertainty/slides/figures/batch002_quality_timeline.png
```

Ouvrez le PNG. Identifiez la zone en alerte, le seuil pédagogique, et les marqueurs de rejet.

## Incident — le silence de battery-shelter-01 — 25 min

N'ouvrez le rapport qu'au signal de l'enseignant.

```bash
python3 -m json.tool data/processed/batch002_quality_report.json
```

Pour chaque zone listée dans `gaps_by_zone`, répondez : quelle est la durée du silence ? le champ `explained_by_rejection` est-il vrai ou faux ? si vrai, quelle ligne de `rejected.csv` explique ce silence ? si faux, qu'est-ce que cela implique sur l'origine du silence ?

Concentrez-vous ensuite sur `battery-shelter-01` : à quelle heure la dernière mesure propre avant le silence a-t-elle été prise ? à quelle heure la mesure reprend-elle, et avec quelle valeur ? Ce silence pourrait-il, à lui seul, expliquer entièrement pourquoi la valeur a franchi le seuil ?

## Brief décisionnel et vote final — 15 min

Rédigez une recommandation de 150 mots maximum contenant :

- une action concrète et son périmètre ;
- un niveau de confiance justifié ;
- deux preuves chiffrées et retrouvables (fichier et champ) ;
- deux incertitudes qui pourraient changer la décision ;
- une vérification prioritaire, terrain ou technique.

Un membre du binôme joue le décideur critique et pose : « Pour quelles zones cette conclusion vaut-elle ? », « Où retrouve-t-on chaque preuve ? », « Quelle hypothèse renverserait votre confiance ? ». Revotez ensuite entre les mêmes options A à D.

## Validation finale à exécuter

```bash
python3 tests/validate_s04_artifacts.py
```

Cette commande vérifie les artefacts et le notebook ; elle ne rédige pas votre recommandation.

## Canevas de recommandation

- **Décision :** quelle action proposez-vous ?
- **Confiance :** très faible / faible / moyenne / élevée ; pourquoi ?
- **Preuves :** quelles deux observations pouvez-vous retrouver et dans quel fichier ?
- **Incertitudes :** qu'est-ce qui pourrait rendre votre conclusion fausse ?
- **Vérification :** que faut-il vérifier avant une action difficilement réversible ?

## Exit ticket

1. « Le contrôle qualité permet d'affirmer que… »
2. « Il ne permet pas d'affirmer que… »
3. « Avant une action irréversible, je vérifierais… »

## Aide en cas de blocage

Avant de demander de l'aide, indiquez : l'étape, la commande ou le fichier, le message d'erreur, ce que vous avez déjà vérifié et l'effet possible sur votre décision. Ne demandez pas seulement la réponse : demandez quelle vérification réaliser ensuite.

Les solutions, valeurs de référence et observations attendues sont réservées au guide enseignant et au corrigé.
