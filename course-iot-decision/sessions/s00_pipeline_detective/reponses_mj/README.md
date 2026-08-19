# Fiches de réponses MJ — prêtes à imprimer et à découper

Cinq fiches PDF, chacune regroupant les réponses scriptées d'un type de requête du catalogue (`guide_etudiant.md`, section « Catalogue des requêtes » ; réponses détaillées dans `../guide_enseignant.md`, section « Fiche maître du jeu — réponses scriptées »). Chaque carte est prête à être découpée et remise telle quelle à une cellule quand elle achète la requête correspondante : le texte de chaque carte est strictement celui qui doit être lu par les cellules, sans aucune indication réservée au MJ (conditions d'achat, ordre de lecture, etc.), à l'exception des deux requêtes de synthèse où le rappel de condition d'accès reprend une règle déjà publique dans le catalogue étudiant.

| Fichier | Requêtes couvertes | Cartes |
|---|---|---|
| `dernier_rapport.pdf` | Dernier rapport d'une source (1 jeton) | 5, une par source |
| `historique_24h.pdf` | Historique des rapports des dernières 24 h (2 jetons) | 5, une par source |
| `journal_incidents.pdf` | Journal des incidents affectant une source (2 jetons) | 5, une par source |
| `verification_terrain.pdf` | Vérification terrain / reconnaissance (3 jetons + délai dé) | 5, une par source |
| `requetes_globales.pdf` | Ordre de bataille, comparaison avec une source témoin, indice de menace consolidé, journal des transmissions radio | 4 |

Non couvert par ces fiches, à garder scripté et oral :

- le refus scripté d'une requête de synthèse demandée avant condition remplie (« cette synthèse n'est communiquée qu'après vérification d'au moins deux sources individuelles distinctes ») — c'est une réponse de refus, pas une carte à distribuer ;
- le twist injecté à 1 h 35 (mise à jour de l'ordre de bataille) — annonce orale simultanée à toutes les cellules, hors catalogue de requêtes ;
- toute requête hors catalogue (« cette information n'est pas disponible dans le système actuel »).

## Utilisation en séance

1. Imprimer les cinq PDF (2 cartes par page A4), découper au ciseau le long de la ligne pointillée « ✂ couper ici ».
2. Trier les cartes par pile lors de la préparation (une pile par fichier, ou une pile par source si vous préférez chercher par source plutôt que par type de requête).
3. Pendant le round, une fois la requête payée en jetons, prendre la carte correspondante dans la pile et la remettre à la cellule — elle fait office de transmission reçue. Le journal de bord oral se dicte à partir de cette carte.
4. Pour la vérification terrain, lancer le dé et annoncer le délai *avant* de remettre la carte (le délai n'est pas indiqué dessus, il se calcule au moment de l'achat selon la table de `guide_enseignant.md`).
5. Pour les deux requêtes de synthèse (comparaison, indice de menace), vérifier la condition d'accès avant de remettre la carte ; sinon, appliquer le refus scripté oral.

## Régénérer les fiches

Le contenu source est dans `generate.py` (données + gabarit HTML/CSS). Pour régénérer après une modification :

```
python generate.py
```

puis reconvertir chaque `.html` modifié en `.pdf`, par exemple avec Edge en mode headless :

```
msedge --headless --disable-gpu --print-to-pdf=nom.pdf --print-to-pdf-no-header --no-pdf-header-footer file:///chemin/absolu/nom.html
```

Les icônes par source sont réutilisées depuis `../dossier_initial/assets/` (même pictogramme que dans la pièce 1 du dossier initial), pour rester cohérentes avec le reste du matériel imprimé.
