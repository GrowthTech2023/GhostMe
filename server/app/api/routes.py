from flask import Blueprint, request
from .models import User
from .dashboard_service import connect_platform, upload_video

auth_routes = Blueprint('auth', __name__)

@auth_routes.route('/signup', methods=['POST'])  
def signup():
  # Get user data from request
  name = request.json['name']
  email = request.json['email']  
  password = request.json['password']

  # Validate input
  if not is_valid(name, email, password):
    return {"error": "Invalid input"}, 400 

  # Create new user
  user = User(name=name, email=email, password=password)
  db.session.add(user)
  db.session.commit()

  return {"message": "User created"}

@auth_routes.route('/login', methods=['POST'])
def login():
  # Get input
  email = request.json['email']
  password = request.json['password']

  # Validate input  
  if not is_valid(email, password):
    return {"error": "Invalid credentials"}, 400

  # Check if user exists with given email
  user = User.query.filter_by(email=email).first()
  if not user:
    return {"error": "User not found"}, 404
  
  # Check if password is correct
  if not user.check_password(password):
    return {"error": "Invalid password"}, 401

  # Login user
  login_user(user)

  return {"message": "Logged in successfully"} 

@auth_routes.route('/logout', methods=['POST'])
def logout():
  logout_user()
  return {"message": "Logged out"}

@auth_routes.route('/connect/<platform>', methods=['POST'])
def connect_platform(platform):
  # Get access token
  access_token = request.json['access_token']

  # Connect platform
  connect_platform(platform, access_token)  

  return {"message": "Platform connected"}

@auth_routes.route('/upload', methods=['POST'])
def upload_video():
  return upload_video()