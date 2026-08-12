# Guide de démarrage — Séquence 7

Toutes les commandes s'exécutent sous Linux dans Bash, depuis la racine du dépôt.

## Environnement et dépendances

```bash
cd /chemin/vers/course-iot-decision
source .venv/bin/activate
python3 -m pip install -r sessions/s07_security_trust_robustness/requirements.txt
export PYTHONPATH=src
python3 -m pytest -q
```

Si `.venv` existe, ne pas la recréer. `which python3` doit pointer vers `.venv/bin/python3`. Installer un client MQTT en ligne de commande (`mosquitto-clients` sur Debian/Ubuntu) pour exécuter `mosquitto_pub`/`mosquitto_sub` pendant la démonstration.

## Deux brokers requis

S7 est la première séquence depuis S2 à nécessiter Docker : elle démarre le broker ouvert existant (port 1883) **et** un nouveau broker protégé (port 1884, authentification et ACL).

```bash
docker compose -f docker/docker-compose.yml up -d --wait mosquitto mosquitto-protected
docker compose -f docker/docker-compose.yml ps
```

Attendu : les deux services affichent `healthy`. En cas d'échec du broker protégé (`exit 13` dans `docker logs iot-decision-mosquitto-protected`), vérifier que les volumes de `mosquitto_protected.conf`, `acl.conf` et `passwd` ne sont pas montés en lecture seule (`:ro`) — l'entrypoint de l'image doit pouvoir ajuster leurs permissions.

## Supports et contrôle à blanc

```bash
test -f notebooks/s07_security_trust_robustness.ipynb
test -f data/samples/batch004_suspect_scenario.jsonl
test -f docker/mosquitto/passwd
mosquitto_pub -h 127.0.0.1 -p 1883 -t airbase/test -m hello
mosquitto_pub -h 127.0.0.1 -p 1884 -t airbase/test -m hello
mosquitto_pub -h 127.0.0.1 -p 1884 -u capteur-lora -P s07-capteur-demo -t airbase/test -m hello
python3 -m iot_decision.chain_trust_cli data/samples/batch004_suspect_scenario.jsonl
python3 tests/validate_s07_artifacts.py
```

Attendu : la publication anonyme réussit sur 1883, échoue avec `not authorised` sur 1884, réussit avec les identifiants `capteur-lora` ; le diagnostic affiche `1 doublon(s) exact(s)`, `1 candidat(s) de rejeu`, `1 incohérence(s) temporelle(s)`, `silence non expliqué maximal 15 min` ; puis `S07 valide`.

## Précautions et matériel

- PDF et guide enseignant ouverts ; guide étudiant distribué sans corrigé.
- Les identifiants `capteur-lora` / `superviseur` (`docker/mosquitto/README.md`) sont pédagogiques et documentés en clair : rappeler qu'ils ne valent que pour ce laboratoire local, jamais au-delà de `127.0.0.1`.
- Préparer les quatre commandes `mosquitto_pub`/`mosquitto_sub` de la démonstration à l'avance dans un terminal visible : le contraste entre échec explicite et rejet silencieux est le point pédagogique central du matin.
- Binômes « cellule sécurité » / « décideur critique » pour le matin ; à 1:55, redistribuer les rôles pour l'analyse de l'après-midi.

## Plan de repli

- Sans Docker fonctionnel : fournir directement le tableau de résultats de la démonstration (guide enseignant, section 3) et maintenir l'exercice de vulnérabilités sur la seule lecture des fichiers de configuration.
- Sans Jupyter : utiliser la CLI ; tous les livrables restent possibles.
- Retard supérieur à 15 min : fournir directement la sortie du diagnostic et la matrice de référence, maintenir la décision finale et l'exit ticket.

## Dernière minute

- [ ] environnement activé, `PYTHONPATH=src`, tests réussis ;
- [ ] `mosquitto-clients` installé (`mosquitto_pub`/`mosquitto_sub` disponibles) ;
- [ ] les deux brokers `healthy` (`docker compose ... ps`) ;
- [ ] `batch004_suspect_scenario.jsonl` disponible ;
- [ ] notebook ou CLI prêt, PDF lisible, corrigé non distribué ;
- [ ] consigne « probabilité, impact, preuve, vérification » visible ;
- [ ] à la fin de la séance : `docker compose -f docker/docker-compose.yml down`.
