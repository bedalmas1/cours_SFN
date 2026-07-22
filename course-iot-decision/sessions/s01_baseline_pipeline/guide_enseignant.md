# Guide enseignant — Séquence 1

## Intention

Cette séquence installe le réflexe des huit séances: une pipeline transforme la portée des preuves qui soutiennent une action. La baseline est volontairement minimale pour rendre visibles, ensuite, les besoins de qualité, traçabilité, sécurité et robustesse.

**Question directrice:** à la fin, les étudiants doivent décider si les mesures justifient de maintenir l’activité de maintenance drone prévue à 14 h 00, de déclencher une inspection terrain, de mettre temporairement la zone en sécurité ou de déclarer les données insuffisantes, avec confiance et limites explicites.

Compétence principale: décider sous incertitude sans confondre disponibilité d’un résultat, vérité de la situation et suffisance de la preuve. Pièges: retained = récent; CSV propre = vrai; 35 °C = norme; maximum = risque certain; pourcentage de confiance sans justification.

## Objectifs évaluables

Conceptuels: identifier message/donnée/indicateur/décision; expliquer topic, retained et les deux horloges. Pratiques: extraire sans altérer; transformer en CSV traçable; visualiser une question. Décisionnels: comparer au seuil sans fausse autorité; recommander, qualifier la confiance et prioriser une vérification.

## Préparation

1. Installer Python 3.10+, dépendances et éventuellement Docker.
2. Exécuter tests, validateur et notebook.
3. Mode MQTT: `docker compose -f docker/docker-compose.yml up -d`, puis:

   ```powershell
   $env:PYTHONPATH=src
   python -m iot_decision.mqtt_tools seed data/samples/batch001_messages.jsonl
   ```

4. Tester une extraction temporaire; garder `extract-sample` en repli.
5. Compiler/projeter les slides; préparer quatre cartes de vote A à D.

Le broker anonyme est strictement local (`127.0.0.1`). Ne jamais déployer cette configuration sur un VPS ou réseau partagé.

## Repères du parcours étudiant

Le `guide_etudiant.md` est désormais le support étudiant unique : il contient les activités conceptuelles, les manipulations et les productions. Annoncer le nom de l'étape puis le TP associé lorsqu'il existe.

| Activité | Repère étudiant | Fonction pédagogique |
|---|---|---|
| A | Vote initial | décision avant les données |
| B–C | Apports guidés + début du TP 1 | comprendre la chaîne et observer le broker |
| D | TP 1 | extraire et préserver le JSONL |
| E | Transition TP 1 → TP 2 | distinguer brut, transformé et exploitable |
| F | TP 2 | produire et contrôler le CSV |
| G | TP 3 | produire et critiquer le graphique |
| H | TP 4 + vote final | recommander, contester et revoter |
| I | Exit ticket | expliciter portée et limites |

Les étapes B, C et E apportent les concepts et les contrôles nécessaires aux productions techniques.

## Déroulé exact (240 min)

| Temps | Activité | Objectif | Modalité | Trace |
|---|---|---|---|---|
| 0:00–0:15 | A — situation + vote initial | révéler hypothèses/coût d’erreur | individuel/binôme | vote, confiance, manque |
| 0:15–0:30 | B — message → décision | distinguer niveaux | apport dialogué | chaîne annotée |
| 0:30–0:45 | confiance/incertitude | éviter certitude artificielle | classement | mini-décision |
| 0:45–1:00 | C — broker/topics | comprendre source/retained | démo prédictive | observations/conclusions |
| 1:00–1:10 | C — enveloppe | distinguer les horloges | lecture collective | deux temps repérés |
| 1:10–1:40 | D / TP 1 — extraction | préserver le brut | binômes | JSONL + contrôles |
| 1:40–1:55 | incident/restitution | repérer fraîcheur | intergroupes | décision révisée |
| 1:55–2:05 | pause | — | — | — |
| 2:05–2:20 | E — brut/transformé/exploitable | lisibilité ≠ vérité | cartes | actions classées |
| 2:20–2:30 | exemple guidé | préparer parsing | live coding | mapping source→colonne |
| 2:30–3:00 | F / TP 2 — transformation | CSV traçable | binômes | CSV + contrôles |
| 3:00–3:10 | contrôle croisé | tester portée | pairs | limite notée |
| 3:10–3:25 | G / TP 3 — graphique | répondre à une question | exécution | PNG |
| 3:25–3:35 | débat “que masque le max?” | contester | avocat contradicteur | limite |
| 3:35–3:47 | H / TP 4 — recommandation | preuve → action | groupes | note ≤120 mots |
| 3:47–3:55 | H — vote final | mesurer effet pipeline | comparaison | vote/confiance |
| 3:55–4:00 | I — exit ticket | fixer réflexe | individuel | exit ticket |

