# Exercices — Séquence 2

Chaque activité se termine par : décision provisoire, confiance, preuve, incertitude et limite.

## Correspondance activités / TP

| Activité | Repère étudiant | Production |
|---|---|---|
| A | Vote initial | hypothèses sur la fiabilité du broker |
| B–C | Apports + TP 1 | vocabulaire MQTT et exploration des topics |
| D | TP 2 | inventaire des messages et zones |
| E | Transition | lot, référentiel, complétude, métadonnées |
| F–G | TP 3 | matrice attendu/observé et diagnostic |
| H | TP 4 + brief | décision après incident et contradiction |
| I | Exit ticket | portée et limites du constat |

## A — Le broker est-il une source fiable ? — 15 min

Une relève doit confirmer que cinq zones critiques disposent d’une information thermique avant 10 h. Un opérateur annonce : « le broker répond et contient des messages retained ». Choisissez : **A. couverture suffisante ; B. inspection ciblée ; C. suspendre la conclusion ; D. impossible à qualifier sans inventaire.** Notez confiance, preuve et information manquante.

## B — Construire le modèle mental MQTT — 20 min

Associez publisher, broker, subscriber, topic, topic filter et payload à leur rôle. Pour chaque confusion, indiquez l’effet sur la décision. Le broker connaît-il la liste métier des capteurs attendus ?

## C / TP 1 — Explorer sans interpréter trop vite — 40 min

```powershell
python -m iot_decision.mqtt_tools extract data/raw/batch002_observed.jsonl --topic airbase/batch002/#
```

En repli, ouvrez `batch002_retained_messages.jsonl`. Relevez topic, niveaux, payload, `measured_at`, `received_at` et retained. Remplissez « j’observe » / « je peux conclure ».

## D / TP 2 — Produire l’inventaire — 35 min

Consignez topic, zone, capteur, identifiant, horodatages et retained. Trace : `batch002_inventory.csv` et tableau zones/capteurs.

```powershell
$env:PYTHONPATH=src
python -m iot_decision.source_inventory_cli data/samples/batch002_retained_messages.jsonl data/samples/batch002_expected_sensors.csv data/processed/batch002_inventory.csv data/processed/batch002_completeness.json
```

## Pause — 10 min

## E — « Complet » par rapport à quoi ? — 25 min

Classez comme observable, vérifiable avec référentiel, ou impossible : « toutes les zones attendues sont présentes », « aucun message n’a été perdu », « chaque retained est récent », « tous les capteurs fonctionnent ».

## F / TP 3 — Matrice attendu / observé — 30 min

Ouvrez `batch002_expected_sensors.csv`. Une ligne par topic attendu : présent/absent, criticité, preuve. Calculez la couverture et expliquez pourquoi le taux ne suffit pas.

## G — Incident : capteur attendu absent — 25 min

L’abri optronique devait être couvert. Distinguez panne, non-publication, filtre incorrect et retained supprimé. Proposez une vérification discriminante. L’absence ne prouve pas une température normale.

## H / TP 4 — Brief contradictoire — 35 min

120 mots maximum : action, confiance, deux preuves, deux incertitudes, périmètre et vérification. Le décideur demande : « puis-je conclure pour toute la base ? » Revotez A à D.

## I — Exit ticket — 5 min

« le broker permet d’affirmer… » ; « il ne permet pas… » ; « pour qualifier l’absence optronique, je vérifierais… ».
