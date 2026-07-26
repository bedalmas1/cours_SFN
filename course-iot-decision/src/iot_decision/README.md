# Paquet `iot_decision`

Modules prévus : générateur MQTT, extracteur, transformations, contrôles qualité et indicateurs.

Séquence 1: `baseline.py` porte les transformations et la recommandation déterministe; `baseline_cli.py` expose le parcours hors broker; `mqtt_tools.py` précharge et extrait Mosquitto; `visualize_baseline.py` produit le graphique décisionnel.

Séquence 2 : `source_inventory.py` et sa CLI comparent l'observé à l'attendu.

Séquence 3 : `traceability.py` parse strictement le JSONL, conserve adresse et empreinte de chaque ligne, vérifie le retour à la source et signale les candidats doublons sans suppression automatique.
