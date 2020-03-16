from flask import request, jsonify

from petexchanger import app, db
from petexchanger.models import User, user_schema, users_schema

# for testing
# get all users
@app.route("/users")
def get_users():
    all_users = User.query.all()
    result = users_schema.dump(all_users)

    return jsonify(result)

# create new user
@app.route("/signup", methods=["POST"])
def add_user():
    first_name = request.json["first_name"]
    last_name = request.json["last_name"]
    email = request.json["email"]
    password = request.json["password"]

    new_user = User(first_name, last_name, email, password)

    db.session.add(new_user)
    db.session.commit()

    return user_schema.jsonify(new_user)