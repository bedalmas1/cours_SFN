Tu es un expert en ingénierie pédagogique, data engineering, IoT, systèmes cyber-physiques, prise de décision opérationnelle, et formation d’officiers de l’École de l’air et de l’espace.

Je prépare un cours de 8 séquences de 4 h intitulé :

**De la donnée capteur à la décision opérationnelle : qualité, confiance et incertitude dans une pipeline IoT**

Le public est composé d’officiers ou élèves officiers de l’École de l’air et de l’espace. Ils ont quelques bases en Python et un peu de machine learning, mais ne sont pas spécialistes en ETL, data engineering, IoT ou cybersécurité.

L’objectif du cours n’est pas d’en faire des experts techniques, mais de développer leur **esprit critique décisionnel** face à une chaîne de données. Ils doivent comprendre comment une pipeline de données influence la qualité d’une décision opérationnelle : confiance, incertitude, erreurs, biais, indicateurs trompeurs, traçabilité, sécurité, robustesse, limites de la donnée.

Le scénario fil rouge est celui d’une **base aérienne projetée** équipée de capteurs environnementaux simples. Des capteurs Arduino/LoRa mesurent la température dans plusieurs zones critiques :

- stockage batteries de drones ;
- shelter transmissions ;
- local informatique tactique ;
- zone de maintenance légère ;
- abri matériel optronique.

Les données sont transmises vers un broker MQTT. Dans la première version du cours, on suppose que le broker contient déjà des données : les étudiants travaillent sur un broker Mosquitto simulé, pré-rempli avec des messages MQTT retained.

La question opérationnelle centrale est :

**Les données disponibles permettent-elles de prendre une décision fiable : maintenir l’activité prévue, déclencher une inspection, protéger du matériel, différer une opération ou demander une vérification terrain ?**

La logique pédagogique générale est :

Données capteurs imparfaites  
→ pipeline de traitement  
→ indicateurs  
→ décision opérationnelle  
→ niveau de confiance, incertitude et risques.

Les outils utilisés sont volontairement légers :

- VPS Ubuntu ;
- Docker / Docker Compose ;
- Mosquitto ;
- Python ;
- paho-mqtt ;
- JSONL ;
- pandas ;
- DuckDB ;
- CSV / Parquet ;
- matplotlib ;
- JupyterLab ;
- éventuellement Node-RED ;
- éventuellement Pydantic ;
- éventuellement pytest.

Le code doit être en **Python**.  
Les slides doivent être rédigées en **LaTeX Beamer standard**, sans template complexe, afin que je puisse les copier-coller dans mon propre template.  
Les sources doivent être **fiables, récentes lorsque nécessaire, sourcées et référencées**. Il faut citer les sources dans les slides et fournir une bibliographie ou liste de références à la fin. Pour toute information susceptible d’avoir changé, il faut vérifier avec des sources récentes. Privilégier les sources officielles, documentations techniques, publications académiques, normes, guides reconnus, rapports institutionnels.

Je veux préparer en détail la séquence suivante :

**Séquence à préparer : Comprendre la source : broker, topics et messages**

Objectif général de la séquence :

Comprendre ce que contient réellement le broker et ce que l'on risque de mal interpréter dès l'extraction.

Déroulé indicatif prévu :

Temps                                Activité

0:00-0:15                            Accroche : le broker est-il une source fiable ?

0:15-0:45                            Concepts : MQTT, broker, topic, payload, retained message

0:45-1:20                            Exploration guidée des topics

1:20-1:55                            Exercice : inventaire des zones, capteurs et messages

1:55-2:05                            Pause

2:05-2:30                            Concepts : lot, complétude, métadonnées

2:30-3:15                            Exercice : vérifier si le lot est complet

3:15-3:40                            Incident injecté : un capteur attendu est absent

3:40-3:55                            Brief décisionnel : peut-on conclure ?

3:55-4:00                            Synthèse

Question décisionnelle : Avant même de nettoyer les données, peut-on savoir si le lot est suffisant pour soutenir une
décision ?

Livrables : Inventaire des messages ; tableau zones/capteurs ; diagnostic de complétude ; note courte sur les limites
du brut.

Engagement : Binômes : équipe data et décideur qui pose des questions critiques.

## Arborescence du projet et règles de lecture/écriture

