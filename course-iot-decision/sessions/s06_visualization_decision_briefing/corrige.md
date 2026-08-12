# Corrigé et débrief — Séquence 6 (enseignant)

## Résultat de référence

`battery-shelter-01` (`data/processed/batch002_measurements_clean.csv`) compte trois mesures propres : 34,1 °C à 09:40, 34,6 °C à 09:45, puis 36,2 °C à 10:05, après un silence de vingt minutes non expliqué par un rejet qualité (identique au diagnostic de la séquence 4). Aucune de ces valeurs ne change entre les deux graphiques produits par `visualize_briefing.py`.

Le premier graphique (`create_misleading_chart`) trace un axe vertical borné à 34–36,5 °C, relie les trois points par un trait continu et n'affiche ni seuil ni annotation : la hausse paraît spectaculaire et ininterrompue. Le second (`create_honest_chart`) trace un axe de 0 à 40 °C, affiche le seuil pédagogique de 35 °C, rompt le trait au niveau du silence détecté et l'annote explicitement (« vide de données (20 min) non expliqué par un rejet qualité »).

La note de briefing (`briefing.py::summarize_zone`) associe une confiance **faible** à toute zone où une mesure franchit le seuil juste après un silence non expliqué, et une confiance **moyenne** à toute zone sans franchissement de seuil (silence ou non). Sur ce lot : `battery-shelter-01` → faible (1/3 mesure ≥ 35 °C, vide de 20 min) ; `comms-shelter-01`, `it-room-01`, `maintenance-zone-01`, `optronics-shelter-01` → moyenne (aucun franchissement).

Conclusion recevable : **présenter systématiquement la version à échelle complète, seuil affiché et silences annotés, accompagnée de sa note de briefing (message principal, limite, confiance, vérification). Réserver un axe ajusté aux cas où il sert réellement la lisibilité d'une variation significative, jamais pour l'exagérer.** Confiance faible pour `battery-shelter-01` tant que le silence n'est pas expliqué ; confiance moyenne pour les quatre autres zones du lot.

## Débriefs

- **Vote initial :** accepter tout choix honnêtement justifié à partir du seul premier graphique ; faire noter explicitement ce que l'axe tronqué laissait croire.
- **Concepts du matin :** échelle, seuil, annotation et incertitude visuelle sont quatre choix de mise en forme, jamais des faits imposés par la donnée.
- **TP 1 :** faire vérifier que les valeurs affichées sur les deux images d'une même zone sont identiques ; seule la mise en forme change. L'écart d'impression est maximal sur `battery-shelter-01` (seuil franchi après un silence), minimal sur `comms-shelter-01` (aucun franchissement, aucun silence).
- **Débrief graphique utile/trompeur :** refuser l'idée qu'une échelle tronquée est intrinsèquement fausse ; le problème est de l'utiliser sans indiquer ses bornes ni le seuil pertinent devant une décision.
- **Concepts de l'après-midi :** le message principal doit contenir un chiffre retrouvable ; une limite vague (« les données ne sont pas parfaites ») n'oriente aucune vérification, contrairement à « la mesure haute suit un vide de 20 minutes ».
- **TP 2 :** le mini-rapport doit citer le graphique honnête, pas le trompeur, comme pièce jointe à la recommandation ; le trompeur reste utile en comparaison pédagogique uniquement.
- **Brief oral et questions contradictoires :** une bonne réponse nomme le levier de mise en forme précis (échelle, seuil, annotation, silence) plutôt que de défendre le graphique dans son ensemble.
- **Exit ticket :** un graphique honnête n'est pas celui qui minimise l'alerte, mais celui dont l'échelle, le seuil et les silences sont justifiés et visibles.

Sorties déterministes : `battery-shelter-01: 1/3 mesure(s) >= 35 °C, maximum 36.2 °C`, `Niveau de confiance : faible` ; `comms-shelter-01: 0/5 mesure(s) >= 35 °C, maximum 29.9 °C`, `Niveau de confiance : moyenne`.
