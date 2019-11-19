# TEXT ANALYZER.
# Developers: A.Mazenkov -- 70 %
#             K.Kravtsov  -- 55 %
#             A.Mikhailov -- 40 %
import dictionaries as dt
import analysis as al
import localization as lc

lc.lang = str()

text = input(lc.inp).lower()

rus = 0
en = 0

for i in range(len(text)):
    if text[i] in dt.alp_ru:
        rus += 1
    elif text[i] in dt.alp_en:
        en += 1

if rus > en:
    al.rus_text(text)
elif en > rus:
    al.en_text(text)

while rus == en:
    text = input(lc.inp).lower()
