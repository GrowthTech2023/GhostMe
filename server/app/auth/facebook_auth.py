# facebook_auth.py

from flask import Blueprint, redirect, request, session
from flask_login import login_user
import requests
import os

facebook_auth_blueprint = Blueprint('facebook_auth', __name__)  

FACEBOOK_CLIENT_ID = os.getenv("FACEBOOK_CLIENT_ID")
FACEBOOK_CLIENT_SECRET = os.getenv("FACEBOOK_CLIENT_SECRET")

@facebook_auth_blueprint.route('/login/facebook')
def login_facebook():

  facebook_login_url = "https://www.facebook.com/v3.3/dialog/oauth"

  params = {
    "client_id": FACEBOOK_CLIENT_ID,
    "redirect_uri": "http://localhost:5000/facebook/callback",
    "scope": "email", # comma separated string  
  }
  
  # Redirect user to Facebook's OAuth page
  return redirect(facebook_login_url + "?&" + urlencode(params))

@facebook_auth_blueprint.route('/facebook/callback')
def callback_facebook():

  # Get access token  
  access_token_url = "https://graph.facebook.com/v3.3/oauth/access_token"

  params = {
    "client_id": FACEBOOK_CLIENT_ID,
    "redirect_uri": "http://localhost:5000/facebook/callback",
    "client_secret": FACEBOOK_CLIENT_SECRET, 
    "code": request.args.get('code') 
  }

  access_token_response = requests.get(access_token_url, params=params)

  access_token = access_token_response.json()['access_token']

  # Use access token to get user's profile  
  profile_url = "https://graph.facebook.com/me"

  profile_response = requests.get(profile_url, params={"fields": "id,name,email", "access_token": access_token})

  profile = profile_response.json()

  # Login user
  # TODO: Lookup user in DB  
  user = User(profile['id'], profile['name'], profile['email']) 
  login_user(user)

  return redirect("/dashboard")