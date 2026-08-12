# Corrigé et débrief — Séquence 5 (enseignant)

## Résultat de référence

La moyenne globale du lot `batch001` est **30,75 °C**, bien en dessous du seuil pédagogique de 35 °C : elle paraît normale. Elle masque pourtant `battery-shelter-01`, dont le maximum observé est **35,4 °C**, au-dessus du seuil. La durée observée au-dessus du seuil est de 0 minute : une seule mesure franchit le seuil, ce qui interdit de parler d'un dépassement prolongé.

Le score automatique (`risk_score.py`, révélé au débrief) applique une règle fixe calibrée une fois sur les cinq zones d'origine : 70 % du ratio maximum/35 °C, 30 % de la durée observée au-dessus de 35 °C, seuil de décision à 65/100. Sur les cinq zones connues, il retrouve correctement `battery-shelter-01` (score 71/100, inspection recommandée) et laisse les quatre autres sous le seuil de décision (56 à 64/100).

Sur `fuel-storage-01`, une zone de stockage carburant jamais vue à la calibration du score, il produit un score de **62/100 — aucune action requise** : indiscernable des zones réellement sûres. Le stockage de carburant a pourtant un seuil de sécurité opérationnel réel bien plus bas que 35 °C (vapeurs inflammables) ; à 30,9 °C et en hausse, la zone mériterait une attention que le score, calibré sur un tout autre référentiel de zones, ne peut pas produire.

Conclusion recevable : **aucun indicateur unique — ni la moyenne, ni le score automatique — ne suffit seul. La moyenne masque une zone à seuil identique ; le score masque une zone à seuil différent de celui sur lequel il a été calibré. La recommandation doit combiner le maximum par zone (transparent, audité) et une vérification humaine pour toute zone nouvelle ou atypique avant de faire confiance au score.** Confiance moyenne pour les cinq zones connues, faible pour toute zone nouvelle tant qu'elle n'a pas été explicitement intégrée au calcul.

## Débriefs

- **Vote initial :** accepter tout choix honnêtement justifié à partir de la seule phrase d'accroche.
- **Concepts du matin :** un indicateur est un choix de compression ; la moyenne, le maximum et la durée au-dessus du seuil racontent chacun une histoire différente du même lot.
- **TP indicateurs :** 30,75 °C de moyenne, `battery-shelter-01` à 35,4 °C ; faire vérifier que les étudiants recalculent la moyenne à la main sur au moins une zone pour ancrer que rien n'est caché dans le calcul lui-même.
- **Concepts de l'après-midi :** un modèle est un indicateur qu'on ne peut plus décomposer à la main ; le biais d'automatisation consiste à lui accorder plus de confiance qu'à un calcul qu'on pourrait pourtant vérifier soi-même.
- **TP score automatique :** insister sur l'interdiction de lire `risk_score.py` avant l'incident ; le score doit être utilisé, pas audité, à ce stade.
- **Incident `fuel-storage-01` :** refuser toute affirmation que le score « sait » ou « comprend » la zone. Il applique une règle fixe hors de son domaine de calibration. Faire nommer explicitement l'hypothèse cachée : le seuil de 35 °C, jamais remis en cause pour un nouveau type de zone.
- **Procès à trois :** aucune des trois parties ne doit gagner sans réserve. La moyenne masque `battery-shelter-01` ; le maximum seul ignore la fraîcheur et la durée ; le score masque `fuel-storage-01`. Le meilleur argument final combine plusieurs indicateurs et une vérification humaine pour tout cas nouveau.
- **Exit ticket :** affirmer seulement ce que le calcul démontré permet ; ne jamais conclure à la sécurité réelle d'une zone à partir d'un score non calibré pour elle.

Sorties déterministes : moyenne globale `30.75`, `battery-shelter-01: score 71/100 -> inspection recommandée`, `fuel-storage-01: score 62/100 -> aucune action requise`.
