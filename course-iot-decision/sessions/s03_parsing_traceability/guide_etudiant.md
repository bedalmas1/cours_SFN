# Guide étudiant — Séquence 3

## Mission

Une inspection du shelter batteries a été déclenchée après un indicateur de 35,4 °C. La décision est contestée : il faut montrer quel message a alimenté la table, quelles transformations furent appliquées et quelles limites subsistent.

**À la fin, vous devez décider si l’indicateur est assez traçable pour justifier la décision a posteriori, avec quel niveau de confiance et quelles réserves.**

Livrables : `batch001_structured.csv`, schéma commenté, justification de huit champs, réponse à l’incident et brief de 150 mots.

## Déroulé

| Temps | Activité | Trace |
|---|---|---|
| 0:00–0:15 | vote sur la décision contestée | choix, confiance, preuve manquante |
| 0:15–0:45 | brut, structuré, provenance | carte brut → transformation → table |
| 0:45–1:25 | TP 1 parsing | CSV et journal d’erreurs |
| 1:25–1:55 | TP 2 schéma | schéma commenté |
| 1:55–2:05 | pause | — |
| 2:05–2:30 | identifiants, temps, hash | tableau « prouve / ne prouve pas » |
| 2:30–3:10 | TP 3 retour au brut | deux preuves rejouées |
| 3:10–3:35 | incident doublon | verdict et règle |
| 3:35–3:55 | débat et brief | décision argumentée |
| 3:55–4:00 | exit ticket | réponse individuelle |

Rôles : l’**équipe data** exécute et conserve les traces ; le **décideur critique** demande ce que chaque champ prouve et interdit les surconclusions. Inversez après la pause.

## Activité 1 — Décider avant de parser

Sans ouvrir les fichiers, choisissez : A décision justifiée ; B décision plausible mais non auditable ; C inspection à maintenir par prudence ; D décision à annuler. Notez confiance de 0 à 100 %, fait disponible, première preuve à demander et coût d’une mauvaise décision.

Séparez quatre niveaux : message reçu ; ligne structurée ; indicateur calculé ; action décidée. Tracez les liens nécessaires pour remonter de l’action au message.

## TP 1 — Parser sans perdre la source

```bash
source .venv/bin/activate
export PYTHONPATH=src
mkdir -p data/processed /tmp/s03
wc -l data/samples/batch001_messages.jsonl
head -n 1 data/samples/batch001_messages.jsonl
python3 -m iot_decision.traceability_cli parse \
  data/samples/batch001_messages.jsonl \
  data/processed/batch001_structured.csv
head -n 3 data/processed/batch001_structured.csv
tail -n +2 data/processed/batch001_structured.csv | wc -l
```

Attendu : 15 lignes. Distinguez les colonnes d’enveloppe, de payload et de pipeline. Quel champ retrouve la source ? détecte sa modification ? indique la règle de parsing ?

Testez une erreur explicite :

```bash
printf '%s\n' '{"topic":"x","received_at":"2026-10-12T10:00:00Z","retained":true,"payload":{}}' > /tmp/s03/incomplete.jsonl
python3 -m iot_decision.traceability_cli parse /tmp/s03/incomplete.jsonl /tmp/s03/incomplete.csv
```

La commande doit échouer avec les champs manquants. Expliquez pourquoi inventer une valeur vide serait dangereux. Terminez par décision provisoire, confiance, preuve, incertitude et limite.

## TP 2 — Concevoir le schéma

Ouvrez `schema_donnees.md`. Pour huit champs, ajoutez : obligatoire/facultatif ; règle de contrôle ; effet d’une absence ; responsable présumé. Classez : calcul, contexte opérationnel, retour au brut, contrôle du traitement.

Peut-on supprimer `topic` si `zone` existe ? `received_at` si `measured_at` existe ? `source_line` si `message_id` existe ? `unit` si tout semble en Celsius ? Pour chaque suppression, décrivez une contestation devenue impossible.

## Après la pause — Ce que les métadonnées prouvent

Complétez « prouve / ne prouve pas » pour `message_id`, `source_line`, `raw_sha256`, `measured_at`, `received_at`, `schema_version`. Une empreinte identique montre que les octets comparés correspondent à la référence ; elle ne prouve pas qui a créé cette référence.

## TP 3 — Relier table et brut

```bash
python3 -m iot_decision.traceability_cli verify data/samples/batch001_messages.jsonl data/processed/batch001_structured.csv
```

Attendu : `traçabilité vérifiée`. Choisissez les lignes CSV 3 et 14. Relevez `source_line`, `message_id`, `topic`, `raw_sha256`, puis retrouvez le brut :

```bash
sed -n '3p;14p' data/samples/batch001_messages.jsonl
sed -n '3p' data/samples/batch001_messages.jsonl | sha256sum
sed -n '14p' data/samples/batch001_messages.jsonl | sha256sum
```

`sha256sum` inclut le saut de ligne, tandis que le pipeline empreinte son contenu sans ce saut. Utilisez la CLI comme référence et expliquez cette convention. Pour chaque ligne : observation, preuve, conclusion autorisée, conclusion interdite, confiance et limite.

```bash
cp data/samples/batch001_messages.jsonl /tmp/s03/altered.jsonl
sed -i '1s/33.8/33.9/' /tmp/s03/altered.jsonl
python3 -m iot_decision.traceability_cli verify /tmp/s03/altered.jsonl data/processed/batch001_structured.csv
```

La vérification doit échouer pour la ligne 1. Le brut de référence reste intact.

## Incident — Deux messages semblent identiques

N’ouvrez le fichier qu’au signal de l’enseignant.

```bash
python3 -m iot_decision.traceability_cli parse data/samples/batch001_traceability_incident.jsonl /tmp/s03/incident.csv
python3 -m iot_decision.traceability_cli candidates /tmp/s03/incident.csv
column -s, -t < /tmp/s03/incident.csv
```

Comparez mesure, contexte, identifiant, topic, deux horloges, retained, ligne et empreinte. Verdict : identiques, doublons certains, candidats doublons ou événements distincts ? Proposez règle, autorité, risque de faux positif et trace à conserver.

## Débat et brief final

Groupe A défend la suppression du brut après validation ; groupe B sa conservation. Traitez coût, audit, nouveau schéma, confidentialité, intégrité, durée et accès. Formulez une politique conditionnelle.

En 150 mots : action ; périmètre ; confiance ; deux preuves avec fichier et champ ; deux incertitudes ; une limite ; une vérification. Le décideur demande : « puis-je retrouver le message ? », « le hash prouve-t-il l’auteur ? », « que savez-vous du terrain ? ».

## Validation et exit ticket

```bash
python3 tests/validate_s03_artifacts.py
```

Complétez : « Je peux justifier… parce que… » ; « Je ne peux pas affirmer… » ; « Je conserverais… pendant… sous l’autorité de… ».
