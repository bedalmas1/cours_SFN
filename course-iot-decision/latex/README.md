# Ressources LaTeX partagées

Le dossier `common/` contient les éléments communs aux huit présentations :

- `preamble.tex` : dépendances et commandes Beamer minimales ;
- `references.bib` : bibliographie BibTeX commune.

Chaque présentation reste dans le dossier `slides/` de sa séquence. Depuis ce
dossier, le préambule est chargé avec :

```tex
\input{../../../latex/common/preamble}
```

Les fichiers produits par la compilation sont ignorés par Git.
