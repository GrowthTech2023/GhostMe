# descript_transcription.py

from descript_api import Client, DescriptException
import os
from dotenv import load_dotenv 

from app.models import db, Video

load_dotenv()

DESCRIPTIVE_API_KEY = os.getenv("DESCRIPTIVE_API_KEY")

client = Client(DESCRIPTIVE_API_KEY)

def start_transcription(video):

  try:
    response = client.overdub_generate_async(
      text=video.title,  
      voice_id=video.voice_id
    )
  except DescriptException as e:
    # Handle any client errors 
    print(e)
    return

  if response.status_code == 201:
    video.transcription_job_id = response.id
    db.session.commit()
  else:
    print(f"Error starting transcription, status {response.status_code}")  

def check_transcription_status(video):

  if not video.transcription_job_id:
    return

  try:
    response = client.overdub_generate_async_get(
      overdub_id=video.transcription_job_id  
    )
  except DescriptException as e:
    # Handle errors
    print(e)
    return

  if response.status_code == 200:
    # Transcription succeeded
    video.transcription_text = response.url
    db.session.commit()
  elif response.status_code == 404:
    print("Transcription job not found")
  else:
    print(f"Error checking status, status {response.status_code}")

# Rest of service code...