# Séquence 3 — Parsing, structuration et traçabilité

Cette séquence transforme les enveloppes MQTT JSONL de `batch001` en table structurée sans rompre le lien avec la source. Question directrice : **quelles informations faut-il conserver pour justifier plus tard un indicateur et la décision qu’il a soutenue ?**

## Résultat attendu

- `data/processed/batch001_structured.csv` (15 lignes) ;
- un schéma commenté fondé sur `schema_donnees.md` ;
- une justification des champs conservés ;
- une décision avec confiance, preuves, incertitudes et limites.

Le CSV conserve `source_file`, `source_line` et `raw_sha256`. Ils permettent de retrouver la ligne brute et de vérifier qu’elle n’a pas changé, mais ne prouvent ni vérité physique ni identité de l’auteur.

## Parcours

1. Lire `instructions_avant_seance.md`, puis `guide_etudiant.md`.
2. Exécuter `notebooks/s03_parsing_traceability.ipynb` ou la CLI.
3. Traiter `exercices.md`, puis utiliser `evaluation.md`.
4. Réserver `corrige.md` et `guide_enseignant.md` à l’enseignant.

```bash
source .venv/bin/activate
export PYTHONPATH=src
python3 -m iot_decision.traceability_cli parse data/samples/batch001_messages.jsonl data/processed/batch001_structured.csv
python3 -m iot_decision.traceability_cli verify data/samples/batch001_messages.jsonl data/processed/batch001_structured.csv
python3 tests/validate_s03_artifacts.py
```

## Décision de référence

L’indicateur issu des 15 lignes est reproductible et relié au brut : confiance élevée dans la correspondance brut/table. La confiance reste moyenne dans l’usage opérationnel : le hash ne valide ni capteur, ni horloge, ni calibration, ni exhaustivité.
