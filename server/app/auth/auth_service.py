import os
from logging import info
from wsgiref import headers

import requests
import uri as uri
from flask import Flask, redirect, request, render_template, url_for, flash, session
from oauthlib.oauth2 import WebApplicationClient
from dotenv import load_dotenv, find_dotenv
import json
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin

login_manager = LoginManager()

load_dotenv(find_dotenv())
app = Flask(__name__, template_folder='../../templates', static_folder='../../static')
login_manager.init_app(app)
app.secret_key = os.getenv("APP_SECRET_KEY")  # read secret key from .env file
key = os.getenv("API_KEY")
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
FACEBOOK_CLIENT_ID = os.getenv("FACEBOOK_CLIENT_ID")
FACEBOOK_CLIENT_SECRET = os.getenv("FACEBOOK_CLIENT_SECRET")


class User(UserMixin):  # fecth from database
    def __init__(self, email):
        self.id = email

    @classmethod
    def get(cls, email):
        # TODO: Implement this method to get a user from your database
        return cls(email)

    @classmethod
    def create(cls, email):
        # TODO: Implement this method to create a new user in your database
        return cls(email)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


GOOGLE_DATA = {
        'response_type': "code",  # this tells the auth server that we are invoking authorization workflow
        'redirect_uri': "https://postme.video/callback_google",  # redirect URI https://console.developers.google.com/apis/credentials
        'scope': 'https://www.googleapis.com/auth/userinfo.email',  # resource we are trying to access through Google API
        'client_id': GOOGLE_CLIENT_ID,  # client ID from https://console.developers.google.com/apis/credentials
        'prompt': 'consent'}  # adds a consent screen

FACEBOOK_DATA = {
        'response_type': "code",
        'redirect_uri': "https://postme.video/callback_facebook",
        'scope': 'email',
        'client_id': FACEBOOK_CLIENT_ID,
        'prompt': 'consent'}

URL_DICT = {
        'google_oauth': 'https://accounts.google.com/o/oauth2/v2/auth',  # Google OAuth URI
        'facebook_oauth': 'https://www.facebook.com/v10.0/dialog/oauth',  # Facebook OAuth URI
        'google_token_gen': 'https://oauth2.googleapis.com/token',  # URI to generate token to access Google API
        'facebook_token_gen': 'https://graph.facebook.com/v10.0/oauth/access_token',  # URI to generate token to access Facebook API
        'get_google_user_info': 'https://www.googleapis.com/oauth2/v3/userinfo',  # URI to get the user info
        'get_facebook_user_info': 'https://graph.facebook.com/me'  # URI to get the user info
        }

# Create a Sign in URI
GOOGLE_CLIENT = WebApplicationClient(GOOGLE_CLIENT_ID)
GOOGLE_REQ_URI = GOOGLE_CLIENT.prepare_request_uri(
    uri=URL_DICT['google_oauth'],
    redirect_uri=GOOGLE_DATA['redirect_uri'],
    scope=GOOGLE_DATA['scope'],
    prompt=GOOGLE_DATA['prompt'])

FACEBOOK_CLIENT = WebApplicationClient(FACEBOOK_CLIENT_ID)
FACEBOOK_REQ_URI = FACEBOOK_CLIENT.prepare_request_uri(
    uri=URL_DICT['facebook_oauth'],
    redirect_uri=FACEBOOK_DATA['redirect_uri'],
    scope=FACEBOOK_DATA['scope'],
    prompt=FACEBOOK_DATA['prompt'])

# Assume we have a User model and user_loader
# @login_manager.user_loader
# def load_user(user_id):
#     return User.get(user_id)

user = User.get(info['email'])
if user is None:
    user = User.create(info['email'])
    # TODO: Store other user data and tokens
login_user(user)

# Error handling
try:
    response_user_info = requests.get(uri, headers=headers, data=body)
    response_user_info.raise_for_status()  # This will raise a HTTPError if the response was an error
except requests.exceptions.HTTPError as err:
    flash(f"HTTP error occurred: {err}")  # Flash a message to the user
except Exception as err:
    flash(f"An error occurred: {err}")  # Flash a message to the user

@app.route('/welcome')
def welcome():
    return render_template('home.html')


@app.route('/login_google')
def login_google():
    # redirect to newly created Sign-In URI
    return redirect(GOOGLE_REQ_URI)


@app.route('/login_facebook')
def login_facebook():
    # redirect to newly created Sign-In URI
    return redirect(FACEBOOK_REQ_URI)


@app.route('/callback_google')
def callback_google():
    """Redirect after Google login & consent"""

    # Get the code after authenticating from the URL
    code = request.args.get('code')

    # Generate URL to generate token
    token_url, headers, body = GOOGLE_CLIENT.prepare_token_request(
        URL_DICT['google_token_gen'],
        authorization_response=request.url,
        redirect_url=request.base_url,
        code=code)

    # Generate token to access Google API
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET))

    # Parse the token response
    GOOGLE_CLIENT.parse_request_body_response(json.dumps(token_response.json()))

    # Add token to the  Google endpoint to get the user info
    uri, headers, body = GOOGLE_CLIENT.add_token(URL_DICT['get_google_user_info'])

    # Get the user info
    response_user_info = requests.get(uri, headers=headers, data=body)
    info = response_user_info.json()

    # Login user and redirect
    # user = User.get(info['email'])
    # login_user(user)

    return redirect('/user/%s' % info['email'])


@app.route('/callback_facebook')
def callback_facebook():
    """Redirect after Facebook login & consent"""

    # Get the code after authenticating from the URL
    code = request.args.get('code')

    # Generate URL to generate token
    token_url, headers, body = FACEBOOK_CLIENT.prepare_token_request(
        URL_DICT['facebook_token_gen'],
        authorization_response=request.url,
        redirect_url=request.base_url,
        code=code)

    # Generate token to access Facebook API
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(FACEBOOK_CLIENT_ID, FACEBOOK_CLIENT_SECRET))

    # Parse the token response
    FACEBOOK_CLIENT.parse_request_body_response(json.dumps(token_response.json()))

    # Add token to the  Facebook endpoint to get the user info
    uri, headers, body = FACEBOOK_CLIENT.add_token(URL_DICT['get_facebook_user_info'])

    # Get the user info
    response_user_info = requests.get(uri, headers=headers, data=body)
    info = response_user_info.json()

    # Login user and redirect
    # user = User.get(info['email'])
    # login_user(user)

    return redirect('/user/%s' % info['email'])


@app.route('/user/<email>')
def login_success(email):
    """Landing page after successful login"""
    flash(f"Hello, you're signed in as {email}")
    return render_template('dashboard.html')


@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('welcome'))


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
