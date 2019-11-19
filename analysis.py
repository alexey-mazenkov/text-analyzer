from textblob import TextBlob

import localization as lc
import dictionaries as dt


def rus_text(text):
    """
    :param text:
    :return:
    """

    count_sentens = 0
    count_words = 0
    count_syllables = 0

    # Count sentences for punctuation marks.
    # Count the syllables by vowels.
    # Count the words by the number of spaces.
    for i in range(len(text)):
        if text[i] == '.' or text[i] == '!' or text[i] == '?':
            if text[i] == '.' and not text[i - 1] in dt.numbers and text[i - 1] != '.':
                count_sentens += 1
            elif text[i] == '!' or text[i] == '?':
                count_sentens += 1

        if text[i] == ' ':
            count_words += 1

        if text[i] in dt.vowels_ru:
            count_syllables += 1

    if count_words > 0:
        count_words += 1

    asw = float(count_syllables / count_words)           # Average length of a word in syllables.
    asl = float(count_words / count_sentens)             # Average sentence length in words.
    fre = float(206.835 - 1.3 * asl - 60.1 * asw)        # Flash Readability Index.

    print('Предложений:', count_sentens)
    print('Слов:', count_words)
    print('Слогов:', count_syllables)
    print('Средняя длина предложения в словах:', asl)
    print('Средняя длина слова в слогах:', asw)
    print('Индекс удобочитаемости Флеша:', fre)

    fre = round(fre)

    if fre >= 80:
        print('Текст очень легко читается (для младших школьников).')
    elif fre >= 50:
        print('Простой текст (для школьников).')
    elif fre >= 25:
        print('Текст немного трудно читать (для студентов).')
    else:
        print('Текст трудно читается (для выпускников ВУЗов).')

def en_text(text):
    """
    :param text:
    :return:
    """

    count_sentens = 0
    count_words = 0
    count_syllables = 0

    # Count sentences for punctuation marks.
    # Count the syllables by vowels.
    # Count the words by the number of spaces.
    for i in range(len(text)):
        if text[i] == '.' or text[i] == '!' or text[i] == '?':
            if text[i] == '.' and not text[i - 1] in dt.numbers and text[i - 1] != '.':
                count_sentens += 1
            elif text[i] == '!' or text[i] == '?':
                count_sentens += 1

        if text[i] == ' ':
            count_words += 1

        if text[i].lower() in dt.vowels_en:
            count_syllables += 1

    if count_words > 0:
        count_words += 1

    asw = float(count_syllables / count_words)          # Average length of a word in syllables.
    asl = float(count_words / count_sentens)            # Average sentence length in words.
    fre = float(206.835 - 1.015 * asl - 84.6 * asw)     # Flash Readability Index.

    analysis = TextBlob(text)
    print(analysis.sentiment)

    subjective = 100 - analysis.sentiment.subjectivity * 100
    polarity = analysis.sentiment.polarity

    if polarity > 0.5:
        polarity = 'позитивный'
    elif polarity > -0.5:
        polarity = 'нейтральный'
    else:
        polarity = 'негативный'

    print('Предложений:', count_sentens)
    print('Слов:', count_words)
    print('Слогов:', count_syllables)
    print('Средняя длина предложения в словах:', asl)
    print('Средняя длина слова в слогах:', asw)
    print('Индекс удобочитаемости Флеша:', fre)

    fre = round(fre)

    if fre >= 80:
        print('Текст очень легко читается (для младших школьников).')
    elif fre >= 50:
        print('Простой текст (для школьников).')
    elif fre >= 25:
        print('Текст немного трудно читать (для студентов).')
    else:
        print('Текст трудно читается (для выпускников ВУЗов).')

    print('Тональность текста:' + polarity)
    print('Объективность:', subjective, '%')
