# TEXT ANALYZER.
# Developers: A.Mazenkov
#             K.Kravtsov 55%
#             A.Mikhailov
import dictionaries
import analysis as al

# TODO(Mkhlva): Здесь должна быть проверка того, на каком языке введён текст.
text = input()
cnt = len(text)
for vowels in dictionaries.vowels_ru:
    text = text.replace(vowels, '')
if len(text) == cnt:
    al.en_text(text)
else:
    al.en_text(text)




