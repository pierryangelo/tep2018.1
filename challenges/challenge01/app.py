import os

from flask import Flask
from flask import request
from flask import jsonify
from flask_accept import accept

from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "users.db"))

app = Flask(__name__)

# All the responses will be UTF-8
app.config['JSON_AS_ASCII'] = False

#
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), unique=False, nullable=False, primary_key=False)
    email = db.Column(db.String(200), unique=False, nullable=False, primary_key=False)

    def __repr__(self):
        return f"Id: {self.id} | Name: {self.name} | E-mail: {self.email}"

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email
        }


@app.route('/user/new', methods=["POST"])
def new_user():
    """
    Creates a new user
    """
    req_data = request.get_json()

    name = req_data['name']
    email = req_data['email']

    if name and email:
        u = User(name=name, email=email)
        db.session.add(u)
        db.session.commit()
        return jsonify(u.serialize()), 201

    return "", 400


@app.route('/user/<int:user_id>', methods=["GET"])
def user_profile(user_id):
    """
    Returns an user according to his id
    """
    u = User.query.get(user_id)
    if u:
        return jsonify(id=u.id, name=u.name, email=u.email)

    return "", 400


@app.route('/users', methods=["GET"])
def list_users():
    """
    Returns a list user in JSON format
    """
    users = User.query.all()
    return jsonify([u.serialize() for u in users]), 200


if __name__ == "__main__":
    app.run()