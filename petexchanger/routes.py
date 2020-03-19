from flask import request, jsonify

from petexchanger import app, db, bcrypt
from petexchanger.models import User, Pet, Post, user_schema, users_schema, pet_schema, pets_schema, post_schema, posts_schema

# for testing
# get all users
@app.route("/users")
def get_users():
    all_users = User.query.all()
    result = users_schema.dump(all_users)

    return jsonify({"data": result})

# create new user
@app.route("/signup", methods=["POST"])
def add_user():
    first_name = request.json["first_name"]
    last_name = request.json["last_name"]
    email = request.json["email"]
    password = request.json["password"]

    hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")

    new_user = User(first_name, last_name, email, hashed_password)

    db.session.add(new_user)
    db.session.commit()

    result = user_schema.dump(new_user)

    return jsonify({"data": result})

# login the user
@app.route("/login", methods=["POST"])
def login():
    email = request.json["email"]
    password = request.json["password"]

    user = User.query.filter_by(email = email).first()

    if user is None:
        return jsonify({"error": "This user does not exist"})

    if user.password != password:
        return jsonify({"error": "Invalid password"})

    return jsonify({"data": user.email})

# get user by id
@app.route("/user/<id>")
def user_by_id(id):
    user = User.query.get(id)
    result = user_schema.dump(user)

    return jsonify({"data": result})

# get all pets
@app.route("/pets")
def get_pets():
    all_pets = Pet.query.all()
    result = pets_schema.dump(all_pets)

    return jsonify({"data": result})

# add a new pet
@app.route("/user/<id>/addpet", methods=["POST"])
def add_pet(id):
    pet_name = request.json["pet_name"]
    favorite_food = request.json["favorite_food"]
    favorite_toy = request.json["favorite_toy"]
    location = request.json["location"]
    bio = request.json["bio"]
    image_url = request.json["image_url"]
    user_id = id

    new_pet = Pet(pet_name, favorite_food, favorite_toy, location, bio, image_url, user_id)

    db.session.add(new_pet)
    db.session.commit()

    result = pet_schema.dump(new_pet)

    return jsonify({"data": result})

# get pet by id
@app.route("/pet/<id>", methods=["GET"])
def pet_by_id(id):
    pet = Pet.query.get(id)
    result = pet_schema.dump(pet)

    return jsonify({"data": result})

# get all posts
@app.route("/posts")
def get_posts():
    all_posts = Post.query.all()
    result = posts_schema.dump(all_posts)

    return jsonify({"data": result})

# add a new post
@app.route("/user/<id>/addpost", methods=["POST"])
def add_post(id):
    item_name = request.json["item_name"]
    wants = request.json["wants"]
    description = request.json["description"]
    location = request.json["location"]
    tags = request.json["tags"]
    image_url = request.json["image_url"]
    date_posted = request.json["date_posted"]
    user_id = id

    new_post = Post(item_name, wants, description, location, tags, image_url, user_id)

    db.session.add(new_post)
    db.session.commit()

    result = post_schema.dump(new_post)

    return jsonify({"data": result})

# get post by id
@app.route("/post/<id>")
def post_by_id(id):
    post = Post.query.get(id)
    result = post_schema.dump(post)

    return jsonify({"data": result})