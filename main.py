# TEXT ANALYZER.
# Developers: A.Mazenkov -- 70%
#             K.Kravtsov  -- 55%
#             A.Mikhailov
import dictionaries as dt
import analysis as al

text = input('Введите текст:').lower()

rus = 0
en = 0

for i in range(len(text)):
    if text[i] in dt.alp_ru:
        rus += 1
    elif text[i] in dt.alp_en:
        en += 1

print(rus, en)
if rus > en:
    al.rus_text(text)
elif en > rus:
    al.en_text(text)

while rus == en:
    text = input('Введите текст:').lower()
