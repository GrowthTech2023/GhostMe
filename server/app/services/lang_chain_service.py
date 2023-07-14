from langchain import LLMChain, OpenAI, LLM
from langchain.agents import Tool
from langchain.embeddings import Embeddings

from app.services.agents import FacebookAgent, InstagramAgent, TwitterAgent, TiktokAgent 
from app.models import Video, Caption
from app import db

import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") 

llm = LLMChain(
    agent=Tool(
        name=LLM.OPENAI,
        api_key=OPENAI_API_KEY
    )
)

agent_classes = [FacebookAgent, InstagramAgent, TwitterAgent, TiktokAgent]

for AgentClass in agent_classes:
  agent = AgentClass()
  llm.add_agent(agent)

def refine_captions(video, initial_captions):
  
  try:
    captions = llm.run(
      prompt=f"Refine these video captions to meet platform guidelines:\n\n{initial_captions}\n\n",
      agent=LLM.OPENAI, 
      stop=["Human:", "Assistant:"]  
    )
  except OpenAIError as e:
    print(f"Error communicating with OpenAI: {e}")
    return None

  final_captions = {}
  for line in captions.splitlines():
    if line.startswith(tuple(agents.keys())):
      platform = line.split(":")[0]
      caption = line.split(":")[1].strip()
      final_captions[platform] = caption

  for platform, caption in final_captions.items():
    db_caption = Caption(video=video, platform=platform, text=caption)
    db.session.add(db_caption)

  db.session.commit()

  return final_captions