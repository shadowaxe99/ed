```python
from flask import Blueprint, request, jsonify
from backend.database.models.user import User

users = Blueprint('users', __name__)

@users.route('/api/users/', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(data)
    new_user.save()
    return jsonify(new_user.to_dict()), 201

@users.route('/api/users/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get(id)
    if user:
        return jsonify(user.to_dict())
    else:
        return jsonify({"error": "User not found"}), 404

@users.route('/api/users/<int:id>/preferences', methods=['PUT'])
def update_preferences(id):
    data = request.get_json()
    user = User.query.get(id)
    if user:
        user.update_preferences(data)
        return jsonify(user.to_dict())
    else:
        return jsonify({"error": "User not found"}), 404
```