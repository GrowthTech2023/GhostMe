# All caption generation logic: calls to GPT-4 API, etc
from app.
import openai
import json

# Set your OpenAI secret key
openai.api_key = 'openai_secret_key'

def generate_caption(transcript, prompt, max_length=150):
    """
    Generate caption using GPT-3 model.

    Parameters:
    - transcript: The transcript of the video
    - prompt: The user prompt for caption
    - max_length: Maximum length of generated caption

    Returns:
    - A string representing the generated caption.
    """
    # Combine transcript and user prompt to create GPT-3 prompt
    gpt_prompt = f"{transcript}\n{prompt}\nCaption:"

    # Call OpenAI API to generate caption
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=gpt_prompt,
        temperature=0.5,
        max_tokens=max_length,
    )

    # Extract and return the generated caption
    caption = response.choices[0].text.strip()
    return caption


if __name__ == "__main__":
    # Test the function with a sample transcript and prompt
    sample_transcript = "In this video, we talk about the incredible advances in technology..."
    sample_prompt = "write me captions in the voice of Steve Jobs about why the MacBook is the best computer in the world."
    print(generate_caption(sample_transcript, sample_prompt))
