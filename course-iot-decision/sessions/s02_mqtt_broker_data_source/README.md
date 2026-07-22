# Séquence 2 — Comprendre la source : broker, topics et messages

Séance de 4 h pour inventorier un instantané MQTT retained, le comparer à un référentiel attendu et décider si sa couverture suffit avant tout nettoyage.

## Question directrice

**À la fin, les étudiants doivent être capables de décider si l’état observé du broker couvre suffisamment les zones critiques pour soutenir une analyse, avec confiance, preuves, incertitudes et vérification prioritaire explicites.**

## Démarrage rapide

```powershell
python -m pip install -r sessions/s02_mqtt_broker_data_source/requirements.txt
$env:PYTHONPATH=src
python -m iot_decision.source_inventory_cli data/samples/batch002_retained_messages.jsonl data/samples/batch002_expected_sensors.csv data/processed/batch002_inventory.csv data/processed/batch002_completeness.json
python -m pytest -q
python tests/validate_s02_artifacts.py
```

Livrables : inventaire CSV, matrice attendu/observé, diagnostic de complétude et brief de 120 mots maximum. Le PDF projetable est `slides/s02_mqtt_broker_data_source.pdf`.
