from transformers import pipeline


def translate_item(language, item):
    supported_languages = {
        # Add more languages and their corresponding models here
        'french': 'Helsinki-NLP/opus-mt-en-fr',  # France
        'german': 'Helsinki-NLP/opus-mt-en-de',  # Germany
        'spanish': 'Helsinki-NLP/opus-mt-en-es',  # Spain
        'italian': 'Helsinki-NLP/opus-mt-en-it',  # Italy
        'chinese': 'Helsinki-NLP/opus-mt-en-zh',  # China
        'arabic': 'Helsinki-NLP/opus-mt-en-ar',  # Arabic-speaking countries
        'hindi': 'Helsinki-NLP/opus-mt-en-hi',  # India
        'tagalog': 'Helsinki-NLP/opus-mt-en-tl',  # Philippines (Tagalog)
        'vietnamese': 'Helsinki-NLP/opus-mt-en-vi',  # Vietnam
        'korean': 'Helsinki-NLP/opus-mt-en-ko',  # South Korea
        'greek': 'Helsinki-NLP/opus-mt-en-el',  # Greece
        'punjabi': 'Helsinki-NLP/opus-mt-en-pa',  # Punjab region
        'bengali': 'Helsinki-NLP/opus-mt-en-bn',  # Bangladesh
        'tamil': 'Helsinki-NLP/opus-mt-en-ta',  # Tamil Nadu, India
        'sinhala': 'Helsinki-NLP/opus-mt-en-si',  # Sri Lanka (Sinhala)
        'persian': 'Helsinki-NLP/opus-mt-en-fa',  # Iran
        'turkish': 'Helsinki-NLP/opus-mt-en-tr',  # Turkey
        'russian': 'Helsinki-NLP/opus-mt-en-ru',  # Russia
        'filipino': 'Helsinki-NLP/opus-mt-en-fil',  # Philippines (Filipino)
        'indonesian': 'Helsinki-NLP/opus-mt-en-id',  # Indonesia
        'thai': 'Helsinki-NLP/opus-mt-en-th',  # Thailand
        'malay': 'Helsinki-NLP/opus-mt-en-ms',  # Malaysia
        'japanese': 'Helsinki-NLP/opus-mt-en-ja',  # Japan
        'portuguese': 'Helsinki-NLP/opus-mt-en-pt',  # Portugal
        'dutch': 'Helsinki-NLP/opus-mt-en-nl',  # Netherlands
        'polish': 'Helsinki-NLP/opus-mt-en-pl',  # Poland
        'ukrainian': 'Helsinki-NLP/opus-mt-en-uk',  # Ukraine
    }

    language = language.lower()

    if language in supported_languages:
        translator = pipeline("translation", model=supported_languages[language])
        return translator(item)
    else:
        return f"Translation for {language} is not supported."


translated_item = translate_item('german', "Hello, My name is: ")
print(translated_item[0]['translation_text'])
