# All transcription logic: Descript API calls, etc
from descript_api import Client
import os
from dotenv import load_dotenv

from app.models import db, Video  

load_dotenv()

DESCRIPTIVE_API_KEY = os.getenv("DESCRIPTIVE_API_KEY")

client = Client(DESCRIPTIVE_API_KEY)

def start_transcription(video):
  """Start async transcription job for video"""

  response = client.overdub_generate_async(
    text=video.title,
    voice_id=video.voice_id
  )

  video.transcription_job_id = response.id
  db.session.commit()

def check_transcription_status(video):
  """Check status of transcription job"""

  if not video.transcription_job_id:
    return

  response = client.overdub_generate_async_get(
    overdub_id=video.transcription_job_id
  )

  if response.state == 'done':
    video.transcription_text = response.url 
    db.session.commit()

def transcribe_video(video):
  """Main entry point"""

  start_transcription(video)

  # Poll every few seconds until done
  while True:
    check_transcription_status(video)
    if video.transcription_text:
      break
    time.sleep(5)

  return video.transcription_text