# Séquence 7 — Confiance, sécurité et robustesse de la chaîne

Séance de 4 h pour relier sécurité, intégrité des données et qualité de décision. Le matin compare, sur le même broker Mosquitto, un accès anonyme et un accès authentifié restreint par ACL. L'après-midi diagnostique un lot suspect (`data/samples/batch004_suspect_scenario.jsonl`) où un doublon exact, un candidat de rejeu et une incohérence temporelle coexistent avec des mesures physiquement normales.

Cette séquence est la première depuis la séquence 2 à remettre le broker MQTT au premier plan : elle en interroge la protection, pas le contenu.

## Question directrice

**À la fin, les étudiants doivent décider que vaut une décision opérationnelle si l'on ne peut pas qualifier la confiance dans la chaîne de données, avec une matrice des risques data/cyber et une recommandation de sécurisation minimale.**

## Démarrage rapide

```bash
python3 -m pip install -r sessions/s07_security_trust_robustness/requirements.txt
export PYTHONPATH=src
docker compose -f docker/docker-compose.yml up -d --wait mosquitto mosquitto-protected
python3 -m iot_decision.chain_trust_cli data/samples/batch004_suspect_scenario.jsonl
python3 -m pytest -q
python3 tests/validate_s07_artifacts.py
docker compose -f docker/docker-compose.yml down
```

Livrables : matrice des risques data/cyber ; diagnostic de confiance ; recommandations de sécurisation minimale. Le PDF projetable est `slides/s07_security_trust_robustness.pdf`.

Le notebook `notebooks/s07_security_trust_robustness.ipynb` propose un parcours guidé sans corrigé. Identifiants et configuration du broker protégé documentés dans `docker/mosquitto/README.md` — usage strictement local, jamais à réexposer.
