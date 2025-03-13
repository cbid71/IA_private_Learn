# My notes about AI


* Partial Dependance Plot (PDP)
-> "Graphique de dépendance partielle"
-> Aide à connaitre la relation entre une variable et un modèle pour comprendre et interpréter les résultats obtenus.
-> Montre comment une feature influence un résultat

* Feature 
La partie d'un dataset 
-> un dataset "les maisons en vente" va avoir des features du genre
---> le prix
---> la surface
---> la location
---> ...

* Summurization chatbot ==> RAG --> Parfait pour extraire les données clefs d'une masse de données.

* Clarification et rangement ---> "Rangement binaire" ----> **Descision tree**
----> Revient à faire un classement en sous-catégories

* "Accuracy" : littéralement "précision", parfois assimilé à "performance".
--> should be used to measure the performances of an image rekognition LLM (or other LLM)

* **Adjusting Prompt** is the beast solution for customizing the answer of a chatbot (Ex: "Make it short please !" in the request)

* SageMaker : platforme de gestion de modele, peut notamment créer un modèle from scratch
---> Si la question "with real time latency" -> "Real Time Inference"
---> Si la question "with NEAR real time latency" -> "Asynchronous inference"

* La notion de Transfer Learning permet d'enrichir un modèle LM préconcu avec des données spécifiques sans avoir à réentrainer un modèle.
Le principe est d'utiliser un modèle entrainé avec des données, pour le faire travailler avec des données différences mais 
dans un domaine proche à celui pour lequel le modèle a été entrainé
---> Cela ressemble un peu au RAG mais pas vraiment.

* Quand on est sur des données particulièrement sensibles à manipuler, on peut opter pour de la manipulation de données par LM avec vérification "human in the loop".


* Amazon Bedrock : Mise à disposition d'IA + fine-tunning
* Amazon Rekognition : reconnaissance d'image
* Amazon Quicksight Q : Sorte de PowerBI Generatif, permet d'avoir des dashboards à présenter à des gens qui ne sont pas des fans IA

* Notion de **Foundation Model**
Terme générique qui englobe toutes les IA de grande taille dont LLM éventuellement en multi-modal (gère plusieurs types de média, texte, son, vidéo, en input ou ouput)
Il s'agit de models d'intelligence artificielle à usage générique, les LLM en sont un sous-genre spécialisé dans la compréhension du langage naturel

* Il est important que Bedrock puisse accéder aux ressources --> "assume IAM role"

* Edge Devices + Small specialized model -> Lowest Latency possible
---> "SLM" -> Small Language Model" -> modèle hyper spécialisé et généralement dédié à un type d'action

* SageMaker Feature Store -> Pour AWS, Partage de données entre plusieurs équipes

* SageMaker Data Wrangler -> Préparation de données
---> Litt: un gestionnaire de données
---> Ici Wrangle peut se traduire comme "range le fouilli"

SageMaker Model Cards -> Metadata/Readme à propos d'un modèle et qui va contenir toutes les informations sur ce modèle (nom, version, risque, biais...)

* Private Link : pas spécialement lié à l'IA, chez AWS private link est un mode de connexion entre des composants, qui passe par le réseau interne d'AWS -> Utile si pas de réseau publique autorisé

* NOTE : parfois l'IA n'est pas utile -> si un algorithme simple fait le travail, l'IA est inutile -> trop chere et trop de travail
---> De plus l'IA n'a pas pour but de fournir des réponses absolument exactes à des besoins.

* Mesure du runtime efficiency d'un modèle IA -> Average response time

* Amazon Transcribe -> Speech to text

* Amazon Lex -> Sorte d'Alexa mais pour AWS

* Unsupervised Learning
--> Methodologie pertinente pour définir des patterns et grouper la data quand elle est "unlabelled", c'est à dire sans metadata particulière permettant de discriminer et de ranger

* Multimodal Model : Model able to handle queries composed of several types of texts or images

* embeddings : pourrait être traduit par "vecteur" au sens AI du terme, il s'agit de données, récupérées au préalable dans une base vectorielle, généralement c'est une IA qui fait une première recherche pour identifier les meilleures embeddings pour répondre à une requête client, ces embeddings sont ensuite refilé dans une LLM pour formater proprement la réponse.

