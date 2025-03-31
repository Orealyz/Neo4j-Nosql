# models.py
from py2neo import Graph, Node, Relationship
from datetime import datetime

# Connexion à la base de données Neo4j
graph = Graph("bolt://localhost:7687", auth=("neo4j", "password"))

# Fonction pour créer un utilisateur
def create_user(name, email):
    user = Node("User", name=name, email=email, created_at=datetime.now().isoformat())
    graph.create(user)
    return user

# Fonction pour créer un post
def create_post(user_id, title, content):
    user = graph.nodes.match("User", id=user_id).first()

    if not user:
        # Créer l'utilisateur si il n'existe pas
        user = Node("User", id=user_id)
        graph.create(user)
    
    post = Node("Post", title=title, content=content, created_at=datetime.now().isoformat())
    graph.create(post)
    
    created = Relationship(user, "CREATED", post)
    graph.create(created)
    
    return post

# Fonction pour créer un commentaire
def create_comment(user_id, post_id, content):
    user = graph.nodes.match("User", id=user_id).first()
    post = graph.nodes.match("Post", id=post_id).first()
    comment = Node("Comment", content=content, created_at=datetime.now().isoformat())
    graph.create(comment)
    created = Relationship(user, "CREATED", comment)
    graph.create(created)
    has_comment = Relationship(post, "HAS_COMMENT", comment)
    graph.create(has_comment)
    return comment

