from googletrans import Translator, LANGUAGES


def translate_item(language, item):
    language = language.lower()

    if language in LANGUAGES:
        print(LANGUAGES[language])
        translator = Translator()
        translated = translator.translate(item, "german", 'english')
        return translated.text
    else:
        return f"Translation for {language} is not supported."


translated_item = translate_item('en', "Hello, My name is: ")
print(translated_item)
