import tkinter as ttk


class UltraShifr(ttk.Frame):
    def __init__(self):
        self.vivod = "1"
        self.dict = {"а": 1, "А": -1, "б": 2, "Б": -2, "в": 3, "В": -3,
                     "г": 4, "Г": -4, "д": 5, "Д": -5, "е": 6, "Е": -6,
                     "ё": 7, "Ё": -7, "ж": 8, "Ж": -8, "з": 9, "З": -9,
                     "и": 10, "И": -10, "й": 11, "Й": -11, "к": 12, "К": -12,
                     "л": 13, "Л": -13, "м": 14, "М": -14, "н": 15, "Н": -15,
                     "о": 16, "О": -16, "п": 17, "П": -17, "р": 18, "Р": -18,
                     "с": 19, "С": -19, "т": 20, "Т": -20, "у": 21, "У": -21,
                     "ф": 22, "Ф": -22, "х": 23, "Х": -23, "ц": 24, "Ц": -24,
                     "ч": 25, "Ч": -25, "ш": 26, "Ш": -26, "щ": 27, "Щ": -27,
                     "ъ": 28, "Ъ": -28, "ы": 29, "Ы": -29, "ь": 30, "Ь": -30,
                     "э": 31, "Э": -31, "ю": 32, "Ю": -32, "я": 33, "Я": -33,
                     " ": 34, 1: "а", -1: "А", 2: "б", -2: "Б", 3: "в", -3: "В",
                     4: "г", -4: "Г", 5: "д", -5: "Д", 6: "е", -6: "Е",
                     7: "ё", -7: "Ё", 8: "ж", -8: "Ж", 9: "з", -9: "З",
                     10: "и", -10: "И", 11: "й", -11: "Й", 12: "к", -12: "К",
                     13: "л", -13: "Л", 14: "м", -14: "М", 15: "н", -15: "Н",
                     16: "о", -16: "О", 17: "п", -17: "П", 18: "р", -18: "Р",
                     19: "с", -19: "С", 20: "т", -20: "Т", 21: "у", -21: "У",
                     22: "ф", -22: "Ф", 23: "х", -23: "Х", 24: "ц", -24: "Ц",
                     25: "ч", -25: "Ч", 26: "ш", -26: "Ш", 27: "щ", -27: "Щ",
                     28: "ъ", -28: "Ъ", 29: "ы", -29: "Ы", 30: "ь", -30: "Ь",
                     31: "э", -31: "Э", 32: "ю", -32: "Ю", 33: "я", -33: "Я",
                     34: " ", ",": 35, 35: ",", 36: ".", ".": 36, 37: "!", "!": 37, 38: "?", "?": 38}
        self.txt = "ошибка"
        ttk.Frame.__init__(self)
        self.pack()
        self.master.title("Матричный Шифратор 3000")
        self.create_widgets()


    def create_widgets(self):
        self.Baton_for_zashifr = ttk.Button(text="Зашифровать", command=self.code())
        self.Text_for_zashifr = ttk.Text()
        self.Baton_for_deshifr = ttk.Button(text="Дешифровать", command=self.decode())
        self.Label_for_zashifr = ttk.Label(text=self.vivod)
        self.Baton_for_zashifr.pack()
        self.Text_for_zashifr.pack()
        self.Baton_for_deshifr.pack()
        self.Label_for_zashifr.pack()
        self.txt = self.Text_for_zashifr.get(ttk.END)

    def code(self):
        if len(self.txt) % 4 != 0:
            while len(self.txt) % 4 != 0:
                self.txt += " "
        bukvi = []
        for i in range(0, len(self.txt)):
            bukvi.append(self.txt[i])
        with_dict = []
        for k in bukvi:
            with_dict.append(self.dict[k])
        matr = []
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

    def decode(self):
        f = open("poslanie.txt", "r")
        data = list(map(int, f.readline()[0:-1].split(" ")))
        matr = []
        f.close()
        for i in range(0, len(data), 2):
            matr.append(data[i:i+4])
        del matr[1::2]
        matr_deshifr = [2, -3, -1, 2]
        decoded = []
        for i in range(0, len(matr)):
            deshifr = [(matr[i][0] * int(matr_deshifr[0])) + (matr[i][1] * matr_deshifr[2]), (matr[i][0] * matr_deshifr[1]) + (matr[i][1] * matr_deshifr[3]),
                       (matr[i][2] * matr_deshifr[0]) + (matr[i][3] * matr_deshifr[2]), (matr[i][2] * matr_deshifr[1]) + (matr[i][3] * matr_deshifr[3])]
            decoded.append(deshifr)
        k_bukvam = []
        for i in range(0, len(decoded)):
            for g in range(0, 4):
                k_bukvam.append(decoded[i][g])
        self.vivod = []
        for i in k_bukvam:
            self.vivod.append(self.dict[i])


UltraShifr().mainloop()
