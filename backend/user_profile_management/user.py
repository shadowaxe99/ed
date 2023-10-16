```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/influencer_db'
db = SQLAlchemy(app)
ma = Marshmallow(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(120), unique=True)
    password_hash = db.Column(db.String(128))
    preferences = db.Column(db.JSON)

    def __init__(self, username, email, password_hash, preferences):
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.preferences = preferences

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'email', 'password_hash', 'preferences')

user_schema = UserSchema()
users_schema = UserSchema(many=True)

@app.route('/users/', methods=['POST'])
def add_user():
    username = request.json['username']
    email = request.json['email']
    password_hash = request.json['password_hash']
    preferences = request.json['preferences']

    new_user = User(username, email, password_hash, preferences)

    db.session.add(new_user)
    db.session.commit()

    return user_schema.jsonify(new_user)

@app.route('/users/<id>', methods=['GET'])
def get_user(id):
    user = User.query.get(id)
    return user_schema.jsonify(user)

@app.route('/users/<id>/preferences', methods=['PUT'])
def update_user(id):
    user = User.query.get(id)

    preferences = request.json['preferences']

    user.preferences = preferences

    db.session.commit()

    return user_schema.jsonify(user)

if __name__ == '__main__':
    app.run(debug=True)
```