# Séquence 0 — Le détective de la pipeline (jeu sans écran)

Séance de 3 h (marge comprise), animée par l'enseignant en maître du jeu (MJ), sans ordinateur, sans réseau et sans dépendance à Docker ou Internet. Conçue pour être jouée même dans une salle sans aucun accès informatique, y compris en ouverture du cours avant la séquence 1.

## Un cas volontairement différent des séquences suivantes

Les séquences 1 à 8 portent sur des capteurs de température remontés par un broker MQTT. La séquence 0 change délibérément de terrain : il s'agit d'une **fusion de renseignement avant l'entrée d'une patrouille dans un secteur**, construite à partir de rapports d'observation, d'interceptions radio et de témoignages, sans capteur, sans broker, sans MQTT. L'objectif est de faire vivre les mêmes pièges de raisonnement sous une autre forme, pour que la séance ne ressemble pas à une répétition anticipée de la séquence 1 ou des incidents des séquences suivantes.

## Question directrice

**À la fin, chaque cellule doit décider si la patrouille peut entrer dans le secteur comme prévu, s'il faut renforcer la surveillance ou vérifier avant, la dérouter par précaution, ou déclarer le renseignement insuffisant — en nommant explicitement les problèmes qui limitent sa confiance dans les sources reçues.**

## Principe du jeu

Après un premier choix décidé à l'aveugle, chaque cellule reçoit un **dossier initial** papier : un mélange de pièces utiles, de pièces sans rapport et de pièces ambiguës à trier collectivement en 20 minutes, avant même d'interroger le MJ — c'est ce tri, et le plan d'achat de requêtes qu'il produit, qui constitue le cœur de la séance. Le maître du jeu détient ensuite une fiche scriptée qui fixe une fois pour toutes ce que révèle chaque type de requête (dernier rapport, historique, journal d'incidents, vérification terrain...) pour chacune des cinq sources du scénario. Chaque cellule dépense un budget de jetons pour interroger le MJ, tient un journal de bord, puis ne peut ouvrir son enveloppe de décision qu'après avoir nommé et justifié au moins quatre problèmes distincts rencontrés dans ses preuves. Une mise à jour scriptée de l'ordre de bataille est injectée à mi-séance pour toutes les cellules.

## Livrables et démarrage rapide

Aucune commande, aucun fichier de données à exécuter : le matériel est entièrement imprimé. Livrables attendus par cellule : une fiche de tri du dossier initial et un plan d'achat, un journal de bord oral enregistré, une enveloppe de décision ouverte et complétée, un brief oral de restitution.

- `guide_enseignant.md` : mode d'emploi complet du MJ — scénario, fiche des réponses scriptées, classification de référence du dossier initial, minutage, débrief.
- `discours_ouverture_mj.md` : texte scripté à lire à voix haute par le MJ pour ouvrir la séance, avant le choix à l'aveugle.
- `reponses_mj/` : fiches PDF prêtes à imprimer et à découper, une carte par réponse scriptée du catalogue de requêtes, à remettre directement à une cellule au lieu de lire la réponse à voix haute — voir son `README.md`.
- `guide_etudiant.md` : mission, dossier initial à trier, catalogue des requêtes, journal de bord et enveloppe de décision distribués aux cellules.
- `dossier_initial/` : fichiers prêts à imprimer du dossier initial (un fichier par pièce, texte ou image selon le cas) — voir son `README.md`.
- `corrige.md` : résultat de référence condensé, pour préparation rapide ou relecture après séance.
- `debrief_synthese.md` : support de débrief détaillé — analyse pièce par pièce du dossier initial et correspondance complète avec les sujets des séquences 1 à 8, pour approfondir l'étape 9 de `guide_enseignant.md` si le temps le permet.
- `evaluation.md` : grille de notation.
- `instructions_avant_seance.md` : matériel à imprimer et préparer avant la séance.
