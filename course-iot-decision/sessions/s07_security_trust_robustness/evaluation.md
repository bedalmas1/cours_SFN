# Évaluation flash — Séquence 7

Évaluation de binôme sur les artefacts et individuelle sur l'exit ticket. La réussite technique seule ne peut dépasser 10/20 : l'objet est le raisonnement décisionnel sur la confiance dans la chaîne.

| Critère | Points | Indices observables |
|---|---:|---|
| Concepts de sécurité correctement distingués | 4 | intégrité, authentification, ACL, injection et rejeu non confondus entre eux |
| Démonstration broker ouvert/protégé interprétée | 3 | asymétrie explicite/silencieux du refus de connexion vs du rejet ACL identifiée |
| Vulnérabilités identifiées | 3 | liste couvrant au moins l'accès anonyme, le dépassement de périmètre et l'absence de TLS |
| Diagnostic du lot suspect | 4 | les quatre signaux relevés avec leurs valeurs exactes, candidat de rejeu relié à sa mesure d'origine |
| Matrice des risques et recommandation | 4 | quatre hypothèses classées par probabilité et impact, non traitées comme mutuellement exclusives ; recommandation d'isolement justifiée |
| Exit ticket | 2 | distingue clairement contrôle qualité (séquence 4) et confiance dans la chaîne (séquence 7) |

Niveaux : 17–20 diagnostic défendable distinguant précisément confiance dans la source, confiance dans le traitement et qualité au sens de la séquence 4 ; 13–16 diagnostic correct, distinctions peu hiérarchisées ; 10–12 vulnérabilités identifiées mais matrice ou recommandation faibles ; <10 confusion entre qualité et sécurité, ou conclusion catégorique sans vérification proposée.

Attribuer les points techniques seulement si `python3 tests/validate_s07_artifacts.py` réussit. Une aide IA via `prompts/s07_assessment_prompt.md` reste une pré-évaluation : l'enseignant vérifie les citations, protège les données et décide de la note.
