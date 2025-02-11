# n8n

Management de workflow impliquant l'IA


# Installation 

https://docs.n8n.io/integrations/community-nodes/installation/

```
docker pull n8nio/n8n
docker volume create n8n_data

mkdir -p /home/cyrille-biard/travail/Sources/n8n

//Attaché :
docker run -it --rm --name n8n -p 5678:5678 -v n8n_data:/home/cyrille-biard/travail/Sources/n8n n8nio/n8n
//OU détaché :
docker run -d --rm --name n8n -p 5678:5678 -v n8n_data:/home/cyrille-biard/travail/Sources/n8n n8nio/n8n

//Accès IHM
http://localhost:5678/setup
```

On peut configurer n8n via une série de variables d'environnement : 
`https://docs.n8n.io/hosting/configuration/environment-variables/`
