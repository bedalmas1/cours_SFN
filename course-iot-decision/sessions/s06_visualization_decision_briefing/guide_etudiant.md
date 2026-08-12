# Guide étudiant — Séquence 6

## Mission

Une cellule de supervision transmet un premier graphique de `battery-shelter-01` pour justifier une inspection immédiate. Un second graphique, construit à partir des mêmes trois mesures, donne une impression très différente. Vous devrez d'abord comprendre pourquoi, puis produire vous-même une visualisation honnête et une note de briefing pour une zone de votre choix, et enfin défendre votre recommandation à l'oral face à des questions contradictoires.

**À la fin, vous devez savoir présenter une alerte sans donner une impression excessive de certitude.**

Livrables : 2 à 3 graphiques (mise en forme trompeuse et honnête d'une même zone) ; mini-rapport ≤ 100 mots ; niveau de confiance explicite ; recommandation.

## Parcours

1. Voter sur la seule base du premier graphique.
2. Comparer les deux mises en forme du même incident et nommer ce qui change.
3. Produire la courbe temporelle d'une autre zone, sous ses deux formes.
4. Rédiger une note de briefing complète (message principal, limite, confiance, vérification).
5. Défendre un brief oral de 3 minutes face à des questions contradictoires.

À chaque étape, conservez une trace : action, confiance, preuve, incertitude, vérification.

## Parcours pédagogique — 4 h

| Temps | Étape | Trace attendue |
|---|---|---|
| 0:00–0:15 | Accroche et vote initial | choix, confiance, information manquante |
| 0:15–0:45 | Échelle, seuil, annotation, incertitude visuelle | fiche concept annotée |
| 0:45–1:30 | TP 1 — courbe temporelle par zone | deux images comparées |
| 1:30–1:55 | Débrief — graphique utile ou trompeur ? | classement argumenté |
| 1:55–2:05 | Pause | — |
| 2:05–2:30 | Briefing décisionnel, message principal, limites | fiche concept annotée |
| 2:30–3:15 | TP 2 — 2 visualisations et une mini-note | mini-rapport ≤ 100 mots |
| 3:15–3:40 | Brief oral | prestation orale |
| 3:40–3:55 | Questions contradictoires du commandement | réponses argumentées |
| 3:55–4:00 | Exit ticket | trois phrases individuelles |

## Règle d'exécution

Les blocs `bash` sont des commandes à copier-coller depuis la racine du dépôt `course-iot-decision`. Après chaque commande, vérifiez l'absence d'erreur et notez le résultat obtenu.

## Préparer l'environnement

```bash
python3 -m pip install -r sessions/s06_visualization_decision_briefing/requirements.txt
export PYTHONPATH=src
python3 -m pytest -q
```

Cette séquence ne nécessite pas Docker ni de broker MQTT : elle travaille sur `data/processed/batch002_measurements_clean.csv`, déjà produit par la séquence 4.

## Vote initial

Sur la seule base du premier graphique projeté (`battery-shelter-01`), choisissez :

- **A.** déclencher l'inspection immédiatement ;
- **B.** demander d'abord le graphique complet et le contexte ;
- **C.** maintenir l'activité par prudence en attendant plus d'information ;
- **D.** suspendre l'activité par prudence en attendant plus d'information.

Notez une confiance de 0 à 100 %, ce que l'axe vertical vous laisse croire, et l'information que ce graphique ne montre pas.

## TP 1 — Courbe temporelle par zone — 45 min

```bash
export PYTHONPATH=src
python3 -m iot_decision.visualize_briefing data/processed/batch002_measurements_clean.csv <votre_zone> /tmp/mislead.png /tmp/honest.png
```

Zones disponibles : `battery-shelter-01`, `comms-shelter-01`, `it-room-01`, `maintenance-zone-01`, `optronics-shelter-01`. Choisissez-en une autre que `battery-shelter-01`.

Questions à répondre :

1. Les bornes de l'axe vertical sont-elles les mêmes sur les deux images ?
2. Un silence de données apparaît-il sur votre zone ? Est-il annoté sur l'une, l'autre, ou aucune des deux images ?
3. Le seuil pédagogique apparaît-il sur l'une, l'autre, ou aucune des deux images ?
4. L'écart d'impression entre vos deux images est-il plus fort ou plus faible que celui observé sur `battery-shelter-01` ? Pourquoi ?

## Débrief — graphique utile ou trompeur ? — 25 min

Discutez en binôme : un graphique à échelle tronquée est-il toujours trompeur ? Que faudrait-il exiger systématiquement avant de projeter un graphique devant un décideur pressé ?

## Briefing décisionnel, message principal, limites — 25 min

Classez les affirmations suivantes en « vrai » ou « faux », en justifiant : un graphique sans annotation est plus objectif qu'un graphique annoté ; le niveau de confiance d'un briefing peut être choisi librement par celui qui le rédige ; une limite vague vaut mieux qu'aucune limite ; un message principal doit toujours contenir un chiffre retrouvable.

## TP 2 — 2 visualisations et une mini-note — 45 min

```bash
export PYTHONPATH=src
python3 -m iot_decision.briefing_cli data/processed/batch002_measurements_clean.csv <votre_zone>
```

Contrôle Python optionnel :

```python
from iot_decision.briefing import summarize_zone, briefing_note
from iot_decision.indicators import load_measurements

rows = load_measurements("data/processed/batch002_measurements_clean.csv")
summary = summarize_zone(rows, "<votre_zone>")
print(briefing_note(summary))
```

Construisez un mini-rapport de moins de 100 mots contenant :

- l'image retenue (trompeuse ou honnête) et pourquoi ;
- le message principal, avec chiffre ;
- la limite ;
- le niveau de confiance ;
- la vérification recommandée.

Conservez l'image écartée : elle servira au brief oral pour illustrer ce qu'un choix de mise en forme différent aurait produit.

## Jeu de rôle et brief oral — 25 min

Trois rôles, permutés à chaque passage : **cellule data** (présente le mini-rapport en 3 minutes), **décideur pressé** (interrompt si le message principal n'est pas clair en moins de 30 secondes), **red team** (cherche l'angle mort : échelle, silence non mentionné, seuil confondu avec une norme officielle).

Structure du brief, dans l'ordre : la situation en une phrase ; le graphique retenu, projeté ; le message principal et la limite, dits explicitement ; le niveau de confiance et la recommandation ; une vérification prioritaire.

## Questions contradictoires du commandement — 15 min

Préparez une réponse courte à chacune :

1. « Ce graphique est-il pire ou meilleur que celui du groupe précédent, et pourquoi précisément ? »
2. « Si je vous impose l'autre mise en forme de la même zone, votre recommandation change-t-elle ? »
3. « Qu'est-ce qui, dans ce graphique, n'est pas une mesure mais un choix de votre part ? »
4. « Combien de temps faudrait-il pour vérifier ce que votre limite signale ? »

## Validation finale à exécuter

```bash
python3 tests/validate_s06_artifacts.py
```

## Canevas de mini-rapport

- **Image retenue :** trompeuse ou honnête, et pourquoi ?
- **Message principal :** quelle observation chiffrée et retrouvable ?
- **Limite :** qu'est-ce que cette observation ne permet pas d'affirmer ?
- **Confiance :** faible / moyenne / élevée, et pourquoi ?
- **Vérification :** que faut-il vérifier avant une action difficilement réversible ?

## Exit ticket

1. « Un graphique honnête, sur ces données, doit toujours montrer… »
2. « Un graphique peut rester exact et pourtant donner une impression fausse quand… »
3. « Avant de projeter un graphique devant un décideur, je vérifierais… »

## Aide en cas de blocage

Avant de demander de l'aide, indiquez : l'étape, la commande ou le fichier, le message d'erreur, ce que vous avez déjà vérifié et l'effet possible sur votre décision. Ne demandez pas seulement la réponse : demandez quelle vérification réaliser ensuite.

Les solutions, valeurs de référence et observations attendues sont réservées au guide enseignant et au corrigé.
