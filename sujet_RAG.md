# Retrieval Augmented Generation

l’idée c’est d’avoir une source de données, en markdown par exemple
pour la découper sous forme de chunks dans une base de données type vectordb
puis d’intégrer des questions par rapport à cette documentation
pour ainsi permettre d’avoir une documentation qu’on pourra interroger  


Source tuto : https://python.langchain.com/docs/tutorials/rag/




_____________________________

## Installation 

```
mkdir -p RAG/venv
cd RAG
python3.10 -m venv venv/
source venv/bin/activate
```


A ce stade on a une source web quelconque ( une page web, un markdown etc...)

PUIS
On va établir un modèle à partir de ça, le modele est une sorte de """"base de données"""" au format particulier qu'on va pouvoir interroger.
Pour faire un modele on a trois possibilités
 - **from scratch :** un modèle de zéro
 - **finetune :** un modèle préexistant qu'on va venir configurer avec des données spécifiques qui vont être intégrées dans le modèle
 - **RAG :** on définit une base de données contenant des données maison et la requête client va être comparée aux données maison avant d'être passée dans un modèle préexistant pour établir une réponse compréhensible par un humain




**CHOIX :** Ici on prend RAG qui est la solution majoritaire

Pour réaliser notre RAG, on va prendre le framework LangChain

LangChain is a framework for developing applications powered by large language models (LLMs).

Avec langchain on va pouvoir attaquer notre source ( exemple une documentation écrite en markdown ou une page web)
et la découper en "chunks" en gros des morceaux de texte représentés mathématiquement sous la forme de vecteurs, et que l'intelligence va pouvoir interpréter./

*source du tuto :* https://python.langchain.com/docs/tutorials/rag/


## C'est quoi un RAG ?

Typiquement un "RAG" se compose de deux éléments :

 - **une indexation :** a pipeline for ingesting data from a source and indexing it. This usually happens offline.
 - **une partie Retrieval and Generation :** the actual RAG chain, which takes the user query at run time and retrieves the relevant data from the index, then passes that to the model.

Et l'idée va être de passer notre source au travers de plusieurs étapes :

*** trois étapes pour l'indexation : 

 - **Load :** First we need to load our data. This is done with Document Loaders.
 - **Split :** Text splitters break large Documents into smaller chunks. 
 - **Store :** We need somewhere to store and index our splits, ( le stockage est fait sous forme de vecteurs dans une base )


*** deux étapes pour le retrieval and generation :
 - **Retrieve :** Given a user input, relevant splits are retrieved from storage using a Retriever.
 - **Generate :** sous la forme d'un ChatModel/Prompt, qui va transmettre à un LLM - produces an answer using a prompt that includes both the question with the retrieved data

Apparemment on peut orchestrer les RAG via ce que langchain appelle LangGraph mais c'est plutôt quelque chose de propre à LangChain

## Installation pour réaliser le RAG

### le splitter

```
pip install --quiet --upgrade langchain-text-splitters langchain-community langgraph
```


### la plateforme de développement LangSmith (optionnel)

https://smith.langchain.com/

```
import getpass
import os

os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_API_KEY"] = getpass.getpass()
```

### Le chat model 

Nous choisissons Ollama parce qu'on l'a en local, le produit Ollama en tant que serveur d'inférence peut remplir plusieurs role dont celui-ci, mais nous pourrions aussi utiliser NVidia)

Puisque nous choisissons d'utiliser Ollama pour la partie ChatModel
```
pip install -qU langchain-ollama
```
Test de fonctionnement associé : `RAG/test-ollama-chatmodel.py`


Si nous avions choisi NVidia
```
pip install -qU langchain-nvidia-ai-endpoints
```
Test de fonctionnement associé : `RAG/test-nvidia-chatmodel.py`


Petit point à ce stade, on aura la notion de prompt :
```
 - Prompt : une question envoyée en entrée "quel est la capitale de la France ?"
 - System Prompt : instruction spéciale envoyé à l'IA avant qu'elle ne réponde "tu devras répondre comme si tu étais un boulanger Afghan au 19ème siècle" 
 - Chain of Thought (COT Prompt) : fait en sorte de décrire comment l'IA doit répondre :
       sans la COT "5*6=30"
       avec la COT "5*6=30, ce qui est la meme chose que 6+6+6+6+6"
 - Few Shot Prompt : un prompt préentrainé avec des questions/réponses
```