Toutes les routes ci-dessous sont relatives à la racine `course-iot-decision/`.
Avant de produire la séquence, lire les fichiers de cadrage et les ressources déjà
présentes afin de conserver la cohérence du cours. Ne pas créer de fichiers à la
racine lorsqu'un dossier dédié existe.

Remplacer dans toutes les routes suivantes :

- `<session>` par le dossier de la séquence préparée, parmi
  `s01_baseline_pipeline`, `s02_mqtt_broker_data_source`,
  `s03_parsing_traceability`, `s04_data_quality_uncertainty`,
  `s05_indicators_decision_traps`, `s06_visualization_decision_briefing`,
  `s07_security_trust_robustness` ou `s08_final_decision_project` ;
- `<sXX_nom_sequence>` par le même identifiant, utilisé comme préfixe des
  fichiers propres à la séquence.

### Fichiers et dossiers à lire

Lire systématiquement :

- `README.md` : objectifs du dépôt, conventions générales et organisation ;
- `syllabus/syllabus_overall.md` : progression, objectifs et déroulé de référence
  des huit séquences ;
- `sessions/README.md` : conventions communes aux séquences et aux slides ;
- `sessions/<session>/README.md` : cadrage propre à la séquence ;
- `latex/README.md`, `latex/common/preamble.tex` et
  `latex/common/references.bib` : conventions Beamer, commandes partagées et
  références déjà disponibles ;
- `data/README.md`, `data/raw/README.md`, `data/processed/README.md` et
  `data/samples/README.md` : règles applicables aux données ;
- `src/README.md` et `src/iot_decision/README.md` : organisation du code Python ;
- `notebooks/README.md`, `docker/README.md`, `docker/mosquitto/README.md`,
  `tests/README.md` et `prompts/README.md` : conventions des autres livrables.

Lire lorsqu'ils existent ou sont pertinents pour la séquence :

- `sessions/<session>/slides/<sXX_nom_sequence>.tex` et tout fichier placé dans
  `sessions/<session>/slides/figures/` ;
- les guides, exercices, corrigés, évaluations et autres supports déjà présents
  dans `sessions/<session>/` ;
- les scripts de `src/iot_decision/`, les notebooks de `notebooks/`, les tests de
  `tests/`, les prompts et grilles de `prompts/` ;
- les configurations de `docker/` et `docker/mosquitto/` ;
- les jeux de données de `data/raw/`, `data/processed/` et `data/samples/` ;
- les ressources d'une séquence antérieure uniquement si elles sont nécessaires
  à la continuité pédagogique. Ne pas les modifier dans ce cas.

### Fichiers et dossiers dans lesquels écrire

Produire ou mettre à jour les livrables aux emplacements suivants :

- `sessions/<session>/README.md` : vue d'ensemble et mode d'emploi de la séquence ;
- `sessions/<session>/instructions_avant_seance.md` : checklist enseignant avant séance,
  incluant installation, dépendances, broker/Docker, supports, matériel, plan de
  repli et contrôles de dernière minute ;
- `sessions/<session>/slides/<sXX_nom_sequence>.tex` : slides Beamer principales ;
- `sessions/<session>/slides/<sXX_nom_sequence>.pdf` : PDF compilé et directement
  projetable, produit depuis le `.tex` de la séquence ;
- `sessions/<session>/slides/figures/` : figures propres aux slides ;
- `sessions/<session>/guide_enseignant.md` : déroulé détaillé, timing, consignes,
  réponses attendues, points de vigilance et débriefs ;
- `sessions/<session>/guide_etudiant.md` : support étudiant unique réunissant consignes, activités et exercices ;
- `sessions/<session>/corrige.md` : éléments de correction séparés des énoncés ;
- `sessions/<session>/evaluation.md` : modalités, critères et barème de
  l'évaluation de la séquence ;
- `src/iot_decision/` : modules et scripts Python réutilisables, simples et
  commentés ;
- `notebooks/` : notebooks Jupyter d'exploration ou de manipulation ;
- `tests/` : tests automatisés associés au code et aux cas de qualité des données ;
- `data/raw/` : messages reçus ou simulés conservés sans transformation ;
- `data/processed/` : données nettoyées, enrichies ou agrégées ;
- `data/samples/` : petits jeux de données reproductibles à distribuer ;
- `docker/` et `docker/mosquitto/` : Docker Compose, configuration Mosquitto et
  fichiers nécessaires à l'environnement MQTT local ;
