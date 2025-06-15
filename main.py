import requests

def translate_text(text, source_lang="en", target_lang="es"):
    url = "https://api.mymemory.translated.net/get"
    
    params = {
        "q": text,
        "langpair": f"{source_lang}|{target_lang}"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data["responseData"]["translatedText"]
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

# Main function to accept user input
if _name_ == "_main_":
    print("=== Simple Language Translator ===")
    text = input("Enter text to translate: ")
    source_lang = input("Enter source language code (e.g., 'en' for English): ").strip()
    target_lang = input("Enter target language code (e.g., 'fr' for French): ").strip()

    result = translate_text(text, source_lang, target_lang)
    print("\nTranslated Text:", result)