### Le embedding Model 

Le but du Embedding model va être d'aller fouiller dans les vecteurs ( appelés "embeddings" ) pour isoler les bonnes sources qui serviront plus tard à faire la réponse.
On choisi Ollama parce qu'on a un serveur d'inférence en local, mais on pourrait choisir AWS, Azure ou OpenAI.
Là encore Ollama peut remplir plusieurs role dont celui de embedding Model.

Note : Ollama n'est pas un model mais un serveur d'inférence, un serveur d'API qui accepte des requêtes et va les passer dans un n'importe quel modèle de données.

```
pip install -qU langchain-ollama
```

Test de fonctionnement associé : test-ollama-embeddingsmodel.py


### Le vector Store

La base de données vectorielle qui stocke les vecteurs issus du découpage

Pour , on pourrait choisir des BDD comme pgvector)

```
pip install -qU langchain-core
```

Test de fonctionnement associé : `test-inmemory-vector-store.py`


Pour des raisons pratiques ultérieures nous essayons un autre vector Store : postgresql+PGVector

```
sudo apt install postgresql-16-pgvector
psql
  create role test with password 'password' login;
  create database mydb;
  \c mydb
  GRANT USAGE ON SCHEMA public TO test;
  GRANT CREATE ON SCHEMA public TO test;
  CREATE EXTENSION vector;
  \dx



pip install -qU langchain-postgres
```

Test de fonctionnement associé : `test-pgvector-vector-store.py`


# Premier script de génération d'un RAG

A présent nous pouvons faire notre premier script de génération d'un RAG


Dépendances : 
```
#       - jouer la partie sur postgresql+pgvector juste au dessus
#	- installer Ollama sur la machine
#	- télécharger le modèle llama3.2
#	- installer le package beautifulsoup4 pour le parsing de la source
#		pip install beautifulsoup4
```

Test de fonctionnement
```
python3.10 -m venv venv/
source venv/bin/activate
export LANGSMITH_API_KEY="MON_API_KEY_Recuperee_sur_https://smith.langchain.com/"
python parse-split-index-retrieve-generate.py
```

# Amusons-nous

A ce stade nous devrions adapter ce script pour deux objectifs :

- Avoir un prompt/ un chatmodel / des questions que j'ai défini moi-même

Test de fonctionnement : 

```
python3.10 -m venv venv/
source venv/bin/activate
export LANGSMITH_API_KEY="MON_API_KEY_Recuperee_sur_https://smith.langchain.com/"
python custom_prompt_parse-split-index-retrieve-generate.py
```

Pour le concept nous en profitons pour explorer la partie promptIA.

```
	Un prompt consiste à récupérer la question utilisateur, l'intégrer dans un contexte, et la soumettre à un modèle logique
	Le "contexte" c'est un objet composé de la façon de répondre, des précédentes questions, de sources externes éventuelles... 
	L'idée c'est que le prompt est en plusieurs couches
		- system message
		- shots
		- user message
		- parametre
```


