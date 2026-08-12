# Guide étudiant — Séquence 5

## Mission

Une phrase circule : « la température moyenne de la base est normale. » Vous devez déterminer si cette moyenne suffit à décider de maintenir l'activité, ou si elle cache un risque localisé. L'après-midi, vous interrogerez un score automatique fourni par le système, sans en lire la logique, avant de découvrir qu'une zone nouvelle le met en défaut.

**À la fin, vous devez décider quel indicateur, ou quel processus de décision, mérite réellement votre confiance.**

Livrables : tables d'indicateurs, zone masquée identifiée, journal des requêtes au score automatique, recommandation finale sur le processus de décision à suivre.

## Parcours

1. Voter sur la seule moyenne annoncée.
2. Calculer des indicateurs transparents et retrouver la zone que la moyenne masque.
3. Interroger un score automatique sans lire sa logique.
4. Diagnostiquer pourquoi ce score se trompe silencieusement sur un cas nouveau.
5. Décider quel processus présenter au commandant, avec quelle confiance.

À chaque étape, conservez une trace : action, confiance, preuve, incertitude, vérification.

## Parcours pédagogique — 4 h

| Temps | Étape | Trace attendue |
|---|---|---|
| 0:00–0:15 | Alerte et vote initial | choix, confiance, information manquante |
| 0:15–0:40 | Moyenne, maximum, seuil : compression | fiche concept annotée |
| 0:40–1:10 | TP 1 — indicateurs et zone masquée | tableau d'indicateurs |
| 1:10–1:30 | Débrief — que cache un indicateur ? | classement argumenté |
| 1:30–1:55 | Du calcul transparent au calcul opaque | fiche concept annotée |
| 1:55–2:05 | Pause | — |
| 2:05–2:45 | TP 2 — interroger le score | journal de requêtes |
| 2:45–3:10 | Incident — fuel-storage-01 | verdict argumenté |
| 3:10–3:40 | Procès à trois | plaidoirie et arbitrage |
| 3:40–3:55 | Restitution | note ≤150 mots |
| 3:55–4:00 | Exit ticket | trois phrases individuelles |

## Règle d'exécution

Les blocs `bash` sont des commandes à copier-coller depuis la racine du dépôt `course-iot-decision`. Les blocs `python` sont de petits contrôles à exécuter dans un notebook ou un fichier temporaire. Après chaque commande, vérifiez l'absence d'erreur et notez le résultat obtenu.

**Règle impérative de la séance : n'ouvrez `src/iot_decision/risk_score.py` sous aucun prétexte avant 2:45.** L'intérêt de l'exercice de l'après-midi dépend entièrement de ne pas connaître sa logique à l'avance.

## Préparer l'environnement

```bash
python3 -m pip install -r sessions/s05_indicators_decision_traps/requirements.txt
export PYTHONPATH=src
python3 -m pytest -q
```

Cette séquence ne nécessite pas Docker ni de broker MQTT : elle travaille sur des fichiers déjà produits par la séquence 1.

## Vote initial

Sans consulter aucun fichier, choisissez une seule réponse à partir de la seule phrase d'accroche :

- **A.** La moyenne suffit, maintenir l'activité.
- **B.** Il faut d'abord décomposer par zone avant de décider.
- **C.** Maintenir par prudence en attendant une décomposition.
- **D.** Suspendre par prudence en attendant une décomposition.

Notez une confiance de 0 à 100 %, votre raison principale et l'information qui vous manque le plus.

## TP 1 — Indicateurs et zone masquée — 30 min

```bash
export PYTHONPATH=src
python3 -m iot_decision.indicators_cli data/processed/batch001_measurements.csv
```

Contrôle Python optionnel, pour vérifier un calcul à la main :

```python
from iot_decision.indicators import load_measurements, global_mean, zone_maxima

rows = load_measurements("data/processed/batch001_measurements.csv")
print("moyenne globale :", global_mean(rows))
print("maxima par zone :", zone_maxima(rows))
```

Relevez la moyenne globale, le maximum de chaque zone, et identifiez la ou les zones que le contrôle qualifie de « masquées par la moyenne ». Vérifiez par un calcul manuel sur une zone que le résultat affiché est bien reproductible à la main.

Questions à répondre :

