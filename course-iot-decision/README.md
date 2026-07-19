# De la donnée capteur à la décision opérationnelle

Support pédagogique destiné aux officiers et élèves officiers de l’École de l’air et de l’espace.

Le cours étudie comment des données de capteurs imparfaites traversent une pipeline IoT et deviennent des indicateurs utilisés pour décider. Le fil rouge relie systématiquement qualité des données, confiance, incertitude, risques et décision opérationnelle.

## État du dépôt

Cette première étape installe uniquement l’arborescence. Les contenus seront ajoutés progressivement : syllabus, puis une séquence complète à la fois, scripts testés et vérification finale.

## Organisation

- `syllabus/` : syllabus général et bibliographie ;
- `sessions/` : huit séquences de quatre heures ;
- `src/` : code Python pédagogique ;
- `data/` : données brutes, traitées et échantillons ;
- `notebooks/` : notebooks Jupyter ;
- `docker/` : environnement MQTT local ;
- `tests/` : tests automatisés ;
- `prompts/` : grilles et prompts d’évaluation assistée par IA.

## Principe de progression

Chaque étape importante fait l’objet d’une validation avant modification. Le dépôt privilégie de petits changements et des commits explicites.
