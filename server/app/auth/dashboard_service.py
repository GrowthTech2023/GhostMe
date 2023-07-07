# Dashboard logic: user uploads, caption generation, post generation
from ..models.video_model import Video
from ..models.social_platform_model import SocialPlatform

def connect_social_account(user_id, platform_name, access_token):
    # Connect the user's social media account
    platform = SocialPlatform.query.filter_by(name=platform_name).first()
    if not platform:
        return None, 'Invalid social media platform'

    # Save the user's access token for the platform
    platform.access_token = access_token
    db.session.commit()

    return platform, None

def upload_video(user_id, video_file):
    # Upload the video file
    video = Video(user_id=user_id, video_file=video_file)
    db.session.add(video)
    db.session.commit()

    return video, None

def add_prompt(video_id, prompt):
    # Add a prompt to the video
    video = Video.query.get(video_id)
    if not video:
        return None, 'Video not found'

    video.prompt = prompt
    db.session.commit()

    return video, None

def get_user_social_platforms(user_id):
    # Get the social media platforms connected by the user
    platforms = SocialPlatform.query.filter_by(user_id=user_id).all()
    return platforms

def create_post(video_id, platform_id):
    # Create a post for the selected platform
    video = Video.query.get(video_id)
    platform = SocialPlatform.query.get(platform_id)
    if not video or not platform:
        return None, 'Invalid video or platform'

    # Create a post using the video and platform information
    post = {
        'video_id': video.id,
        'platform_id': platform.id,
        'video_url': video.url,
        'platform_name': platform.name,
        # Add more fields specific to the platform if needed
    }

    return post, None
