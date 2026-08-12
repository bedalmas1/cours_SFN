# Guide de démarrage — Séquence 5

Toutes les commandes s'exécutent sous Linux dans Bash, depuis la racine du dépôt.

## Environnement et dépendances

```bash
cd /chemin/vers/course-iot-decision
source .venv/bin/activate
python3 -m pip install -r sessions/s05_indicators_decision_traps/requirements.txt
export PYTHONPATH=src
python3 -m pytest -q
```

Si `.venv` existe, ne pas la recréer. `which python3` doit pointer vers `.venv/bin/python3`.

## Pas de broker requis

S5 travaille entièrement sur des fichiers déjà produits : `data/processed/batch001_measurements.csv` (séquence 1) et `data/raw/batch001_raw.jsonl`. Docker et MQTT ne sont pas nécessaires. Vérifier simplement leur présence :

```bash
test -f data/processed/batch001_measurements.csv && echo "présent"
test -f data/raw/batch001_raw.jsonl && echo "présent"
test -f data/samples/batch003_shift_scenario.jsonl && echo "présent"
```

## Supports et contrôle à blanc

```bash
test -f notebooks/s05_indicators_decision_traps.ipynb
mkdir -p /tmp/s05
python3 -m iot_decision.indicators_cli data/processed/batch001_measurements.csv
python3 -m iot_decision.risk_score_cli data/raw/batch001_raw.jsonl
python3 -m iot_decision.risk_score_cli data/samples/batch003_shift_scenario.jsonl
python3 -m iot_decision.visualize_indicators data/processed/batch001_measurements.csv /tmp/s05/masked_zone.png
python3 -m iot_decision.visualize_risk_score data/raw/batch001_raw.jsonl data/samples/batch003_shift_scenario.jsonl /tmp/s05/risk_score_shift.png
python3 tests/validate_s05_artifacts.py
```

Attendu : `moyenne globale: 30.75 °C`, `battery-shelter-01` signalée comme zone masquée ; `battery-shelter-01: score 71/100 -> inspection recommandée` ; `fuel-storage-01: score 62/100 -> aucune action requise` ; puis `S05 valide`.

## Précautions et matériel

- PDF et guide enseignant ouverts ; guide étudiant distribué sans corrigé.
- **Ne jamais ouvrir ni projeter `src/iot_decision/risk_score.py` avant 2:45** : c'est le fichier révélé au débrief de l'incident, pas un support de cours.
- Binômes « équipe data » / « décideur critique » pour le matin ; à 1:55, redistribuer les rôles pour l'après-midi.
- Ne jamais qualifier 35 °C ou le seuil de décision 65/100 de norme réelle : ce sont des choix pédagogiques.
- Le procès à trois (moyenne / maximum / score) n'a de sens qu'après l'incident : ne pas l'anticiper avant 3:10.

## Plan de repli

- Sans Jupyter : utiliser la CLI ; tous les livrables restent possibles.
- Poste en panne : fournir les sorties CLI (`indicators_cli`, `risk_score_cli`) en consignant leur provenance.
- Retard supérieur à 15 min : fournir directement les deux figures et le rapport du validateur, maintenir le procès et la décision finale.

## Dernière minute

- [ ] environnement activé, `PYTHONPATH=src`, tests réussis ;
- [ ] `batch001_measurements.csv`, `batch001_raw.jsonl` et `batch003_shift_scenario.jsonl` disponibles ;
- [ ] `risk_score.py` fermé, non projeté, non mentionné avant le débrief ;
- [ ] notebook ou CLI prêt, PDF lisible, corrigé non distribué ;
- [ ] consigne « décision, confiance, preuves, incertitudes, limites » visible.
