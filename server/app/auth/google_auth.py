# auth_service.py

import os
from flask import Flask, redirect, request, session, render_template, url_for
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin
from oauthlib.oauth2 import WebApplicationClient
import requests
import json

app = Flask(__name__)
app.secret_key = os.getenv("APP_SECRET_KEY")  

login_manager = LoginManager()
login_manager.init_app(app)

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")

class User(UserMixin):
  def __init__(self, id, name, email):
    self.id = id
    self.name = name
    self.email = email

@login_manager.user_loader
def load_user(user_id):
  return User.get(user_id)

def get_google_provider_cfg():
  return requests.get("https://accounts.google.com/.well-known/openid-configuration").json()

@app.route('/login/google')
def login_google():
  google_provider_cfg = get_google_provider_cfg()
  authorization_endpoint = google_provider_cfg["authorization_endpoint"]

  request_uri = client.prepare_request_uri(
    authorization_endpoint,
    redirect_uri=request.base_url + "/callback",
    scope=["openid", "email", "profile"],
  )

  return redirect(request_uri)

@app.route('/login/google/callback')
def callback():
  code = request.args.get('code')

  google_provider_cfg = get_google_provider_cfg()
  token_endpoint = google_provider_cfg["token_endpoint"]

  token_url, headers, body = client.prepare_token_request(
    token_endpoint,
    authorization_response=request.url,
    redirect_url=request.base_url,
    code=code
  )
  
  token_response = requests.post(
    token_url,
    headers=headers,
    data=body,
    auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET),
  )

  client.parse_request_body_response(json.dumps(token_response.json()))

  userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
  uri, headers, body = client.add_token(userinfo_endpoint)
  userinfo_response = requests.get(uri, headers=headers, data=body)

  if userinfo_response.json().get("email_verified"):
    unique_id = userinfo_response.json()["sub"]
    users_email = userinfo_response.json()["email"]
    picture = userinfo_response.json()["picture"]
    users_name = userinfo_response.json()["given_name"]
  else:
    return "User email not available or not verified by Google.", 400
  
  user = User(
    id_=unique_id, name=users_name, email=users_email
  ) 

  if not User.get(unique_id):
    User.create(unique_id, users_name, users_email)

  login_user(user) 

  session['profile'] = {
    "name": users_name,
    "email": users_email,
    "picture": picture
  }
  
  return redirect("/dashboard")

@app.route("/dashboard")
# @login_required
def dashboard():
  return render_template('template/index.html')

@app.route("/logout")
@login_required
def logout():
  logout_user()
  return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True, port='5000', ssl_context="adhoc")
