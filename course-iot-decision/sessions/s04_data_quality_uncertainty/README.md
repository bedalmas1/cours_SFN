# Séquence 4 — Qualité des données et incertitude

Séance de 4 h pour séparer les messages exploitables des messages rejetés, distinguer un silence réel d'un simple effet du filtrage, et décider du niveau de confiance à accorder à une alerte température.

## Question directrice

**À la fin, les étudiants doivent décider à partir de quel niveau d'erreur et de silence une alerte température devient insuffisante pour agir seule, avec une confiance, des preuves et une vérification prioritaire explicites.**

## Démarrage rapide

```bash
python3 -m pip install -r sessions/s04_data_quality_uncertainty/requirements.txt
export PYTHONPATH=src
python3 -m iot_decision.quality_cli data/samples/batch002_quality_messages.jsonl data/processed/batch002_measurements_clean.csv data/processed/batch002_rejected.csv data/processed/batch002_quality_report.json
python3 -m iot_decision.visualize_quality data/processed/batch002_measurements_clean.csv data/processed/batch002_rejected.csv sessions/s04_data_quality_uncertainty/slides/figures/batch002_quality_timeline.png
python3 -m pytest -q
python3 tests/validate_s04_artifacts.py
```

Livrables : `batch002_measurements_clean.csv`, `batch002_rejected.csv` (avec raison de rejet), `batch002_quality_report.json`, une chronologie figurée, et un rapport qualité rédigé avec niveau de confiance. Le PDF projetable est `slides/s04_data_quality_uncertainty.pdf`.

Le mode MQTT et le plan de repli sont dans `guide_enseignant.md`. Le notebook `notebooks/s04_data_quality_uncertainty.ipynb` propose un parcours guidé sans corrigé.
