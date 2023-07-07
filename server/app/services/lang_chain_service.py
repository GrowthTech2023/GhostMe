# Communication with LangChain, decision-making layer
from . import langchain_api

def translate_captions(captions, target_language):
    # Translate captions using LangChain API
    translated_captions = langchain_api.translate_captions(captions, target_language)

    return translated_captions
