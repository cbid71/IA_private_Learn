# Kubeflow

## Introduction

https://www.kubeflow.org/docs/started/introduction/


Kubeflow is a community and ecosystem of open-source projects to address each stage in the machine learning (ML) lifecycle with support for best-in-class open source tools and frameworks. Kubeflow makes AI/ML on Kubernetes simple, portable, and scalable.

The Kubeflow ecosystem is composed of multiple open-source projects that address different aspects of the ML lifecycle. Many of these projects are designed to be usable both within the Kubeflow Platform and independently. These Kubeflow components can be installed standalone on a Kubernetes cluster. It provides flexibility to users who may not require the full Kubeflow Platform capabilities but wish to leverage specific ML functionalities such as model training or model serving.

The Kubeflow Platform refers to the full suite of Kubeflow components bundled together with additional integration and management tools. Using Kubeflow as a platform means deploying a comprehensive ML toolkit for the entire ML lifecycle.


## Ecosystem


[Kubeflow Platform](./pictures/kubeflow-intro-diagram.drawio.svg)


## Kubeflow Pipeline

https://www.kubeflow.org/docs/components/pipelines/overview/

A pipeline is a definition of a workflow that composes one or more components together to form a computational directed acyclic graph (DAG). At runtime, each component execution corresponds to a single container execution, which may create ML artifacts. Pipelines may also feature control flow.

### Pipelines components

https://www.kubeflow.org/docs/components/pipelines/user-guides/components/

### First hello world components

https://www.kubeflow.org/docs/components/pipelines/getting-started/

Results will appear in the UI

## Kubeflow Central Dashboard

https://www.kubeflow.org/docs/components/central-dash/overview/

[Central Dashboard](./pictures/centraldashboardhomepage.png)

## Model registry

https://www.kubeflow.org/docs/components/model-registry/overview/

A model registry provides a central index for ML model developers to index and manage models, versions, and ML artifacts metadata. It fills a gap between model experimentation and production activities. It provides a central interface for all stakeholders in the ML lifecycle to collaborate on ML models.

[Model registry illustration](./pictures/ml-lifecycle-kubeflow-modelregistry.drawio.svg)

Here following the full Kubeflow architecture centralized around the Model Registry

[Model Reigstry + Architecture](./pictures/ml-lifecycle-kubeflow-modelregistry.drawio.svg)

## Kubeflow Trainer

**Note :** replace the legacy project `Kubeflow Training Operator`

Model training

https://www.kubeflow.org/docs/components/trainer/overview/

It's a multi-sub-component project, composed of several tools useful depending of your job (refered as Users Personas)

Kubeflow Trainer is a Kubernetes-native project designed for large language models (LLMs) fine-tuning and enabling scalable, distributed training of machine learning (ML) models across various frameworks, including PyTorch, JAX, TensorFlow, and XGBoost.

You can integrate other ML libraries such as HuggingFace, DeepSpeed, or Megatron-LM with Kubeflow Trainer to orchestrate their ML training on Kubernetes.

Kubeflow Trainer allows you to effortlessly develop your LLMs with the Kubeflow Python SDK and build Kubernetes-native Training Runtimes with Kubernetes Custom Resources APIs.


The Kubeflow Trainer is mostly targeted to be used by two "User Personas"

 - *ML Users:* engineers and scientists who develop AI models using the Kubeflow Python SDK and TrainJob.
 - *Cluster Operators:* administrators responsible for managing Kubernetes clusters and Kubeflow Training Runtimes.

[Who is this for](./pictures/user-personas.drawio.svg)




The Kubeflow Trainer supports key phases on the AI/ML lifecycle, including model training and LLMs fine-tuning, as shown in the diagram below:

[ML Lifecycle](./pictures/ml-lifecycle-trainer.drawio.svg)


## Kubeflow Katib

Model Tuning

https://www.kubeflow.org/docs/components/katib/overview/

Katib is a Kubernetes-native project for automated machine learning (AutoML). Katib supports hyperparameter tuning, early stopping and neural architecture search (NAS). Learn more about AutoML at fast.ai, Google Cloud, Microsoft Azure or Amazon SageMaker.

Katib is the project which is agnostic to machine learning (ML) frameworks. It can tune hyperparameters of applications written in any language of the users’ choice and natively supports many ML frameworks, such as TensorFlow, MXNet, PyTorch, XGBoost, and others.

Katib supports a lot of various AutoML algorithms, such as Bayesian optimization, Tree of Parzen Estimators, Random Search, Covariance Matrix Adaptation Evolution Strategy, Hyperband, Efficient Neural Architecture Search, Differentiable Architecture Search and many more. Additional algorithm support is coming soon.

The Katib project is open source. The developer guide is a good starting point for developers who want to contribute to the project.


[Katib Overview](./pictures/katib-overview.drawio.png)


Katib addresses AutoML step for hyperparameter optimization or Neural Architecture Search in AI/ML lifecycle as shown on that diagram:

[Katib Lifecycle](./pictures/ml-lifecycle-katib.drawio.svg)


## Kubeflow KServe

Model serving


Serverless inferencing, model Inference Platform on Kubernetes, looks more like distributed over k8s nodes


[KServer Overview](./pictures/kserve_new.png)


https://kserve.github.io/website/latest/

Is composed of several sub-components : 

 - Model Serving : Provides Serverless deployment for model inference
 - Modelmesh : Distributed load over nodes
 - Captum : Model explainability, to help explain the predictions and gauge the confidence of those predictions
 - Model Monitoring : KServe integrates AI Fairness 360, Adversarial Robustness Toolbox (ART) to help monitor the ML models on production


## Kserve Spark Operator

Data preparation

**Spark:** Engine for large-scale data analytics
https://spark.apache.org/


https://www.kubeflow.org/docs/components/spark-operator/overview/

Will allow to use Spark as data preparator, since Spark is officially starts supporting K8s as backend.

Spark can be used to prepare and preprocess large datasets for training machine learning models. It can handle distributed data transformations and large-scale ETL (extract, transform, load) jobs.
Spark can also train models using its MLlib library, which provides algorithms for classification, regression, clustering, etc. However, it is not the go-to solution for deployment.


