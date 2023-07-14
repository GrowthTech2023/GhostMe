# Dashboard logic: user uploads, caption generation, post generation
# this is what the user sees and deos on the dashboard
#
# Connects either of 5 socials -- Instagram, Threads, Facebook, TikTok and YouTube (Top of page)
# Upload their video (right under the connect tab, and is the far left side within the page margin)
# Add optional prompt (this text field area with a placeholder, this section is in the middle)
# on the right side is a vertical beautiful tab where users can select which platform they want to post to (this gives them more flexibility to decide wether tha tparticular post should go on which platofrom)

# dashboard_service.py

from app import db
from models import User, Video, SocialPlatform
from flask_login import current_user

@app.route('/connect/<platform>')
def connect_platform(platform):

  # Handle OAuth flow for platform
  # Get access token
  
  social_platform = SocialPlatform(
    user_id=current_user.id,
    platform=platform,
    access_token=access_token
  )

  db.session.add(social_platform)
  db.session.commit()

  return {"message": "Platform connected"}

@app.route('/upload', methods=['POST'])  
def upload_video():

  video_file = request.files['video']

  video = Video(
    user_id=current_user.id,
    video_file=video_file
  )

  db.session.add(video)
  db.session.commit()

  return {"message": "Video uploaded"}