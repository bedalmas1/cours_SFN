# Guide de démarrage — Séquence 6

Toutes les commandes s'exécutent sous Linux dans Bash, depuis la racine du dépôt.

## Environnement et dépendances

```bash
cd /chemin/vers/course-iot-decision
source .venv/bin/activate
python3 -m pip install -r sessions/s06_visualization_decision_briefing/requirements.txt
export PYTHONPATH=src
python3 -m pytest -q
```

Si `.venv` existe, ne pas la recréer. `which python3` doit pointer vers `.venv/bin/python3`.

## Pas de broker requis

S6 travaille entièrement sur un fichier déjà produit : `data/processed/batch002_measurements_clean.csv` (séquence 4). Docker et MQTT ne sont pas nécessaires. Vérifier simplement sa présence :

```bash
test -f data/processed/batch002_measurements_clean.csv && echo "présent"
```

## Supports et contrôle à blanc

```bash
test -f notebooks/s06_visualization_decision_briefing.ipynb
test -f sessions/s06_visualization_decision_briefing/slides/figures/battery_misleading.png
test -f sessions/s06_visualization_decision_briefing/slides/figures/battery_honest.png
mkdir -p /tmp/s06
python3 -m iot_decision.briefing_cli data/processed/batch002_measurements_clean.csv battery-shelter-01
python3 -m iot_decision.briefing_cli data/processed/batch002_measurements_clean.csv comms-shelter-01
python3 -m iot_decision.visualize_briefing data/processed/batch002_measurements_clean.csv battery-shelter-01 /tmp/s06/misleading.png /tmp/s06/honest.png
python3 tests/validate_s06_artifacts.py
```

Attendu : `battery-shelter-01: 1/3 mesure(s) >= 35 °C, maximum 36.2 °C` et `Niveau de confiance : faible` ; `comms-shelter-01: 0/5 mesure(s) >= 35 °C, maximum 29.9 °C` et `Niveau de confiance : moyenne` ; puis `S06 valide`.

## Précautions et matériel

- PDF et guide enseignant ouverts ; guide étudiant distribué sans corrigé.
- Projeter le premier graphique (`battery_misleading.png`) seul, sans le second, avant le vote initial.
- Ne jamais qualifier l'échelle tronquée de « fausse » ni le seuil pédagogique de 35 °C de norme officielle.
- Binômes « cellule data » / « décideur critique » pour le matin ; à 1:55, redistribuer les rôles pour le jeu de rôle de l'après-midi (cellule data, décideur pressé, red team).
- Prévoir un chronomètre visible pour le brief oral de 3 minutes par groupe.

## Plan de repli

- Sans Jupyter : utiliser la CLI ; tous les livrables restent possibles.
- Poste en panne : fournir les sorties CLI (`briefing_cli`, `visualize_briefing`) en consignant leur provenance.
- Retard supérieur à 15 min : fournir directement les deux figures et la note de briefing de référence, maintenir le brief oral et les questions contradictoires.

## Dernière minute

- [ ] environnement activé, `PYTHONPATH=src`, tests réussis ;
- [ ] `batch002_measurements_clean.csv` disponible ;
- [ ] les deux figures de démonstration présentes et lisibles ;
- [ ] notebook ou CLI prêt, PDF lisible, corrigé non distribué ;
- [ ] consigne « message principal, limite, confiance, vérification » visible ;
- [ ] chronomètre prêt pour le brief oral.
