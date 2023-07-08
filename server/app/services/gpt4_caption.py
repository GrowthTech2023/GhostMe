# All caption generation logic: calls to GPT-4 API, etc
# from app import secrets
# from app.services import descript_transcription
import json
import openai
import os
from dotenv import load_dotenv

load_dotenv()

# Set your OpenAI secret key
openai.api_key = os.getenv('OPENAI_API_KEY')


def generate_caption(transcript, prompt, max_length=150):
    """
    Generate caption using GPT-3.5-turbo model.

    Parameters:
    - transcript: The transcript of the video
    - prompt: The user prompt for caption
    - max_length: Maximum length of generated caption

    Returns:
    - A string representing the generated caption.
    """
    # Combine transcript and user prompt to create GPT-4 prompt | transcription comes from Descript API, passed as "transcript"
    user_prompt = f"{transcript}\n{prompt}\nCaption:"

    # Call OpenAI API to generate caption
    response = openai.getChatCompletion(
        model="gpt-3.5-turbo",
        prompt=user_prompt,
        temperature=0.5,
        max_tokens=150,
    )

    # Extract and return the generated caption
    caption = response.choices[0].text.strip()
    return caption


if __name__ == "__main__":
    # Test the function with a sample transcript and prompt
    sample_transcript = "In this video, we talk about the incredible advances in technology..."
    sample_prompt = "write me captions in the voice of Steve Jobs about why the MacBook is the best computer in the world."
    print(generate_caption(sample_transcript, sample_prompt))
