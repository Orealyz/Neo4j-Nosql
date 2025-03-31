# app.py
from flask import Flask, request, jsonify
from models import create_user, create_post, create_comment
from py2neo import Graph

app = Flask(__name__)
graph = Graph("bolt://localhost:7687", auth=("neo4j", "password"))

# Route pour créer un utilisateur
@app.route('/users', methods=['POST'])
def create_user_route():
    data = request.get_json()
    user = create_user(data['name'], data['email'])
    return jsonify({'id': user['id'], 'name': user['name'], 'email': user['email']}), 201

# Route pour créer un post
@app.route('/users/<user_id>/posts', methods=['POST'])
def create_post_route(user_id):
    data = request.get_json()
    post = create_post(user_id, data['title'], data['content'])
    return jsonify({'id': post['id'], 'title': post['title'], 'content': post['content']}), 201

# Route pour créer un commentaire
@app.route('/posts/<post_id>/comments', methods=['POST'])
def create_comment_route(post_id):
    data = request.get_json()
    comment = create_comment(data['user_id'], post_id, data['content'])
    return jsonify({'id': comment['id'], 'content': comment['content']}), 201

if __name__ == '__main__':
    app.run(debug=True)