Context Window+Prompt ----soumet à-----> LLM (via serveur d'inférence) ----répond----> Completion


- Avoir une source locale

Test de fonctionnement (basé sur le repo keycloack)

```
git clone https://github.com/keycloak/keycloak.git
python3.10 -m venv venv/
source venv/bin/activate
pip install unstructured
python local_source_prompt_parse-split-index-retrieve-generate.py
```

Maintenant ce qui serait drole, ce serait de différencier l'alimentation du modèle, et l'interrogation du modèle, de telle sorte 
	- un serveur alimente la base
	- un client ne fait que requêter la base

Test de fonctionnement (basé sur le repo keycloack en local) :

```
python3.10 -m venv venv/
source venv/bin/activate
# load des chunks des données
python create_vector.py
# interrogation du LLM enrichi avec les données client
python query_handler.py
```

# Petit exercice perso le chatbot && un RAG simple

Voir le dossier `chatbot/`
- un script qui récupère les données dans les sources clients
- un serveur qui récupère les questions clientes et établit une réponse
- une IHM pour que ce soit plus agréable pour l'utilisateur ( à établir )


-------


# Notion de Graph Rag
- le RAG convertit des entrants en vecteurs (que ce soit des questions ou des réponses), et quand tu poses une question, il va traduire ça en vector et te renvoyer les vectors les plus proches.
- imaginons on a un RAG, qui est composé de chunks, on lui associe une BDD graph pour tordre la simple proximité des vectors et ajouter en plus des liens explicites entre les chunks -> par exemple dans le cadre d'une logique métier 


# Notion de Rag chain :

- Jusqu'à maintenant nous n'avons travailler qu'avec de la RAG simple

- voici une RAG simple :
```
	Un utilisateur	--> pose une question
			--> interceptée dans un objet prompt
			--> Retrieval : Recherche d'infos pertinentes dans une source de données ( BDD Vectorielle par exemple )
			--> Generation : passage dans un modèle LLM
			--> réalisation de la réponse 
```
- La Rag chain se caractérise par une double récupération d'informations:
```
        Un utilisateur  --> pose une question
                        --> interceptée dans un objet prompt
			--> Première interrogation avec une base de données vectorielle
			--> Première envoi à un LLM (Retrieval - spectre large)
			--> Affinage de la requête (En fait il s'agit d'une deuxième question, dans le même style que
						 la première, et on tient des documents répondus à la première question pour affiner la réponse de la seconde)
			--> Seconde interrogation avec une base de données vectorielle
			--> Second envoi à un LLM (Retrieval - spectre plus précis) 
                        --> réalisation de la réponse
```

REMARQUE : quand un LLM (+Base vectorielle) répond, il renvoit une réponse ainsi qu'une série de documents de référence.
	Dans une RAG Chain, l'utilisateur pose une question à chaque boucle question->réponse
	Dans une RAG Chain, on va conserver les documents renvoyés par la réponse à la question N, et les renvoyer comme contexte pour la réponse à la question N+1 
	Dans une RAG Chain, on ignore les réponses à chaque tour de boucle, c'est contre-intuitif, mais cela permet d'éviter l'effet "téléphone arabe"
		On ne veut PAS que la réponse à la question N influence la réponse à la question N+1
		On veut que les DOCUMENTS récupérés lors de l'établissement de la réponse à la question N influencent la réponse à la question N+1


Concrètement la *RAG chain* est un enchainement de questions-réponses par lequel chaque document récupéré pour la question N va servir à préciser le contexte de la question suivante.

- L'utilisateur entre une première question, obtient une réponse et des documents de référence, la réponse est affichée, les documents sont conservés en mémoire coté client
- L'utilisateur entre une seconde question, en contexte sont précisés les documents associés à la réponse de la première question, et une seconde réponse va être générée et affichée les documents associés à la seconde réponse sont ajoutés aux documents associés à la première réponse
- L'utilisateur entre une troisième question, en contexte sont précisés les documents des réponses 1 et 2, une réponse est générée et affichée, les documents sont conservés en mémoire

La boucle de ces trois points se répètent boucle jusqu'à une clause de fin de la discussion.


# Petit exercice perso le chatbot et une RAG chain

```
TODO à se faire ça plus tard, avec une boucle de questions qui reprennent les documents associés à la réponse de la question précédente et conservent l'ensemble des documents
```


# Notion de temperature :

Nous avons finalisé le travail iachatbot (voir le dossier dédié).

A ce stade nous avons vu que nous réalisions des RAG avec deux appels de modèle :
	- un objet embedding qui manipule/récupère les données dans un vector_store
	- un objet LLM qui génère la réponse

Lors de la connexion au modèle des embeddings (object OllamaEmbeddings) ou au modèle génératif (objet OllamaLLM) on peut déclarer une temperature.
Concrètement il s'agit d'un flottant 0.0 à 1.0 qui va définir de façon abstraite la "créativité" de l'IA.

Cette température va permettre de qualifier la marge de manoeuvre dont l'IA dispose pour manipuler les données.

La variation de la température des embeddings va affecter la récupération des sources en controlant la similarité avec les chunks du vector_store.
La variation de la température sur la connexion au modèle génératif va permettre de controler le coté travaillé ou "poetique" des réponses.

Une température plus haute sur les embeddings va donner davantage de sources dans le cadre d'un vector_store mais a potentiellement plus d'éloignement avec la question.
Une température plus basse sur les embeddings va donner moins de sources piochées dans un vector_store mais sera plus rigoureux vis-à-vis de la question.

Une température plus haute sur le modèle génératif va provoquer une IA plus créative
Une température plus basse sur le modèle génératif va davantage coller aux sources remontées par l'embedding, mais va demander des questions plus exactes.


A l'usure :
nous avons constaté qu'un embedding avec une température haute permettait d'avoir des sources (==documents) larges
nous avons constaté qu'un génération avec une température basse permettait de ne pas trop s'éloigner des sources indiquées. 

Une bonne pratique de RAG consiste à placer la température des embeddings à 0.1 pour bien coller aux sources et la génération de la réponse à 0.2 pour pas trop halluciner.
A l'usure nous avons constaté que ces mesures sont bonnes.


# Source vidéo 

https://www.youtube.com/watch?v=ZbWL2W53BXY


# Notion de deeplearning et de modèle fine tuned

Le deeplearning c'est la base de la création des modèles LLM, mais dans son fonctionnement ça n'a rien à voir.

C'est ce qui permet de créer un *modèle de données* from scratch ou de le *customiser au besoin*.

  - Deeplearning : création d'un nouveau modèle de données à partir de sources associées à un algorithme
  - Fine tunning : customisation d'un modèle de données existant

Le *deeplearning* est à la base de la créations des modèles de données. Mais le deeplearning prend des entrants, les passe dans un algorithme et sort une informations. C'est du machine learning.
Un *modèle de données* peut sortir de nouvelles données à partir de divers calculs de similarités avec un entrant + une part de créativité. On parle d'IA générative.


Outils principaux :
	- pytorch
	- tensorflow ( très bientôt obsolète )


L'idée derrière le traitement des données par IA va toujours être plus ou moins le même principe :
	- on a une source métier, des données brutes
	- on va filtrer cette source métier
	- on va passer ce filtrat dans un LLM pour qu'il génère une réponse


**Exemple :** On veut récupérer les meilleures entreprises parmis notre liste, selon des critères établis complexes.

On part d'une liste d'entreprises avec des infos associées (age, CA...) :

**Source** -----------------------------> nos données brutes sur les entreprises
**Filtering** --------------------------> on réalise les embeddings (liste des entreprises avec leurs caractéristiques) AKA une entreprise == un vector, le découpage peut être complexe
**Obtention d'une réponse/scoring** ------------> on fine tune un modèle pour le besoin client en travaillant les données métiers dans le modèle (on lui apprend à faire un score)

On cale du deeplearning aux étapes de filtering et de scoring.
A ce stade on n'a pas encore vu de fine tuning

Note : On parle de BERT comme nom des premiers modèles d'interprétation de langage naturel, camemBERT par exemple permet de comprendre le français.


# le découpage de vecteurs/embeddings

Sur le papier on pourrait penser qu'un vecteur == une donnée (pour reprendre notre exemple au dessus un vecteur == une entreprise)
Dans les faits c'est un choix raide, et on aura tendance à découper des données en plusieurs vecteurs avec du metric-learning par exemple.
Une des modélisations type deeplearning, on peut jouer avec un concept d'attention.

---> attention tout ce travail peut être très chronophage.
Il ne faut pas chercher la perfection, sous peine d'avoir quelque chose de sur-optimisé.

# Déploiement

- la recherche prend beaucoup de temps
- on peut sortir le réseau neuronal ( pytorch ) au format ONNX `TODO : ça veut dire quoi ? `
- petit budget ==> optimisation du modèle

optimisation du modèle, c'est tout le travail sur:
- la récupération des données
- le traitement des erreurs
- le suivi de la conso du GPU

# principe de trainer et de training
A voir


# FINALEMENT : les modèles génératifs !!

## Modèle de base

Génération = prédiction statistique
A l'aide du deeplearning on créé un modèle basé sur des milliards de mots, et on fait des calculs statistiques sur la présence de chaque mot après chaque autre. On obtient un modèle.

Une fois le modèle obtenu on peut lui donner un entrant, il va générer une sortie en se basant sur des arrondissements statistiques.


On retrouve le principe de prompting pour améliorer l'entrée du modèle génératif =!= fine tunning

Il s'avère que le fine tuning n'est pas à la portée de n'importe qui, c'est même très complexe, surtout sur les modèles génératifs, du coup on va préférer du prompting

- prompting = on améliore l'élément en entrée du modèle avec tout un contexte
- fine tuning = on spécialise le modèle

Problème du prompting = implique un gros modèle pour de meilleurs résultats, surtout pour un modèle qui devra répondre "à tout"

Ce sont ces gros modèles généralistes que l'on nomme concrètement **LLM**.

Il y a eu un gros travail de recherche pour optimiser la taille du modèle et la taille du jeu de données pour entrainer, mais on est toujours sur des milliards de paramètres et de données.

en fin de parcours on a développé le concept de prompt ingeniering, la "science" de comment optimiser un prompt pour obtenir les meilleurs résultats.

Problème de cette approche du modèle LLM "de base", il fait plus de la complétion que du dialogue, c'est un assez mauvais chatbot, c'est ce pourquoi on a créé des modèles faits pour les interactions.

## Modèles avec interaction

Ici les modèles vont être influencés sur la qualité de leur réponse : 
- Soit par scoring : couteux et peu pratique
- Soit par prompting : demande plusieurs essais (few shot) et un contexte pertinent (chain of though)
- Soit par fine tunning OU pré-training : templating de prompt pour simplifier l'approche --> prompt + instruction sur comment répondre, l'utilisateur pose sa question et a déjà un prompt context qui informe précisément comment répondre.

La dernière méthode est la plus simple à aborder, et efficace sur les modèles généralistes.


Le soucis : c'est que quelque soit l'approche on a toujours un coté statistique et on va quand même avec des générations fausses ou biaisées dites "toxiques".
- Soit on opte pour une approche humaine systématique, impossible sur les gros jeux de données)
- Soit on opte pour une approche RLHF : on créé un deuxième modèle qui va avoir pour but de prédire la qualité de la génération du premier modèle

