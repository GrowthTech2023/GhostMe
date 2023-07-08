# All transcription logic: Descript API calls, etc
from . import descript_api
from ..models.video_model import Video

def transcribe_video(video_id):
    video = Video.query.get(video_id)
    if not video:
        return None, 'Video not found'

    # Use Descript API to transcribe the video
    transcription = descript_api.transcribe_video(video.file_path)

    # Update the video model with the transcription
    video.transcription = transcription
    db.session.commit()

    return transcription, None
