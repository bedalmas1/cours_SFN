# Guide enseignant — Séquence 3

> Conducteur opérationnel : faire formuler une décision, exiger une preuve retrouvable, puis seulement exécuter. Chaque activité se clôt par action, confiance, preuve, incertitude et limite.

## Finalité

S03 établit le pont entre l’observation MQTT de S02 et les contrôles qualité de S04. Les étudiants apprennent qu’une table « propre » est une projection utile, non une nouvelle vérité. Ils doivent pouvoir revenir à l’octet reçu, décrire la transformation et borner ce que l’auditabilité permet de conclure.

**À la fin, ils doivent décider si un indicateur peut être justifié a posteriori à partir des artefacts conservés, avec quel niveau de confiance et quelles réserves.**

Décision de référence : l’indicateur à 35,4 °C est reproductible depuis une ligne identifiée du brut ; la chaîne brut/table est auditée avec confiance élevée. Maintenir l’inspection comme action réversible peut être défendu, mais l’exactitude physique, l’authenticité et l’exhaustivité restent non démontrées ; confiance moyenne au mieux dans la décision opérationnelle.

## Objectifs évaluables

### Conceptuels

- distinguer donnée brute, payload, enveloppe, donnée structurée, provenance et auditabilité ;
- expliquer la différence entre temps déclaré de mesure et temps observé de réception ;
- expliquer ce qu’une empreinte contrôle et ce qu’elle ne contrôle pas.

### Pratiques

- parser 15 enveloppes JSON en rejetant les erreurs explicites ;
- produire une table sous schéma commenté ;
- retrouver et vérifier une ligne brute depuis une ligne structurée ;
- signaler des candidats doublons sans suppression automatique.

### Décisionnels

- justifier les champs dont la suppression fragiliserait une contestation ;
- qualifier séparément confiance technique et confiance opérationnelle ;
- recommander une politique de conservation proportionnée au besoin d’audit.

## Conducteur — 240 minutes

| Temps | Activité | Objectif | Modalité | Trace |
|---|---|---|---|---|
| 0:00–0:15 | décision contestée | révéler les besoins de preuve | vote individuel puis binôme | choix, confiance, manque |
| 0:15–0:30 | brut vs structuré | séparer source et projection | exemple annoté | carte de transformation |
| 0:30–0:45 | provenance/auditabilité | relier preuve et confiance | questions guidées | prouve/ne prouve pas |
| 0:45–1:25 | TP 1 parser | produire sans correction silencieuse | binômes | CSV, erreur expliquée |
| 1:25–1:55 | TP 2 schéma | justifier les champs | matrice + revue croisée | schéma commenté |
| 1:55–2:05 | pause | — | — | — |
| 2:05–2:30 | identifiants, temps, hash | borner chaque métadonnée | classement | tableau de portée |
| 2:30–3:10 | TP 3 retour au brut | rejouer la preuve | manipulation + contradiction | deux liens vérifiés |
| 3:10–3:35 | incident doublon | distinguer ressemblance et identité | enquête | verdict et règle |
| 3:35–3:45 | débat conservation | arbitrer audit/coût/risque | débat mouvant | politique conditionnelle |
| 3:45–3:55 | brief final | décider sous limites | rédaction + oral | 150 mots |
| 3:55–4:00 | exit ticket | transfert individuel | sans écran | trois phrases |

## Préparation

Exécuter `instructions_avant_seance.md`. Référence :

```bash
source .venv/bin/activate
export PYTHONPATH=src
python3 -m pytest -q
python3 tests/validate_s03_artifacts.py
```

Garder `corrige.md` et l’incident cachés. Le broker est facultatif ; l’échantillon local est la source pédagogique stable.

## 1. Accroche — 15 min

Afficher : « 35,4 °C dans le shelter batteries ; inspection déclenchée ». Choix A justifiée, B plausible non auditable, C maintenir par prudence, D annuler.

| Question | Direction | Réponse attendue |
|---|---|---|
| Que savez-vous ? | interdire tout fichier imaginé | valeur et action annoncées, sans chaîne de preuve |
| Que demander ? | exiger un artefact | ligne de table, règle, message brut |
| Action prudente = preuve ? | séparer risque et vérité | non ; elle peut rester rationnelle selon le coût d’erreur |
| Quelle confiance ? | séparer technique/opérationnel | faible avant source et transformation |

Débrief : une décision peut être raisonnable et insuffisamment justifiable. Il faut rendre la chaîne contestable.

## 2. Brut, structuré, provenance — 30 min

Faire annoter une enveloppe. Le brut est « au plus près de la réception », pas « sans structure ». Le CSV est une sélection sous schéma.

| Concept | Définition | Piège | Effet décisionnel |
|---|---|---|---|
| donnée brute | observation conservée | la croire vraie ou pure | permet le reparsing |
| structurée | projection sous colonnes | oublier les champs écartés | calcul facile, contestation réduite |
| provenance | origine et activités | la réduire au nom du fichier | soutient qualité et confiance |
| auditabilité | examiner et rejouer | la confondre avec exactitude | rend l’erreur détectable |
| schéma | contrat de champs/règles | le tenir pour éternel | stabilise l’interprétation |

