# Séquences

Le cours comprend huit séquences de quatre heures. Chaque dossier reçoit les
slides Beamer, leur PDF compilé, un guide enseignant, un guide étudiant, les
exercices, l'évaluation et une checklist `instructions_avant_seance.md`.

## Convention pour les slides

Chaque dossier de séquence contient :

```text
slides/
├── sXX_nom_sequence.tex
├── sXX_nom_sequence.pdf
└── figures/
```

Le fichier `.tex` charge le préambule commun situé dans `latex/common/preamble.tex`.
Les images propres à la séquence sont placées dans `slides/figures/`. La compilation
doit être lancée depuis le dossier `slides/`. Le PDF est compilé et vérifié
avant livraison; seuls les fichiers intermédiaires (`.aux`, `.log`, `.nav`,
etc.) restent exclus du dépôt.