* Vecteur : on parle ici de vecteur au sens IA du terme, qui partage des liens communs avec les vecteurs mathématiques classiques qui en sont une représentation.
Un vecteur est un token, associé à des probabibilités sur 1 à N prochain mots possibles.
De ce que j'ai lu les vecteurs peuvent aussi contenir des chunks (voir plus loin)

* Dans une base vectorielle, les vecteurs avec des critères similaires se retrouvent avec des valeurs similaires.
--> ainsi selon le critère retenu pour l'entrainement du modèle, celui-ci va être plus à même de trouver des recoupements de données similaires
--> par sémantique, thème... ("plage" et "rivage" par exemple sont proches, inversement "maison" et "baleine" vont avoir des valeurs éloignées )

* Token : division élémentaire de données en IA

* **Decoupage d'un texte :**
Texte complet --*division*--> chunks --*division*--> token

* fine-tunning : améliorer le comportement d'un modèle avec des données spécialisées, pour l'entrainer.
Idéalement il faudrait pouvoir fournir des données propres et labelled au modèle dans le cadre de son entrainement.

* AI to protect from threats -> Develop an anomaly detection system

* Opensearch is a good tool to build a dataset due to its scalable index management its nearest neighboor search capacity 

* Use case for generative model AI : Text to image generation (among other)

* Financial forecast is not the best usage for AI since it's more about statistical analysis than generative AI

* A context window defines the maximum length of the input

* Batch size = number of prompts processed at once

* Model size : overall capacity and complexity of the model

