# Installer Ollama (serveur IA - serveur d'inférence ?) 

```
sudo apt-get install curl
curl -fsSL https://ollama.com/install.sh | sh
```
puis redémarrage de la machine.

*note:* ce serait bien de déployer Ollama via docker la prochaine fois

A ce stade on peut utiliser un model de donnees en invite de commande

```
ollama run llama3.2

# donne acccès à un prompt
# on peut même y accéder par API

curl http://localhost:11434/api/generate -d '{
  "model": "llama3.2",
  "prompt":"Why is the sky blue?"
}'
```

# installer docker pour l'IHM

https://docs.docker.com/engine/install/ubuntu/


## Add Docker's official GPG key:

```
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
```

## Add the repository to Apt sources:
```
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```
## Ajouter l'utilisateur au groupe docker
```
sudo usermod -aG docker cyrille-biard
newgrp docker
```
# Pull l'image docker de l'interface graphique et démarrage de l'interface graphique

```
docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main
#accès via http://localhost:3000

# OU si open-webui rencontre des problèmes pour se connecter à ollama en local
docker run -d --network=host -v open-webui:/app/backend/data -e OLLAMA_BASE_URL=http://127.0.0.1:11434 --name open-webui --restart always ghcr.io/open-webui/open-webui:main
# accès via http://localhost:8080
```

# Pour ajouter un model en local 

```
ollama run llama3.2
# OU
ollama pull llama3.2
```

Le modèle peut ainsi être choisi dans l'interface web


# Si on a besoin de redémarrer

```
systemctl restart ollama
```
