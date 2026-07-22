# Guide enseignant — Séquence 2

## Intention et compétence décisionnelle

La séquence 1 montrait qu’une pipeline produit une preuve limitée. La séquence 2 revient à la source : avant parsing et nettoyage, il faut établir ce que l’on a réellement observé et par rapport à quel attendu. La compétence principale est de **borner une décision par la couverture démontrée**, sans confondre réponse du broker, présence d’un retained, fonctionnement du capteur et complétude métier.

**Question directrice : à la fin, les étudiants doivent être capables de décider si l’état observé du broker couvre suffisamment les zones critiques pour soutenir une analyse, avec confiance et limites explicites.**

Pièges : broker accessible = source fiable ; retained = récent ; silence = état normal ou panne certaine ; filtre = topic ; quatre messages = lot complet ; 80 % = suffisant indépendamment de la criticité ; référentiel supposé parfait.

## Objectifs évaluables

Conceptuels : expliquer publisher/broker/subscriber ; distinguer topic, filtre, payload et retained ; définir lot et complétude relativement à un attendu. Pratiques : explorer une branche ; inventorier les métadonnées ; comparer observé/attendu ; détecter une absence. Décisionnels : borner le périmètre ; qualifier la confiance ; proposer une vérification discriminante et une action réversible.

## Correspondance activités / TP

| Activité | Repère | Fonction |
|---|---|---|
| A | Vote initial | révéler les critères implicites de fiabilité |
| B–C | Apports + TP 1 | modèle MQTT et observation contrôlée |
| D | TP 2 | inventaire reproductible |
| E | Transition | construire le dénominateur de complétude |
| F–G | TP 3 | comparer puis injecter l’absence |
| H | TP 4 | brief, contradiction et vote final |
| I | Exit ticket | fixer portée, non-conclusion et vérification |

## Déroulé exact — 240 min

| Temps | Activité | Objectif | Modalité | Trace |
|---|---|---|---|---|
| 0:00–0:15 | A — situation + vote | révéler les hypothèses | individuel/binôme | choix, confiance, manque |
| 0:15–0:35 | B — architecture MQTT | attribuer les rôles | apport dialogué | schéma annoté |
| 0:35–0:45 | topic vs filtre | éviter l’absence fabriquée | prédiction | filtres testés |
| 0:45–1:05 | retained et limites | séparer disponibilité/fraîcheur | exemple guidé | vrai/faux justifié |
| 1:05–1:25 | C / TP 1 — exploration | observer sans surconclure | binômes | observe/conclus |
| 1:25–1:55 | D / TP 2 — inventaire | décrire le broker | manipulation | CSV + matrice zones |
| 1:55–2:05 | pause | — | — | — |
| 2:05–2:30 | E — lot/attendu/métadonnées | définir complétude | cartes + débat | définition bornée |
| 2:30–3:00 | F / TP 3 — comparaison | construire attendu/observé | binômes | matrice + taux |
| 3:00–3:15 | revue croisée | tester filtre et preuve | pairs | objection écrite |
| 3:15–3:40 | G — incident optronique | raisonner sur le silence | injection | hypothèses/vérifications |
| 3:40–3:52 | H / TP 4 — brief | recommander sans généraliser | rôles data/décideur | note ≤120 mots |
| 3:52–3:55 | vote final | mesurer la révision | individuel | choix + confiance |
| 3:55–4:00 | I — exit ticket | stabiliser le réflexe | individuel | trois phrases |

## Conduite détaillée

### A — Situation et vote

**Préparer :** cartes A–D et fiche action/confiance/preuve/manque. **Conduire :** lire la situation sans afficher les fichiers ; vote silencieux puis échange. **Relancer :** « quelle propriété du broker soutient votre choix ? » et « quel coût aurait une zone oubliée ? ». **Débloquer :** proposer le canevas sans révéler cinq topics attendus. **Débriefer :** distinguer disponibilité technique et suffisance opérationnelle.

### B — Modèle MQTT

