from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from google_auth import google_auth_blueprint
from facebook_auth import facebook_auth_blueprint

app = Flask(__name__)
db = SQLAlchemy(app)

app.register_blueprint(google_auth_blueprint)
app.register_blueprint(facebook_auth_blueprint)

if __name__ == '__main__':
    app.run()
