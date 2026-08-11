# Échantillons

Emplacement réservé aux petits jeux de données versionnés utilisés dans les exercices.

`batch001_messages.jsonl` contient 15 enveloppes MQTT reproductibles couvrant cinq zones. Une zone possède des mesures volontairement anciennes pour l’incident pédagogique de la séquence 1.

`batch001_traceability_incident.jsonl` contient deux messages aux champs métier semblables mais dont identifiant, topic, réception et empreinte diffèrent.

`batch002_quality_messages.jsonl` contient 24 messages sur cinq zones autour d'une alerte température, avec cinq erreurs injectées (champ manquant, unité incohérente, valeur hors plage, incohérence temporelle, doublon exact) et un silence réel de vingt minutes sur `battery-shelter-01` juste avant la valeur haute.