## Facilitation

Ne révéler la fraîcheur optronique qu’après extraction. Demander toujours: action? confiance? preuve? incertitude? vérification? Accepter “maintenir sous réserve” ou “inspection” si le risque est explicite. Une bonne pipeline peut diminuer la confiance. Rappeler que 35 °C est un paramètre pédagogique à valider par l’autorité compétente.

## Fiches de conduite des exercices

Les étapes ci-dessous sont destinées à l’enseignant. Les résultats de référence restent dans `corrige.md`; pendant l’accompagnement, donner d’abord un indice et ne montrer une solution qu’après une tentative documentée.

### Exercice A — Situation initiale et vote

**Préparer.** Distribuer une fiche par étudiant avec quatre cases: action, confiance, raison, information manquante. Ne montrer ni fichier ni graphique.

**Situation à lire.** « Une activité de maintenance drone est prévue à 14 h 00 sur une base aérienne projetée. Un message de supervision signale une possible hausse de température dans le stockage batteries. Des données sont disponibles dans le broker MQTT, mais aucune analyse consolidée n’a encore été réalisée. Une vérification terrain prendrait 30 minutes. Reporter l’activité a un coût opérationnel. »

**Conduire.** Lire la situation une fois. Faire écrire en silence, puis demander aux binômes de comparer leurs hypothèses sans chercher à se convaincre. Faire voter entre **A. maintenir l’activité; B. déclencher une inspection terrain; C. mettre temporairement la zone en sécurité; D. données insuffisantes pour décider.** Noter séparément le choix et la confiance.

**Relancer.** Si un étudiant demande “quelle est la bonne réponse?”, demander: “Quelle preuve avez-vous réellement?” puis “Quel serait le coût d’une erreur?”. Faire distinguer le coût certain de l’inspection (30 minutes), le coût annoncé mais non chiffré du report et les conséquences possibles d’une hausse non confirmée. Si tous choisissent maintenir, demander quelle information pourrait rendre ce choix dangereux.

**Débloquer.** Proposer uniquement le canevas: action → preuve disponible → information manquante → niveau de confiance. Ne pas fournir de température.

**Débriefer.** Faire verbaliser la différence entre intuition, hypothèse et preuve. Conserver les fiches pour le vote final.

### Exercice B — Lire la chaîne

**Préparer.** Projeter la chaîne capteur → message → donnée → indicateur → décision. Former des binômes et attribuer une flèche à chacun.

**Conduire.** Demander à chaque binôme d’identifier ce qui entre, ce qui sort et une erreur plausible à sa flèche. Faire placer les erreurs sur le schéma, sans corriger immédiatement.

**Relancer.** Questions successives: “Qu’est-ce qui est effectivement transmis?”, “Quel contexte manque?”, “Qui choisit le résumé?”, “Quelle action serait affectée?”.

**Débloquer.** Donner les quatre étiquettes (message, donnée, indicateur, décision), jamais leur définition complète; demander aux étudiants de les illustrer avec la température.

**Débriefer.** Insister sur le fait qu’une erreur technique peut devenir une erreur d’action seulement après transformation ou interprétation.

### Exercice C — Observer le broker

**Préparer.** Lancer le broker et le seed, ou ouvrir `data/samples/batch001_messages.jsonl` en repli. Montrer d’abord un seul message et masquer les autres.

