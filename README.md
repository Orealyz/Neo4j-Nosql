# Projet API - Neo4j

## Description

Ce projet est une API Flask connectée à une base de données Neo4j. Il permet de gérer des utilisateurs et des publications (posts). Les utilisateurs peuvent créer des posts, et chaque post est associé à un utilisateur spécifique.

## Prérequis

Avant de commencer, assurez-vous d'avoir les éléments suivants installés sur votre machine :

- **Python 3.x** (recommandé : 3.12)
- **Neo4j** (version 4.x ou supérieure)
- **pip** (gestionnaire de paquets Python)

## Installation

### Étape 1 : Cloner le repository

Clonez le repository avec la commande suivante :

```bash
git clone https://github.com/Orealyz/Neo4j-Nosql.git
cd Neo4j-Nosql
```
Environnement virtuel:
```
python3 -m venv venv
```

Activez l'environnement:
```
source venv/bin/activate
```

Installer les requiremetns:
```
pip install -r requirements.txt
```

Lancer le docker:
```
docker run --name neo4j -d \
  -p 7474:7474 -p 7687:7687 \
  -e NEO4J_AUTH=neo4j/password \
  neo4
```

Lancer l'app:
```
python app.py
```

Créer un utilisateur :
```
curl -X POST http://127.0.0.1:5000/users \
                        -H "Content-Type: application/json" \
                        -d '{"name": "Alice", "email": "alice@example.com"}'
```

Créer un post :

```
curl -X POST http://127.0.0.1:5000/users/user123/posts -H "Content-Type: application/json" -d '{"title": "Mon premier post", "content": "Ceci est le contenu de mon premier post."}'
```
