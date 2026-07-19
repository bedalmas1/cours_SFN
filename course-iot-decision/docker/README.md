# Environnement Docker

Ce dossier accueillera Docker Compose et la configuration Mosquitto nécessaires au broker MQTT local.

`docker-compose.yml` lance Mosquitto 2.0.22 en local uniquement. Depuis la racine: `docker compose -f docker/docker-compose.yml up -d --wait`. Précharger ensuite avec `python -m iot_decision.mqtt_tools seed data/samples/batch001_messages.jsonl`.
