# Guide étudiant — Séquence 2

## Mission

Le broker répond, mais votre décision porte sur la **couverture de cinq zones critiques**, pas sur une connexion réussie.

**Avant tout nettoyage, l’état observé du broker suffit-il pour soutenir une décision couvrant toute la base ?**

## Règles

- Binôme : équipe data / décideur critique, rôles inversés après la pause.
- Séparez observation, interprétation et décision.
- Une absence n’a de sens que par rapport à un attendu explicite.
- Retained signifie disponible à l’abonnement, pas récent ni fonctionnel.
- Après chaque TP : décision, confiance, preuve, incertitude, limite.

## Préparer

```powershell
python -m pip install -r sessions/s02_mqtt_broker_data_source/requirements.txt
$env:PYTHONPATH=src
python -m pytest -q
```

## TP 1 — Explorer les topics

```powershell
python -m iot_decision.mqtt_tools extract data/raw/batch002_observed.jsonl --topic airbase/batch002/#
```

En repli, utilisez `batch002_retained_messages.jsonl`. Relevez topic, zone, capteur, `measured_at`, `received_at`, retained. Le symbole `#` appartient au filtre, pas au topic publié.

## TP 2 — Construire l’inventaire

```powershell
python -m iot_decision.source_inventory_cli data/samples/batch002_retained_messages.jsonl data/samples/batch002_expected_sensors.csv data/processed/batch002_inventory.csv data/processed/batch002_completeness.json
```

Ouvrez d’abord le CSV sans regarder le JSON. Vérifiez effectif, unicité, zones et retained. Un inventaire décrit l’observé ; il ne prouve pas la complétude.

## TP 3 — Diagnostiquer la complétude

Comparez l’inventaire au référentiel attendu. Une ligne par topic : criticité, observé, preuve, vérification si absent. Calculez la couverture, puis ouvrez le diagnostic JSON.

Questions : filtre correct ? référentiel autorisé et à jour ? panne, non-publication, suppression ou erreur d’extraction ?

## TP 4 — Brief de décision

120 mots maximum : décision et périmètre ; confiance justifiée ; deux preuves ; deux incertitudes ; vérification prioritaire. Le décideur demande quelle hypothèse renverserait la conclusion et quelle action réversible réduit le risque.

## Validation

```powershell
python tests/validate_s02_artifacts.py
```

Le validateur ne valide ni l’autorité du référentiel ni votre décision.

## Exit ticket

1. Le broker permet d’affirmer que…
2. Il ne permet pas d’affirmer que…
3. Pour qualifier l’absence optronique, je vérifierais d’abord…
