# Corrigé et débrief — Séquence 1 (enseignant)

## Résultat de référence

Le jeu contient 15 messages retained, cinq zones, trois observations par zone et une seule unité. Le maximum est **35,4 °C** dans `battery-shelter-01`, au-dessus du seuil pédagogique. Les mesures de `optronics-shelter-01` ont 65 à 75 minutes à 10 h 05, contre 5 à 15 minutes ailleurs.

Recommandation recevable: **inspection ciblée du stockage batteries et vérification terrain de l’abri optronique avant maintien sans réserve; confiance faible**. Preuves: 35,4 °C et fraîcheur optronique. Limites: seuil non homologué, calibration/intégrité/exhaustivité non démontrées, mesures ponctuelles retained. D’autres formulations sont acceptables si elles explicitent l’arbitrage.

## Débriefs

- **Vote initial:** accepter toute option A à D honnêtement justifiée à partir du message de supervision, du délai d’inspection et du coût opérationnel du report. La confiance mesure l’adéquation des preuves, pas l’assurance du décideur.
- **Chaîne:** message = contenu transmis; donnée = représentation contextualisée; indicateur = synthèse construite; décision = choix d’action. Un graphique n’est pas une preuve exhaustive.
- **Broker:** retained signifie stocké puis remis au nouvel abonné, pas récent. `received_at` trace l’extraction; `measured_at` est l’événement déclaré par le capteur.
- **Extraction:** 15 enveloppes; topic, réception et retained conservés. Refuser toute correction du brut. Reproductible ne signifie ni authentique ni exhaustif.
- **Incident:** faire demander “quelle horloge utilisez-vous?”. Diminuer la confiance et vérifier, ne pas supprimer la donnée ancienne.
- **Transformation:** 15 lignes, 12 colonnes. Le CSV facilite tri/comparaison; il ne calibre rien. `message_id` + topic assurent une traçabilité minimale.
- **Graphique:** le maximum répond à l’attention immédiate, mais masque fraîcheur, durée et dispersion. Accepter un autre graphique mieux justifié.
- **Décision:** exiger action, confiance, deux preuves, deux incertitudes et vérification. Valoriser les décisions conditionnelles et réversibles.
- **Exit ticket:** affirmer seulement les maxima des messages extraits; ne pas conclure à la sécurité réelle ni au futur.

Sorties déterministes: `15 messages conservés`, `15 mesures écrites`, inspection ciblée, confiance faible.
