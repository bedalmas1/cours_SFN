# Guide étudiant — Séquence 2

## Mission et résultat attendu

Le broker MQTT répond. Vous devez déterminer si son état observé couvre les cinq zones critiques attendues avant le briefing de 10 h.

**Question directrice : avant tout nettoyage, l’état observé du broker suffit-il pour soutenir une décision couvrant toute la base ?**

À la fin, votre binôme remet quatre traces :

1. une fiche « j’observe / je peux conclure » ;
2. `data/processed/batch002_inventory.csv` ;
3. une matrice attendu/observé et un diagnostic de complétude ;
4. un brief décisionnel de 120 mots maximum.

Après chaque TP, complétez dans votre journal : **décision provisoire, confiance, preuve, incertitude, limite et prochaine vérification**.

## Rôles du binôme

- **Équipe data** : exécute les commandes, conserve les chemins et cite les traces.
- **Décideur critique** : vérifie le périmètre, interdit les surconclusions et pose les questions indiquées.

Inversez les rôles après la pause.

## 0 — Préparer le terminal

Ouvrez PowerShell à la racine du dépôt `course-iot-decision`. Vérifiez le dossier courant :

```powershell
Get-Location
Test-Path sessions/s02_mqtt_broker_data_source
Test-Path data/samples/batch002_retained_messages.jsonl
```

Les deux `Test-Path` doivent afficher `True`. Préparez Python :

```powershell
python -m pip install -r sessions/s02_mqtt_broker_data_source/requirements.txt
$env:PYTHONPATH=src
python -m pytest -q
```

Résultat attendu : les tests se terminent sans échec. En cas d’erreur, notez la commande, le message exact et le dernier contrôle réussi.

## TP 1 — Explorer les topics sans surinterpréter — 20 min

### Étape 1 — Prédire avant d’exécuter

Écrivez ce que vous pensez recevoir avec le filtre `airbase/batch002/#`. Répondez :

1. Le symbole `#` appartient-il au topic publié ou au filtre d’abonnement ?
2. Ce filtre renvoie-t-il l’historique complet ?
3. Un retained reçu maintenant a-t-il forcément été mesuré maintenant ?
4. Quelle information permettra de vérifier vos réponses ?

### Étape 2 — Extraire

Si l’enseignant a démarré le broker :

```powershell
python -m iot_decision.mqtt_tools extract data/raw/batch002_observed.jsonl --topic airbase/batch002/#
```

Sortie attendue : `4 messages extraits`. Si le broker n’est pas disponible, copiez l’échantillon sans le modifier :

```powershell
Copy-Item data/samples/batch002_retained_messages.jsonl data/raw/batch002_observed.jsonl -Force
```

### Étape 3 — Contrôler le fichier

```powershell
Test-Path data/raw/batch002_observed.jsonl
(Get-Content data/raw/batch002_observed.jsonl).Count
Get-Content data/raw/batch002_observed.jsonl -First 1
```

Attendu : `True`, puis `4`, puis une enveloppe JSON contenant `topic`, `received_at`, `retained` et `payload`.

### Étape 4 — Produire la trace

Pour chaque ligne, remplissez : topic complet ; niveaux du topic ; zone ; capteur ; `measured_at` ; `received_at` ; retained ; « j’observe » ; « je peux conclure ».

Questions à rendre :

1. Combien de topics avez-vous effectivement observés ?
2. Quel filtre exact a défini votre champ de vision ?
3. Quels champs viennent de l’enveloppe d’extraction ? Du payload ?
4. Quelle différence constatez-vous entre `measured_at` et `received_at` ?
5. Pouvez-vous déjà affirmer que le lot est complet ? Pourquoi ?

**Fin du TP 1 :** vous savez décrire exactement ce qui a été reçu sans affirmer que tout l’attendu est présent.

## TP 2 — Construire et vérifier l’inventaire — 30 min

### Étape 1 — Générer les deux artefacts

```powershell
python -m iot_decision.source_inventory_cli data/raw/batch002_observed.jsonl data/samples/batch002_expected_sensors.csv data/processed/batch002_inventory.csv data/processed/batch002_completeness.json
```

La commande annonce `4/5 topics attendus observés`. N’ouvrez pas encore le JSON de diagnostic : contrôlez d’abord l’inventaire.

### Étape 2 — Vérifier le CSV

```powershell
Test-Path data/processed/batch002_inventory.csv
Import-Csv data/processed/batch002_inventory.csv | Format-Table topic,zone,sensor,retained
(Import-Csv data/processed/batch002_inventory.csv).Count
(Import-Csv data/processed/batch002_inventory.csv | Select-Object -ExpandProperty topic | Sort-Object -Unique).Count
```

