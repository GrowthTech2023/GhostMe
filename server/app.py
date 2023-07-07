# Runs the application
from flask import Flask
from flask_cors import CORS
from .api.routes import auth_routes, video_routes

def create_app():
    app = Flask(__name__)
    CORS(app)  # Enable CORS for the app

    app.register_blueprint(auth_routes)  # Register authentication routes
    app.register_blueprint(video_routes)  # Register video routes

    return app
