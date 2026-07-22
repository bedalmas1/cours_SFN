# Guide de démarrage — Séquence 2

Ce guide est destiné à **tous les étudiants**. Exécutez-le sur votre machine Linux au début de la séquence 2. Il réutilise l’environnement Python et Docker préparé pendant la séquence 1.

Toutes les commandes sont à lancer depuis la racine du dépôt `course-iot-decision` dans un terminal Bash.

## 1. Retrouver le dépôt et actualiser l’environnement

```bash
cd /chemin/vers/course-iot-decision
pwd
test -f README.md && test -d sessions/s02_mqtt_broker_data_source && echo "Dépôt trouvé"
```

Remplacez le chemin d’exemple par le chemin réel sur votre machine. La dernière commande doit afficher `Dépôt trouvé`.

Activez ensuite l’environnement créé en séquence 1 :

```bash
source .venv/bin/activate
export PYTHONPATH=src
python3 --version
which python3
```

Le chemin retourné par `which python3` doit se terminer par `.venv/bin/python3`.

Si `.venv` n’existe pas, créez-le avant de continuer :

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
```

## 2. Installer les dépendances de la séquence 2

```bash
python3 -m pip install -r sessions/s02_mqtt_broker_data_source/requirements.txt
```

Vérifiez ensuite le code et les ressources :

```bash
python3 -m pytest -q
```

Résultat attendu : les tests se terminent sans échec. Le validateur complet reste volontairement réservé à la fin, car son exécution révélerait une partie du diagnostic à construire pendant la séance.

## 3. Vérifier Docker et démarrer MQTT

```bash
docker --version
docker compose version
docker compose -f docker/docker-compose.yml up -d --wait
docker compose -f docker/docker-compose.yml ps
```

Le service Mosquitto doit être indiqué comme démarré ou sain. Le broker est anonyme mais limité à votre machine sur `127.0.0.1` : ne modifiez pas cette exposition.

## 4. Charger les messages de la séquence 2

```bash
python3 -m iot_decision.mqtt_tools seed data/samples/batch002_retained_messages.jsonl
```

Extrayez uniquement la branche demandée vers un fichier temporaire :

```bash
rm -f /tmp/s02_student_check.jsonl
python3 -m iot_decision.mqtt_tools extract /tmp/s02_student_check.jsonl --topic 'airbase/batch002/#'
wc -l /tmp/s02_student_check.jsonl
head -n 1 /tmp/s02_student_check.jsonl
```

Les guillemets autour du filtre MQTT empêchent Bash d’interpréter le caractère `#`.

Résultat attendu :

- `wc -l` affiche `4` ;
- la première ligne contient une enveloppe JSON avec le topic, l’instant de réception, l’indicateur `retained` et le payload.

Quatre messages observés ne prouvent pas que quatre capteurs fonctionnent ni que la source est complète.

## 5. Vérifier les fichiers de travail

```bash
test -w data/raw && echo "data/raw accessible"
test -w data/processed && echo "data/processed accessible"
test -f data/samples/batch002_expected_sensors.csv && echo "Référentiel trouvé"
test -f notebooks/s02_mqtt_source_inventory.ipynb && echo "Notebook trouvé"
test -f sessions/s02_mqtt_broker_data_source/guide_etudiant.md && echo "Guide trouvé"
```

Les cinq confirmations doivent s’afficher. N’ouvrez le référentiel attendu que lorsque le guide étudiant vous le demande.

Pour chaque extraction, conservez dans votre journal :

- le filtre MQTT exact ;
- l’heure et la durée de l’observation ;
- le nombre de messages et de topics observés ;
- la provenance du fichier ;
- les limites de ce que vous pouvez conclure.

## 6. Plan de secours sans broker

Si Docker ou MQTT reste indisponible, produisez l’inventaire depuis l’échantillon fourni :

```bash
python3 -m iot_decision.source_inventory_cli \
  data/samples/batch002_retained_messages.jsonl \
  data/samples/batch002_expected_sensors.csv \
  data/processed/batch002_inventory.csv \
  data/processed/batch002_completeness.json
python3 -m json.tool data/processed/batch002_completeness.json
```

Notez explicitement dans votre journal : `source = échantillon local fourni`. Un accès impossible au broker est une limite de preuve, pas une preuve d’absence de messages.

## 7. Dépannage

### `.venv/bin/activate` est introuvable

Créez l’environnement et installez les dépendances :

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r sessions/s02_mqtt_broker_data_source/requirements.txt
export PYTHONPATH=src
```

### `No module named iot_decision`

```bash
pwd
source .venv/bin/activate
export PYTHONPATH=src
```

Vérifiez que `pwd` correspond bien à la racine de `course-iot-decision`.

### Docker affiche `permission denied`

Essayez les mêmes commandes avec `sudo`. Pour une correction permanente, suivez la procédure de votre distribution pour autoriser votre compte à utiliser Docker.

### Le broker ne démarre pas

```bash
sudo systemctl start docker
docker compose -f docker/docker-compose.yml ps
docker compose -f docker/docker-compose.yml logs mosquitto
```

Si le problème persiste, utilisez le plan de secours et prévenez l’enseignant.

### Le fichier extrait contient zéro ligne

```bash
docker compose -f docker/docker-compose.yml ps
python3 -m iot_decision.mqtt_tools seed data/samples/batch002_retained_messages.jsonl
python3 -m iot_decision.mqtt_tools extract /tmp/s02_student_check.jsonl --topic 'airbase/batch002/#'
wc -l /tmp/s02_student_check.jsonl
```

Vérifiez le filtre exact avant de conclure à une absence.

## 8. Validation finale

Vous êtes prêt pour la séquence 2 si toutes les affirmations suivantes sont vraies :

- [ ] je suis à la racine de `course-iot-decision` ;
- [ ] `.venv` est activé et `PYTHONPATH=src` est défini ;
- [ ] les dépendances de la séquence 2 sont installées ;
- [ ] les tests Python réussissent ;
- [ ] le broker local fonctionne, ou j’ai identifié que j’utiliserai le plan de secours ;
- [ ] mon extraction de contrôle contient quatre lignes, ou l’échantillon local est disponible ;
- [ ] je peux ouvrir le guide étudiant et le notebook ;
- [ ] je sais que le filtre et la provenance doivent accompagner toute conclusion.

À la fin de la séquence, arrêtez le broker local :

```bash
docker compose -f docker/docker-compose.yml down
```
