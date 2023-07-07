# Scheduling logic: determine optimal times to post
from . import scheduling_api

def determine_optimal_post_time(platform, video_id):
    # Get real-time engagements for the platform
    engagements = agent_service.get_realtime_engagements(platform)

    # Determine the optimal post time using scheduling API
    optimal_time = scheduling_api.determine_optimal_post_time(engagements)

    return optimal_time
