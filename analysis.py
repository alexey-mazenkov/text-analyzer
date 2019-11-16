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
    # Функция для анализа русского текста(модуль textblob).

    count_sentens = 0
    count_words = 0
    count_syllables = 0

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

    print('Предложений:', count_sentens)
    print('Слов:', count_words)
    print('Слогов:', count_syllables)


def asw(text):
    """

    :param text:
    :return:
    """

    sum_len = 0
    quantity = 0

    for i in range(len(text)):
        if text[i] in dt.vowels_en:
            sum_len += 1
        elif text[i] == ' ' or i == len(text) - 2:
            quantity += 1

    ASW = float(sum_len / quantity)
    print('Средняя длина слова в слогах:', ASW)

def asl(text):
    """

    :param text:
    :return:
    """

    sum_word = 0
    sum_sent = 0

    for i in range(len(text)):
        if text[i] == ' ' and text[i - 1] != '.':
            sum_word += 1
        elif text[i] == '.' and not text[i - 1] in dt.numbers and text[i - 1] != '.':
            sum_sent += 1

    ASL = float(sum_word / sum_sent)
    print('Средняя длина предложения в словах:', ASL)


def fre(ASL, ASW):
    """

    :param ASL:
    :param ASW:
    :return:
    """

    FRE = float(206.835 - 1.015 * ASL - 84.6 * ASW)
    print('Индекс удобочитаемости Флеша:', FRE)