**Conduire.** Demander aux étudiants de repérer topic, payload, zone, unité, `measured_at`, `received_at` et retained. Leur faire remplir deux colonnes: “j’observe” / “je peux conclure”.

**Relancer.** Faire pointer chaque réponse vers un champ précis. Demander: “Cette date vient-elle du capteur ou de notre extraction?”

**Débloquer.** Si le broker est inaccessible, ne pas perdre l’objectif: fournir l’échantillon et demander de distinguer enveloppe et payload.

**Débriefer.** Faire reformuler retained avec les mots des étudiants; corriger seulement la confusion entre stockage par le broker et fraîcheur de la mesure.

### Exercice D — Extraire sans altérer

**Préparer.** Vérifier `docker compose ... up -d --wait`, le port local et le seed. Faire créer un nom de fichier propre à chaque groupe si les productions sont collectées.

**Conduire.** Exécuter la commande une fois en projetant le terminal, puis laisser les binômes la rejouer. Demander un contrôle après chaque étape: fichier créé, nombre de lignes, première ligne, dernière ligne, zones.

**Relancer.** Demander “quelle métadonnée vous permettrait de retrouver la source?” et “que se passerait-il si vous éditez cette ligne?”.

**Débloquer techniquement.** Vérifier dans l’ordre: répertoire courant; `$env:PYTHONPATH=src`; conteneur sain; dépendance `paho-mqtt`; topic et port. Passer à `extract-sample` après deux essais infructueux et noter l’incident dans le journal.

**Débloquer pédagogiquement.** Ne pas corriger une ligne avec eux; leur demander de comparer une ligne au fichier échantillon et de décrire la différence.

**Débriefer.** Vérifier que le brut est conservé et que la décision porte sur la suffisance de la preuve, pas sur la réussite de la commande.

### Exercice E — Brut, transformé, exploitable et incident

**Préparer.** Préparer six cartes d’action: conserver, renommer, convertir, agréger, supprimer, tracer. Garder le mot “ancien” hors de la consigne initiale.

**Conduire.** Faire classer individuellement, puis demander un classement argumenté par binôme. Injecter ensuite la question de fraîcheur et laisser les étudiants réviser leur confiance sans supprimer les données.

**Relancer.** Pour chaque action: “La preuve originale est-elle encore disponible?”, “Cette opération est-elle réversible?”, “Quel effet sur la décision?”.

**Débloquer.** Donner un seul exemple neutre (changer l’ordre des lignes) et demander aux étudiants de généraliser eux-mêmes.

**Débriefer.** Faire nommer la zone dont l’horizon temporel fragilise la comparaison, puis distinguer donnée inutilisable et donnée utilisable avec réserve.

### Exercice F — Transformer

**Préparer.** Ouvrir un JSONL et le CSV attendu côte à côte. Ne pas afficher le CSV complet avant la tentative.

**Conduire.** Faire lancer `baseline_cli transform`, puis distribuer une grille de contrôle: colonnes, lignes, zones, unités, horodatages, identifiant source. Chaque binôme doit retrouver une ligne CSV dans le JSONL.

**Relancer.** Demander quelle colonne vient du payload et laquelle vient de l’enveloppe. Faire expliquer pourquoi `topic` et `received_at` doivent rester présents.

**Débloquer techniquement.** Vérifier chemin d’entrée, JSONL non vide, indentation non requise et `PYTHONPATH`. En cas d’erreur de champ manquant, demander de localiser le champ dans l’enveloppe avant toute modification.

**Débloquer conceptuellement.** Si “propre” est confondu avec “vrai”, demander quelle calibration ou quelle mesure terrain le script n’a jamais réalisée.

**Débriefer.** Faire comparer deux lignes par des groupes différents et faire expliciter la traçabilité minimale.

### Exercice G — Visualiser

**Préparer.** Vérifier que matplotlib fonctionne et que le dossier `slides/figures/` est accessible. Montrer la question avant de montrer le graphique.

