# Installer le chatbot

## Créer le virtual Env

```
mkdir -p chatbot/venv
python3 -m venv chatbot/venv
source chatbot/venv/bin/activate
```

## Installer la base de données Postgresql + PGVector

```
TODO : procedure à écrire
```

## Installer Ollama + récupérer le modèle llama3.2

```
TODO : procedure à écrire
```

## Déploiement des dépendances

```
pip install fastapi fastapi[standard] uvicorn gitpython langchain ollama psycopg2-binary sqlalchemy unstructured langchain-community langchain-postgres langchain-ollama markdown
```

## Lancer l'accumulateur en chargeur de récupérer les données brutes et les transformer en données vectorielles avant de les stocker

```
python accumulator.py
```

## Lancer le serveur API qui va réception les requêtes POST envoyées par le client et réaliser l'intelligence autour du RAG

```
# A faire dans le dossier contenant docapi.py
uvicorn docapi:app --reload --port 9876
```

## Tester les requêtes via CURL

```
curl -X 'POST' 'http://127.0.0.1:9876/api/search' -H 'Content-Type: application/json' -d '{"query": "Hello FastAPI"}'
```

## Lancer l'IHM

```
sudo apt install python3.10-tk
pip install requests

python ihm.py
```
