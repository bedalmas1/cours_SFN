# Schéma commenté — `batch001_structured.csv`

| Champ | Type | Origine | Rôle décisionnel |
|---|---|---|---|
| `schema_version` | texte | pipeline | indique les règles de parsing |
| `source_file` | chemin POSIX | pipeline | nomme le brut utilisé |
| `source_line` | entier ≥ 1 | pipeline | retrouve la ligne exacte |
| `raw_sha256` | hexadécimal | pipeline | détecte une modification du brut |
| `topic` | texte | enveloppe | conserve le périmètre de publication |
| `received_at` | RFC 3339 | enveloppe | date l’observation par la chaîne |
| `retained` | booléen | enveloppe | qualifie le mode de réception |
| `batch_id` | texte | payload | rattache au lot déclaré |
| `message_id` | texte | payload | identifie le message déclaré |
| `site_id` | texte | payload | borne le site |
| `zone` | texte | payload | localise la portée |
| `asset_type` | texte | payload | explicite le matériel exposé |
| `sensor` | texte | payload | nomme la grandeur |
| `measured_at` | RFC 3339 | payload | date déclarée de mesure |
| `value` | nombre | payload | valeur non corrigée en S03 |
| `unit` | texte | payload | empêche une comparaison sans unité |
| `sequence` | entier ≥ 0 | payload | aide à détecter répétition ou trou |

## Clés et règles

- Retour au brut : (`source_file`, `source_line`, `raw_sha256`).
- Identifiant métier déclaré : (`site_id`, `message_id`), contrôlé mais non authentifié.
- Candidat doublon : mêmes site, zone, capteur, instant, valeur et unité. Ce regroupement signale ; il ne supprime rien.
- Une empreinte contrôle l’intégrité, ce n’est pas une signature.

Le JSONL brut reste conservé selon la politique de rétention. Le CSV n’est pas un substitut probatoire autonome.
