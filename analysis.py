import textblob
import dostoevsky
import localization as lc
import dictionaries as dt


def rus_text(text):
    """
    :param text:
    :return:
    """
    # Function for analyzing Russian text (dostoevsky module).

    count_sentens = 0
    count_words = 0
    count_syllables = 0

    # Count sentences for punctuation marks
    # Count the syllables by vowels
    # Count the words by the number of spaces
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

    asw = float(count_syllables / count_words)          # Average length of a word in syllables
    asl = float(count_words / count_sentens)            # Average sentence length in words
    fre = float(206.835 - 1.015 * asl - 84.6 * asw)     # Flash Readability Index

    print('Предложений:', count_sentens)
    print('Слов:', count_words)
    print('Слогов:', count_syllables)
    print('Средняя длина предложения в словах:', asl)
    print('Средняя длина слова в слогах:', asw)
    print('Индекс удобочитаемости Флеша:', fre)
    print('Предложений:', count_sentens)
    print('Слов:', count_words)
    print('Слогов:', count_syllables)


def en_text(text):
    """
    :param text:
    :return:
    """
    # Function for parsing English text (textblob module).

    count_sentens = 0
    count_words = 0
    count_syllables = 0

    # Count sentences for punctuation marks
    # Count the syllables by vowels
    # Count the words by the number of spaces
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

    asw = float(count_syllables / count_words)          # Average length of a word in syllables
    asl = float(count_words / count_sentens)            # Average sentence length in words
    fre = float(206.835 - 1.015 * asl - 84.6 * asw)     # Flash Readability Index

    print('Предложений:', count_sentens)
    print('Слов:', count_words)
    print('Слогов:', count_syllables)
    print('Средняя длина предложения в словах:', asl)
    print('Средняя длина слова в слогах:', asw)
    print('Индекс удобочитаемости Флеша:', fre)
