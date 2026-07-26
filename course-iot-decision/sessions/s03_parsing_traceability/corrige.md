# Corrigé et débrief — Séquence 3

## Résultat de référence

Le lot contient 15 enveloppes valides et produit 15 lignes structurées. Chaque ligne référence une ligne brute et son SHA‑256. La vérification affiche `traçabilité vérifiée`.

Conclusion : **l’indicateur peut être reproduit et contesté à partir de la source ; confiance élevée dans la correspondance brut/table, moyenne au mieux pour l’interprétation.** Le dispositif ne prouve pas calibration, authenticité, horloge ou complétude.

## Réponses essentielles

- La donnée brute est conservée au plus près de la réception ; elle possède déjà une structure.
- La donnée structurée est une projection sous schéma ; elle facilite le calcul mais sélectionne.
- La provenance décrit entités, activités et responsabilités ; ici source, ligne, empreinte, version.
- SHA‑256 détecte une différence d’octets ; sans signature, il ne démontre ni auteur ni antériorité.
- `measured_at` vient du payload ; `received_at` vient de la collecte.
- Un identifiant aide à relier mais ne garantit ni unicité réelle ni authenticité.

## Incident

Les messages ont mêmes site, zone, capteur, instant, valeur, unité et séquence. Ils diffèrent par topic, réception, retained, identifiant, ligne et empreinte. Verdict : **candidats doublons métier**, pas messages identiques. Les conserver et signaler l’ambiguïté est la référence. Une déduplication exige une règle autorisée et une trace de la ligne écartée.

## Débat

Le CSV ne remplace pas le brut pour contester le parsing. Le brut ne doit pas être conservé indéfiniment sans politique : coût, confidentialité, minimisation et sécurité comptent. Attendu : rétention gouvernée, accès contrôlé, intégrité et durée alignée sur l’audit.
