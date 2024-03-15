from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from flask_bcrypt import Bcrypt
import jwt
from functools import wraps

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/nutrition_app'
mongo = PyMongo(app)
bcrypt = Bcrypt(app)

# User registration
@app.route('/register', methods=['POST'])
def register():
    try:
        username = request.json['username']
        password = request.json['password']
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        users = mongo.db.users
        existing_user = users.find_one({'username': username})
        if existing_user:
            return jsonify({'message': 'Username already exists'}), 400

        user_id = users.insert({'username': username, 'password': hashed_password})
        return jsonify({'message': 'User registered successfully'}), 201
    except Exception as e:
        return jsonify({'message': 'Error registering user'}), 500

# User login
@app.route('/login', methods=['POST'])
def login():
    try:
        username = request.json['username']
        password = request.json['password']

        users = mongo.db.users
        user = users.find_one({'username': username})
        if not user or not bcrypt.check_password_hash(user['password'], password):
            return jsonify({'message': 'Invalid username or password'}), 401

        token = jwt.encode({'user_id': str(user['_id'])}, 'secretKey', algorithm='HS256')
        return jsonify({'token': token.decode('utf-8')}), 200
    except Exception as e:
        return jsonify({'message': 'Error logging in'}), 500

# Middleware for authentication
def authenticate_token(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Access denied'}), 401

        try:
            data = jwt.decode(token, 'secretKey', algorithms=['HS256'])
            current_user = mongo.db.users.find_one({'_id': ObjectId(data['user_id'])})
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired'}), 403
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token'}), 403

        return func(current_user, *args, **kwargs)

    return wrapper

# Add a meal (authenticated route)
@app.route('/meals', methods=['POST'])
@authenticate_token
def add_meal(current_user):
    try:
        meal_data = request.json
        meal_data['user_id'] = current_user['_id']

        meals = mongo.db.meals
        meals.insert(meal_data)

        return jsonify({'message': 'Meal added successfully'}), 201
    except Exception as e:
        return jsonify({'message': 'Error adding meal'}), 500

# Retrieve meals for a user (authenticated route)
@app.route('/meals', methods=['GET'])
@authenticate_token
def get_meals(current_user):
    try:
        meals = mongo.db.meals.find({'user_id': current_user['_id']})
        return jsonify(meals), 200
    except Exception as e:
        return jsonify({'message': 'Error retrieving meals'}), 500

if __name__ == '__main__':
    app.run(debug=True)