1. La moyenne globale franchit-elle le seuil pédagogique de 35 °C ?
2. Quelle zone le franchit malgré tout, et de combien ?
3. Que signifie une durée observée au-dessus du seuil égale à zéro ?
4. Un indicateur plus simple est-il nécessairement moins fiable qu'un indicateur composé ?

## Débrief — que cache toujours un indicateur ? — 20 min

Discutez en binôme : la moyenne et le maximum racontent-ils la même histoire sur ce lot ? Que faudrait-il systématiquement faire avant de se fier à un résumé global ?

## Du calcul transparent au calcul opaque — 25 min

Classez les affirmations suivantes en « vrai » ou « faux », en justifiant : un score automatique est plus objectif qu'une moyenne parce qu'il est automatique ; un modèle calibré une fois reste valable pour toujours ; on peut auditer un score aussi facilement qu'une moyenne ; le biais d'automatisation consiste à faire davantage confiance à une machine qu'à un calcul qu'on pourrait vérifier soi-même.

## TP 2 — Interroger le score sans le lire — 40 min

```bash
export PYTHONPATH=src
python3 -m iot_decision.risk_score_cli data/raw/batch001_raw.jsonl
```

Consignez, pour chaque zone : le score obtenu et la décision affichée. Comparez ce classement à celui du TP 1 : la zone la plus haute au score correspond-elle à celle identifiée ce matin ?

**N'ouvrez pas `risk_score.py`.** Notez plutôt, sans preuve, une hypothèse sur ce que le score pourrait prendre en compte.

## Incident — fuel-storage-01 — 25 min

N'exécutez cette commande qu'au signal de l'enseignant.

```bash
python3 -m iot_decision.risk_score_cli data/samples/batch003_shift_scenario.jsonl
```

Comparez le score de `fuel-storage-01` à ceux du TP 2. Puis, seulement maintenant, ouvrez `src/iot_decision/risk_score.py` et lisez sa logique.

Questions à répondre :

1. Le score de `fuel-storage-01` se distingue-t-il des zones jugées sûres ce matin ?
2. Quelle information sur le stockage de carburant le score n'a-t-il jamais reçue ?
3. Le score a-t-il un bug, ou applique-t-il correctement une règle hors de son domaine ?
4. Que devriez-vous vérifier avant de faire confiance à un score sur une zone nouvelle ou atypique ?

## Procès à trois — 30 min

Un groupe défend la moyenne globale, un deuxième défend le score automatique, un troisième arbitre. Chaque défenseur doit citer un cas où son indicateur suffit ; l'arbitre doit citer un cas, tiré de la séance, où chacun des deux a échoué. Concluez par un processus de décision recommandé, combinant plusieurs indicateurs plutôt qu'un seul.

## Restitution — 150 mots maximum

Rédigez une recommandation contenant :

- le processus de décision retenu (moyenne, maximum, score, ou combinaison) ;
- un niveau de confiance justifié, différencié selon que la zone est connue ou nouvelle ;
- deux preuves chiffrées et retrouvables (fichier et champ) ;
- deux incertitudes qui pourraient changer la décision ;
- une vérification prioritaire, terrain ou technique.

## Validation finale à exécuter

```bash
python3 tests/validate_s05_artifacts.py
```

## Canevas de recommandation

- **Décision :** quel processus de décision proposez-vous ?
- **Confiance :** très faible / faible / moyenne / élevée ; pourquoi, et pour quel périmètre de zones ?
- **Preuves :** quelles deux observations pouvez-vous retrouver et dans quel fichier ?
- **Incertitudes :** qu'est-ce qui pourrait rendre votre conclusion fausse ?
- **Vérification :** que faut-il vérifier avant une action difficilement réversible ?

## Exit ticket

1. « Un indicateur, transparent ou automatique, permet d'affirmer que… »
2. « Il ne permet pas d'affirmer que… »
3. « Avant une décision automatisée, je vérifierais… »

## Aide en cas de blocage

Avant de demander de l'aide, indiquez : l'étape, la commande ou le fichier, le message d'erreur, ce que vous avez déjà vérifié et l'effet possible sur votre décision. Ne demandez pas seulement la réponse : demandez quelle vérification réaliser ensuite.

Les solutions, valeurs de référence et observations attendues sont réservées au guide enseignant et au corrigé.
