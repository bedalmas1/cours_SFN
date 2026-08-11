# Guide de démarrage — Séquence 4

Toutes les commandes s'exécutent sous Linux dans Bash, depuis la racine du dépôt.

## Environnement et dépendances

```bash
cd /chemin/vers/course-iot-decision
source .venv/bin/activate
python3 -m pip install -r sessions/s04_data_quality_uncertainty/requirements.txt
export PYTHONPATH=src
python3 -m pytest -q
```

Si `.venv` existe, ne pas la recréer. `which python3` doit pointer vers `.venv/bin/python3`.

## Broker et Docker

S04 peut fonctionner sans broker, à partir de l'échantillon conservé en séance. Pour redémontrer l'origine MQTT :

```bash
docker compose -f docker/docker-compose.yml up -d --wait
python3 -m iot_decision.mqtt_tools seed data/samples/batch002_quality_messages.jsonl
python3 -m iot_decision.mqtt_tools extract /tmp/s04_teacher_check.jsonl --topic airbase/batch002/#
wc -l /tmp/s04_teacher_check.jsonl
```

Attendu : `24`. Le broker étant repris à neuf à chaque séance, aucun message d'une séquence précédente n'y persiste. Arrêt : `docker compose -f docker/docker-compose.yml down`.

## Supports et contrôle à blanc

```bash
test -f data/samples/batch002_quality_messages.jsonl
test -f notebooks/s04_data_quality_uncertainty.ipynb
mkdir -p /tmp/s04
python3 -m iot_decision.quality_cli data/samples/batch002_quality_messages.jsonl /tmp/s04/clean.csv /tmp/s04/rejected.csv /tmp/s04/report.json
python3 -m iot_decision.visualize_quality /tmp/s04/clean.csv /tmp/s04/rejected.csv /tmp/s04/timeline.png
python3 tests/validate_s04_artifacts.py
```

Attendu : `19 lignes propres; 5 lignes rejetées`, un silence réel signalé sur `battery-shelter-01` et trois silences expliqués par un rejet, puis `S04 valide`.

## Précautions et matériel

- PDF et guide enseignant ouverts ; guide étudiant distribué sans corrigé.
- Binômes « équipe data » / « décideur critique » ; incident du silence caché jusqu'au moment indiqué du conducteur.
- Ne jamais qualifier les bornes de valeur (-10 à 60 °C) ou le seuil de 35 °C de spécification capteur réelle.
- Ne jamais corriger silencieusement une valeur : rejeter et documenter la raison, ou laisser propre.
- Faire vérifier, avant toute conclusion sur un silence, qu'aucune ligne rejetée de la même zone ne s'y trouve.

## Plan de repli

- Sans Docker : utiliser l'échantillon et noter sa provenance dans le journal.
- Sans Jupyter : utiliser la CLI ; tous les livrables restent possibles.
- Poste en panne : fournir `/tmp/s04/clean.csv` et `/tmp/s04/rejected.csv` en consignant leur provenance.
- Retard supérieur à 15 min : fournir directement les CSV et le rapport JSON, maintenir le débat sur le silence et la décision finale.

## Dernière minute

- [ ] environnement activé, `PYTHONPATH=src`, tests réussis ;
- [ ] 24 messages bruts disponibles, cinq zones, silence de `battery-shelter-01` non révélé ;
- [ ] notebook ou CLI prêt, PDF lisible, corrigé non distribué ;
- [ ] plan de repli testé ;
- [ ] consigne « décision, confiance, preuves, incertitudes, limites » visible.
