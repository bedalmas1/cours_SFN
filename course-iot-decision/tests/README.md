# Tests

Les tests vérifieront les scripts Python et les cas de qualité de données. Ils seront ajoutés avec le code lors de l’étape 4.

`test_baseline_pipeline.py` teste les fonctions de la séquence 1. `validate_s01_artifacts.py` reconstruit le brut, le CSV et la figure dans un dossier temporaire, puis exécute le notebook.

`test_traceability.py` couvre parsing strict, erreurs, empreintes et candidats doublons. `validate_s03_artifacts.py` reconstruit et vérifie le CSV S03.

`test_quality.py` couvre les quatre contrôles de validité, la détection de doublon exact et la distinction silence réel/silence expliqué par un rejet. `validate_s04_artifacts.py` reconstruit `clean.csv`, `rejected.csv`, le rapport et la figure, puis exécute le notebook.
