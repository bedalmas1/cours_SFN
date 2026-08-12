# Corrigé et débrief — Séquence 7 (enseignant)

## Résultat de référence

Le broker ouvert (`mosquitto.conf`, port 1883, `allow_anonymous true`) accepte toute publication anonyme sans notification particulière. Le broker protégé (`mosquitto_protected.conf`, port 1884, `allow_anonymous false`, `password_file`, `acl_file`) refuse explicitement toute connexion anonyme ou tout mot de passe incorrect (`Connection Refused: not authorised`). En revanche, un compte authentifié qui dépasse son ACL (`superviseur` tentant de publier, alors que son rôle n'autorise que la lecture sur `airbase/#`) voit son message silencieusement écarté par le broker : la commande se termine sans erreur, mais aucun abonné autorisé ne reçoit jamais ce message. De même, `capteur-lora` (autorisé en écriture seule) qui tente de s'abonner reste connecté sans jamais recevoir aucun message, sans erreur non plus.

Sur `data/samples/batch004_suspect_scenario.jsonl` (`chain_trust.py`), le diagnostic relève, sans aucun nouveau calcul : 1 doublon exact (`comms-shelter-01-0004` retransmis avec le même identifiant), 1 candidat de rejeu (`comms-shelter-01-0000` à 09:40, 29,3\,°C, republiée sous `comms-shelter-01-replay-x` à 10:10 avec un nouvel identifiant), 1 incohérence temporelle (`comms-shelter-01-badclock`, horodatage de mesure 10:20 postérieur à la réception 10:05), et un silence non expliqué de 15 minutes sur `comms-shelter-01` entre 09:45 et 10:00. La mesure du candidat de rejeu franchit intégralement les contrôles de qualité de la séquence 4 : aucun champ manquant, unité correcte, valeur dans la plage physique, horodatage de mesure antérieur à la réception — seul le recoupement de son identité métier (zone, capteur, horodatage, valeur) avec un autre message révèle le lien.

La matrice des risques classe « suspicion data/cyber » en tête (probabilité forte, impact élevé), devant « problème réseau » (forte, moyen), « panne capteur » (moyenne, moyen) et « incident réel » (faible, élevé — impact potentiellement élevé mais aucun signal ne le rend probable ici, puisqu'aucune valeur ne franchit de seuil).

Conclusion recevable : **ne pas agir directement sur ce lot ; isoler `comms-shelter-01`, vérifier l'identité et la source des messages suspects avant toute décision opérationnelle. Une authentification et une ACL protègent contre la connexion anonyme et le dépassement de périmètre, mais ni l'une ni l'autre ne détecte un rejeu par un compte pourtant autorisé, ni ne remplace les contrôles qualité de la séquence 4 -- ce sont trois vérifications distinctes et complémentaires.**

## Débriefs

- **Vote initial :** accepter tout choix honnêtement justifié à partir du seul constat ; faire vérifier explicitement que les valeurs elles-mêmes ne sont pas en cause.
- **Concepts du matin :** intégrité, authentification, ACL, injection et rejeu sont cinq notions distinctes ; l'authentification répond à « qui es-tu ? », l'ACL à « que peux-tu faire ? », ni l'une ni l'autre à « ce contenu est-il nouveau ? ».
- **Démonstration broker ouvert/protégé :** insister sur l'asymétrie observée : refus de connexion explicite, rejet ACL au niveau message silencieux. C'est le point le plus souvent mal compris : beaucoup d'étudiants supposent par défaut qu'un rejet de permission produit toujours une erreur visible.
- **Exercice vulnérabilités :** l'absence de TLS et la possibilité d'un rejeu par un compte autorisé restent hors du périmètre de ce laboratoire, même avec authentification et ACL actives.
- **Concepts de l'après-midi :** un contrôle qualité ligne à ligne (séquence 4) et un contrôle de confiance dans la chaîne (séquence 7) ne se recouvrent pas ; le candidat de rejeu de ce lot le démontre concrètement.
- **Analyse du lot suspect :** faire vérifier chaque contrôle de la séquence 4 un par un sur la ligne du candidat de rejeu, pour ancrer qu'aucun n'aurait pu le détecter seul.
- **Matrice des risques :** refuser toute hiérarchisation qui traiterait les quatre hypothèses comme mutuellement exclusives ; plusieurs peuvent coexister et orienter des vérifications différentes.
- **Exit ticket :** distinguer nettement ce qu'une chaîne qualité valide de ce qu'une chaîne de confiance valide.

Sorties déterministes : `1 doublon(s) exact(s)`, `1 candidat(s) de rejeu`, `1 incohérence(s) temporelle(s)`, `silence non expliqué maximal 15 min`, `suspicion data/cyber: probabilité forte, impact élevé`.
