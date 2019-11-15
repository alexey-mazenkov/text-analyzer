import textblob
import dostoevsky
import localization as lc
import dictionaries as dt


def rus_text(text):
    """
    :param text:
    :return:
    """
    # Функция для анализа русского текста(модуль dostoevsky).

    count_sentens = 0
    count_words = 0
    count_syllables = 0

    for i in range(len(text)):
        if text[i] == '.' or text[i] == '!' or text[i] == '?':
            if text[i] == '.' and text[i - 1].isalnum():
                if not text[i].isalnum():
                    count_sentens += 1
            elif text[i] == '.' and not text[i - 1].isalnum():
                count_sentens += 1
            elif text[i] == '!' or text[i] == '?':
                count_sentens += 1

        if text[i] == ' ':
            count_words += 1

        if text[i] in dt.vowels:
            count_syllables += 1

    if count_words > 0:
        count_words += 1

    print('Предложений:', count_sentens)
    print('Слов:', count_words)
    print('Слогов:', count_syllables)
    # print('Средняя длина предложения в словах:', ASL)
    # print('Средняя длина слова в слогах:', ASW)
    # print('Индекс удобочитаемости Флеша:', FRE)


def en_text(text):
    """
    :param text:
    :return:
    """
    # TODO(Kravtsov): Анализ английского(модуль textblob).

    # print('Предложений:', count_sentens)
    # print('Слов:', count_words)
    # print('Слогов:', count_syllables)
    # print('Средняя длина предложения в словах:', ASL)
    # print('Средняя длина слова в слогах:', ASW)
    # print('Индекс удобочитаемости Флеша:', FRE)
