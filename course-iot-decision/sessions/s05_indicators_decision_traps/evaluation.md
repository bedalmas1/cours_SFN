# Évaluation flash — Séquence 5

Évaluation de binôme sur les artefacts et individuelle sur l'exit ticket. La réussite technique seule ne peut dépasser 10/20 : l'objet est le raisonnement décisionnel.

| Critère | Points | Indices observables |
|---|---:|---|
| Indicateurs transparents et zone masquée | 4 | moyenne globale calculée, `battery-shelter-01` identifiée, durée au-dessus du seuil non sur-interprétée |
| Interrogation du score sans lecture prématurée | 3 | score utilisé comme un décideur pressé le ferait, `risk_score.py` non ouvert avant le débrief |
| Incident hors distribution diagnostiqué | 4 | `fuel-storage-01` reconnue comme jamais vue à la calibration, seuil de sécurité réel du carburant cité |
| Procès à trois (moyenne / maximum / score) | 4 | arguments pour chaque partie, portée et limite de chaque indicateur explicitées |
| Recommandation et confiance | 3 | processus de décision choisi et justifié, deux preuves, deux incertitudes, vérification prioritaire |
| Exit ticket | 2 | distingue ce qu'un indicateur, transparent ou non, permet et ne permet pas d'affirmer |

Niveaux : 17–20 diagnostic défendable distinguant compression transparente et opaque ; 13–16 diagnostic correct, limites peu hiérarchisées ; 10–12 indicateurs corrects mais confiance ou vérification faibles ; <10 confusion moyenne/maximum, lecture prématurée du score, ou surconclusion sur `fuel-storage-01`.

Attribuer les points techniques seulement si `python3 tests/validate_s05_artifacts.py` réussit. Une aide IA via `prompts/s05_assessment_prompt.md` reste une pré-évaluation : l'enseignant vérifie les citations, protège les données et décide de la note.
