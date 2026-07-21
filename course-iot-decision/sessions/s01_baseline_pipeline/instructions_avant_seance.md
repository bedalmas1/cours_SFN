# Instructions avant séance — Séquence 1

Ce document est destiné à l’enseignant. Prévoir environ 30 à 45 minutes de préparation la veille, puis un contrôle rapide juste avant l’arrivée des étudiants.

## 1. Installer les dépendances

Depuis la racine `course-iot-decision`, utiliser Python 3.10 ou plus récent :

```powershell
python -m pip install -r sessions/s01_baseline_pipeline/requirements.txt
$env:PYTHONPATH="src"
```

Vérifier ensuite :

```powershell
python -m pytest -q
python tests/validate_s01_artifacts.py
```

Le second script reconstruit les fichiers dans un répertoire temporaire, vérifie les 15 messages, les cinq zones, la figure et l’exécution du notebook.

## 2. Préparer le broker MQTT

Docker Desktop doit être démarré. Depuis la racine :

```powershell
docker compose -f docker/docker-compose.yml up -d --wait
python -m iot_decision.mqtt_tools seed data/samples/batch001_messages.jsonl
```

Tester une extraction dans un fichier temporaire :

```powershell
python -m iot_decision.mqtt_tools extract C:\tmp\s01_teacher_check.jsonl
```

Le fichier doit contenir 15 enveloppes JSONL et cinq zones. Ne pas exposer ce broker sur un réseau partagé : la configuration est anonyme et strictement locale (`127.0.0.1`).

Après le test, arrêter l’environnement si aucun autre groupe ne l’utilise :

```powershell
docker compose -f docker/docker-compose.yml down
```

## 3. Vérifier les supports

Ouvrir les fichiers suivants avant la séance :

- `guide_enseignant.md` pour le déroulé et les réponses attendues ;
- `guide_etudiant.md` et `exercices.md` pour préparer la distribution ;
- `corrige.md` pour le débrief ;
- `evaluation.md` et `prompts/s01_assessment_prompt.md` pour la correction ;
- `slides/s01_baseline_pipeline.tex` pour les transitions et le timing.

Ne pas distribuer `corrige.md` ni le prompt d’évaluation IA.

## 4. Préparer le matériel de séance

- projeter le PDF compilé des slides ;
- préparer quatre cartes de vote : A. maintenir l’activité, B. déclencher une inspection terrain, C. mettre temporairement la zone en sécurité, D. données insuffisantes pour décider ;
- prévoir une feuille par binôme pour le journal de décision ;
- distribuer le guide étudiant et les exercices ;
- vérifier que chaque binôme peut ouvrir un terminal et écrire dans un espace de travail ;
- garder le mode hors broker disponible si Docker ou le réseau échoue.

## 5. Vérifications pédagogiques à faire avant l’accueil

1. Rappeler que 35 °C est un seuil pédagogique, pas une consigne opérationnelle.
2. Préparer la question « quelle horloge utilisez-vous ? » pour l’incident de fraîcheur.
3. Ne pas révéler que `optronics-shelter-01` est ancien avant l’extraction.
4. Prévoir des groupes capables de jouer l’avocat contradicteur.
5. Relever séparément le choix et la confiance au vote initial et au vote final.
6. Décider à l’avance où seront déposés les livrables étudiants; ne pas écraser les fichiers de référence du dépôt.

## 6. Plan B immédiat

Si le broker, Docker ou `paho-mqtt` est indisponible, exécuter :

```powershell
python -m iot_decision.baseline_cli extract-sample data/samples/batch001_messages.jsonl data/raw/batch001_raw.jsonl
python -m iot_decision.baseline_cli transform data/raw/batch001_raw.jsonl data/processed/batch001_measurements.csv
python -m iot_decision.visualize_baseline data/processed/batch001_measurements.csv sessions/s01_baseline_pipeline/slides/figures/batch001_max_by_zone.png
```

La discussion reste identique : disponibilité d’un message, fraîcheur, traçabilité, seuil, confiance et vérification terrain.

## 7. Contrôle juste avant la séance

Le démarrage est prêt si :

- le test automatisé affiche `5 passed` ;
- le validateur affiche `S01 valide` ;
- le broker, s’il est utilisé, renvoie 15 messages ;
- le PDF s’ouvre et comporte 47 pages ;
- la figure montre le maximum par zone et le seuil ;
- les cartes de vote, les supports étudiants et le chronomètre sont disponibles.

En cas de doute, privilégier le mode échantillon et conserver le problème technique comme exemple de discussion sur la confiance dans la pipeline.
