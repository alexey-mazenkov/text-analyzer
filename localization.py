# Localization packages on RU, EN languages.

lang = input('''
Выберите язык:
Choose the language(ru/en):
''')

if lang == 'ru':
    inp = 'Введите текст:'

    sent = 'Предложений:'
    words = 'Слов:'
    syllab = 'Слогов:'
    awls = 'Средняя длина слова в слогах:'
    aslw = 'Средняя длина предложения в словах:'
    flash_i = 'Индекс удобочитаемости Флеша:'

    easy = 'Текст очень легко читается (для младших школьников).'
    simple = 'Простой текст (для школьников).'
    hard = 'Текст немного трудно читать (для студентов).'
    veryhard = 'Текст трудно читается (для выпускников ВУЗов).'

    positive = 'позитивный'
    neutral = 'нейтральный'
    negative = 'негативный'

    polar = 'Тональность текста:'
    subj = 'Объективность:'


if lang == 'en':
    inp = 'Enter text:'

    sent = 'Sentences:'
    words = 'Words:'
    syllab = 'Syllables:'
    awls = 'Average word length in syllables:'
    aslw = 'Average sentence length in words:'
    flash_i = 'The index of readability of the Flash:'

    easy = 'The text is very easy to read (for younger students).'
    simple = 'Simple text (for schoolchildren).'
    hard = 'The text is a bit hard to read (for students).'
    veryhard = 'The text is hard to read (for University graduates).'

    positive = 'positive'
    neutral = 'neutral'
    negative = 'negative'

    polar = 'The tone of the text:'
    subj = 'Objectivity:'