* Solution pour un chatbot ayant pour but de régler des problèmes sans intervention humaine, tout en étant en accord avec le ton de l'entreprise.
    - Pour les données : fine-tunning OU embeddings (embeddings= mise en place d'un RAG)
    - Pour le ton de l'entreprise : Mise en place d'un *system-level prompt* décrivant le ton à adopter avec l'utilisateur du chat

* Sentimental analysis through LLM --> AWS Comprehend
-----> Think about providing both positive and negative reviews for the model while fune-tuning to understand the feelings

* How to monitor AWS Bedrock Foundation Model API calls --> Cloudtrail

* Amazon SageMaker Serverless Inference do host the model and serve predictions without managing any of the inderlying infrastructures

* AWS Artifacts -> Provide on demand downloads of AWS security and compliance reports and documents.

* Several people have to work on the same prompt -> Prompt template

* What is the most secured responsible model ? A model from scratch 

* Limited budget on AI ? do On Demand work, it's pay as you do. Spot instance is not available for AI work.

* **REINFORCEMENT LEARNING** : Apprentissage par scoring avec pénalité en cas d'erreur fausse ou non optimale, le but est d'avoir le score le plus haut

* métrique **ROUGE** : Métrique permettant de qualifier les *text sumarizations* et les *text generations*

* métrique **BLEU** : Métrique permettant de qualifier la qualité d'une traduction (translate)

* Fine-tunning : entrainer un model avec des données pour le rendre plus performant dans un ou plusieurs domaines -> peut le rendre plus spécialisé.

* **F1-Score** : qualité des résultats en fonction des recall (nombre de requêtes pour avoir le résultat voulu) et de la précision (accuracy=qualité=perf=précision)



---

Au sein d'un model on peut utiliser plusieurs méthodes pour ranger les données
- clustering : grouper les données entre elles
- dimensional reduction : simplifier les données
- regression: prédiction (probabilité) des N prochaines valeurs
- classification : classer les objets par catégories

**Bias :** 
```
soit un modèle ayant été entrainé avec des données bien précises.
Ces données font créer un biais de décision dans le modèle qui va alors orienter ses réponses d'une certaine façon.
Si aucun modèle de décision n'est parfait, il est important de connaitre le biais dans la réponse pour obtenir la meilleure réponse possible.
```

**Variance :**
Soit des données et un modèle. Dans quelle mesure les réponses d'un modèle vont varier selon que l'on modifie le dataset de travail ?

Si un modèle fonctionne très bien avec des données d'entrainement mais très mal avec des données réelles = Overfitting
il a été réglé trop serré et ne sait pas extrapoler
Un modèle overfitted va avoir tendance à donner des résultats très différents selon le dataset (entrainement ou réel) la variance est donc très forte.

Si un modèle donne de très mauvais résultats quelque soit le jeu de données, il n'a pas encore appris de pattern = Underfitting
La variance d'un modèle underfitted peut être forte ou faible selon le bias.
Un bias élevé indique un entrainement très orienté, avec une variante basse.
Un bias faible indique un entrainement beaucoup moins orienté, avec une variante haute
Dans les deux cas avec un entrainement inachevé (underfitted) les résultats seront mauvais. 


**RNN** : Recurrent Neuronal Network 
  Type de réseau de données fonctionnant en neurone, très bon pour générer des séries de données comme des textes ou des séries de valeurs.

**Bedrock** : Good for 
+ fine-tunning of existing models
+ RAG
+ LLM

GenAI : sous ensemble du deeplearning fait pour générer du NOUVEAU contenu similaire au contenu connu.

Model Multimodal : modèle qui prend plusieurs types d'entrées
-> Image
-> Son
-> Texte
-> ...

**Un modèle plus petit est un modèle moins cher mais aussi un modèle moins performant**

Fundation model chez AWS : Amazon Titan

---

Exemple de fine-tunning 
- Instruction based
- Continued pre-training
- Single turn = message+prompt

- One shot fine-tuning = Un exemple de paire prompt-answer valide, donné au modèle
- Few shots fine-tuning= Quelques exemples de paire prompt-answer valide, donnés au modèle

**RAG** Consiste à augmenter un modèle sans le ré-entrainer en le liant à une base de connaissances externe
--> Liée à la notion de base vectorielle

---

PRICING :

ON DEMAND = Pay as you go
BATCH = multiple input at a time => up to 50% cheaper prediction
PROVISIONED THROUGHPUT => Purchase the service for up 1 to 6 months, mandatory for fine-tunning, can be expensive


COST OF USAGE (Cheaper to most expensive)
-> Prompt engineering	+
-> RAG			++
-> fine-tunning		+++
-> model from scratch	++++

The more input -> the more expensive

---

* Prompting :
- basic
- improved
- negative

* Stop Sequence token ; A way to tell the model to stop generation new stuff

* Prompting metrics :
- temperature = + ou - créatif (0 pas créatif, 1 très créatif)
- top K = % de mot similaire (0 à 1)
- top P = limite de mots probables (0 à 1)

* System prompt : donne + d'infos sur comment doit répondre un modèle

* Chain of through : s'inclue dans le prompt, explique au modèle comment il doit répondre.

* Amazon Q business : Workflow lié aux entreprise -> on parle bien de pipeline ici

* AWS SageMaker : va permettre de créer un modèle from scratch + lifecycle ==> **LE SERVICE LE PLUS IMPORTANT**

* AWS SageMaker Training data -> sur des données qui doivent être nettoyées


MODE D'APPRENTISSAGE :

- Supervised Learning : Les données sont claires, propres, et des metadata/labels ont été renseignées, et on a expliqué au modèle ce qu'il doit faire
- Unsupervised learning : Les données sont claires et propres, mais on n'explique pas au modèle comment il doit les traiter et on le laisse trouver un pattern
- Self supervised learning : beaucoup de données raw, le modèle est laissé à faire tout le travail

Hyper-parameters : les paramètres sont à fixer avant entrainement


---

LES DIFFERENTS SERVICES :

- Amazon Comprehend : comprend le langage naturel, full managed, serverless, et comprend les sentiments, peut identifier quelques données utiles

- Amazon Translate : passe d'une langue à l'autre

- Amazon Transcribe : speech-to-text 
` Le scribe est celui qui écrit les paroles des discours sur du papier`
peut également cacher quelques PII

- Polly : Text-to-speech
` Polly speaks to you politely`

- Rekognition : Reconnaissance d'image

- Lex : sorte d'Alexa pour AWS

- Amazon Personalize : permet de proposer des recommandations utilisateur à la manière de ce qui se fait sur une boutique type Amazon.com