Questions : qu’a-t-on ajouté à la réception ? Quelle information disparaît ? Un tiers peut-il reproduire ? Quelle version fut appliquée ? Sources : W3C PROV ; RFC 3339 ; RFC 8785.

## 3. TP 1 — Parser — 40 min

Faire prédire le nombre de lignes et les trois origines de champs, puis exécuter la CLI.

| Contrôle | Attendu | Surconclusion refusée |
|---|---|---|
| entrée | 15 enveloppes | lot exhaustif |
| sortie | 15 lignes, 17 colonnes | mesures physiquement exactes |
| erreur incomplète | arrêt avec champs manquants | remplacement silencieux par vide |
| ordre | `source_line` 1 à 15 | ordre temporel garanti |

Pourquoi strict ? Une ligne rejetée ne doit pas disparaître : arrêt ou quarantaine tracée. Pourquoi exclure bool de `value` ? En Python, bool est un sous-type d’int ; sinon `true` deviendrait 1.

Fin : « 15 enveloppes conformes au contrat S03-v1 ; vérité terrain non validée ». Ajouter décision provisoire, confiance, preuve, incertitude et limite.

## 4. TP 2 — Schéma — 30 min

Attribuer quatre champs à défendre par binôme puis revue croisée. Pour chaque suppression, exiger une contestation devenue impossible.

- `topic` conserve le périmètre même si `zone` existe ;
- les deux horloges séparent déclaration et observation ;
- `message_id` est déclaré, `source_line` attribué par le fichier ;
- `raw_sha256` détecte un changement avec la référence ;
- `schema_version` nomme les règles ; `unit` contextualise le nombre.

## 5. Identifiants, temps et empreintes — 25 min

Faire classer : démontré, plausible, non démontré.

- `message_id` est présent : démontré ; capteur authentique : non démontré.
- CSV et brut de référence correspondent : démontré après vérification.
- Le brut n’a jamais été altéré avant le hash : non démontré.
- `received_at` est postérieur à `measured_at` : calculable ici ; horloge capteur juste : non démontré.

Insister : hash ≠ signature, identifiant ≠ identité, horodatage ≠ horloge fiable.

## 6. TP 3 — Retour au brut — 40 min

La vérification globale réussit. Le hash manuel par `sha256sum` diffère car il inclut le saut de ligne ; valoriser l’identification de la convention. Le test `altered.jsonl` doit signaler `source_line=1`.

| Question | Réponse attendue |
|---|---|
| Que prouve l’échec ? | les octets ne correspondent plus à l’empreinte CSV |
| Lequel est vrai ? | impossible avec ce seul contrôle ; il faut une autorité/ancrage |
| Pourquoi fichier + ligne + hash ? | adresse rejouable et intégrité se complètent |
| Le CSV suffit sans brut ? | non pour reparsing, champs omis ou contestation |

## 7. Incident — 25 min

Révéler les deux messages à 3 h 10. Afficher d’abord les colonnes métier, puis toutes.

Attendu : mêmes site, zone, capteur, temps mesuré, valeur, unité, séquence ; différences de topic, réception, retained, message_id, source_line et hash. Verdict : candidats doublons métier, non identiques.

Refuser la suppression sur la seule égalité valeur/temps. Une règle acceptable nomme clé, fenêtre, autorité, sort de la ligne écartée, risque de faux positif et possibilité de rejouer.

## 8. Débat et décision — 20 min

Conservation : reparsing, nouveau schéma, preuve, investigation. Suppression : minimisation, confidentialité, coût, surface d’attaque. Synthèse : rétention bornée, accès, empreinte/ancrage, journal des transformations et destruction autorisée.

Le brief contient action, périmètre, confiance, deux preuves retrouvables, deux incertitudes, limite et vérification. Une réponse alternative est recevable si coût d’erreur et réversibilité sont explicites.

## 9. Exit ticket et critères

Réponse type : « Je peux justifier la correspondance ligne/brut grâce à source_line et raw_sha256. Je ne peux pas affirmer que le capteur disait vrai. Je conserve brut, code/version et journal selon une politique autorisée couvrant l’audit. »

Observer : vocabulaire borné ; fichier/champ cités ; deux confiances séparées ; aucune suppression silencieuse ; décision réversible.

## Dépannage

| Symptôme | Contrôle | Repli |
|---|---|---|
| import impossible | `pwd`, `export PYTHONPATH=src` | CLI depuis la racine |
| CSV absent | chemins, droits, entrée | CSV enseignant consigné |
| hash différent partout | fichier ou convention newline | relancer la CLI |
| notebook bloqué | kernel/environnement | poursuivre en CLI |

## Références

- W3C, *PROV Overview* et *PROV Data Model*, 2013.
- IETF, RFC 3339, *Date and Time on the Internet: Timestamps*, 2002.
- IETF, RFC 8785, *JSON Canonicalization Scheme*, 2020.
- Python Software Foundation, documentation `json`, version 3 courante.
