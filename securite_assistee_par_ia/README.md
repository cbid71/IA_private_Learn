# EPP/Endpoint Protection Platform

## Définition

Une plate-forme de protection des terminaux, en anglais endpoint protection platform (EPP), est une solution déployée sur les terminaux pour empêcher les attaques de logiciels malveillants basés sur des fichiers, détecter les activités malveillantes et fournir les capacités d'investigation et de correction nécessaires pour répondre aux incidents et alertes de sécurité dynamiques. 

**Source :** https://fr.wikipedia.org/wiki/Plate-forme_de_protection_des_terminaux

Le terme "terminaux" ici regroupe : 
- les PC & laptops
- les smartphones/tablettes
- les serveurs
- les appareils IoT
- les appareils de point de vente/appareils métier
- les machines virtuelles et les containers

Ce type de plateforme regroupe un ensemble de logiciels réglés autour de la sécurité :
- antivirus & antimalware
- pare-feu
- controle des applications (app non autorisée ou suspecte)
- Détection et réponse sur le terminal (EDR) : analyse avancée sur le comportement d'un terminal pour détecter un comportement suspect, avec analyse comportementale et détection de menaces inconnues
- Gestion des vulnérabilités : identification des failles de sécurité à destination de patching avant exploitation malfaisante
- Cryptage des données : protection des données sensibles en les chiffrant sur les terminaux, que ce soit en transite ou au repos

## Principaux produits actuels

Plusieurs plateforme remplissent les qualités nommées ci-dessus :
- CrowdStrike Falcon
- Symantec Endpoint Protection
- Sophox Intercept X
- MacAfee Endpoint Security
- Trend Micro Apex One
- Bitdefender GravityZone
- Panda Security (Watchguard)
- Kaspersky Endpoint Security
- Cisco AMP for Endpoints
- Microsoft Defender for Endpoints

Ces produits opèrent de la détection de menace par IA ( voir le fichier `comparatif_epp.md` )

`TODO: comment interagissent concrètement l'AI et l'antivirus... s'ils agissent ensemble. A moins que l'IA n'intervienne que sur la partie détection des menaces et des comportements suspects ? concrètement comment ça se passe aussi pour la partie antivirale et la partie détection des menaces comment ça se fait également ?`

## Equivalence dans le cloud

Les clouders également ont des équivalents adaptés à ces EPP, généralement représentés par plusieurs services spécialisés qui travaillent ensemble à la réalisation d'une infrastructure commune ( voir le fichier comparatif `comparatif_cloud_securite.md` )



Détection de menace par IA
Interaction antivirale
Complémentarité avec les EDR


