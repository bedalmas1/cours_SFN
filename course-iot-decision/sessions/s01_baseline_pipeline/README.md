# Séquence 1 — Introduction et pipeline baseline

Séance de 4 h directement exploitable pour passer de messages MQTT retained à une recommandation opérationnelle prudente.

## Question directrice

**À la fin, les étudiants doivent décider si les mesures justifient de maintenir l’activité de maintenance drone prévue à 14 h 00, de déclencher une inspection terrain, de mettre temporairement la zone en sécurité ou de déclarer les données insuffisantes, avec un niveau de confiance et des limites explicites.**

## Livrables et démarrage rapide

Les livrables sont `data/raw/batch001_raw.jsonl`, `data/processed/batch001_measurements.csv`, `slides/figures/batch001_max_by_zone.png` et une recommandation structurée.

```bash
python3 -m pip install -r sessions/s01_baseline_pipeline/requirements.txt
export PYTHONPATH=src
python3 -m iot_decision.baseline_cli extract-sample data/samples/batch001_messages.jsonl data/raw/batch001_raw.jsonl
python3 -m iot_decision.baseline_cli transform data/raw/batch001_raw.jsonl data/processed/batch001_measurements.csv
python3 -m iot_decision.visualize_baseline data/processed/batch001_measurements.csv sessions/s01_baseline_pipeline/slides/figures/batch001_max_by_zone.png
python3 -m iot_decision.baseline_cli decide data/raw/batch001_raw.jsonl
python3 -m pytest -q
python3 tests/validate_s01_artifacts.py
```

Le mode MQTT et le plan de repli sont dans `guide_enseignant.md`. Le notebook propose un parcours guidé. Compiler les slides depuis leur dossier avec deux passes de `pdflatex`; les sorties LaTeX ne sont pas versionnées.

`instructions_avant_seance.md` rassemble la checklist de préparation enseignant. Le PDF distribué est `slides/s01_baseline_pipeline.pdf`.
