# Chain of through & graph chain of though


## c'est quoi le chain of though ?

Le chain of through est une technique d'entrainement et de raisonnement pour les modèles de langage consistant à expliciter les étapes intermédiaires de pensée pour orienter la réflexion du modèle.
Les modèles de langage ont tendance à donner des réponses provenant d'une mesure purement statistique passant à coté d'une partie de la réflexion. Cela peut conduire à obtenir des résultats faux ou sous optimaux, et augmente le risque d'hallucinations (= le risque que l'IA comble un manque par pure extrapolation quand un résultat précis est attendu).

Cette notion de Chain of though est particulièrement utile dans les domaines nécessitant un déroulé de plusieurs étapes précises.
- les mathématiques : où un calcul complexe nécessite plusieurs étapes à faire dans un ordre précis avec des résultats intermédiaires importants à connaitre
- le raisonnement logique : suivre des enchainements logiques explicites
- la compréhension de textes longs : meilleure structure de réponses correctes.

**Exemple**:

Si un train part à 14h30 et met trois heures à arriver à destinations à quelle heure arrive-t-il ?

Réponse sans la CoT : `18h00`
Réponse avec la CoT :
```
- Le train part à 14h30
- Le train voyage pendant 3h30
- On ajoute 3h30m à 14h30 
- On obtient 18h00
- réponse finale : 18h00
```

Le tooling, méthode consistant à assister le modèle de réflexion avec des outils externes, peut être vu comme une alternative au chain of though, et va s'inscrire plus largement dans ce qu'on appelle les Agent IA (outils d'acquisitions greffés sur le modèle).
Les workflows, consistant à chainer des méthodes d'acquisition de données pour produire les entrants d'un travail d'IA est la suite logique du chain of though.

## Configuration du chain of though par la méthode du prompting

De base le chain of though se configure par la méthode du prompting. Elle consiste basiquement à fournir à l'IA toutes les informations sur la façon dont elle doit travailler pour traiter les données entrées, ainsi que pour fournir les résultats sous la forme attendue par l'utilisateur.
Des exemples fournis dans le system prompt, une partie du prompt qui n'a pas vocation à être fournie par le client mais par son interface de communication avec l'IA, peuvent constitue>

## Configuration du chain of though par la méthode du fine-tunning

Soit un modèle donné.
On va entrainer un modèle sur des milliers d'exemples avec toute la mécanique de réflexion systématiquement donnée.
Cette méthode systématiquement donnée va apprendre au modèle une certaine réflexion et conduire celui-ci à présenter les prochains résultats sous le même format.

Trois étapes :
- Collection de données -> établissement d'un dataset de plusieurs milliers d'infos
- Entrainement du modèle -> le modèle générique devient un modèle spécialisé
- Tests et affinages

Cette méthode, bien que plus contraignante à mettre en place, donne de bien meilleurs résultats

## Configuration par N-shots

### 0-shot CoT

Une petite astuce pour obtenir un meilleur résultat consiste à demander au modèle de travailler sur sa propre réflexion avant de donner un résultat pertinent.
**Exemple :** `Si un train part à 14h et met 3h30 pour arriver, quelle est l’heure d’arrivée ?  Réfléchissons étape par étape.`

### Self consistency CoT

On peut également demander au modèle de fournir plusieurs réponses et choisir la réponse la plus appropriée, celle-ci sera comprise comme une meilleure approche et facilitera des prochaines réponses plus adaptées.
Cela peut aussi être vu comme une extension du 0-shot CoT précédemment précisé.

### Tree of though

Extension où le modèle explore plusieurs chemins de raisonnement en parallèle, comme un arbre de décision, avec l'éllagation des mauvaises pistes.

Une variante plus connue de cette méthodologie est la `Graph chain of though` qui comporte la particularité de conserver plusieurs bonnes réponses.


## C'est quoi le graph chain of though ?

Il s'agit d'une variante de la Chain of Though où la réflexion n'est plus seulement donnée sous forme linéaire mais sous forme d'arbre de réflexion avec plusieurs pistes de réflexions en parallèle.
Alors que le CoT classique suit un chemin séquentiel (une suite d’étapes logiques de A → B → C), le Graph CoT représente le raisonnement comme un graphe où différentes idées, hypothèses ou étapes peuvent être explorées en parallèle, converger ou diverger selon la logique du problème.

But principal : Permettre aux modèles d’IA d’explorer plusieurs pistes de raisonnement en même temps, d’évaluer différentes hypothèses et de fusionner les résultats de manière plus robuste.

## Comment fonctionne le Graph CoT ?

On a l'habitude de représenter les méthodes de réflexion par un vocabulaire adapté :

- Les nodes (noeuds) = des faits, sous-raisons ou sous-problèmes.
- Les edges (arêtes) = des relations entre ces sous-raisons (ex. dépendances logiques, liens de causalité, etc.).
- Les paths (chemins multiples) = différentes stratégies pour résoudre un problème donné.

Ce genre d'approche est notamment très utile quand un problème soumis à l'IA ne permet pas d'obtenir une réponse unique parfaite mais qu'il est attendu en sortie plusieurs bonnes réponses.


**Exemple :** Tom a volé un gateau. Qui pourrait être son complique ?

*Réponse avec une CoT classique (forcément fausse dans notre cas) :*
```
- Tom a volé un gateau
- Il devait avoir un complice
- Qui aurait pu l'aide ? une personne présente
- Une personne présent avec Mike est complice du vol du gateau
```

*Réponse avec un Graph CoT :*
```
Tom a volé un gateau, le fait qu'il ait un complice est une supposition
---> Soit Tom a agit seul
---> réponse 1 : Tom n'avait pas de complice et a agit seul

---> Soit Tom avait un complice
---> Qui aurait pu l'aider ? une personne présente
---> Qui était présent ?
---> réponse 2 : Une personne présente est complice du vol du gateau
```

Le grand avantage est de permettre un choix ultérieur par intervention d'une machine ou d'un humain, limitant ainsi les erreurs potentielles qui surviendraient par l'établissement d'une réponse unique.

