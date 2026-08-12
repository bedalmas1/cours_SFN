# Guide étudiant — Séquence 7

## Mission

Un extrait de `comms-shelter-01` contient deux messages étranges : l'un a un horodatage de mesure postérieur à sa réception, l'autre semble revenir sur une mesure déjà vue vingt-neuf minutes plus tôt. Aucune des deux valeurs n'est physiquement anormale. Vous devrez comprendre ce qu'une authentification et une ACL protègent réellement, puis diagnostiquer ce lot sans recalculer aucun contrôle qualité.

**À la fin, vous devez décider que vaut une décision opérationnelle si l'on ne peut pas qualifier la confiance dans la chaîne de données.**

Livrables : matrice des risques data/cyber, diagnostic de confiance, recommandations de sécurisation minimale.

## Parcours

1. Voter sur la seule base du constat initial.
2. Comparer un broker ouvert et un broker protégé sur des cas concrets.
3. Identifier les vulnérabilités d'une chaîne MQTT à partir de la configuration observée.
4. Diagnostiquer un lot suspect sans aucun nouveau calcul.
5. Classer des hypothèses concurrentes et recommander.

À chaque étape, conservez une trace : action, confiance, preuve, incertitude, vérification.

## Parcours pédagogique — 4 h

| Temps | Étape | Trace attendue |
|---|---|---|
| 0:00–0:15 | Accroche et vote initial | choix, confiance, information manquante |
| 0:15–0:45 | Intégrité, authentification, ACL, injection, rejeu | fiche concept annotée |
| 0:45–1:25 | Démonstration : broker ouvert vs protégé | tableau de résultats observés |
| 1:25–1:55 | Exercice : vulnérabilités d'une chaîne MQTT | liste de vulnérabilités annotée |
| 1:55–2:05 | Pause | — |
| 2:05–2:30 | Confiance dans la source, confiance dans le traitement | fiche concept annotée |
| 2:30–3:15 | Analyse d'un lot suspect | diagnostic complet |
| 3:15–3:40 | Matrice des risques data/cyber | matrice remplie |
| 3:40–3:55 | Décision : peut-on agir sur ces données ? | recommandation argumentée |
| 3:55–4:00 | Exit ticket | trois phrases individuelles |

## Règle d'exécution

Les blocs `bash` sont des commandes à copier-coller depuis la racine du dépôt `course-iot-decision`. Après chaque commande, vérifiez l'absence d'erreur et notez le résultat obtenu.

## Préparer l'environnement

```bash
python3 -m pip install -r sessions/s07_security_trust_robustness/requirements.txt
export PYTHONPATH=src
docker compose -f docker/docker-compose.yml up -d --wait mosquitto mosquitto-protected
python3 -m pytest -q
```

Cette séquence démarre deux brokers Mosquitto (`docker/docker-compose.yml`) : un ouvert (port 1883, déjà utilisé en séquence 1-2) et un protégé (port 1884, nouveau). Les identifiants du broker protégé sont documentés dans `docker/mosquitto/README.md`.

## Vote initial

Sur la seule base du constat (deux messages incohérents, valeurs normales), choisissez :

- **A.** traiter le lot normalement, rien ne semble alarmant en valeur ;
- **B.** isoler le lot avant toute analyse plus poussée ;
- **C.** traiter les zones non concernées, isoler `comms-shelter-01` ;
- **D.** demander une vérification terrain avant tout traitement.

Notez une confiance de 0 à 100 %, ce qui pourrait ne pas être fiable dans un message MQTT, et ce que la seule valeur mesurée ne peut jamais garantir.

## Démonstration — broker ouvert vs broker protégé — 40 min

```bash
mosquitto_pub -h 127.0.0.1 -p 1883 -t airbase/test -m hello
mosquitto_pub -h 127.0.0.1 -p 1884 -t airbase/test -m hello
mosquitto_pub -h 127.0.0.1 -p 1884 -u capteur-lora -P s07-capteur-demo -t airbase/test -m hello
mosquitto_pub -h 127.0.0.1 -p 1884 -u superviseur -P s07-superviseur-demo -t airbase/test -m hello
```

Questions à répondre :

