# Corrigé et débrief — Séquence 2 (enseignant)

## Résultat de référence

L’instantané contient **4 topics retained observés** pour **5 topics attendus**. Batteries, transmissions, informatique tactique et maintenance sont présentes. Le topic `airbase/batch002/optronics-shelter-01/temperature` est absent. Couverture numérique : **80 %**, mais couverture optronique : **0 %**.

Conclusion recevable : **ne pas généraliser le diagnostic thermique à toute la base ; poursuivre sur les quatre zones couvertes avec réserves et vérifier la chaîne optronique ou le terrain. Confiance faible pour une décision globale, moyenne au mieux pour décrire l’état observé des quatre topics.**

## Réponses attendues

- Broker : reçoit et distribue les publications ; il ne connaît pas spontanément la liste métier attendue.
- Topic : chaîne hiérarchique choisie par l’application ; elle fournit du contexte selon une convention documentée.
- Topic filter : expression d’abonnement ; `+` couvre un niveau et `#` une branche terminale. Un filtre trop étroit fabrique une absence apparente.
- Payload : contenu applicatif, non validé métier par le broker.
- Retained : dernier message retained stocké pour un topic et remis à un nouvel abonnement correspondant ; ni historique complet ni preuve de fraîcheur.
- Lot : périmètre pédagogique défini par instant d’extraction, filtre, site et référentiel ; MQTT ne fournit pas automatiquement cette notion métier.
- Complétude : comparaison observé/attendu. Le dénominateur, l’autorité et la date du référentiel doivent être cités.
- Absence : constat conditionnel à la connexion, au filtre, au délai et au référentiel ; elle ne révèle pas sa cause.

## Incident optronique

Hypothèses et vérifications : capteur en panne → état terrain ; publication interrompue → journaux publisher/passerelle ; filtre erroné → répéter avec `airbase/batch002/#` ; retained absent → vérifier publication/configuration ; référentiel obsolète → confirmer auprès du responsable de configuration.

Refuser : « température normale », « capteur forcément en panne », « 80 % suffit », « retained signifie récent ».

## Sorties déterministes

`4/5 topics attendus observés`, `complete=false`, confiance `faible`, topic optronique absent. Accepter d’autres décisions si leur périmètre, coût d’erreur et vérifications sont explicites.
