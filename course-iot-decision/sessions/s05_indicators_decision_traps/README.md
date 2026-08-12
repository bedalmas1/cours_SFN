# Séquence 5 — Indicateurs, agrégations et pièges décisionnels

Séance de 4 h pour montrer qu'un indicateur — un simple calcul statistique ou un score produit par un modèle automatique — compresse toujours la réalité et peut masquer un risque. Plus ce calcul devient opaque, plus il doit être interrogé avant d'être suivi.

Cette séquence ne touche pas le broker MQTT : elle travaille entièrement sur des données déjà produites par les séquences précédentes (`data/processed/batch001_measurements.csv`, `data/raw/batch001_raw.jsonl`), ce qui illustre qu'un indicateur ou une décision automatisée se situe toujours en aval de toute une chaîne déjà vue.

## Question directrice

**À la fin, les étudiants doivent décider quel indicateur, ou quel processus de décision, est réellement digne de confiance pour décider de maintenir ou non l'activité, avec confiance, preuves et vérification prioritaire explicites.**

## Démarrage rapide

```bash
python3 -m pip install -r sessions/s05_indicators_decision_traps/requirements.txt
export PYTHONPATH=src
python3 -m iot_decision.indicators_cli data/processed/batch001_measurements.csv
python3 -m iot_decision.risk_score_cli data/raw/batch001_raw.jsonl
python3 -m iot_decision.risk_score_cli data/samples/batch003_shift_scenario.jsonl
python3 -m iot_decision.visualize_indicators data/processed/batch001_measurements.csv sessions/s05_indicators_decision_traps/slides/figures/batch001_masked_zone.png
python3 -m iot_decision.visualize_risk_score data/raw/batch001_raw.jsonl data/samples/batch003_shift_scenario.jsonl sessions/s05_indicators_decision_traps/slides/figures/batch003_risk_score_shift.png
python3 -m pytest -q
python3 tests/validate_s05_artifacts.py
```

Livrables : tables d'indicateurs ; zone masquée par la moyenne identifiée ; journal des requêtes au score automatique ; recommandation sur le processus de décision à suivre. Le PDF projetable est `slides/s05_indicators_decision_traps.pdf`.

Le notebook `notebooks/s05_indicators_decision_traps.ipynb` propose un parcours guidé sans corrigé. `src/iot_decision/risk_score.py` ne doit pas être ouvert par les étudiants avant le débrief : c'est le fichier qui est révélé à 2:45, pas un support de lecture.
