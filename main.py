# TEXT ANALYZER.
# Developers: A.Mazenkov
#             K.Kravtsov
#             A.Mikhailov
import dictionaries
import analysis as al

# TODO(Mkhlva): Здесь должна быть проверка того, на каком языке введён текст.
text = input()
cnt = len(text)
for vs in dictionaries.vowels_ru:
    text = text.replace(vs, '')
if len(text) == cnt:
    print('Язык: en')
else:
    print('Язык: ru')




# TODO(Mkhlva): Здесь должны вызываться функции анализа(с учетом языка введённого текста).

al.en_text(text)

al.rus_text(text)