**Préparer :** schéma publisher → broker → subscriber. **Conduire :** attribuer à chaque binôme un composant et lui faire nommer entrée, sortie, connaissance et ignorance. **Relancer :** « qui connaît la liste des capteurs attendus ? ». **Débloquer :** donner les étiquettes, pas les définitions. **Débriefer :** MQTT transporte et distribue ; le contrat métier vient d’ailleurs.

### C / TP 1 — Explorer

**Préparer :** broker seedé ou JSONL ; masquer le référentiel. **Conduire :** faire prédire le résultat de `airbase/batch002/#`, puis extraire. Exiger le filtre dans le journal. **Relancer :** « ceci est-il dans le topic, l’enveloppe ou le payload ? ». **Blocage technique :** vérifier `PYTHONPATH`, Docker, port, topic, puis passer au JSONL après deux essais. **Débriefer :** un filtre définit le champ de vision.

### D / TP 2 — Inventorier

**Préparer :** matrice vierge. **Conduire :** une ligne par topic ; contrôler unicité, zone, capteur, deux horloges, retained. **Relancer :** « que perdez-vous si vous ne gardez que la zone ? ». **Débloquer :** montrer une ligne exemplaire, pas le tableau complet. **Débriefer :** l’inventaire est une preuve sur l’observé, pas sur l’exhaustivité.

### E — Définir lot et complétude

**Préparer :** cartes d’affirmations et référentiel encore fermé. **Conduire :** classer observable / nécessite attendu / non démontrable. Révéler ensuite le CSV attendu et son rôle. **Relancer :** « qui autorise ce référentiel et à quelle date ? ». **Débloquer :** écrire `complétude = observé ∩ attendu`, puis faire nommer le dénominateur. **Débriefer :** un taux sans périmètre masque les zones critiques.

### F / TP 3 — Comparer

**Préparer :** commande CLI testée. **Conduire :** faire produire la matrice manuellement, puis comparer au JSON. **Relancer :** « 4/5 décrit quoi exactement ? ». **Blocage :** vérifier chemins, en-têtes CSV et topic complet. **Débriefer :** valider 80 % global et 0 % optronique ; séparer exactitude du calcul et autorité de l’attendu.

### G — Incident absent

**Préparer :** garder le nom optronique jusqu’à 3:15. **Conduire :** révéler l’absence et imposer au moins trois hypothèses concurrentes. **Relancer :** « quelle observation départagerait panne et filtre erroné ? ». **Débloquer :** proposer catégories équipement / publication / transport / extraction / référentiel. **Débriefer :** le silence n’indique pas sa cause et n’est jamais une mesure normale.

### H / TP 4 — Brief et contradiction

**Préparer :** canevas décision-confiance-preuves-incertitudes-vérification. **Conduire :** rédaction silencieuse, interrogation par le décideur, inversion des rôles, vote final. **Relancer :** « votre phrase vaut-elle pour quatre zones ou cinq ? ». **Débloquer :** amorce « nous pouvons décrire…, mais pas conclure… ». **Débriefer :** accepter analyse partielle + vérification ciblée ; refuser généralisation à la base.

### I — Exit ticket

Faire répondre sans écran. Si « prouve » apparaît, demander le topic ou champ exact. Conserver les tickets pour ouvrir la séquence 3 sur la traçabilité.

## Résultat et décision attendus

Quatre topics retained sont observés contre cinq attendus ; l’optronique manque. Décision recommandée : poursuivre l’analyse limitée aux quatre zones, ne pas conclure pour toute la base, vérifier en priorité la chaîne ou le terrain optronique. Confiance faible pour la couverture globale. Preuves : inventaire 4/5 et topic attendu absent. Incertitudes : cause du silence et autorité/fraîcheur du référentiel.

## Sources

MQTT 5.0, OASIS Open (2019), sections topics, subscriptions et retained messages ; manuels officiels `mosquitto_sub` et `mosquitto_pub`, Eclipse Mosquitto. Les slides citent les URL et la bibliographie commune.
