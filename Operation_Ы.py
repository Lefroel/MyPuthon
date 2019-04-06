dict = {"а":1, "А":1, "б":2, "Б":2, "в":3, "В":3,
        "г":4, "Г":4, "д":5, "Д":5, "е":6, "Е":6,
        "ё":7, "Ё":7, "ж":8, "Ж":8, "з":9, "З":9,
        "и":10, "И":10, "й":11, "Й":11, "к":12, "К":12,
        "л":13, "Л":13, "м":14, "М":14, "н":15, "Н":15,
        "о":16, "О":16, "п":17, "П":17, "р":18, "Р":18,
        "с":19, "С":19, "т":20, "Т":20, "у":21, "У":21,
        "ф":22, "Ф":22, "х":23, "Х":23, "ц":24, "Ц":24,
        "ч":25, "Ч":25, "ш":26, "Ш":26, "щ":27, "Щ":27,
        "ъ":28, "Ъ":28, "ы":29, "Ы":29, "ь":30, "Ь":30,
        "э":31, "Э":31, "ю":32, "Ю":32, "я":33, "Я":33,
        " ":34}
txt = input()
bukvi = []
for i in range(0, len(txt)):
    bukvi.append(txt[i])
with_dict = [] #[18, 1, 17, 34, 1, 18, 1, 17]
for k in bukvi:
    with_dict.append(dict[k])
matr = []
#[[18, 1, 17, 34],
# [1, 18, 1, 17]]
for i in range(0, len(with_dict), 2):
    matr.append(with_dict[i:i+4])
matr_shifr = [2, 3, 1, 2]
vivod = []
del matr[1::2]
for i in range(0, len(matr)):
    zashifr = [(matr[i][0] * int(matr_shifr[0])) + (matr[i][1] * matr_shifr[2]), (matr[i][0] * matr_shifr[1]) + (matr[i][1] * matr_shifr[3]),
               (matr[i][2] * matr_shifr[0]) + (matr[i][3] * matr_shifr[2]), (matr[i][2] * matr_shifr[1]) + (matr[i][3] * matr_shifr[3])]
    vivod.append(zashifr)
zashifr = []
for i in vivod:
    zashifr += i
f = open("poslanie.txt", "w")
for i in zashifr:
    f.write(str(i) + " ")