1. La deuxième commande échoue-t-elle silencieusement ou avec un message explicite ?
2. Les troisième et quatrième commandes se terminent-elles toutes deux sans erreur visible ?
3. Comment vérifieriez-vous, sans lire le code source du broker, si le message de la quatrième commande a réellement été délivré ?

## Exercice — identifier les vulnérabilités d'une chaîne MQTT — 30 min

À partir de `docker/mosquitto/mosquitto.conf`, `mosquitto_protected.conf` et `acl.conf`, listez pour chaque vulnérabilité si elle est couverte, partiellement couverte, ou non couverte dans ce laboratoire :

1. connexion anonyme non autorisée ;
2. lecture ou écriture hors du périmètre d'un compte ;
3. absence de chiffrement entre le client et le broker ;
4. rejeu d'un message par un compte pourtant autorisé à publier.

## Confiance dans la source, confiance dans le traitement — 25 min

Classez les affirmations suivantes en « vrai » ou « faux », en justifiant : une source authentifiée est nécessairement une source de confiance ; un contrôle qualité qui valide champs, unité et plage détecte automatiquement un rejeu ; deux confiances distinctes (source, traitement) peuvent avoir des niveaux différents sur le même message.

## Analyse d'un lot suspect — 45 min

```bash
export PYTHONPATH=src
python3 -m iot_decision.chain_trust_cli data/samples/batch004_suspect_scenario.jsonl
```

Contrôle Python optionnel :

```python
from iot_decision.chain_trust import collect_signals, rank_hypotheses, recommend
from iot_decision.quality import flatten, load_raw

rows = [flatten(e) for e in load_raw("data/samples/batch004_suspect_scenario.jsonl")]
for r in rows: r["value"] = float(r["value"])
signals = collect_signals(rows)
print(signals)
for h in rank_hypotheses(signals):
    print(h)
```

Relevez le nombre de doublons exacts, de candidats de rejeu, d'incohérences temporelles et la durée du silence non expliqué. Pour chaque signal, retrouvez la ou les lignes brutes concernées dans le fichier JSONL. Vérifiez que la mesure du candidat de rejeu passait bien tous les contrôles de qualité de la séquence 4.

Questions à répondre :

1. Quelle mesure porte le candidat de rejeu, et sous quels deux identifiants apparaît-elle ?
2. Cette mesure aurait-elle été rejetée par `quality.classify` ? Pourquoi ?
3. Un seul de ces quatre signaux, pris isolément, aurait-il suffi à alerter ?

## Matrice des risques data/cyber — 25 min

Remplissez une matrice à quatre hypothèses (incident réel, panne capteur, problème réseau, suspicion data/cyber), chacune avec une probabilité et un impact (faible/moyen(ne)/forte/élevé), justifiés par un signal précis du diagnostic.

## Décision — peut-on agir sur ces données ? — 15 min

Rédigez une recommandation contenant :

- la ou les hypothèses retenues, avec probabilité et impact ;
- un niveau de confiance dans la chaîne, distinct de la confiance dans les valeurs mesurées ;
- deux preuves chiffrées et retrouvables, avec leur fichier source ;
- une vérification prioritaire avant toute décision opérationnelle.

## Validation finale à exécuter

```bash
python3 tests/validate_s07_artifacts.py
docker compose -f docker/docker-compose.yml down
```

## Canevas de recommandation

- **Hypothèses retenues :** lesquelles, avec quelle probabilité et quel impact ?
- **Confiance dans la chaîne :** distincte de la confiance dans les valeurs, pourquoi ?
- **Preuves :** quelles deux observations pouvez-vous retrouver et dans quel fichier ?
- **Vérification :** que faut-il vérifier avant une action difficilement réversible ?

## Exit ticket

1. « Un message peut être valide au sens de la séquence 4 et pourtant… »
2. « L'authentification protège contre… ; l'ACL protège en plus contre… »
3. « Avant d'agir sur un lot dont la chaîne n'est pas qualifiée, je vérifierais… »

## Aide en cas de blocage

Avant de demander de l'aide, indiquez : l'étape, la commande ou le fichier, le message d'erreur, ce que vous avez déjà vérifié et l'effet possible sur votre décision. Ne demandez pas seulement la réponse : demandez quelle vérification réaliser ensuite.

Les solutions, valeurs de référence et observations attendues sont réservées au guide enseignant et au corrigé.
