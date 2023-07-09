# All caption generation logic: calls to GPT-4 API, etc
# from app.services import descript_transcription
import os
import openai
from dotenv import load_dotenv

load_dotenv()

# Set your OpenAI secret key
openai.api_key = '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'

def generate_caption(transcript, prompt, max_length=150, model="gpt-3.5-turbo"):
    """
    Generate caption using GPT-3.5-turbo model.

    Parameters:
    - transcript: The transcript of the video
    - prompt: The user prompt for caption
    - max_length: Maximum length of generated caption

    Returns:
    - A string representing the generated caption.
    """
    # Combine transcript and user prompt to create GPT-3.5-turbo prompt. Transcription comes from Descript API, passed as "transcript".
    messages = [
        {"role": "system", "content": transcript},
        {"role": "user", "content": prompt}
    ]

    # Call OpenAI API to generate caption
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        max_tokens=max_length,
    )

    # Extract and return the generated caption
    caption = response['choices'][0]['message']['content'].strip()
    return caption


if __name__ == "__main__":
    # Test the function with a sample transcript and prompt
    sample_transcript = "In this video, we talk about the incredible advances in technology..."
    sample_prompt = "write me captions in the voice of Steve Jobs about why the MacBook is the best computer in the world."
    print(generate_caption(sample_transcript, sample_prompt))
