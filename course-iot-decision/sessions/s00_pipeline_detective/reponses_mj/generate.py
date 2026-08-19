"""Génère les fiches HTML de réponses MJ (séquence 0) à partir des données ci-dessous.

Usage : python generate.py
Régénère tous les fichiers .html de ce dossier. Les .pdf doivent ensuite être
recréés manuellement (impression navigateur, ou Edge headless --print-to-pdf),
un par fichier .html.
"""

from pathlib import Path

HERE = Path(__file__).parent
ICON_DIR = "../dossier_initial/assets"

SOURCE_ICONS = {
    "Poste d'observation fixe Nord": "icone_jumelles.svg",
    "Écoute radio et interception": "icone_antenne.svg",
    "Informateur local": "icone_contact.svg",
    "Poste frontalier allié": "icone_drapeau.svg",
    "Patrouille avancée": "icone_patrouille.svg",
}

CSS = """
@page { size: A4; margin: 12mm; }
* { box-sizing: border-box; }
body {
  font-family: "Georgia", "Times New Roman", serif;
  color: #1a1a1a;
  margin: 0;
}
.sheet { display: flex; flex-direction: column; gap: 0; }
.card {
  border: 2px solid #1a1a1a;
  border-radius: 4px;
  padding: 10mm 12mm;
  min-height: 125mm;
  display: flex;
  flex-direction: column;
  position: relative;
  page-break-inside: avoid;
}
.card + .cut { margin: 6mm 0; border-top: 2px dashed #999; position: relative; text-align: center; }
.card + .cut::after {
  content: "✂ couper ici";
  position: relative;
  top: -2.2mm;
  background: #fff;
  padding: 0 3mm;
  font-family: sans-serif;
  font-size: 8pt;
  color: #999;
  letter-spacing: 0.05em;
}
.card-header {
  display: flex;
  align-items: center;
  gap: 4mm;
  border-bottom: 1px solid #1a1a1a;
  padding-bottom: 3mm;
  margin-bottom: 5mm;
}
.card-header img { height: 9mm; width: auto; }
.card-header .titles { flex: 1; }
.source-name { font-size: 14pt; font-weight: bold; }
.request-type { font-family: sans-serif; font-size: 9pt; text-transform: uppercase; letter-spacing: 0.06em; color: #444; margin-top: 1mm; }
.badge {
  font-family: sans-serif;
  font-size: 9pt;
  font-weight: bold;
  border: 1px solid #1a1a1a;
  border-radius: 3px;
  padding: 1.5mm 3mm;
  white-space: nowrap;
  align-self: flex-start;
}
.stamp {
  font-family: sans-serif;
  font-size: 8pt;
  color: #b00;
  border: 1px solid #b00;
  border-radius: 3px;
  padding: 1mm 2.5mm;
  transform: rotate(-3deg);
  position: absolute;
  top: 8mm;
  right: 10mm;
}
.response {
  font-size: 12.5pt;
  line-height: 1.5;
  flex: 1;
}
.footer-note {
  font-family: sans-serif;
  font-size: 8pt;
  color: #777;
  margin-top: 4mm;
  border-top: 1px dotted #ccc;
  padding-top: 2mm;
}
.page-title {
  font-family: sans-serif;
  font-size: 8pt;
  color: #aaa;
  text-align: right;
  margin-bottom: 2mm;
}
"""


def card_html(source, response, request_type, cost, icon=None, ref="", note=""):
    icon_html = f'<img src="{ICON_DIR}/{icon}" alt="">' if icon else ""
    note_html = f'<div class="footer-note">{note}</div>' if note else ""
    return f"""
<div class="card">
  <div class="stamp">TRANSMISSION</div>
  <div class="card-header">
    {icon_html}
    <div class="titles">
      <div class="source-name">{source}</div>
      <div class="request-type">{request_type}</div>
    </div>
  </div>
  <div class="response">{response}</div>
  {note_html}
  <div class="badge">{cost}</div>
</div>
"""


