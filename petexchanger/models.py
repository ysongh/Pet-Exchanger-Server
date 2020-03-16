from petexchanger import db, ma

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    email = db.Column(db.String(100), unique = True, nullable = False)
    password = db.Column(db.String(50), nullable = False)

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "first_name", "last_name", "email", "password")

user_schema = UserSchema()
users_schema = UserSchema(many = True)

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    pet_name = db.Column(db.String(30))
    favorite_food = db.Column(db.String(50))
    favorite_toy = db.Column(db.String(50))
    location = db.Column(db.String(50))
    bio = db.Column(db.String(300))
    image_url = db.Column(db.String(100))

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable = False)

    def __init__(self, pet_name, favorite_food, favorite_toy, location, bio, image_url, user_id):
        self.pet_name = pet_name
        self.favorite_food = favorite_food
        self.favorite_toy = favorite_toy
        self.location = location
        self.bio = bio
        self.image_url = image_url
        self.user_id = user_id

class PetSchema(ma.Schema):
    class Meta:
        fields = ("id", "pet_name", "favorite_food", "favorite_toy", "location", "bio", "image_url", "user_id")

pet_schema = PetSchema()
pets_schema = PetSchema(many = True)