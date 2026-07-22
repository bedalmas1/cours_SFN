# Exercices — Séquence 2

Ce document donne les consignes distribuables. Les commandes sont exécutées depuis la racine du dépôt. Chaque activité produit une réponse écrite ; une commande réussie sans interprétation ne suffit pas.

## Tableau de progression

| Activité | Temps | Repère | Livrable |
|---|---:|---|---|
| A | 15 min | vote initial | décision, confiance, preuve manquante |
| B | 20 min | modèle MQTT | tableau rôle / sait / ignore / risque |
| C | 20 min | TP 1 | fiche observe/conclus |
| D | 30 min | TP 2 | inventaire CSV contrôlé |
| E | 25 min | complétude | classement des affirmations |
| F–G | 55 min | TP 3 | matrice, taux, hypothèses, vérifications |
| H | 15 min | TP 4 | brief ≤120 mots et vote final |
| I | 5 min | exit ticket | trois phrases individuelles |

## A — Décider avant l’inventaire

Situation : cinq zones critiques doivent être couvertes avant 10 h. Le broker répond et contient des retained.

1. Choisissez A couverture suffisante, B inspection ciblée, C suspendre la conclusion globale ou D impossible sans inventaire.
2. Donnez une confiance de 0 à 100 %.
3. Citez la seule preuve réellement disponible dans l’énoncé.
4. Nommez l’information manquante qui pourrait changer votre décision.
5. Expliquez le coût possible d’une zone critique oubliée.

## B — Qui sait quoi dans MQTT ?

Complétez pour publisher, broker et subscriber : entrée reçue ; sortie produite ; information connue ; information ignorée ; erreur possible ; effet sur la décision.

Questions : qui choisit le topic ? qui conserve éventuellement un retained ? qui connaît la liste métier attendue ? le payload est-il automatiquement validé par le broker ?

## C / TP 1 — Explorer l’état observé

1. Prédisez le résultat du filtre `airbase/batch002/#`.
2. Exécutez l’extraction broker ou le plan de repli indiqué dans `guide_etudiant.md`.
3. Vérifiez présence, effectif et première ligne avec `Test-Path` et `Get-Content`.
4. Produisez une ligne « j’observe / je peux conclure » par message.

Répondez : combien de topics ? quel filtre ? quels champs dans l’enveloppe ? quels champs dans le payload ? retained démontre-t-il la fraîcheur ? pouvez-vous conclure à la complétude ?

## D / TP 2 — Construire l’inventaire

1. Exécutez `source_inventory_cli` avec les quatre chemins du guide.
2. Ouvrez le CSV avec `Import-Csv`.
3. Contrôlez quatre lignes et quatre topics uniques.
4. Relevez les quatre zones et les métadonnées conservées.

Répondez : quelle colonne prouve le périmètre interrogé ? pourquoi conserver les deux horloges ? pourquoi « quatre topics observés » est-il plus exact que « quatre capteurs fonctionnent » ?

## E — Complet par rapport à quoi ?

Classez chaque phrase : directement observable ; vérifiable seulement avec un référentiel ; non démontrable dans cette séance.

- toutes les zones attendues sont présentes ;
- aucun message n’a été perdu ;
- chaque retained est récent ;
- le filtre couvre la branche batch002 ;
- tous les capteurs fonctionnent ;
- quatre topics uniques ont été inventoriés.

Pour chaque classement, citez le fichier ou la métadonnée nécessaire.

## F / TP 3 — Comparer attendu et observé

1. Affichez le référentiel avec `Import-Csv` et comptez cinq lignes.
2. Construisez la matrice manuelle avant d’ouvrir le diagnostic JSON.
3. Calculez la couverture globale.
4. Contrôlez votre résultat avec `ConvertFrom-Json`.
5. Localisez la zone absente et sa criticité.

Répondez : quel est le numérateur ? le dénominateur ? quelle est l’autorité supposée du référentiel ? pourquoi 80 % global masque-t-il une couverture optronique de 0 % ?

## G — Incident optronique

Produisez un tableau avec au moins quatre hypothèses : panne, non-publication, retained supprimé, filtre erroné, extraction interrompue, référentiel obsolète. Pour chaque hypothèse : ce qui serait observable ; vérification ; résultat qui la renforce ; résultat qui l’affaiblit ; action provisoire.

Question centrale : quelle vérification permet de réduire l’incertitude le plus vite sans transformer le silence en mesure ?

## H / TP 4 — Brief contradictoire

Rédigez 120 mots maximum avec action, périmètre, confiance, deux preuves, deux incertitudes et une vérification. Le décideur doit pouvoir retrouver chaque preuve dans `batch002_inventory.csv`, `batch002_completeness.json` ou le référentiel attendu.

Le contradicteur pose les cinq questions du guide étudiant. Révisez puis votez. Remettez le brief initial, l’objection principale et le brief révisé.

## I — Exit ticket

Complétez les trois phrases du guide étudiant. Une réponse contenant « tous », « aucun risque », « capteur en panne » ou « température normale » doit citer la preuve correspondante ou être reformulée.
