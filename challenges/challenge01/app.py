import os

from flask import Flask
from flask import request
from flask import jsonify
from flask_accept import accept

from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "users.db"))

app = Flask(__name__)
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
@accept('application/json')
def new_user():
    content = request.get_json()
    name = content['name']
    email = content['email']

    if request.method == 'POST' and name and email:
        u = User(name=name, email=email)
        db.session.add(u)
        db.session.commit()
        return jsonify(sucess=True), 201

    return jsonify(sucess=False), 400


@app.route('/user/<int:user_id>', methods=["GET"])
# @accept('application/json')
def user_profile(user_id):
    u = User.query.get(user_id)
    if u:
        return jsonify(id=u.id, name=u.name, email=u.email)

    return jsonify(sucess=False), 404 # or 400


@app.route('/users', methods=["GET"])
# @accept('application/json')
def list_users():
    users = User.query.all()
    return jsonify(users_list=[u.serialize() for u in users])


if __name__ == "__main__":
    app.run()