**Conduire.** Faire générer le PNG, puis demander une revue en quatre points: question, unité, seuil, lisibilité. Chaque binôme écrit une observation et une interprétation sur deux lignes séparées.

**Relancer.** “Que voit-on réellement?”, “Que suppose-t-on?”, “Quelle information disparaît quand on garde seulement le maximum?”

**Débloquer techniquement.** Vérifier l’installation de matplotlib, le chemin du CSV et les droits d’écriture. Utiliser la figure de référence si nécessaire, mais maintenir l’analyse critique.

**Débloquer conceptuellement.** Demander de proposer un indicateur alternatif (médiane, durée, fraîcheur) sans exiger son implémentation.

**Débriefer.** Faire valider le titre comme une question décisionnelle et rappeler que le seuil est pédagogique.

### Exercice H — Décider, voter, contester

**Préparer.** Distribuer le canevas décision–confiance–preuves–incertitudes–vérification. Désigner dans chaque groupe un rédacteur, un vérificateur des sources et un contradicteur.

**Conduire.** Accorder une première rédaction silencieuse, puis demander au contradicteur de chercher l’hypothèse qui pourrait renverser la recommandation. Faire voter à nouveau individuellement entre les mêmes options A à D avant la restitution.

**Relancer.** Exiger une citation de ligne, de zone ou de valeur pour chaque preuve. Demander si la vérification proposée est faisable avant l’action.

**Débloquer.** Si le groupe reste catégorique, proposer la phrase “sous réserve de...” et demander de compléter la réserve avec une donnée concrète.

**Débriefer.** Comparer vote initial et final; valoriser une baisse de confiance lorsqu’elle résulte d’une meilleure compréhension des limites.

### Exercice I — Exit ticket

**Conduire.** Faire répondre individuellement, sans écran ni discussion, aux trois phrases. Ramasser les réponses avant la synthèse orale.

**Relancer.** Si une phrase contient “prouve”, demander “quelle observation exacte?”; si elle contient “tout”, demander “quel périmètre?”.

**Débriefer.** Utiliser deux réponses anonymisées: une conclusion correctement limitée et une surconclusion à reformuler collectivement.

## Fiches concepts décisionnelles

| Concept | Définition/exemple | Piège → conséquence | Question / source |
|---|---|---|---|
| Message brut | enveloppe conservée avant transformation | brut = vrai → authenticité supposée | Qu’observe-t-on? RFC 8259 |
| Topic MQTT | nom hiérarchique de routage | nom pris comme preuve → mauvaise zone | Topic/payload concordent? OASIS MQTT 5 |
| Retained | dernier message stocké par topic | reçu = récent → action sur ancien | Quelle horloge? OASIS MQTT §3.3.1.3 |
| Horodatage | instant avec fuseau | horloge naïve/fausse → chronologie fragile | mesure ou réception? ISO 8601 |
| Brut/transformé/exploitable | preuve/structure/adéquation | propre = correct → excès de confiance | Quelle opération change la preuve? NISTIR 8286A |
| Seuil | convention déclenchant l’attention | seuil pédagogique = norme | Qui fixe 35 °C? JCGM 100 |
| Agrégation | résumé, ici maximum | masque fraîcheur/durée → alerte mal calibrée | Que perd le max? pandas docs |
| Visualisation | représentation pour une question | décor = démonstration | Quelle action éclaire-t-elle? matplotlib docs |
| Traçabilité | lien résultat-source | correction silencieuse → indéfendable | Retrouve-t-on le message? NISTIR 8286A |
| Confiance | adéquation argumentée des preuves | précision artificielle | Quelle preuve change le niveau? JCGM 100 |
| Incertitude | limite pertinente pour l’action | liste sans effet | Laquelle renverse la décision? JCGM 100 |

## Plans de repli

Broker indisponible: `extract-sample`. Matplotlib absent: critiquer la figure préparée. Retard de 15 min: fournir le JSONL mais garder transformation/débat/vote. Avance: graphique de fraîcheur par zone.

Références complètes dans `latex/common/references.bib` et la dernière slide.
