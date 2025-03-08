# Kafka Producer/Consumer avec Docker Compose

Ce projet illustre l'utilisation de Kafka pour l'échange de données entre un Producer et un Consumer, conteneurisés avec Docker.

## Architecture
```
kafka-project/
├── producer/
│   ├── producer.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── .env
├── consumer/
│   ├── consumer.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── .env
├── docker-compose.yml
└── README.md
```

## Prérequis

* Docker
* Docker Compose

## Comment lancer le projet

1. Cloner le dépôt.
2. Naviguer vers le répertoire du projet.
3. Lancer les conteneurs avec `docker-compose up --build`.

## Configuration

* Les configurations du Producer et du Consumer sont gérées via des fichiers `.env` respectifs.
* Le Producer génère des tableaux NumPy aléatoires et les envoie à Kafka.
* Le Consumer lit ces tableaux depuis Kafka et les affiche.

## Réseau

Les conteneurs Producer et Consumer communiquent via un réseau Docker privé nommé `kafka-network`.

## 🛠️ Built With

<p align="left">
  <a href="https://www.python.org/" style="text-decoration: none;">
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  </a>
  <a href="https://www.python.org/" style="text-decoration: none;">
    <img src="https://img.shields.io/badge/docker-257bd6?style=for-the-badge&logo=docker&logoColor=white" alt="Docker">
  </a>
  <a href="https://www.python.org/" style="text-decoration: none;">
    <img src="https://img.shields.io/badge/Docker%20Compose-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker-compose">
  </a>  
  <a href="https://www.python.org/" style="text-decoration: none;">
    <img src="https://img.shields.io/badge/Apache_Kafka-231F20?style=for-the-badge&logo=apache-kafka&logoColor=white&logoColor=white" alt="Kafka">
  </a>   
</p>

### Top contributors:

<a href="https://github.com/DeVerMyst/docker-compose-kafka/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=DeVerMyst/docker-compose-kafka" alt="contrib.rocks image" />
</a>
