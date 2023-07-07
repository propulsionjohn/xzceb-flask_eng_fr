"""translator.py - used to translate English to French and French to English"""
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    This function translates English text to French using the MyMemoryTranslator.

    Parameters:
    english_text (str): The text in English to translate.

    Returns:
    str: The translated text in French.
    """
    translator = MyMemoryTranslator(source="english", target="french")
    french_text = translator.translate(english_text)
    return french_text

def french_to_english(french_text):
    """
    This function translates French text to English using the MyMemoryTranslator.

    Parameters:
    french_text (str): The text in French to translate.

    Returns:
    str: The translated text in English.
    """
    translator = MyMemoryTranslator(source="french", target="english")
    english_text = translator.translate(french_text)
    return english_text
