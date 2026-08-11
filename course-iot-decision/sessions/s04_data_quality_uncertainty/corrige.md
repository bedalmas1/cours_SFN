# Corrigé et débrief — Séquence 4 (enseignant)

## Résultat de référence

La fenêtre d'alerte contient 24 messages bruts sur cinq zones. Le contrôle qualité isole exactement cinq lignes rejetées, une par type d'erreur : un champ `unit` manquant (`it-room-01`), une unité incohérente `fahrenheit` (`maintenance-zone-01`), une valeur hors plage physique de 214,7 (`optronics-shelter-01`), une incohérence temporelle où `measured_at` est postérieur à `received_at` (`it-room-01`), et un doublon exact issu d'une retransmission (`comms-shelter-01`). Il reste **19 lignes propres**.

La détection de silence signale quatre zones, mais un seul silence est réel : celui de **`battery-shelter-01`**, 20 minutes sans aucun message reçu (09 h 45 à 10 h 05), immédiatement suivi d'une valeur de **36,2 °C** qui franchit le seuil pédagogique de 35 °C. Les trois autres silences (`it-room-01`, `maintenance-zone-01`, `optronics-shelter-01`) sont entièrement expliqués par une ligne rejetée tombant dans la même fenêtre : ce ne sont pas des messages perdus, mais des messages reçus puis écartés par le contrôle qualité.

Conclusion recevable : **ne pas conclure seul sur la hausse de `battery-shelter-01` ; vérifier le terrain avant toute action, car les vingt minutes qui précèdent la valeur haute sont muettes, sans qu'aucune ligne rejetée ne l'explique. Confiance faible.** Preuves : le silence non expliqué et la valeur de 36,2 °C. Limites : bornes de plausibilité pédagogiques, calibration non démontrée, fenêtre restreinte à 24 messages. D'autres formulations sont acceptables si elles distinguent explicitement silence réel et silence expliqué par un rejet.

## Débriefs

- **Vote initial :** accepter toute option honnêtement justifiée à partir de la seule alerte annoncée ; aucune analyse n'a encore été faite. La confiance mesure l'adéquation des preuves, pas l'aisance du décideur.
- **Concepts qualité :** validité = la ligne respecte les règles déclarées (champ, unité, plage) ; complétude = tout ce qui était attendu est arrivé ; cohérence = les champs d'une même ligne ne se contredisent pas entre eux ; précision = la mesure reflète l'ordre de grandeur physique réel, ce qu'aucun contrôle automatique ne peut ici démontrer.
- **TP champs manquants/unités/valeurs impossibles :** les quatre erreurs de contenu ne se ressemblent pas et n'ont pas la même gravité pour la décision ; un champ manquant est un signal de collecte, une unité incohérente est un signal de configuration, une valeur hors plage est un signal de capteur ou de transmission.
- **Rejet, correction, quarantaine :** ce cours rejette et documente, il ne corrige jamais silencieusement une valeur. Corriger reviendrait à remplacer une observation par une hypothèse non vérifiée.
- **Incident silence :** faire vérifier systématiquement si une ligne rejetée tombe dans la fenêtre du silence avant de parler de « donnée manquante ». Diminuer la confiance et proposer une vérification terrain, ne jamais interpoler une valeur.
- **Décision :** exiger action, confiance, deux preuves, deux incertitudes et vérification. Valoriser une action réversible et proportionnée au silence réel identifié.
- **Exit ticket :** affirmer seulement ce que 19 lignes propres et un silence documenté permettent ; ne pas conclure à une panne, à une valeur normale, ni à la sécurité de la zone.

Sorties déterministes : `19 lignes propres`, `5 lignes rejetées`, silence réel unique sur `battery-shelter-01`, confiance faible.
