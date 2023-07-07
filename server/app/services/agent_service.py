# Agent manager that interacts with individual agent services
from .agents import facebook_agent, instagram_agent, twitter_agent, linkedin_agent

def get_realtime_engagements(platform):
    if platform == 'facebook':
        return facebook_agent.get_realtime_engagements()
    elif platform == 'instagram':
        return instagram_agent.get_realtime_engagements()
    elif platform == 'twitter':
        return twitter_agent.get_realtime_engagements()
    elif platform == 'linkedin':
        return linkedin_agent.get_realtime_engagements()
    else:
        return None