Le RLHF, c'est basiquement le fait de créer un mini-modèle basé sur un dataset de données contrôlées, et ce modèle/ va controler que la réponse du premier modèle n'est pas toxique, fausse etc...
Reinforcement Learning with Human Feedback

Concernant ce système à deux modèles le mini-modèle sert d'alignement, le fait d'essayer de casser cet alignement s'appelle le jailbreaking.

A ce moment on obtient un produit qui commence à bien fonctionner.

## Modèles multimodaux

c'est avec ce type de modèle qu'on va pouvoir avoir des entrées non plus seulement textuelles mais aussi des images.
 
## A propos des hallucinations

Les modèles font des aproximations continues, empêchant d'avoir des résultats purs et parfaits, et on tombe régulièrement sur des résultats extrapolés alors qu'on voudrait des résultats précis.
L'idée pour limiter ces hallucinations est de forcer un travail du LLM en plusieurs étapes et d'**adjoindre aux LLM une source ou un outil externe pour les étapes nécessitant de la précision/** : 
- Base de données wikipedia pour l'histoire
- Une calculatrice pour faire des maths
- ...

**Exemple d'un outil framework pour faire cette aide externe via prompt engineering:** Framework ReAct (rien à avoir avec le langage)

Gros avantage de cette approche : pas d'apprentissage de modèle, tout passe par du prompt engineering.
Défaut prévus à terme pour cette approche : le prompt est limité, on devra à terme revenir sur du fine-tuning ( intégration de notre gros contexte directement dans le modèle )
Autre gros défaut : pour des besoins très avancés ce n'est pas parfait à 100%

## Déport du prompt dans le modèle

**rappel :** fine-tunning = spécialisation du modèle pour obtenir un résultat optimisé dans un domaine spécifique.

Comme dit dans le chapitre précédent, le prompt engineering est très pratique mais il reste limité, surtout quand le prompt devient très gros, il faut alors retourner sur du fine-tunning et réincorporer les données du prompt dans le modèle

**Exemple d'un famework permettant de libérer le prompt et de travailler avec du fine-tunning :** Toolformer 

Le dataset pour entrainer le modèle peut même est généré via IA lui-même.

## Modèles augmentés (approche par plugin)

On peut donc utiliser des outils externes pour ajuster les résultats et éviter les hallucinations.
Certaines structures -comme Open AI- mettre à disposition un écosystème de plugins pour venir compléter les retours des IA.
Chez Open AI (chatGPT) le store s'appelle les GPT plugins.

Ces plugins peuvent faire des maths, taper dans une base, aller regarder sur wikipedia etc...
 
**Pour ces modèles assistés par outils, on parle de modèle augmenté.**

La suite logique est de permettre aux modèles ( et à leurs plugins ) d'aller plus loins que la seule recherche de données sources, en offrant des outils de récupération de données.
On parle d'agents AI.

Cette approche par modèle assisté est très puissantes, mais peu sécurisées (hack par prompt vérolé), risque de boucles infinies, et hallucinations plus difficiles à détecter.

## Enrichissement par Agent AI

Les agents AI sont des outils et des interfaces qui vont permettre de récupérer des informations de façon complexe, et réaliser des actions complexe sur ordre, rompant avec les seules chaines de caractère simples.
- mise en place d'un dialogue d'échange (chatbot)
- outil d'automatisation vocale avec langage naturel (Alexa, Siri...)
- Agent de recommandation ( Netflix, Spotify, Amazon ) typiquement la section "vous pourrez aimer"
- Robotique autonome ( voiture autonome )
- Agent de trading haute fréquence
- Agent de sécurité et détection des fraudes ( IA bancaire, cyber sécu )
- ...

 
L'intéret est qu'on peut **commencer à jouer avec des workflows** et intégrer de l'IA dans des infrastructures préexistances classiques pour y apporter une touche d'automatisation par IA

Chacun de ces agents a la caractéristique d'avoir une méthode bien précise et une utilisation clairement définie pour obtenir des informations.

L'agent IA n'a pas seulement pour vocation de servir d'entrée mais aussi d'outil de manipulation après traitement par les modèles : 
--> Soit un ordre passé de façon vocal, cet ordre est transcrit en texte, puis passé dans un agent AI pour executer concrètement l'ordre.

**Exemple d'interface de construction de workflow avec Agent AI :** N8N , qui existe en version pro ou en version community


Exemple de workflow impliquant un agent AI : 
Je demande vocalement via un micro dans l'interface Telegram à envoyer un message à Michel

```
Get message telegram
--> switch <if audio>
-----> get audio file
-----> transcription du fichier audio en texte --> chatgpt sait faire ça
-----> passage de l'ordre textuel dans l'agent AI qui va bien
---------> Passage dans le chat antropomorphique pour que l'AI agent comprenne ce que l'on veut (on peut connecter à ce stade un produit comme Claude, Mistral, GPT etc...)
---------> connexion de l'agent AI au connector Gmail (penser à définir le prompt à ce stade)

PUIS pour tester

On envoit un message qui demande l'envoi d'un message à Michel

Le message vocal est enregistré
----> le message vocal est extrait
----> Le message vocal est transcrit en texte
----> l'agent IA intercepte l'ordre
-------> l'agent IA comprend ce qu'on veut par application du message dans le chat anthropomorphique
-------> l'agent IA a un connector gmail approprié, un "système message" qui lui templatise le message à envoyer & finalement l'agent IA envoi un message
```

Autre exemple : https://www.youtube.com/watch?v=yWF3NvWdCPA



## Un petit lab amusant : on monte un n8n en local et on fait un workflow

Voir le dossier n8n