- `prompts/` : prompts et grilles d'évaluation assistée par IA ;
- `latex/common/references.bib` : références bibliographiques partagées ;
- `latex/common/preamble.tex` : uniquement les commandes ou dépendances réellement
  communes à plusieurs séquences.

Conserver dans `sessions/<session>/` les ressources spécifiques à une seule
séquence. Placer dans les dossiers partagés uniquement ce qui est réutilisable.
Utiliser dans les slides le préambule commun avec
`\input{../../../latex/common/preamble}` et placer les citations BibTeX dans
`latex/common/references.bib`. Ne pas écrire ni versionner les fichiers générés par
LaTeX (`.aux`, `.log`, `.nav`, `.out`, `.snm`, `.toc`, `.vrb`, `.bbl`,
`.blg`, `.fls`, `.fdb_latexmk`, `.synctex.gz`). Le PDF compilé
`slides/<sXX_nom_sequence>.pdf` est désormais un livrable obligatoire et peut
être versionné; les autres intermédiaires restent exclus.

Après chaque préparation, compiler le deck depuis `sessions/<session>/slides/`,
rendre les pages du PDF et vérifier visuellement la lisibilité, les figures,
les références, les transitions et l'absence de débordement.

Contraintes :

- La séquence dure 4 h.
- Elle doit alterner théorie, concepts, exemples, exercices pratiques, discussions, débats et restitutions.
- Il faut maintenir l’engagement des étudiants.
- Chaque activité doit être reliée à une question de décision opérationnelle.
- La technique ne doit jamais être enseignée comme une fin en soi.
- Chaque concept doit être relié à son effet possible sur la qualité de la décision.
- L’évaluation doit être rapide, claire, et idéalement partiellement automatisable ou évaluée avec l’aide d’une IA.
- Les supports doivent être directement exploitables par un enseignant.

Je veux que tu produises une préparation complète de cette séquence avec les éléments suivants.

---

## 1. Intention pédagogique de la séquence

Présente en quelques paragraphes :

- le rôle de cette séquence dans l’ensemble du cours ;
- ce que les étudiants doivent comprendre à la fin ;
- la compétence décisionnelle principale travaillée ;
- les risques de mauvaise compréhension à anticiper ;
- la question opérationnelle qui structure la séance.

Formule clairement la question directrice de la séquence sous la forme :

**“À la fin de cette séquence, les étudiants doivent être capables de décider si…”**

---

## 2. Objectifs d’apprentissage évaluables

Produis une liste de 5 à 8 objectifs d’apprentissage formulés avec des verbes observables, par exemple :

- identifier ;
- expliquer ;
- extraire ;
- comparer ;
- justifier ;
- évaluer ;
- recommander ;
- qualifier le niveau de confiance.

Sépare les objectifs en trois catégories :

1. objectifs conceptuels ;
2. objectifs pratiques ;
3. objectifs décisionnels / esprit critique.

---

## 3. Plan détaillé de la séance de 4 h

Propose un déroulé minuté réaliste sur 4 h, alternant :

- accroche opérationnelle ;
- apport conceptuel ;
- exemple guidé ;
- manipulation pratique ;
- incident ou surprise injectée ;
- discussion ou débat ;
- restitution ;
- synthèse.

Utilise un tableau avec les colonnes :

- temps ;
- activité ;
- objectif ;
- modalité ;
- livrable ou trace attendue.

La structure doit éviter un bloc de théorie trop long. Préférer des cycles courts :

situation opérationnelle  
→ concept  
→ exercice  
→ débat  
→ décision  
→ débrief.

---

## 4. Concepts clés à enseigner

Pour chaque concept important de la séquence, produire une fiche synthétique comprenant :

- définition simple ;
- explication adaptée à des officiers non spécialistes ;
- exemple dans le scénario de base aérienne projetée ;
- erreur fréquente ou piège ;
- conséquence sur la décision ;
- question à poser aux étudiants ;
- référence ou source à citer.

Les concepts doivent être reliés à la prise de décision. Par exemple :

- message brut ;
- topic MQTT ;
- retained message ;
- horodatage ;
- donnée manquante ;
- doublon ;
- valeur aberrante ;
- seuil ;
- agrégation ;
- visualisation ;
- traçabilité ;
- confiance dans la donnée ;
- incertitude ;
