# Instructions avant séance — Séquence 2

Prévoir 30 à 45 minutes la veille, puis dix minutes juste avant l’accueil.

## 1. Dépendances et contrôles

```powershell
python -m pip install -r sessions/s02_mqtt_broker_data_source/requirements.txt
$env:PYTHONPATH=src
python -m pytest -q
python tests/validate_s02_artifacts.py
```

Le validateur doit détecter 4 topics sur 5 et l’absence optronique.

## 2. Broker local

```powershell
docker compose -f docker/docker-compose.yml up -d --wait
python -m iot_decision.mqtt_tools seed data/samples/batch002_retained_messages.jsonl
python -m iot_decision.mqtt_tools extract C:\tmp\s02_teacher_check.jsonl --topic airbase/batch002/#
```

Le test produit quatre enveloppes. Le broker anonyme écoute uniquement sur `127.0.0.1` ; ne pas l’exposer. Pour arrêter : `docker compose -f docker/docker-compose.yml down`.

## 3. Supports et matériel

- ouvrir PDF, guide enseignant, corrigé et évaluation ;
- distribuer uniquement guide étudiant et exercices ;
- préparer cartes A–D, matrice attendu/observé vierge et journal par binôme ;
- vérifier terminal, Python et droits d’écriture ;
- garder le JSONL comme plan B ;
- ne pas montrer le référentiel avant l’activité E.

## 4. Précautions pédagogiques

1. Ne pas révéler l’absence optronique pendant l’exploration.
2. Exiger le filtre exact avant une affirmation d’absence.
3. Distinguer « quatre topics observés » de « quatre capteurs fonctionnels ».
4. Ne pas laisser 80 % masquer la criticité de la zone absente.
5. Exiger décision, confiance et périmètre.
6. Rappeler qu’un référentiel réel a une autorité et une date de validité.

## 5. Plan B

```powershell
python -m iot_decision.source_inventory_cli data/samples/batch002_retained_messages.jsonl data/samples/batch002_expected_sensors.csv data/processed/batch002_inventory.csv data/processed/batch002_completeness.json
```

Un échec d’accès à la source devient une trace qui diminue la confiance.

## 6. Dernière minute

Tests réussis ; quatre messages ou échantillon disponible ; référentiel masqué ; PDF lisible ; cartes, matrices et chronomètre prêts ; rôles attribuables ; plan B testé.
