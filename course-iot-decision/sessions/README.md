# Séquences

Le cours comprend huit séquences de quatre heures. Chaque dossier recevra progressivement des slides Beamer, un guide enseignant, un guide étudiant, des exercices et une évaluation.

## Convention pour les slides

Chaque dossier de séquence contient :

```text
slides/
├── sXX_nom_sequence.tex
└── figures/
```

Le fichier `.tex` charge le préambule commun situé dans `latex/common/preamble.tex`.
Les images propres à la séquence sont placées dans `slides/figures/`. La compilation
doit être lancée depuis le dossier `slides/`.
