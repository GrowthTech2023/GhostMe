# agent_service.py 

from langchain.agents import Agent
import requests
from requests.exceptions import RequestException

class BaseAgent(Agent):

  def __init__(self, name):
    self.name = name

  def converse(self, prompt):
    raise NotImplementedError()
    
  def get_guidelines(self):
    raise NotImplementedError()

class InstagramAgent(BaseAgent):

  def __init__(self):
    super().__init__("Instagram")

  def converse(self, prompt):
    try:
      guidelines = self.get_guidelines()
      # Analyze prompt based on guidelines
      return modified_prompt 
    except Exception as e:
      print(f"Error getting Instagram guidelines: {e}")
      return prompt

  def get_guidelines(self):
    try:
      response = requests.get("https://instagram/api/v1/guidelines")
      return response.json()
    except RequestException as e:
      print(f"Error calling Instagram API: {e}")
      return None

class TwitterAgent(BaseAgent):

  def __init__(self):
    super().__init__("Twitter")

  def converse(self, prompt):
    try:
      guidelines = self.get_guidelines()
      # Analyze prompt based on guidelines  
      return modified_prompt
    except Exception as e:
      print(f"Error getting Twitter guidelines: {e}")
      return prompt

  def get_guidelines(self):
    try:
      response = requests.get("https://twitter/api/v2/tweets/guidelines") 
      return response.json()
    except RequestException as e:
      print(f"Error calling Twitter API: {e}")
      return None

class FacebookAgent(BaseAgent):
  
  def __init__(self):
    super().__init__("Facebook")

  def converse(self, prompt):
    try:
      guidelines = self.get_guidelines()
      # Analyze prompt based on guidelines
      return modified_prompt 
    except Exception as e:
      print(f"Error getting Facebook guidelines: {e}")
      return prompt

  def get_guidelines(self):
    try:
      response = requests.get("https://facebook/api/v3/content_guidelines")
      return response.json()
    except RequestException as e:
      print(f"Error calling Facebook API: {e}")
      return None

class TiktokAgent(BaseAgent):

  def __init__(self):
    super().__init__("Tiktok")

  def converse(self, prompt):
    try:
      guidelines = self.get_guidelines()
      # Analyze prompt based on guidelines
      return modified_prompt
    except Exception as e:
      print(f"Error getting Tiktok guidelines: {e}")
      return prompt

  def get_guidelines(self):
    try:
      response = requests.get("https://tiktok/api/v2/content_guidelines")
      return response.json()
    except RequestException as e:
      print(f"Error calling Tiktok API: {e}")
      return None