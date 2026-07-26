# Guide de démarrage — Séquence 3

Toutes les commandes s’exécutent sous Linux dans Bash, depuis la racine du dépôt.

## Environnement et dépendances

```bash
cd /chemin/vers/course-iot-decision
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r sessions/s03_parsing_traceability/requirements.txt
export PYTHONPATH=src
python3 -m pytest -q
```

Si `.venv` existe, ne pas la recréer. `which python3` doit pointer vers `.venv/bin/python3`.

## Broker et Docker

S03 utilise normalement le JSONL conservé en S01 ; le broker n’est pas requis. Vérifier la continuité :

```bash
docker --version
docker compose version
docker compose -f docker/docker-compose.yml config --quiet
```

Pour redémontrer l’origine MQTT :

```bash
docker compose -f docker/docker-compose.yml up -d --wait
python3 -m iot_decision.mqtt_tools seed data/samples/batch001_messages.jsonl
docker compose -f docker/docker-compose.yml ps
```

Arrêter avec `docker compose -f docker/docker-compose.yml down`. Ne jamais réextraire par-dessus le brut de référence.

## Supports et contrôle à blanc

```bash
test -f data/samples/batch001_messages.jsonl
test -f data/samples/batch001_traceability_incident.jsonl
test -f notebooks/s03_parsing_traceability.ipynb
wc -l data/samples/batch001_messages.jsonl
mkdir -p /tmp/s03
python3 -m iot_decision.traceability_cli parse data/samples/batch001_messages.jsonl /tmp/s03/teacher.csv
python3 -m iot_decision.traceability_cli verify data/samples/batch001_messages.jsonl /tmp/s03/teacher.csv
python3 tests/validate_s03_artifacts.py
```

Attendu : `15`, `15 lignes structurées`, `traçabilité vérifiée`, puis `S03 valide`.

## Précautions et matériel

- PDF et guide enseignant ouverts ; guide étudiant distribué sans corrigé.
- Binômes « data » / « décideur critique » ; incident caché jusqu’à 3 h 10.
- Ne jamais qualifier le CSV de vérité ou le hash de signature.
- Ne pas laisser une erreur de parsing disparaître silencieusement.
- Distinguer schéma valide, plausibilité physique et authenticité.

## Plan de repli

- Sans Docker : utiliser l’échantillon et noter sa provenance.
- Sans Jupyter : utiliser la CLI ; tous les livrables restent possibles.
- Poste en panne : fournir `/tmp/s03/teacher.csv` en consignant sa provenance.
- Retard supérieur à 15 min : fournir le CSV, maintenir retour au brut et décision.

## Dernière minute

- [ ] environnement activé, `PYTHONPATH=src`, tests réussis ;
- [ ] 15 lignes brutes et incident disponibles, brut intact ;
- [ ] notebook ou CLI prêt, PDF lisible, corrigé non distribué ;
- [ ] incident caché, plan de repli testé ;
- [ ] consigne « décision, confiance, preuves, incertitudes, limites » visible.
