


from deep_translator import GoogleTranslator



to_translate = 'This is a waste of my time!'
translated = GoogleTranslator(source='auto', target='de').translate(to_translate)
print(translated)

translated_back = GoogleTranslator(source='auto', target='en').translate(translated)
print(translated_back)