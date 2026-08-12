# Séquence 6 — Visualisation et communication au décideur

Séance de 4 h pour produire une visualisation claire sans sur-vendre la certitude. Les mêmes trois mesures de `battery-shelter-01` (séquence 4) sont mises en forme deux fois : une version à échelle tronquée qui exagère la hausse, une version à échelle complète qui affiche le seuil et annonce explicitement le silence de vingt minutes qui précède la mesure haute. Aucune valeur n'est recalculée entre les deux : seule la mise en forme change.

Cette séquence ne touche pas le broker MQTT et n'introduit aucune nouvelle donnée : elle travaille entièrement sur `data/processed/batch002_measurements_clean.csv`, déjà produit par la séquence 4.

## Question directrice

**À la fin, les étudiants doivent décider comment présenter une alerte sans donner une impression excessive de certitude, avec un graphique honnête et une note de briefing explicite (message principal, limite, confiance, vérification).**

## Démarrage rapide

```bash
python3 -m pip install -r sessions/s06_visualization_decision_briefing/requirements.txt
export PYTHONPATH=src
python3 -m iot_decision.briefing_cli data/processed/batch002_measurements_clean.csv battery-shelter-01
python3 -m iot_decision.briefing_cli data/processed/batch002_measurements_clean.csv comms-shelter-01
python3 -m iot_decision.visualize_briefing data/processed/batch002_measurements_clean.csv battery-shelter-01 sessions/s06_visualization_decision_briefing/slides/figures/battery_misleading.png sessions/s06_visualization_decision_briefing/slides/figures/battery_honest.png
python3 -m pytest -q
python3 tests/validate_s06_artifacts.py
```

Livrables : 2 à 3 graphiques (mise en forme trompeuse et honnête d'une même zone) ; mini-rapport opérationnel ; niveau de confiance explicite ; recommandation. Le PDF projetable est `slides/s06_visualization_decision_briefing.pdf`.

Le notebook `notebooks/s06_visualization_decision_briefing.ipynb` propose un parcours guidé sans corrigé.