Attendu : fichier présent ; quatre lignes ; quatre topics uniques ; une zone par ligne.

### Étape 3 — Répondre à partir du CSV

1. Quelles quatre zones sont observées ?
2. Chaque ligne permet-elle de retrouver le topic source ?
3. Pourquoi conserver `message_id`, `measured_at`, `received_at` et retained ?
4. Que perdriez-vous en regroupant immédiatement toutes les lignes sous « température » ?
5. L’inventaire prouve-t-il le fonctionnement actuel des quatre capteurs ?

### Étape 4 — Mini-décision avant la pause

Rédigez cinq lignes : action provisoire ; confiance ; preuve citée ; incertitude ; vérification suivante.

**Fin du TP 2 :** `batch002_inventory.csv` comporte quatre topics uniques et votre formulation reste limitée à « quatre topics observés ».

## TP 3 — Diagnostiquer la complétude — 55 min

### Étape 1 — Examiner le référentiel attendu

```powershell
Import-Csv data/samples/batch002_expected_sensors.csv | Format-Table topic,zone,sensor,criticality
(Import-Csv data/samples/batch002_expected_sensors.csv).Count
```

Attendu : cinq topics. Avant de calculer, répondez : qui devrait autoriser ce référentiel en situation réelle ? Pour quel site, quelle mission et quelle date serait-il valide ?

### Étape 2 — Construire manuellement la matrice

Créez une ligne par topic attendu avec : zone ; criticité ; présent/absent ; preuve dans l’inventaire ; vérification si absent. Ne vous contentez pas d’un pourcentage.

### Étape 3 — Calculer puis contrôler

Calculez : `topics attendus observés / topics attendus`. Ouvrez ensuite le diagnostic automatisé :

```powershell
Get-Content data/processed/batch002_completeness.json
Get-Content data/processed/batch002_completeness.json | ConvertFrom-Json | Format-List
```

Attendu : `observed_count = 4`, `expected_count = 5`, `complete = False`, confiance faible et un topic optronique absent.

### Étape 4 — Traiter l’incident sans inventer sa cause

Pour l’absence optronique, complétez au moins quatre lignes : hypothèse ; observation compatible ; vérification discriminante ; conséquence sur la décision. Étudiez au minimum : panne équipement, non-publication, retained supprimé, filtre incorrect, extraction interrompue et référentiel obsolète.

Questions à rendre :

1. Que signifie exactement `4/5` ?
2. Pourquoi `80 %` ne signifie-t-il pas « 80 % du risque couvert » ?
3. Quelle zone a une couverture nulle ? Quelle est sa criticité ?
4. L’absence prouve-t-elle une panne ? une température normale ?
5. Quelle vérification départage le plus vite filtre incorrect et absence réelle dans le broker ?
6. Quelle autre vérification renseigne l’état physique réel ?

**Fin du TP 3 :** vous pouvez citer le topic absent, expliquer la portée de `4/5` et proposer une vérification qui distingue plusieurs causes.

## TP 4 — Rédiger et contester le brief — 15 min

### Étape 1 — Rédiger

En 120 mots maximum, incluez obligatoirement :

- action et périmètre géographique exact ;
- confiance faible, moyenne ou élevée, avec justification ;
- deux preuves retrouvables dans les fichiers ;
- deux incertitudes susceptibles de changer la décision ;
- une vérification prioritaire réalisable avant l’action.

### Étape 2 — Contradiction

Le décideur critique pose successivement :

1. « Votre recommandation vaut-elle pour quatre zones ou pour cinq ? »
2. « Dans quel fichier puis-je retrouver chacune de vos preuves ? »
3. « Quelle hypothèse pourrait renverser votre décision ? »
4. « Que proposez-vous pour l’abri optronique avant 10 h ? »
5. « Votre action est-elle réversible si le diagnostic change ? »

### Étape 3 — Réviser et voter

Corrigez le brief, puis revotez entre A couverture suffisante, B inspection ciblée, C suspendre la conclusion globale, D impossible sans inventaire. Notez le changement de choix ou de confiance.

**Fin du TP 4 :** aucune phrase ne généralise les quatre zones observées à toute la base.

## Validation finale

```powershell
python tests/validate_s02_artifacts.py
```

Attendu : `S02 valide`. Le validateur confirme le calcul et les fichiers ; il ne confirme ni l’autorité du référentiel ni votre décision.

## Exit ticket

Sans écran, complétez :

1. « Avec le filtre …, le broker permet d’affirmer que… »
2. « Ces données ne permettent pas d’affirmer que… »
3. « Pour qualifier l’absence optronique, je vérifierais d’abord… parce que… »
