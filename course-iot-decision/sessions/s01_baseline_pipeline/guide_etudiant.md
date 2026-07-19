# Guide étudiant — Séquence 1

## Mission

À 10 h 05, le commandement doit décider si l’activité prévue peut être maintenue sur la base projetée Alpha. Vous allez construire une petite chaîne de données, puis expliquer exactement ce qu’elle permet — ou ne permet pas — de décider.

## Parcours

1. Comprendre la situation et voter.
2. Observer les messages et préserver la preuve brute.
3. Transformer les messages en table comparable.
4. Produire une représentation pour une question précise.
5. Formuler et contester une recommandation.

À chaque étape, conservez une trace : action, confiance, preuve, incertitude, vérification.

## Règle d’exécution

Les blocs `powershell` ci-dessous sont des commandes à copier-coller dans un terminal. Sauf indication contraire, exécutez-les depuis la racine du dépôt `course-iot-decision`. Les blocs `python` sont de petits contrôles à exécuter dans un notebook ou dans un fichier Python temporaire. Après chaque commande, vérifiez l’absence d’erreur et notez le fichier créé ou modifié.

## Préparer l’environnement

À exécuter par chaque binôme :

```powershell
python -m pip install -r sessions/s01_baseline_pipeline/requirements.txt
$env:PYTHONPATH="src"
python -m pytest -q
```

Si l’enseignant utilise Docker :

```powershell
docker compose -f docker/docker-compose.yml up -d --wait
python -m iot_decision.mqtt_tools seed data/samples/batch001_messages.jsonl
```

Ne démarrez pas le broker sur un réseau partagé.

## Vote initial

Avant les données, choisissez : maintenir / inspecter / protéger / différer / vérifier sur le terrain. Notez une confiance de 0 à 100 %, une raison et l’information qui vous manque le plus.

## TP 1 — Extraire le brut

Mode MQTT, à exécuter :

```powershell
python -m iot_decision.mqtt_tools extract data/raw/batch001_raw.jsonl
```

Mode échantillon si le broker est indisponible, à exécuter à la place :

```powershell
python -m iot_decision.baseline_cli extract-sample data/samples/batch001_messages.jsonl data/raw/batch001_raw.jsonl
```

Ensuite, exécutez éventuellement ce contrôle Python :

```python
from pathlib import Path

raw_path = Path("data/raw/batch001_raw.jsonl")
lines = [line for line in raw_path.read_text(encoding="utf-8").splitlines() if line]
print("lignes reçues :", len(lines))
print("première ligne :", lines[0])
print("dernière ligne :", lines[-1])
```

À faire : repérer topic, zone, valeur, unité, `measured_at`, `received_at` et retained. Notez ce que vous observez et ce que vous pouvez en déduire. Ne modifiez jamais le brut.

## TP 2 — Transformer en CSV

À exécuter :

```powershell
python -m iot_decision.baseline_cli transform data/raw/batch001_raw.jsonl data/processed/batch001_measurements.csv
```

Contrôle Python optionnel :

```python
import csv

with open("data/processed/batch001_measurements.csv", encoding="utf-8", newline="") as stream:
    reader = csv.DictReader(stream)
    rows = list(reader)

print("colonnes :", reader.fieldnames)
print("nombre de lignes :", len(rows))
print("première ligne :", rows[0])
```

À faire : vérifier colonnes, zones, unités et temps ; retrouver une ligne CSV dans le JSONL ; noter ce qui est plus lisible et ce qui n’est pas devenu plus vrai.

## TP 3 — Générer et critiquer le graphique

À exécuter :

```powershell
python -m iot_decision.visualize_baseline data/processed/batch001_measurements.csv sessions/s01_baseline_pipeline/slides/figures/batch001_max_by_zone.png
```

Ouvrez le fichier PNG. Écrivez séparément une observation directement visible, une interprétation prudente et une limite du maximum observé. Le graphique doit répondre à une question de décision explicite.

## TP 4 — Rédiger le brief décisionnel

Rédigez une note de 120 mots maximum contenant :

- une action concrète ;
- un niveau de confiance justifié ;
- deux preuves chiffrées retrouvables ;
- deux incertitudes importantes ;
- une vérification prioritaire.

Un membre du binôme joue le contradicteur : quelle hypothèse pourrait renverser votre décision ? Revotez ensuite avec votre niveau de confiance.

## Vérification finale à exécuter

```powershell
python tests/validate_s01_artifacts.py
```

Cette commande vérifie les artefacts et le notebook ; elle ne rédige pas votre recommandation.

## Aide en cas de blocage

Avant de demander de l’aide, indiquez : l’étape, la commande ou le fichier, le message d’erreur, ce que vous avez vérifié et l’effet possible sur votre décision. Ne demandez pas seulement la réponse : demandez quelle vérification réaliser ensuite.

## Canevas de recommandation

- **Décision :** quelle action proposez-vous ?
- **Confiance :** très faible / faible / moyenne / élevée ; pourquoi ?
- **Preuves :** quelles deux observations pouvez-vous retrouver ?
- **Incertitudes :** qu’est-ce qui pourrait rendre votre conclusion fausse ?
- **Vérification :** que faut-il vérifier avant une action difficilement réversible ?

## Exit ticket

1. « La pipeline permet d’affirmer que… »
2. « Elle ne permet pas d’affirmer que… »
3. « Avant une action irréversible, je vérifierais… »

Les solutions, valeurs de référence et observations attendues sont réservées au guide enseignant et au corrigé.
