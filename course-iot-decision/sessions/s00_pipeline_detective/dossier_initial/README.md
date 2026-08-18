# Dossier initial — matériel à imprimer (Séquence 0)

Ce dossier contient les fichiers prêts à imprimer du dossier initial décrit dans la section « Dossier initial d'investigation » de `../guide_etudiant.md`. Contenu strictement destiné aux cellules : aucune réponse scriptée ni classification n'y figure. La classification de référence (utile / bruit / ambiguë), y compris la note sur le bruit interne aux pièces 2 et 4, reste dans `../guide_enseignant.md`, section « Dossier initial et fiche de classification de référence », à ne jamais imprimer avec ce dossier.

Un jeu complet par cellule. Imprimer chaque fichier, découper les pièces 1 à 8 en fiches séparées ; les deux fiches de référence (ordre de mission, carte du secteur) restent des feuilles pleines A4, non découpées.

Les documents `.md` sont volontairement fournis, réalistes et abondamment illustrés : en-tête, référence de document, pictogramme par rubrique, et pour deux d'entre eux (pièces 2 et 4) un mélange volontaire de points décisifs et de remplissage administratif à l'intérieur du même document — le tri ne s'arrête pas à la pièce, il continue à l'intérieur de chaque pièce. Certains tableaux ont été remplacés par des paragraphes rédigés (pièces 1, 6, 7) pour lire comme de vrais mémos plutôt que des fiches techniques ; d'autres gardent leur tableau mais y ajoutent une synthèse en prose (pièce 5).

## Fiches de référence (gardées entières, non triées)

| Fichier | Format |
|---|---|
| `00_ordre_de_mission.md` | Texte, avec tampon de réception illustré |
| `00_carte_secteur.svg` | Image (à imprimer en A4 paysage) |

## Pièces à trier

| Fichier | Format | Choix de format |
|---|---|---|
| `piece_1_fiche_organique_dispositif.md` | Paragraphes rédigés + organigramme, une icône par source | Cinq portraits de source plutôt qu'un tableau à six colonnes ; se lit comme un vrai dossier organique |
| `piece_2_memo_doctrine_fiabilite.md` | Texte | Mémo doctrinal à six points, dont trois administratifs sans intérêt pour la mission |
| `piece_3_fiche_contact_informateur.svg` | Image | Fiche personnelle caviardée : le rendu visuel (bandes noires, tampon) porte l'information autant que le texte |
| `piece_4_rappel_securite_delais.md` | Paragraphes rédigés | Deux paragraphes plutôt qu'une liste à puces, dont un seul concerne vraiment la mission |
| `piece_5_bulletin_meteo_secteur_sud.md` | Prose + tableau | Synthèse rédigée en tête, tableau détaillé en appui — comme un vrai bulletin météo |
| `piece_6_note_logistique_carburant.md` | Paragraphes rédigés, une icône par rubrique | Quatre rubriques logistiques racontées plutôt que tabulées, aucune ne concernant le renseignement |
| `piece_7_calendrier_maintenance_generique.md` | Prose + frise chronologique illustrée | Une frise visuelle remplace le tableau multi-colonnes, avec une case « ? » bien visible pour le poste Nord |
| `piece_8_note_manuscrite_informateur.svg` | Image | Note manuscrite non signée : le papier froissé, l'écriture à la main et la tache de café sont le message — un fichier texte perdrait tout l'effet |

## Illustrations (`assets/`)

- `sceau_bureau.svg` : bandeau d'en-tête (compas + intitulé du bureau), repris sur chaque document texte pour l'unité visuelle.
- `tampon_reception.svg` : tampon d'encre « reçu à 15 h 58 », sur l'ordre de mission.
- `organigramme_dispositif.svg` : schéma hiérarchique des cinq sources, dans la pièce 1.
- `icone_jumelles.svg`, `icone_antenne.svg`, `icone_contact.svg`, `icone_drapeau.svg`, `icone_patrouille.svg` : un pictogramme par source, un par paragraphe de la pièce 1.
- `icone_loupe.svg` : doctrine de vérification, pièce 2.
- `icone_securite.svg`, `icone_horloge.svg` : sécurité opérationnelle et délais, pièce 4.
- `icone_soleil.svg`, `icone_nuage.svg`, `icone_vent.svg` : bulletin météo, pièce 5.
- `icone_carburant.svg`, `icone_ration.svg`, `icone_piece_detachee.svg`, `icone_courrier.svg` : un pictogramme par rubrique logistique, pièce 6.
- `icone_maintenance.svg`, `chronologie_maintenance.svg` : en-tête et frise chronologique de la pièce 7.

## Impression

Les fichiers `.svg` s'ouvrent dans n'importe quel navigateur et s'impriment directement (Ctrl+P), à l'échelle réelle indiquée dans chaque fichier (A4 paysage pour la carte, format carte/étiquette pour les pièces 3 et 8).

Les fichiers `.md` contiennent de nombreuses images intégrées (balises `<img src="assets/...">`) : un double-clic ouvrant le fichier brut dans un navigateur n'affichera pas la mise en forme. Ouvrez-les avec un visualiseur Markdown (aperçu VS Code, Typora, etc.) ou convertissez-les en HTML/PDF avant impression, par exemple avec Pandoc :

```
pandoc piece_1_fiche_organique_dispositif.md -o piece_1.pdf
```

à exécuter depuis ce dossier, pour que les chemins d'image relatifs (`assets/...`) se résolvent correctement.