def page(title, cards):
    body = f'<div class="page-title">{title}</div>\n<div class="sheet">\n'
    for i, c in enumerate(cards):
        if i > 0:
            body += '<div class="cut"></div>\n'
        body += c
    body += "</div>\n"
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<title>{title}</title>
<style>{CSS}</style>
</head>
<body>
{body}
</body>
</html>
"""


def write(name, title, cards):
    html = page(title, cards)
    out = HERE / f"{name}.html"
    out.write_text(html, encoding="utf-8")
    print(f"écrit : {out}")


# --- 1. Dernier rapport (1 jeton) ---
dernier_rapport = [
    ("Poste d'observation fixe Nord", "Mouvement de véhicules blindés signalé à 6 km au nord du point de contrôle, rapport reçu à 15 h 58, aucune confirmation depuis."),
    ("Écoute radio et interception", "Message intercepté évoquant un déplacement de colonne, deux confirmations radio reçues à 15 h 57."),
    ("Informateur local", "200 véhicules blindés signalés sur l'axe secondaire, rapport reçu à 15 h 55."),
    ("Poste frontalier allié", "Secteur calme, aucun mouvement signalé, rapport reçu à 15 h 56."),
    ("Patrouille avancée", "Aucun rapport reçu ce cycle."),
]
write(
    "dernier_rapport",
    "Dernier rapport d'une source — 1 jeton",
    [card_html(s, r, "Dernier rapport d'une source", "1 jeton", SOURCE_ICONS[s]) for s, r in dernier_rapport],
)

# --- 2. Historique des rapports des dernières 24 h (2 jetons) ---
historique = [
    ("Poste d'observation fixe Nord", "08 h 00 secteur calme ; 11 h 00 calme ; 14 h 05 mouvement signalé, avec une chute de fiabilité de l'optique consignée au même moment ; puis 14 h 05, 14 h 20, 14 h 50, 15 h 20 et 15 h 58 : toujours le même rapport — l'observation n'a plus été renouvelée depuis 14 h 05."),
    ("Écoute radio et interception", "08 h 00 rien ; 11 h 00 rien ; 14 h 00 rien ; 15 h 57 message intercepté par la station A ; 15 h 57 le même message intercepté quelques secondes plus tard par la station B, sur une fréquence relais différente."),
    ("Informateur local", "08 h 00 aucun contact ; 11 h 00 aucun contact ; 14 h 00 aucun contact ; 15 h 55 200 véhicules signalés — rupture isolée, aucune observation intermédiaire cohérente."),
    ("Poste frontalier allié", "08 h 00 calme ; 11 h 00 calme ; 14 h 00 calme ; 15 h 56 calme — aucune variation."),
    ("Patrouille avancée", "Aucun rapport sur les dernières 24 h."),
]
write(
    "historique_24h",
    "Historique des rapports des dernières 24 h — 2 jetons",
    [card_html(s, r, "Historique 24 h d'une source", "2 jetons", SOURCE_ICONS[s]) for s, r in historique],
)

# --- 3. Journal des incidents (2 jetons) ---
incidents = [
    ("Poste d'observation fixe Nord", "14 h 05 — panne d'alimentation de la lunette de guet signalée par l'équipe technique ; poste maintenu en observation dégradée depuis, sans confirmation humaine indépendante."),
    ("Écoute radio et interception", "Aucun incident récent enregistré."),
    ("Informateur local", "Aucun antécédent d'incident ; informateur en contact depuis 3 mois, fiabilité non réévaluée récemment."),
    ("Poste frontalier allié", "Aucun incident récent enregistré."),
    ("Patrouille avancée", "Dernier contact il y a 9 jours pour relève de matériel, motif non précisé dans ce journal."),
]
write(
    "journal_incidents",
    "Journal des incidents affectant une source — 2 jetons",
    [card_html(s, r, "Journal des incidents d'une source", "2 jetons", SOURCE_ICONS[s]) for s, r in incidents],
)

# --- 4. Vérification terrain (3 jetons + délai dé) ---
verification = [
    ("Poste d'observation fixe Nord", "Reconnaissance effectuée : secteur calme, aucun mouvement de véhicule constaté. La lunette de guet du poste est toujours signalée en panne d'alimentation."),
    ("Écoute radio et interception", "Aucune nouvelle interception ne confirme un déplacement de colonne au-delà du message initial."),
    ("Informateur local", "Aucune trace de colonne blindée sur l'axe secondaire ; la route ne permettrait de toute façon pas le passage d'un tel volume."),
    ("Poste frontalier allié", "Secteur confirmé calme sur place."),
    ("Patrouille avancée", "Aucun élément de la patrouille localisé sur sa dernière position connue, quel que soit le moment de la vérification."),
]
write(
    "verification_terrain",
    "Vérification terrain (reconnaissance) — 3 jetons + délai (dé)",
    [
        card_html(s, r, "Vérification terrain d'une source", "3 jetons + délai", SOURCE_ICONS[s],
                  note="Résultat transmis après le délai de reconnaissance (voir dé).")
        for s, r in verification
    ],
)

# --- 5. Requêtes globales ---
globales = [
    ("Ordre de bataille et plan de couverture", "1 jeton — achat unique",
     "Cinq éléments sont officiellement engagés sur le dispositif : poste d'observation fixe Nord, écoute radio, informateur local, poste frontalier allié et patrouille avancée. La patrouille avancée est marquée active, dernier contact confirmé il y a 20 jours.",
     ""),
    ("Comparaison avec une source témoin", "1 jeton — conditionnelle",
     "Source de référence retenue : poste frontalier allié. Secteur calme, stable — référence d'un secteur sans anomalie connue à ce jour.",
     "Condition d'accès : au moins deux requêtes individuelles achetées sur deux sources différentes."),
    ("Indice de menace consolidé", "1 jeton — conditionnelle",
     "L'indice de menace consolidé du secteur est de 25 sur 100, jugé faible ; il agrège observation, interception et renseignement humain sur une échelle commune et ne signale aucune source en alerte. La méthode de consolidation n'est pas communiquée à ce niveau.",
     "Condition d'accès : au moins deux requêtes individuelles achetées sur deux sources différentes."),
    ("Journal des transmissions radio", "2 jetons",
     "Une transmission non identifiée a été captée brièvement sur une fréquence voisine à 15 h 40, sans échange suivi. Aucune autre anomalie de trafic sur la période.",
     ""),
]
write(
    "requetes_globales",
    "Requêtes globales — portée : tout le secteur",
    [card_html(s, r, f"{s} — portée : tout le secteur", cost, note=note) for s, cost, r, note in globales],
)

print("Terminé.")
