# Janus pro

## Introduction

Petits tests persos pour installation du produit sous Docker

## Dépendance

Installer docker en local

## Installation

```
apt-get install -y nvidia-container-toolkit

git clone https://github.com/deepseek-ai/Janus.git
cd Janus
```


modification de demo/app_januspro.py


```
diff --git a/demo/app_januspro.py b/demo/app_januspro.py

index 702e58e..0c15482 100644
--- a/demo/app_januspro.py
+++ b/demo/app_januspro.py
 
 # Load model and processor
-model_path = "deepseek-ai/Janus-Pro-7B"
+model_path = "deepseek-ai/Janus-Pro-1B"


-# demo.queue(concurrency_count=1, max_size=10).launch(server_name="0.0.0.0", server_port=37906, root_path="/path")
+demo.queue(concurrency_count=1, max_size=10).launch(server_name="0.0.0.0", server_port=37906, root_path="/path")

```


Création du Dockerfile qui va bien à la racine du repository


```
# Use the PyTorch base image
FROM pytorch/pytorch:latest

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory into the container
COPY . /app

# Install necessary Python packages
RUN pip install -e .[gradio]

# Set the entrypoint for the container to launch your Gradio app
CMD ["python", "/app/demo/app_januspro.py"]
```

Build de l'image 

```
docker build -t janus . 
```

Déployer un container à partir de cette image


```
docker run -it -p 7860:7860 -d -v huggingface:/home/cyrille-biard/.cache/huggingface --gpus all --name janus janus:latest

docker logs janus
```

Laisser l'image finir de se déployer


Puis contacter l'adresse gradio mise à disposition coté log.
L'interface est également accessible directement en local.
