# Évaluation flash — Séquence 4

Évaluation de binôme sur les artefacts et individuelle sur l'exit ticket. La réussite technique seule ne peut dépasser 10/20 : l'objet est le raisonnement décisionnel.

| Critère | Points | Indices observables |
|---|---:|---|
| Validité ligne à ligne | 3 | quatre types d'erreurs correctement identifiés et nommés, aucune correction silencieuse |
| Séparation propre/rejeté | 3 | `clean.csv` et `rejected.csv` reproductibles, raison de rejet explicite pour chaque ligne écartée |
| Silence réel contre silence expliqué | 4 | distingue le silence de `battery-shelter-01` (réel) des trois autres (expliqués par un rejet) |
| Rapport qualité | 3 | chiffres corrects et retrouvables, formulation prudente, bornes qualifiées de pédagogiques |
| Recommandation et confiance | 5 | action proportionnée, confiance justifiée par le silence réel, deux preuves, deux incertitudes, vérification prioritaire |
| Exit ticket | 2 | distingue ce que le contrôle qualité permet et ne permet pas d'affirmer |

Niveaux : 17–20 diagnostic défendable et traçable ; 13–16 diagnostic correct, limites peu hiérarchisées ; 10–12 séparation propre/rejeté exploitable, confiance ou vérification faibles ; <10 correction silencieuse, confusion silence/rejet, ou surconclusion sur la cause du silence.

Attribuer les points techniques seulement si `python3 tests/validate_s04_artifacts.py` réussit. Une aide IA via `prompts/s04_assessment_prompt.md` reste une pré-évaluation : l'enseignant vérifie les citations, protège les données et décide de la note.
